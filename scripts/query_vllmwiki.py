"""Unified search over VllmWiki indices and markdown pages."""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def contains(text: str, terms: list[str]) -> bool:
    lowered = text.lower()
    return all(term.lower() in lowered for term in terms)


def row_text(row: dict[str, str]) -> str:
    return " ".join(str(value) for value in row.values())


def read_note(row: dict[str, str]) -> str:
    note = row.get("note", "")
    if not note:
        return ""
    path = ROOT / note
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def search_rows(args: argparse.Namespace) -> list[tuple[str, str, str, str]]:
    terms = args.terms
    results: list[tuple[str, str, str, str]] = []

    if args.kind in {"all", "issue"}:
        for row in read_csv(ROOT / "indexes" / "issues.csv"):
            if args.pattern and args.pattern not in row.get("top_patterns", ""):
                continue
            if args.domain and args.domain not in row.get("work_area", ""):
                continue
            if terms and not contains(row_text(row), terms):
                continue
            title = row.get("title", "")
            detail = f"patterns={row.get('top_patterns','')} comments={row.get('comment_body_status','')}"
            results.append(("issue", row.get("issue_number", ""), title, detail))

    if args.kind in {"all", "pr"}:
        for row in read_csv(ROOT / "indexes" / "prs.csv"):
            if args.pattern and args.pattern not in row.get("top_patterns", ""):
                continue
            if args.domain and args.domain not in row.get("work_area", ""):
                continue
            if terms and not contains(row_text(row), terms):
                continue
            detail = f"patterns={row.get('top_patterns','')} merged={row.get('merged','')}"
            results.append(("pr", row.get("pr_number", ""), row.get("title", ""), detail))

    if args.kind in {"all", "ledger"}:
        for row in read_csv(ROOT / "candidates" / "bitwise_ledger.csv"):
            if args.mechanism and args.mechanism != row.get("mechanism", ""):
                continue
            if args.decision and args.decision != row.get("status", ""):
                continue
            note_text = read_note(row)
            if terms and not contains(row_text(row) + " " + note_text, terms):
                continue
            detail = f"{row.get('mechanism','')} status={row.get('status','')} next={row.get('next_action','')} note={row.get('note','')}"
            title = note_text.splitlines()[0].lstrip("# ").strip() if note_text else row.get("id", "")
            results.append(("ledger", row.get("id", ""), title, detail))

    if args.kind in {"all", "page"}:
        for path in sorted(ROOT.rglob("*.md")):
            rel = path.relative_to(ROOT).as_posix()
            if rel.startswith("audit/iteration_"):
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            if terms and not contains(text, terms):
                continue
            title_match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
            title = title_match.group(1) if title_match else rel
            results.append(("page", rel, title, "markdown"))

    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("terms", nargs="*", help="Terms that must all appear.")
    parser.add_argument("--kind", choices=["all", "issue", "pr", "page", "ledger"], default="all")
    parser.add_argument("--pattern", help="Filter issue/PR rows by top pattern id.")
    parser.add_argument("--domain", help="Filter issue/PR rows by work_area fragment.")
    parser.add_argument("--mechanism", help="Filter candidate ledger by mechanism.")
    parser.add_argument(
        "--decision",
        choices=["stable", "include_with_boundary", "defer_blocked", "unresolved_review_risk"],
        help="Filter candidate ledger by status.",
    )
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--compact", action="store_true")
    args = parser.parse_args()

    for kind, ident, title, detail in search_rows(args)[: args.limit]:
        if args.compact:
            print(f"{kind}\t{ident}\t{title}")
        else:
            print(f"[{kind}] {ident} {title}\n  {detail}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
