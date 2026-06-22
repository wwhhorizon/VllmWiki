"""Validate VllmWiki structure, links, and KernelWiki-style governance files."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


REQUIRED = [
    "README.md",
    "WIKI_IMPLEMENTATION.md",
    "Agent_loop.md",
    "audit/manifest.md",
    "data/schemas.yaml",
    "data/tags.yaml",
    "data/aliases.yaml",
    "data/version-claims.yaml",
    "candidates/bitwise_ledger.csv",
    "curated/bitwise/README.md",
    "curated/bitwise/next.md",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def check_required(errors: list[str]) -> None:
    for rel in REQUIRED:
        if not (ROOT / rel).exists():
            errors.append(f"missing required file: {rel}")


def check_links(errors: list[str], full: bool = False) -> None:
    if full:
        files = list(ROOT.rglob("*.md"))
    else:
        files = [
            ROOT / "README.md",
            ROOT / "WIKI_IMPLEMENTATION.md",
            ROOT / "Agent_loop.md",
            ROOT / "curated" / "bitwise" / "README.md",
            ROOT / "curated" / "bitwise" / "next.md",
            *sorted((ROOT / "curated" / "bitwise").glob("*.md")),
        ]
    for md in files:
        if not md.exists():
            continue
        if md.parts[-2:] and "audit" in md.parts and md.name.startswith("iteration_"):
            continue
        text = md.read_text(encoding="utf-8", errors="replace")
        for match in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", text):
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
                errors.append(f"external local link escapes wiki: {md.relative_to(ROOT)} -> {href}")
                continue
            if not target.exists():
                errors.append(f"broken local link: {md.relative_to(ROOT)} -> {href}")


def check_manifest(errors: list[str], warnings: list[str]) -> None:
    manifest_md = ROOT / "audit" / "manifest.md"
    if not manifest_md.exists():
        errors.append("missing audit/manifest.md")
        return
    manifest_path = ROOT / "audit" / "manifest.json"
    if not manifest_path.exists():
        warnings.append("audit/manifest.json is local-generated and not present; skipped coverage numeric checks")
        return
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    coverage = manifest.get("coverage", {})
    if coverage.get("missing_issue_pages", 1) != 0:
        errors.append(f"missing issue pages: {coverage.get('missing_issue_pages')}")
    if coverage.get("unique_issues", 0) < 15000:
        warnings.append("unique issue coverage looks unexpectedly low")


def check_bitwise_ledger(errors: list[str], warnings: list[str]) -> None:
    path = ROOT / "candidates" / "bitwise_ledger.csv"
    if not path.exists():
        return
    rows = read_csv(path)
    required = {
        "id", "status", "priority", "mechanism", "next_action", "note",
    }
    if rows:
        missing = required.difference(rows[0])
        if missing:
            errors.append(f"bitwise ledger missing columns: {sorted(missing)}")
    malformed = [row.get("id", "<missing id>") for row in rows if row.get(None)]
    if malformed:
        errors.append(f"bitwise ledger has malformed CSV rows with extra fields: {malformed}")
    allowed_status = {"stable", "include_with_boundary", "defer_blocked", "unresolved_review_risk"}
    bad_status = sorted({row.get("status", "") for row in rows} - allowed_status)
    if bad_status:
        errors.append(f"bitwise ledger has unknown status values: {bad_status}")
    allowed_priority = {"high", "medium", "low"}
    bad_priority = sorted({row.get("priority", "") for row in rows} - allowed_priority)
    if bad_priority:
        errors.append(f"bitwise ledger has unknown priority values: {bad_priority}")
    allowed_actions = {
        "monitor_regression",
        "track_boundary_closure",
        "track_review_resolution",
        "collect_missing_evidence",
        "review_note",
    }
    bad_actions = sorted({row.get("next_action", "") for row in rows} - allowed_actions)
    if bad_actions:
        errors.append(f"bitwise ledger has unknown next_action values: {bad_actions}")
    for row in rows:
        note = row.get("note", "")
        if not note:
            errors.append(f"bitwise ledger row missing note path: {row.get('id')}")
            continue
        note_path = ROOT / note
        if not note_path.exists():
            errors.append(f"bitwise ledger note does not exist: {row.get('id')} -> {note}")
        if max(len(value) for value in row.values()) > 120:
            warnings.append(f"bitwise ledger row has unexpectedly long machine field: {row.get('id')}")


def check_bitwise_evidence(errors: list[str], warnings: list[str]) -> None:
    path = ROOT / "evidence" / "bitwise_sources.csv"
    if not path.exists():
        return
    rows = read_csv(path)
    source_types = {row.get("source_type", "") for row in rows}
    if len(rows) < 1000:
        warnings.append(f"bitwise evidence index looks small: {len(rows)} rows")
    if not {"issue", "pull"}.issubset(source_types):
        errors.append(f"bitwise evidence index missing source types: {sorted(source_types)}")


def check_curated_markers(errors: list[str], warnings: list[str]) -> None:
    for md in (ROOT / "curated").rglob("*.md"):
        text = md.read_text(encoding="utf-8", errors="replace")
        if "Status:" not in text and "状态：" not in text:
            warnings.append(f"curated page missing Status marker: {md.relative_to(ROOT)}")
        if "github.com/vllm-project/vllm/" not in text and "bitwise_review_queue" not in md.name:
            warnings.append(f"curated page has no upstream vLLM source URL: {md.relative_to(ROOT)}")
        if md.name != "bitwise_review_queue.md" and "##" not in text:
            errors.append(f"curated page has no section headings: {md.relative_to(ROOT)}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--full", action="store_true", help="Also validate generated case/pattern/domain pages.")
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []
    check_required(errors)
    check_links(errors, full=args.full)
    check_manifest(errors, warnings)
    check_bitwise_ledger(errors, warnings)
    check_bitwise_evidence(errors, warnings)
    check_curated_markers(errors, warnings)

    status = "pass" if not errors else "fail"
    report = {"status": status, "errors": errors, "warnings": warnings}
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"status: {status}")
        for err in errors:
            print(f"ERROR: {err}")
        for warning in warnings:
            print(f"WARN: {warning}")
    return 0 if status == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
