"""Regex search across VllmWiki markdown and ledger text."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


GROUPS = {
    "wiki": ["README.md", "METHODOLOGY.md", "WIKI_IMPLEMENTATION.md", "ITERATION_PROTOCOL.md", "OPTIMIZATION_FLOW.md", "QUALITY_GATE.md", "KDA_RESEARCH_NOTES.md", "curated", "patterns", "domains"],
    "cases": ["cases"],
    "sources": ["indexes", "evidence", "candidates", "data"],
}


def iter_paths(group: str | None):
    roots = GROUPS.get(group or "wiki", [])
    if group is None:
        roots = sorted(set(sum(GROUPS.values(), [])))
    for item in roots:
        path = ROOT / item
        if path.is_file():
            yield path
        elif path.exists():
            for child in path.rglob("*"):
                if child.suffix.lower() in {".md", ".csv", ".yaml", ".json"}:
                    yield child


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pattern")
    parser.add_argument("--only", choices=["wiki", "cases", "sources"], help="Restrict search group.")
    parser.add_argument("--ignore-case", action="store_true")
    parser.add_argument("--limit", type=int, default=80)
    args = parser.parse_args()

    flags = re.IGNORECASE if args.ignore_case else 0
    rx = re.compile(args.pattern, flags)
    count = 0
    for path in iter_paths(args.only):
        text = path.read_text(encoding="utf-8", errors="replace")
        for lineno, line in enumerate(text.splitlines(), 1):
            if rx.search(line):
                print(f"{path.relative_to(ROOT).as_posix()}:{lineno}: {line[:220]}")
                count += 1
                if count >= args.limit:
                    return 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
