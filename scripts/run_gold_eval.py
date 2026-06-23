"""Run gold eval against curated bitwise conclusions."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GOLD_PATH = ROOT / "data" / "gold_cases.json"


def load_gold() -> dict:
    if not GOLD_PATH.exists():
        print(f"Gold cases file not found: {GOLD_PATH}")
        return {"cases": []}
    return json.loads(GOLD_PATH.read_text(encoding="utf-8"))


def evaluate() -> dict:
    gold = load_gold()
    cases = gold.get("cases", [])
    if not cases:
        return {"decision_diff_count": 0, "judge_result": "skip", "total_cases": 0}

    diffs = 0
    for case in cases:
        upstream_id = case.get("upstream_id", "")
        expected = case.get("expected_classification", "")
        note_path = ROOT / "candidates" / "notes" / f"{upstream_id}.md"
        if not note_path.exists():
            diffs += 1
            continue
        text = note_path.read_text(encoding="utf-8", errors="replace")
        if expected and expected not in text:
            diffs += 1

    total = len(cases)
    result = "pass" if diffs == 0 else "needs_review"
    return {
        "decision_diff_count": diffs,
        "judge_result": result,
        "total_cases": total,
    }


def main() -> int:
    result = evaluate()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["judge_result"] in {"pass", "skip"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
