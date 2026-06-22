"""Fetch targeted GitHub evidence for the VllmWiki bitwise/deterministic line.

The script reads the current VllmWiki bitwise review queue, candidate ledger,
and curated bitwise pages, then fetches only the upstream issue/PR evidence
needed for that focus area. Raw evidence is written outside the wiki repo in
the targeted source layer so the GitHub source layer stays separate from the
curated wiki.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import csv
import json
import os
import re
import sys
import threading
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[2]
WIKI = ROOT / "VllmWiki"
OUT_ROOT = ROOT / "all" / "data" / "targeted" / "bitwise"
OWNER = "vllm-project"
REPO = "vllm"
API = "https://api.github.com"
RATE_LOCK = threading.Lock()

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


@dataclass
class FetchStats:
    written: int = 0
    skipped_existing: int = 0
    requests: int = 0
    failures: list[dict[str, Any]] = field(default_factory=list)
    rate_limit: dict[str, str] = field(default_factory=dict)
    lock: threading.Lock = field(default_factory=threading.Lock, repr=False)

    def record_request(self, headers: Any | None = None) -> None:
        with self.lock:
            self.requests += 1
            if headers is not None:
                self.rate_limit = {
                    "limit": headers.get("X-RateLimit-Limit", ""),
                    "remaining": headers.get("X-RateLimit-Remaining", ""),
                    "reset": headers.get("X-RateLimit-Reset", ""),
                }

    def record_written(self) -> None:
        with self.lock:
            self.written += 1

    def record_skipped(self) -> None:
        with self.lock:
            self.skipped_existing += 1

    def record_failure(self, kind: str, number: int, error: str) -> None:
        with self.lock:
            self.failures.append({"type": kind, "number": number, "error": error})

    def snapshot(self) -> dict[str, Any]:
        with self.lock:
            return {
                "requests": self.requests,
                "written": self.written,
                "skipped_existing": self.skipped_existing,
                "failures": len(self.failures),
                "rate_limit": dict(self.rate_limit),
            }


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def parse_numbers(text: str) -> set[int]:
    return {int(match) for match in re.findall(r"(?<![\w/])#([1-9]\d*)\b", text or "")}


def parse_pr_refs(text: str) -> set[int]:
    refs: set[int] = set()
    for pattern in [
        r"\bPR\s*#([1-9]\d*)\b",
        r"\b[Pp]ull\s+[Rr]equest\s*#([1-9]\d*)\b",
        r"github\.com/vllm-project/vllm/pull/([1-9]\d*)",
    ]:
        refs.update(int(match) for match in re.findall(pattern, text or ""))
    return refs


def parse_linked_prs(text: str) -> set[int]:
    numbers = set()
    for chunk in re.split(r"[;,\s]+", text or ""):
        chunk = chunk.strip()
        if not chunk:
            continue
        if chunk.startswith("#"):
            chunk = chunk[1:]
        if chunk.isdigit():
            numbers.add(int(chunk))
    return numbers


def parse_github_links(text: str) -> tuple[set[int], set[int]]:
    issues: set[int] = set()
    pulls: set[int] = set()
    for kind, number in re.findall(
        r"github\.com/vllm-project/vllm/(issues|pull)/(\d+)", text or ""
    ):
        if kind == "issues":
            issues.add(int(number))
        else:
            pulls.add(int(number))
    return issues, pulls


def maybe_wait_for_rate_limit(stats: FetchStats, min_remaining: int, label: str) -> None:
    if min_remaining <= 0:
        return
    snap = stats.snapshot()
    rate = snap.get("rate_limit", {})
    try:
        remaining = int(rate.get("remaining") or min_remaining + 1)
        reset = int(rate.get("reset") or 0)
    except ValueError:
        return
    if remaining >= min_remaining or reset <= 0:
        return
    with RATE_LOCK:
        snap = stats.snapshot()
        rate = snap.get("rate_limit", {})
        try:
            remaining = int(rate.get("remaining") or min_remaining + 1)
            reset = int(rate.get("reset") or 0)
        except ValueError:
            return
        if remaining >= min_remaining or reset <= 0:
            return
        wait_seconds = max(1, reset - int(time.time()) + 5)
        print(
            f"[rate-limit] {label}: remaining={remaining}; sleeping {wait_seconds}s until reset",
            flush=True,
        )
        time.sleep(wait_seconds)


def collect_seed_numbers(
    limit: int | None = None,
    *,
    queue_only: bool = False,
) -> tuple[set[int], set[int], dict[str, Any]]:
    issue_numbers: set[int] = set()
    pr_numbers: set[int] = set()
    seed_sources: dict[str, Any] = {
        "queue_issues": 0,
        "queue_linked_prs": 0,
        "ledger_issues": 0,
        "ledger_prs": 0,
        "curated_page_issues": 0,
        "curated_page_prs": 0,
    }

    queue_rows = read_csv(WIKI / "curated" / "bitwise_review_queue.csv")
    if limit is not None:
        queue_rows = queue_rows[:limit]
    for row in queue_rows:
        number = row.get("issue_number", "")
        if number.isdigit():
            issue_numbers.add(int(number))
            seed_sources["queue_issues"] += 1
        linked = parse_linked_prs(row.get("linked_prs", ""))
        pr_numbers.update(linked)
        seed_sources["queue_linked_prs"] += len(linked)

    if not queue_only:
        for row in read_csv(WIKI / "candidates" / "bitwise_ledger.csv"):
            note_text = ""
            note = row.get("note", "")
            if note:
                note_path = WIKI / note
                if note_path.exists():
                    note_text = read_text(note_path)
            numeric_id = row.get("id", "").replace("bitwise-", "")
            source_type_match = re.search(r"^- source type:\s*(.+)$", note_text, re.MULTILINE)
            source_type = source_type_match.group(1).strip() if source_type_match else ""
            upstream_match = re.search(r"^- upstream id:\s*(\d+)$", note_text, re.MULTILINE)
            number = upstream_match.group(1) if upstream_match else numeric_id
            if number.isdigit():
                if "pr" in source_type and "issue_pr_pair" not in source_type:
                    pr_numbers.add(int(number))
                    seed_sources["ledger_prs"] += 1
                else:
                    issue_numbers.add(int(number))
                    seed_sources["ledger_issues"] += 1
            pr_numbers.update(parse_pr_refs(" ".join(row.values())))
            pr_numbers.update(parse_pr_refs(note_text))

        page_text = "\n".join(read_text(path) for path in (WIKI / "curated" / "bitwise").glob("*.md"))
        page_issues, page_prs = parse_github_links(page_text)
        issue_numbers.update(page_issues)
        pr_numbers.update(page_prs)
        seed_sources["curated_page_issues"] = len(page_issues)
        seed_sources["curated_page_prs"] = len(page_prs)

    return issue_numbers, pr_numbers, seed_sources


def request_json(
    path: str,
    *,
    token: str | None,
    params: dict[str, Any] | None = None,
    stats: FetchStats,
    retry: int,
    sleep_seconds: float,
    min_remaining: int,
) -> Any:
    url = f"{API}{path}"
    if params:
        url = f"{url}?{urlencode(params)}"

    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "VllmWiki-targeted-evidence-fetcher",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    for attempt in range(retry + 1):
        maybe_wait_for_rate_limit(stats, min_remaining, "pre-request")
        try:
            req = Request(url, headers=headers)
            with urlopen(req, timeout=30) as response:
                stats.record_request(response.headers)
                data = response.read().decode("utf-8")
                if sleep_seconds:
                    time.sleep(sleep_seconds)
                return json.loads(data) if data else None
        except HTTPError as exc:
            stats.record_request(exc.headers)
            body = exc.read().decode("utf-8", errors="replace")
            if exc.code in {403, 429}:
                maybe_wait_for_rate_limit(stats, 1, f"http-{exc.code}")
            if exc.code in {403, 429, 500, 502, 503, 504} and attempt < retry:
                time.sleep(max(1.0, sleep_seconds) * (attempt + 1))
                continue
            raise RuntimeError(f"GET {url} failed with HTTP {exc.code}: {body[:500]}") from exc
        except URLError as exc:
            if attempt < retry:
                time.sleep(max(1.0, sleep_seconds) * (attempt + 1))
                continue
            raise RuntimeError(f"GET {url} failed: {exc}") from exc

    raise RuntimeError(f"GET {url} failed after retries")


def paged_json(
    path: str,
    *,
    token: str | None,
    stats: FetchStats,
    retry: int,
    sleep_seconds: float,
    min_remaining: int,
    per_page: int = 100,
    max_pages: int = 20,
) -> list[Any]:
    rows: list[Any] = []
    for page in range(1, max_pages + 1):
        batch = request_json(
            path,
            token=token,
            params={"per_page": per_page, "page": page},
            stats=stats,
            retry=retry,
            sleep_seconds=sleep_seconds,
            min_remaining=min_remaining,
        )
        if not batch:
            break
        if not isinstance(batch, list):
            raise RuntimeError(f"Expected list response from {path}, got {type(batch).__name__}")
        rows.extend(batch)
        if len(batch) < per_page:
            break
    return rows


def write_json(path: Path, data: Any, *, force: bool, stats: FetchStats) -> None:
    if path.exists() and not force:
        stats.record_skipped()
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    stats.record_written()


def read_existing_json(
    path: Path,
    *,
    force: bool,
    stats: FetchStats,
    required_keys: set[str],
) -> Any | None:
    if force or not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None
    if not required_keys.issubset(set(data)):
        return None
    stats.record_skipped()
    return data


def fetch_issue(number: int, args: argparse.Namespace, token: str | None, stats: FetchStats) -> dict[str, Any] | None:
    base = f"/repos/{OWNER}/{REPO}/issues/{number}"
    out_path = OUT_ROOT / "issues" / f"{number}.json"
    required = {"issue", "comments"}
    if args.timeline:
        required.add("timeline")
    existing = read_existing_json(out_path, force=args.force, stats=stats, required_keys=required)
    if existing is not None:
        return existing
    try:
        issue = request_json(
            base,
            token=token,
            stats=stats,
            retry=args.retry,
            sleep_seconds=args.sleep,
            min_remaining=args.min_remaining,
        )
        comments = paged_json(
            f"{base}/comments",
            token=token,
            stats=stats,
            retry=args.retry,
            sleep_seconds=args.sleep,
            min_remaining=args.min_remaining,
            max_pages=args.max_pages,
        )
        timeline = []
        if args.timeline:
            timeline = paged_json(
                f"{base}/timeline",
                token=token,
                stats=stats,
                retry=args.retry,
                sleep_seconds=args.sleep,
                min_remaining=args.min_remaining,
                max_pages=args.max_pages,
            )
        bundle = {
            "fetched_at_utc": datetime.now(timezone.utc).isoformat(),
            "source": f"https://github.com/{OWNER}/{REPO}/issues/{number}",
            "issue": issue,
            "comments": comments,
            "timeline": timeline,
        }
        write_json(out_path, bundle, force=args.force, stats=stats)
        return bundle
    except Exception as exc:  # noqa: BLE001 - record and continue batch fetches.
        stats.record_failure("issue", number, str(exc))
        return None


def fetch_pull(number: int, args: argparse.Namespace, token: str | None, stats: FetchStats) -> dict[str, Any] | None:
    base = f"/repos/{OWNER}/{REPO}/pulls/{number}"
    out_path = OUT_ROOT / "pulls" / f"{number}.json"
    existing = read_existing_json(
        out_path,
        force=args.force,
        stats=stats,
        required_keys={"pull", "files", "review_comments", "reviews", "commits", "issue_comments"},
    )
    if existing is not None:
        return existing
    try:
        pull = request_json(
            base,
            token=token,
            stats=stats,
            retry=args.retry,
            sleep_seconds=args.sleep,
            min_remaining=args.min_remaining,
        )
        files = paged_json(
            f"{base}/files",
            token=token,
            stats=stats,
            retry=args.retry,
            sleep_seconds=args.sleep,
            min_remaining=args.min_remaining,
            max_pages=args.max_pages,
        )
        review_comments = paged_json(
            f"{base}/comments",
            token=token,
            stats=stats,
            retry=args.retry,
            sleep_seconds=args.sleep,
            min_remaining=args.min_remaining,
            max_pages=args.max_pages,
        )
        reviews = paged_json(
            f"{base}/reviews",
            token=token,
            stats=stats,
            retry=args.retry,
            sleep_seconds=args.sleep,
            min_remaining=args.min_remaining,
            max_pages=args.max_pages,
        )
        commits = paged_json(
            f"{base}/commits",
            token=token,
            stats=stats,
            retry=args.retry,
            sleep_seconds=args.sleep,
            min_remaining=args.min_remaining,
            max_pages=args.max_pages,
        )
        issue_comments = paged_json(
            f"/repos/{OWNER}/{REPO}/issues/{number}/comments",
            token=token,
            stats=stats,
            retry=args.retry,
            sleep_seconds=args.sleep,
            min_remaining=args.min_remaining,
            max_pages=args.max_pages,
        )
        bundle = {
            "fetched_at_utc": datetime.now(timezone.utc).isoformat(),
            "source": f"https://github.com/{OWNER}/{REPO}/pull/{number}",
            "pull": pull,
            "files": files,
            "review_comments": review_comments,
            "reviews": reviews,
            "commits": commits,
            "issue_comments": issue_comments,
        }
        write_json(out_path, bundle, force=args.force, stats=stats)
        return bundle
    except Exception as exc:  # noqa: BLE001 - record and continue batch fetches.
        stats.record_failure("pull", number, str(exc))
        return None


def print_progress(label: str, done: int, total: int, stats: FetchStats, *, force: bool = False, every: int = 10) -> None:
    if not force and done != total and done % every != 0:
        return
    snap = stats.snapshot()
    rate = snap["rate_limit"]
    remaining = rate.get("remaining", "")
    limit = rate.get("limit", "")
    rate_text = f" rate={remaining}/{limit}" if remaining or limit else ""
    print(
        f"[{label}] {done}/{total} done "
        f"requests={snap['requests']} written={snap['written']} "
        f"skipped={snap['skipped_existing']} failures={snap['failures']}{rate_text}",
        flush=True,
    )


def run_fetch_group(
    label: str,
    numbers: set[int],
    fetcher: Any,
    args: argparse.Namespace,
    token: str | None,
    stats: FetchStats,
) -> list[dict[str, Any]]:
    ordered = sorted(numbers)
    total = len(ordered)
    if total == 0:
        return []
    print(f"[{label}] start total={total} workers={args.workers}", flush=True)
    bundles: list[dict[str, Any]] = []
    progress_every = max(1, args.progress_every)
    if args.workers <= 1:
        for done, number in enumerate(ordered, start=1):
            bundle = fetcher(number, args, token, stats)
            if bundle:
                bundles.append(bundle)
            print_progress(label, done, total, stats, every=progress_every)
        return bundles

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        future_to_number = {
            executor.submit(fetcher, number, args, token, stats): number
            for number in ordered
        }
        for done, future in enumerate(as_completed(future_to_number), start=1):
            number = future_to_number[future]
            try:
                bundle = future.result()
                if bundle:
                    bundles.append(bundle)
            except Exception as exc:  # noqa: BLE001 - defensive guard around worker futures.
                stats.record_failure(label, number, str(exc))
            print_progress(label, done, total, stats, every=progress_every)
    return bundles


def discover_one_hop(
    issue_bundles: list[dict[str, Any]],
    pull_bundles: list[dict[str, Any]],
    known_issues: set[int],
    known_pulls: set[int],
    max_new: int,
) -> tuple[set[int], set[int]]:
    text_parts: list[str] = []
    for bundle in issue_bundles:
        issue = bundle.get("issue") or {}
        text_parts.append(issue.get("title") or "")
        text_parts.append(issue.get("body") or "")
        for comment in bundle.get("comments") or []:
            text_parts.append(comment.get("body") or "")
    for bundle in pull_bundles:
        pull = bundle.get("pull") or {}
        text_parts.append(pull.get("title") or "")
        text_parts.append(pull.get("body") or "")
        for review in bundle.get("reviews") or []:
            text_parts.append(review.get("body") or "")
        for comment in bundle.get("review_comments") or []:
            text_parts.append(comment.get("body") or "")
        for comment in bundle.get("issue_comments") or []:
            text_parts.append(comment.get("body") or "")

    numbers = sorted(parse_numbers("\n".join(text_parts)))
    new_issues: set[int] = set()
    new_pulls: set[int] = set()
    for number in numbers:
        if number in known_issues or number in known_pulls:
            continue
        if len(new_issues) + len(new_pulls) >= max_new:
            break
        # We do not know the type until fetched. Keep it as an issue endpoint
        # candidate; GitHub issue JSON contains a pull_request key for PRs.
        new_issues.add(number)
    return new_issues, new_pulls


def write_manifest(
    *,
    args: argparse.Namespace,
    stats: FetchStats,
    issue_numbers: set[int],
    pr_numbers: set[int],
    seed_sources: dict[str, Any],
) -> None:
    manifest = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "repo": f"{OWNER}/{REPO}",
        "output_root": str(OUT_ROOT),
        "token_source": "GITHUB_TOKEN" if os.environ.get("GITHUB_TOKEN") else "none",
        "args": {
            "limit": args.limit,
            "queue_only": args.queue_only,
            "include_one_hop": args.include_one_hop,
            "timeline": args.timeline,
            "force": args.force,
            "max_pages": args.max_pages,
            "max_one_hop": args.max_one_hop,
            "min_remaining": args.min_remaining,
        },
        "seed_sources": seed_sources,
        "requested": {
            "issues": sorted(issue_numbers),
            "pulls": sorted(pr_numbers),
            "issue_count": len(issue_numbers),
            "pull_count": len(pr_numbers),
        },
        "stats": {
            "requests": stats.requests,
            "written_files": stats.written,
            "skipped_existing_files": stats.skipped_existing,
            "failure_count": len(stats.failures),
            "rate_limit": stats.rate_limit,
        },
        "failures": stats.failures,
    }
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    (OUT_ROOT / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, help="Only use the first N queue rows for a trial run.")
    parser.add_argument("--queue-only", action="store_true", help="Use only bitwise_review_queue.csv seeds; useful for small trial runs.")
    parser.add_argument("--include-one-hop", action="store_true", help="Fetch bounded #number references found in fetched bodies/comments.")
    parser.add_argument("--max-one-hop", type=int, default=50, help="Maximum one-hop references to add.")
    parser.add_argument("--timeline", action="store_true", help="Fetch issue timeline events as well.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing evidence files.")
    parser.add_argument("--dry-run", action="store_true", help="Print planned seed counts without network calls.")
    parser.add_argument("--max-pages", type=int, default=20, help="Maximum paginated pages per endpoint.")
    parser.add_argument("--workers", type=int, default=1, help="Concurrent issue/PR workers.")
    parser.add_argument("--progress-every", type=int, default=10, help="Print progress every N completed items.")
    parser.add_argument("--min-remaining", type=int, default=100, help="Pause until rate reset when remaining requests drop below this value.")
    parser.add_argument("--retry", type=int, default=2)
    parser.add_argument("--sleep", type=float, default=0.15, help="Sleep between requests to be gentle to the API.")
    args = parser.parse_args()

    token = os.environ.get("GITHUB_TOKEN")
    issue_numbers, pr_numbers, seed_sources = collect_seed_numbers(args.limit, queue_only=args.queue_only)
    if args.dry_run:
        print(json.dumps({
            "issues": len(issue_numbers),
            "pulls": len(pr_numbers),
            "seed_sources": seed_sources,
            "output_root": str(OUT_ROOT),
            "token_present": bool(token),
        }, ensure_ascii=False, indent=2))
        return 0

    if not token:
        print("warning: GITHUB_TOKEN is not set; public unauthenticated rate limit is very low.", file=sys.stderr)

    stats = FetchStats()
    issue_bundles: list[dict[str, Any]] = []
    pull_bundles: list[dict[str, Any]] = []

    issue_results = run_fetch_group("issues", issue_numbers, fetch_issue, args, token, stats)
    for bundle in issue_results:
        issue = bundle.get("issue") or {}
        number = int(issue.get("number") or 0)
        if issue.get("pull_request"):
            pr_numbers.add(number)
        else:
            issue_bundles.append(bundle)

    pull_bundles.extend(run_fetch_group("pulls", pr_numbers, fetch_pull, args, token, stats))

    if args.include_one_hop:
        new_issues, new_pulls = discover_one_hop(
            issue_bundles,
            pull_bundles,
            issue_numbers,
            pr_numbers,
            args.max_one_hop,
        )
        one_hop_issue_results = run_fetch_group("one-hop-issues", new_issues, fetch_issue, args, token, stats)
        for bundle in one_hop_issue_results:
            issue = bundle.get("issue") or {}
            number = int(issue.get("number") or 0)
            if issue.get("pull_request"):
                new_pulls.add(number)
            else:
                issue_numbers.add(number)
        pending_pulls = {number for number in new_pulls if number not in pr_numbers}
        one_hop_pull_results = run_fetch_group("one-hop-pulls", pending_pulls, fetch_pull, args, token, stats)
        for bundle in one_hop_pull_results:
            pull = bundle.get("pull") or {}
            number = int(pull.get("number") or 0)
            if number:
                pr_numbers.add(number)

    write_manifest(
        args=args,
        stats=stats,
        issue_numbers=issue_numbers,
        pr_numbers=pr_numbers,
        seed_sources=seed_sources,
    )
    print(json.dumps({
        "status": "ok" if not stats.failures else "partial",
        "issues": len(issue_numbers),
        "pulls": len(pr_numbers),
        "requests": stats.requests,
        "written_files": stats.written,
        "skipped_existing_files": stats.skipped_existing,
        "failures": len(stats.failures),
        "output_root": str(OUT_ROOT),
        "rate_limit": stats.rate_limit,
    }, ensure_ascii=False, indent=2))
    return 0 if not stats.failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
