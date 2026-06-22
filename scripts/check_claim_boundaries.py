\"\"\"Check claim boundary rules for curated bitwise pages.\"\"\"

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def check_stable_no_open_pr(errors: list[str]) -> None:
    for md in (ROOT / \"curated\" / \"bitwise\").glob(\"*.md\"):
        if md.name in (\"README.md\", \"next.md\"):
            continue
        text = md.read_text(encoding=\"utf-8\", errors=\"replace\")
        stable_start = text.find(\"## 稳定证据\")
        boundary_start = text.find(\"## 边界与反例\")
        if stable_start == -1 or boundary_start == -1:
            continue
        stable_section = text[stable_start:boundary_start]
        lower = stable_section.lower()
        if \"open pr\" in lower:
            errors.append(f\"{md.relative_to(ROOT)}: stable evidence contains open PR claim\")
        if \"include with boundary\" in lower or \"include_with_boundary\" in lower:
            errors.append(f\"{md.relative_to(ROOT)}: stable evidence contains include_with_boundary\")
        if \"defer_blocked\" in lower:
            errors.append(f\"{md.relative_to(ROOT)}: stable evidence contains defer_blocked\")
        # Check for comment-level claims without permalink
        if \"comment\" in lower and \"https://github.com\" not in lower:
            errors.append(f\"{md.relative_to(ROOT)}: comment-level claim lacks permalink\")


def check_readme_consistency(errors: list[str]) -> None:
    readme = ROOT / \"README.md\"
    maintenance = ROOT / \"docs\" / \"maintenance.md\"
    if not readme.exists() or not maintenance.exists():
        return
    readme_text = readme.read_text(encoding=\"utf-8\", errors=\"replace\")
    maintenance_text = maintenance.read_text(encoding=\"utf-8\", errors=\"replace\")
    if \"curated\" in readme_text and \"curated\" not in maintenance_text:
        errors.append(\"README.md mentions curated but maintenance.md does not define its scope\")


def main() -> int:
    errors: list[str] = []
    check_stable_no_open_pr(errors)
    check_readme_consistency(errors)
    if errors:
        for err in errors:
            print(f\"CLAIM_BOUNDARY: {err}\")
        return 1
    print(\"All claim boundary rules OK.\")
    return 0


if __name__ == \"__main__\":
    raise SystemExit(main())
