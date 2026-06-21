"""Extract a source-backed evidence index from targeted bitwise GitHub JSON."""

from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
WIKI = ROOT / "VllmWiki"
SOURCE_ROOT = ROOT / "all" / "data" / "targeted" / "bitwise"

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


MECHANISMS = {
    "prefix_cache_equivalence": [
        "prefix cache",
        "prefix caching",
        "cache hit",
        "cache miss",
        "cache-hit",
        "cache-miss",
        "full prefill",
        "partial prefill",
    ],
    "batch_invariance": [
        "batch invariance",
        "batch invariant",
        "VLLM_BATCH_INVARIANT",
        "batch size",
        "cuda graph",
        "torch.compile",
    ],
    "kv_cache_identity": [
        "kv cache",
        "block_table",
        "block table",
        "slot mapping",
        "concurrent prefill",
        "stale",
        "corruption",
        "lora",
        "adapter",
    ],
    "deterministic_dispatch_reduction": [
        "autotune",
        "autotuner",
        "triton",
        "splitk",
        "split-k",
        "atomic",
        "reduction",
        "deterministic",
        "kernel",
    ],
    "quant_dtype_semantics": [
        "fp8",
        "fp4",
        "mxfp4",
        "nvfp4",
        "dtype",
        "bfloat16",
        "bf16",
        "scale",
        "quant",
        "safetensors",
    ],
    "verification_contract": [
        "torch.equal",
        "allclose",
        "assert_close",
        "bit-identical",
        "bitwise",
        "rtol",
        "atol",
        "test",
        "logprob",
    ],
}

SIGNALS = [
    "bitwise",
    "bit-identical",
    "deterministic",
    "non-deterministic",
    "nondeterministic",
    "same output",
    "different output",
    "temperature=0",
    "cache hit",
    "cache miss",
    "batch invariant",
    "batch invariance",
    "torch.equal",
    "allclose",
    "assert_close",
    "rtol",
    "atol",
    "argmax",
    "logprob",
    "divergence",
    "mismatch",
    "drift",
    "corruption",
]


def clean(text: str | None) -> str:
    text = text or ""
    text = re.sub(r"\r\n?", "\n", text)
    text = re.sub(r"<details>.*?</details>", " ", text, flags=re.I | re.S)
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def truncate(text: str, limit: int = 420) -> str:
    text = clean(text)
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "..."


def signal_terms(text: str) -> list[str]:
    low = text.lower()
    return [term for term in SIGNALS if term.lower() in low]


def mechanism_guess(text: str) -> str:
    low = text.lower()
    scores = Counter()
    for mechanism, terms in MECHANISMS.items():
        for term in terms:
            if term.lower() in low:
                scores[mechanism] += 1
    if not scores:
        return "unclassified_bitwise"
    return scores.most_common(1)[0][0]


def snippet(text: str) -> str:
    low = text.lower()
    best = -1
    for term in SIGNALS:
        loc = low.find(term.lower())
        if loc >= 0 and (best < 0 or loc < best):
            best = loc
    if best < 0:
        best = 0
    return truncate(text[max(0, best - 120) : best + 520])


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def collect_issue_rows() -> list[dict[str, str]]:
    rows = []
    for path in sorted((SOURCE_ROOT / "issues").glob("*.json"), key=lambda p: int(p.stem)):
        data = load_json(path)
        issue = data.get("issue") or {}
        text_parts = [issue.get("title") or "", issue.get("body") or ""]
        comment_hits = []
        for comment in data.get("comments") or []:
            body = comment.get("body") or ""
            text_parts.append(body)
            if signal_terms(body):
                comment_hits.append(body)
        timeline = data.get("timeline") or []
        joined = clean(" ".join(text_parts))
        terms = signal_terms(joined)
        rows.append({
            "source_type": "issue",
            "number": str(issue.get("number") or path.stem),
            "title": issue.get("title") or "",
            "url": issue.get("html_url") or data.get("source") or "",
            "state": issue.get("state") or "",
            "mechanism_guess": mechanism_guess(joined),
            "evidence_parts": "issue_body;issue_comments;timeline",
            "comments_count": str(len(data.get("comments") or [])),
            "review_comments_count": "0",
            "files_count": "0",
            "timeline_count": str(len(timeline)),
            "signal_terms": ";".join(terms[:12]),
            "evidence_snippet": snippet(" ".join([issue.get("title") or "", issue.get("body") or ""] + comment_hits[:3])),
            "local_json": path.relative_to(ROOT).as_posix(),
        })
    return rows


def patch_snippets(files: list[dict[str, Any]]) -> str:
    hits = []
    for item in files:
        filename = item.get("filename") or ""
        patch = item.get("patch") or ""
        text = f"{filename}\n{patch}"
        if signal_terms(text):
            hits.append(snippet(text))
    if not hits and files:
        first = files[0]
        hits.append(truncate(f"{first.get('filename', '')}: {first.get('status', '')}"))
    return " / ".join(hits[:3])


def collect_pull_rows() -> list[dict[str, str]]:
    rows = []
    for path in sorted((SOURCE_ROOT / "pulls").glob("*.json"), key=lambda p: int(p.stem)):
        data = load_json(path)
        pull = data.get("pull") or {}
        files = data.get("files") or []
        review_comments = data.get("review_comments") or []
        issue_comments = data.get("issue_comments") or []
        reviews = data.get("reviews") or []
        text_parts = [pull.get("title") or "", pull.get("body") or ""]
        text_parts.extend(comment.get("body") or "" for comment in review_comments)
        text_parts.extend(comment.get("body") or "" for comment in issue_comments)
        text_parts.extend(review.get("body") or "" for review in reviews)
        text_parts.extend((file.get("filename") or "") + "\n" + (file.get("patch") or "") for file in files)
        joined = clean(" ".join(text_parts))
        terms = signal_terms(joined)
        rows.append({
            "source_type": "pull",
            "number": str(pull.get("number") or path.stem),
            "title": pull.get("title") or "",
            "url": pull.get("html_url") or data.get("source") or "",
            "state": pull.get("state") or "",
            "mechanism_guess": mechanism_guess(joined),
            "evidence_parts": "pull_body;changed_files;reviews;review_comments;issue_comments;commits",
            "comments_count": str(len(issue_comments)),
            "review_comments_count": str(len(review_comments)),
            "files_count": str(len(files)),
            "timeline_count": "0",
            "signal_terms": ";".join(terms[:12]),
            "evidence_snippet": snippet(" ".join([pull.get("title") or "", pull.get("body") or "", patch_snippets(files)])),
            "local_json": path.relative_to(ROOT).as_posix(),
        })
    return rows


def write_csv(rows: list[dict[str, str]]) -> None:
    out = WIKI / "evidence" / "bitwise_sources.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "source_type",
        "number",
        "title",
        "url",
        "state",
        "mechanism_guess",
        "evidence_parts",
        "comments_count",
        "review_comments_count",
        "files_count",
        "timeline_count",
        "signal_terms",
        "evidence_snippet",
        "local_json",
    ]
    with out.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_md(rows: list[dict[str, str]]) -> None:
    by_type = Counter(row["source_type"] for row in rows)
    by_mech = Counter(row["mechanism_guess"] for row in rows)
    with_comments = sum(1 for row in rows if row["source_type"] == "issue" and int(row["comments_count"]) > 0)
    with_files = sum(1 for row in rows if row["source_type"] == "pull" and int(row["files_count"]) > 0)
    top_by_mech: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        if row["signal_terms"]:
            top_by_mech[row["mechanism_guess"]].append(row)

    lines = [
        "# Bitwise Source Evidence Index",
        "",
        "状态：由 `scripts/extract_bitwise_evidence.py` 从仓库外 targeted source layer 生成。",
        "用途：把 issue body、issue comments、PR body、changed files、review comments、reviews、commits 和 timeline 统一索引，供后续 ledger promotion 和机制页复核使用。",
        "",
        "## Coverage",
        "",
        "| 项 | 数量 |",
        "| --- | ---: |",
        f"| Issue evidence files | {by_type['issue']:,} |",
        f"| PR evidence files | {by_type['pull']:,} |",
        f"| Issues with fetched comments | {with_comments:,} |",
        f"| PRs with changed files | {with_files:,} |",
        "",
        "## Mechanism Guess",
        "",
        "| Mechanism | Sources |",
        "| --- | ---: |",
    ]
    for mech, count in by_mech.most_common():
        lines.append(f"| `{mech}` | {count:,} |")
    lines.extend([
        "",
        "## High-Signal Examples",
        "",
    ])
    for mech, items in sorted(top_by_mech.items()):
        lines.extend([f"### {mech}", "", "| Source | Signals | Evidence |", "| --- | --- | --- |"])
        for row in items[:8]:
            title = row["title"].replace("|", "/")
            evidence = row["evidence_snippet"].replace("|", "/")
            lines.append(
                f"| [{row['source_type']} #{row['number']}]({row['url']}) {title} | "
                f"{row['signal_terms']} | {evidence} |"
            )
        lines.append("")
    (WIKI / "evidence" / "bitwise_sources.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    if not SOURCE_ROOT.exists():
        print(f"missing source root: {SOURCE_ROOT}", file=sys.stderr)
        return 1
    rows = collect_issue_rows() + collect_pull_rows()
    rows.sort(key=lambda row: (row["source_type"], int(row["number"])))
    write_csv(rows)
    write_md(rows)
    print(json.dumps({
        "status": "ok",
        "rows": len(rows),
        "issues": sum(1 for row in rows if row["source_type"] == "issue"),
        "pulls": sum(1 for row in rows if row["source_type"] == "pull"),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
