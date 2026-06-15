"""Run one automated VllmWiki iteration and write an audit report."""

from __future__ import annotations

import csv
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
WIKI = ROOT / "VllmWiki"
SCRIPTS = WIKI / "scripts"


CORE_LINK_FILES = [
    WIKI / "README.md",
    WIKI / "WIKI_IMPLEMENTATION.md",
    WIKI / "ITERATION_PROTOCOL.md",
    WIKI / "OPTIMIZATION_FLOW.md",
    WIKI / "QUALITY_GATE.md",
    WIKI / "curated" / "bitwise_determinism.md",
]


def run_step(name: str, args: list[str]) -> dict:
    started = datetime.now(timezone.utc)
    proc = subprocess.run(
        [sys.executable, *args],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    finished = datetime.now(timezone.utc)
    return {
        "name": name,
        "args": args,
        "returncode": proc.returncode,
        "started_at_utc": started.isoformat(),
        "finished_at_utc": finished.isoformat(),
        "stdout_tail": proc.stdout[-2000:],
        "stderr_tail": proc.stderr[-4000:],
    }


def read_csv_count(path: Path) -> int:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return sum(1 for _ in csv.DictReader(handle))


def check_links() -> list[dict]:
    files = CORE_LINK_FILES + list((WIKI / "curated" / "bitwise").glob("*.md"))
    missing = []
    for md in files:
        if not md.exists():
            missing.append({"file": str(md), "href": "<file missing>", "target": str(md)})
            continue
        text = md.read_text(encoding="utf-8")
        for match in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", text):
            href = match.group(1)
            if href.startswith(("http://", "https://", "#")):
                continue
            target = (md.parent / href.split("#")[0]).resolve()
            if not target.exists():
                missing.append({"file": str(md), "href": href, "target": str(target)})
    return missing


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_report(report: dict) -> None:
    audit_dir = WIKI / "audit"
    audit_dir.mkdir(parents=True, exist_ok=True)
    stamp = report["iteration_id"]
    (audit_dir / f"iteration_{stamp}.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    lines = [
        f"# VllmWiki 迭代 {stamp}",
        "",
        f"状态：`{report['status']}`",
        f"生成时间 UTC：`{report['generated_at_utc']}`",
        "",
        "## 步骤",
        "",
        "| 步骤 | 返回码 |",
        "| --- | ---: |",
    ]
    for step in report["steps"]:
        lines.append(f"| `{step['name']}` | {step['returncode']} |")
    lines.extend([
        "",
        "## 指标",
        "",
        "| 指标 | 值 |",
        "| --- | ---: |",
    ])
    for key, value in report["metrics"].items():
        lines.append(f"| `{key}` | {value:,} |")
    lines.extend(["", "## 链接检查", ""])
    if report["missing_links"]:
        lines.append("| 文件 | Href | 目标 |")
        lines.append("| --- | --- | --- |")
        for row in report["missing_links"]:
            lines.append(f"| `{row['file']}` | `{row['href']}` | `{row['target']}` |")
    else:
        lines.append("已检查的核心文件中没有缺失的本地链接。")
    lines.extend(["", "## 下一轮焦点", ""])
    lines.extend(f"- {item}" for item in report["next_focus"])
    (audit_dir / f"iteration_{stamp}.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    steps = [
        run_step("generate_vllm_wiki", [str(SCRIPTS / "generate_vllm_wiki.py")]),
        run_step("generate_bitwise_review_queue", [str(SCRIPTS / "generate_bitwise_review_queue.py")]),
        run_step("validate_vllmwiki", [str(SCRIPTS / "validate_vllmwiki.py"), "--json"]),
    ]
    missing_links = check_links()
    manifest = load_json(WIKI / "audit" / "manifest.json")
    metrics = {
        "unique_issues": manifest["coverage"]["unique_issues"],
        "unique_cases": manifest["coverage"]["unique_cases"],
        "unique_prs": manifest["coverage"]["unique_prs"],
        "pattern_evidence_rows": manifest["coverage"]["pattern_evidence_rows"],
        "bitwise_queue_rows": read_csv_count(WIKI / "curated" / "bitwise_review_queue.csv"),
        "bitwise_ledger_rows": read_csv_count(WIKI / "candidates" / "bitwise_ledger.csv"),
        "bitwise_mechanism_pages": len(list((WIKI / "curated" / "bitwise").glob("*.md"))),
        "missing_core_links": len(missing_links),
    }
    status = "pass" if all(step["returncode"] == 0 for step in steps) and not missing_links else "needs_attention"
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    report = {
        "iteration_id": stamp,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": status,
        "steps": steps,
        "metrics": metrics,
        "missing_links": missing_links,
        "next_focus": [
            "审计 LoRA/external KV cache identity case：#44250、#30931/#31069、#38606。",
            "审计 KV metadata cleanup case：#39146/#43741、#39589/#39591、#42572。",
            "审计 deterministic dispatch case：#25404/#25603、#42240、#33383、#33537。",
            "审计 quant/load-order case：#38991、#42007/#42120、#23256。",
        ],
    }
    write_report(report)
    print(json.dumps({"status": status, "iteration_id": stamp, "metrics": metrics}, ensure_ascii=False))
    return 0 if status == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
