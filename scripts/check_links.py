"""Check all internal wiki links for breakage."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def check_links():
    files = list(ROOT.rglob("*.md"))
    missing = []
    link_re = re.compile(r'\]\(([^)]+)\)')
    for md in files:
        if "audit" in md.parts:
            continue
        text = md.read_text(encoding="utf-8", errors="replace")
        for match in link_re.finditer(text):
            href = match.group(1)
            if href.startswith(("http://", "https://", "mailto:", "#")):
                continue
            href_path = href.split("#", 1)[0]
            if not href_path:
                continue
            target = (md.parent / href_path).resolve()
            try:
                target.relative_to(ROOT.resolve())
            except ValueError:
                missing.append(dict(file=str(md.relative_to(ROOT)), href=href, target=str(target)))
                continue
            if not target.exists():
                missing.append(dict(file=str(md.relative_to(ROOT)), href=href, target=str(target)))
    return missing


def main():
    missing = check_links()
    if missing:
        print(f"Found {len(missing)} broken link(s):")
        for m in missing:
            print(f"  {m['file']} -> {m['href']} (target: {m['target']})")
        return 1
    print("All internal links OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
