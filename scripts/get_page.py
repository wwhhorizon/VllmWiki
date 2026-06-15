"""Fetch a VllmWiki page by issue number, PR number, page path, or ledger id."""

from __future__ import annotations

import argparse
import csv
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


def find_page(identifier: str, source: str | None) -> tuple[str, str] | None:
    if source in {None, "issue"} and identifier.isdigit():
        for row in read_csv(ROOT / "indexes" / "issues.csv"):
            if row.get("issue_number") == identifier:
                path = ROOT / row.get("wiki_page", "")
                return (str(path), path.read_text(encoding="utf-8", errors="replace"))

    if source in {None, "ledger"}:
        for row in read_csv(ROOT / "candidates" / "bitwise_ledger.csv"):
            if row.get("id") == identifier or row.get("source_number") == identifier:
                lines = [f"# Candidate {row.get('id','')}", ""]
                for key, value in row.items():
                    lines.append(f"- `{key}`: {value}")
                return (f"candidates/bitwise_ledger.csv:{identifier}", "\n".join(lines) + "\n")

    path = ROOT / identifier
    if path.exists() and path.is_file():
        return (str(path), path.read_text(encoding="utf-8", errors="replace"))

    matches = list(ROOT.rglob(identifier))
    if matches:
        path = matches[0]
        return (str(path), path.read_text(encoding="utf-8", errors="replace"))

    return None


def append_sources(text: str) -> str:
    links = []
    for line in text.splitlines():
        if "github.com/vllm-project/vllm/issues/" in line or "github.com/vllm-project/vllm/pull/" in line:
            links.append(line.strip())
    if not links:
        return text
    return text.rstrip() + "\n\n## Followed Source Links\n\n" + "\n".join(f"- {link}" for link in links[:40]) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("identifier", help="Issue number, page path, or ledger id.")
    parser.add_argument("--source", choices=["issue", "ledger", "path"], help="Restrict lookup source.")
    parser.add_argument("--follow-sources", action="store_true", help="Append detected upstream issue/PR links.")
    parser.add_argument("--frontmatter-only", action="store_true", help="Print only first metadata block/heading section.")
    args = parser.parse_args()

    found = find_page(args.identifier, args.source)
    if not found:
        print(f"not found: {args.identifier}")
        return 1
    path, text = found
    if args.follow_sources:
        text = append_sources(text)
    if args.frontmatter_only:
        text = "\n".join(text.splitlines()[:40]) + "\n"
    print(f"<!-- {path} -->")
    print(text, end="" if text.endswith("\n") else "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
