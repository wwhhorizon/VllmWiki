"""Generate a ledger-driven bitwise review draft from local targeted evidence.

The script is intentionally read-only with respect to curated wiki pages. It
selects unresolved ledger rows, extracts adjacent evidence from the local
targeted GitHub JSON cache, and writes a Chinese review draft under audit/.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE_ROOT = ROOT.parent / "all" / "data" / "targeted" / "bitwise"
LEDGER_PATH = ROOT / "candidates" / "bitwise_ledger.csv"
DEFAULT_AUDIT_DIR = ROOT / "audit"

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


KEYWORDS = [
    "bitwise",
    "determin",
    "prefix",
    "cache",
    "kv",
    "lora",
    "adapter",
    "split",
    "splitk",
    "atomic",
    "fp8",
    "rope",
    "block",
    "tail",
    "dtype",
    "quant",
    "allclose",
    "equal",
]

RISK_ACTIONS = {
    "include_with_boundary": "复核边界是否已经由 follow-up patch、review resolution 或测试覆盖闭环；若没有，只能写成适用边界。",
    "unresolved_review_risk": "优先精读 review comment 和后续 diff，区分已修风险、未修风险和测试盲区。",
    "defer_blocked": "继续寻找 linked fix PR、changed files、测试或 maintainer resolution；未闭环前保持 defer。",
    "stable": "已进入稳定结论层，只在出现新证据时复核。",
}


@dataclass(frozen=True)
class EvidenceDoc:
    kind: str
    number: str
    path: Path
    data: dict[str, Any]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def split_values(values: list[str] | None) -> set[str]:
    if not values:
        return set()
    result: set[str] = set()
    for value in values:
        for part in value.split(","):
            part = part.strip()
            if part:
                result.add(part)
    return result


def row_blob(row: dict[str, str]) -> str:
    return " ".join(value or "" for value in row.values())


def related_numbers(row: dict[str, str]) -> list[str]:
    seen: set[str] = set()
    numbers: list[str] = []
    primary = row.get("source_number", "").strip()
    if primary:
        seen.add(primary)
        numbers.append(primary)
    for number in re.findall(r"#(\d+)", row_blob(row)):
        if number not in seen:
            seen.add(number)
            numbers.append(number)
    return numbers


def load_json(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None


def load_evidence(evidence_root: Path, row: dict[str, str]) -> list[EvidenceDoc]:
    docs: list[EvidenceDoc] = []
    for number in related_numbers(row):
        for kind, dirname in (("issue", "issues"), ("pull", "pulls")):
            path = evidence_root / dirname / f"{number}.json"
            data = load_json(path)
            if data is not None:
                docs.append(EvidenceDoc(kind=kind, number=number, path=path, data=data))
    return docs


def as_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    return json.dumps(value, ensure_ascii=False, sort_keys=True)


def as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def compact(text: str, limit: int = 380) -> str:
    text = re.sub(r"\s+", " ", as_text(text)).strip()
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def compact_block(text: str, limit: int = 620) -> str:
    text = as_text(text).strip()
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def body_head(body: str, limit: int = 700) -> str:
    body = as_text(body).strip()
    if not body:
        return "未提供正文。"
    lines = [line.strip() for line in body.splitlines() if line.strip()]
    return compact(" / ".join(lines[:6]), limit=limit)


def score_text(text: str) -> int:
    lower = text.lower()
    return sum(1 for keyword in KEYWORDS if keyword in lower)


def best_patch_excerpt(patch: str, limit: int = 620) -> str:
    patch = as_text(patch)
    if not patch:
        return "无 patch 摘录。"
    lines = patch.splitlines()
    scored: list[tuple[int, int, str]] = []
    for index, line in enumerate(lines):
        if line.startswith(("+", "-", "@@")):
            scored.append((score_text(line), index, line))
    scored.sort(key=lambda item: (item[0], -item[1]), reverse=True)
    anchors = sorted({index for score, index, _ in scored[:5] if score > 0})
    if not anchors:
        anchors = [0]
    selected: list[str] = []
    used: set[int] = set()
    for anchor in anchors[:3]:
        for index in range(max(0, anchor - 2), min(len(lines), anchor + 3)):
            if index not in used:
                used.add(index)
                selected.append(lines[index])
    return compact_block("\n".join(selected), limit=limit)


def extract_title(doc: EvidenceDoc) -> str:
    if doc.kind == "pull":
        return as_text(doc.data.get("pull", {}).get("title"))
    return as_text(doc.data.get("issue", {}).get("title"))


def extract_body(doc: EvidenceDoc) -> str:
    if doc.kind == "pull":
        return as_text(doc.data.get("pull", {}).get("body"))
    return as_text(doc.data.get("issue", {}).get("body"))


def extract_files(doc: EvidenceDoc, limit: int = 6) -> list[dict[str, str]]:
    files = as_list(doc.data.get("files")) if doc.kind == "pull" else []
    scored = sorted(
        [file for file in files if isinstance(file, dict)],
        key=lambda item: score_text(" ".join([as_text(item.get("filename")), as_text(item.get("patch"))])),
        reverse=True,
    )
    result: list[dict[str, str]] = []
    for file in scored[:limit]:
        result.append(
            {
                "filename": as_text(file.get("filename")),
                "status": as_text(file.get("status")),
                "changes": as_text(file.get("changes")),
                "patch": best_patch_excerpt(as_text(file.get("patch"))),
            }
        )
    return result


def extract_review_comments(doc: EvidenceDoc, limit: int = 8) -> list[dict[str, str]]:
    comments = as_list(doc.data.get("review_comments")) if doc.kind == "pull" else []
    scored = sorted(
        [comment for comment in comments if isinstance(comment, dict)],
        key=lambda item: score_text(" ".join([as_text(item.get("path")), as_text(item.get("body")), as_text(item.get("diff_hunk"))])),
        reverse=True,
    )
    result: list[dict[str, str]] = []
    for comment in scored[:limit]:
        result.append(
            {
                "path": as_text(comment.get("path")),
                "url": as_text(comment.get("html_url")),
                "body": compact(as_text(comment.get("body")), limit=520),
                "diff_hunk": compact(as_text(comment.get("diff_hunk")), limit=420),
            }
        )
    return result


def extract_conversation(doc: EvidenceDoc, limit: int = 5) -> list[dict[str, str]]:
    if doc.kind == "pull":
        raw_items = [
            *as_list(doc.data.get("issue_comments")),
            *as_list(doc.data.get("reviews")),
        ]
    else:
        raw_items = [
            *as_list(doc.data.get("comments")),
            *as_list(doc.data.get("timeline")),
        ]
    items = [item for item in raw_items if isinstance(item, dict)]
    scored = sorted(
        items,
        key=lambda item: score_text(" ".join([as_text(item.get("event")), as_text(item.get("state")), as_text(item.get("body"))])),
        reverse=True,
    )
    result: list[dict[str, str]] = []
    for item in scored[:limit]:
        body = as_text(item.get("body"))
        event = as_text(item.get("event") or item.get("state") or "comment")
        url = as_text(item.get("html_url") or item.get("url"))
        if body or event:
            result.append({"event": event, "url": url, "body": compact(body, limit=430)})
    return result


def evidence_summary(doc: EvidenceDoc) -> dict[str, Any]:
    return {
        "kind": doc.kind,
        "number": doc.number,
        "path": str(doc.path),
        "title": extract_title(doc),
        "body_head": body_head(extract_body(doc)),
        "files": extract_files(doc),
        "review_comments": extract_review_comments(doc),
        "conversation": extract_conversation(doc),
    }


def select_rows(
    rows: list[dict[str, str]],
    *,
    limit: int,
    priorities: set[str],
    risk_statuses: set[str],
    include_stable: bool,
) -> list[dict[str, str]]:
    def keep(row: dict[str, str]) -> bool:
        if priorities and row.get("priority") not in priorities:
            return False
        if risk_statuses and row.get("risk_status") not in risk_statuses:
            return False
        if not risk_statuses and not include_stable and row.get("risk_status") == "stable":
            return False
        return True

    priority_rank = {"high": 0, "medium": 1, "low": 2}
    risk_rank = {"unresolved_review_risk": 0, "include_with_boundary": 1, "defer_blocked": 2, "stable": 3}
    selected = [row for row in rows if keep(row)]
    selected.sort(
        key=lambda row: (
            priority_rank.get(row.get("priority", ""), 9),
            risk_rank.get(row.get("risk_status", ""), 9),
            row.get("mechanism", ""),
            row.get("source_number", ""),
        )
    )
    return selected[:limit]


def build_cycle(rows: list[dict[str, str]], evidence_root: Path) -> dict[str, Any]:
    entries: list[dict[str, Any]] = []
    for row in rows:
        docs = load_evidence(evidence_root, row)
        entries.append(
            {
                "id": row.get("id"),
                "source_number": row.get("source_number"),
                "mechanism": row.get("mechanism"),
                "decision": row.get("decision"),
                "risk_status": row.get("risk_status"),
                "priority": row.get("priority"),
                "review_depth": row.get("review_depth"),
                "blocking_reason": row.get("blocking_reason"),
                "target_evidence": row.get("target_evidence"),
                "promotion_reason": row.get("promotion_reason"),
                "next_action": row.get("next_action"),
                "suggested_action": RISK_ACTIONS.get(row.get("risk_status", ""), "按 ledger 记录人工复核。"),
                "related_numbers": related_numbers(row),
                "evidence": [evidence_summary(doc) for doc in docs],
                "missing_evidence": missing_evidence(row, docs),
            }
        )
    return {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "evidence_root": str(evidence_root),
        "ledger": str(LEDGER_PATH),
        "entries": entries,
    }


def missing_evidence(row: dict[str, str], docs: list[EvidenceDoc]) -> list[str]:
    missing: list[str] = []
    kinds = {doc.kind for doc in docs}
    if row.get("source_type") in {"pr", "issue_pr_pair"} and "pull" not in kinds:
        missing.append("未找到本地 PR targeted JSON。")
    if row.get("source_type") in {"issue", "issue_pr_pair"} and "issue" not in kinds:
        missing.append("未找到本地 issue targeted JSON。")
    if not docs:
        missing.append("没有任何本地 targeted evidence 命中。")
    for doc in docs:
        if doc.kind == "pull" and not extract_review_comments(doc):
            missing.append(f"PR #{doc.number} 没有 review comment 摘录，若风险来自 review，需要定向补抓或确认无评论。")
        if doc.kind == "pull" and not extract_files(doc):
            missing.append(f"PR #{doc.number} 没有 files/patch 摘录。")
    return missing


def md_escape(text: str) -> str:
    return as_text(text).replace("|", "\\|")


def render_markdown(cycle: dict[str, Any]) -> str:
    lines: list[str] = []
    lines.append("# Bitwise 持续复核草稿")
    lines.append("")
    lines.append(f"生成时间：{cycle['generated_at_utc']}")
    lines.append(f"证据根目录：`{cycle['evidence_root']}`")
    lines.append("")
    lines.append("用途：这是一份从 ledger 和本地 targeted evidence 自动生成的人工精读草稿。它不代表 promotion，也不会自动修改机制页。")
    lines.append("")
    lines.append("## 本轮对象")
    lines.append("")
    lines.append("| ID | 机制 | 决策 | 风险状态 | 优先级 | 复核深度 |")
    lines.append("| --- | --- | --- | --- | --- | --- |")
    for entry in cycle["entries"]:
        lines.append(
            "| {id} | {mechanism} | {decision} | {risk_status} | {priority} | {review_depth} |".format(
                id=md_escape(entry["id"]),
                mechanism=md_escape(entry["mechanism"]),
                decision=md_escape(entry["decision"]),
                risk_status=md_escape(entry["risk_status"]),
                priority=md_escape(entry["priority"]),
                review_depth=md_escape(entry["review_depth"]),
            )
        )
    lines.append("")
    for entry in cycle["entries"]:
        lines.append(f"## {entry['id']}：{entry['mechanism']}")
        lines.append("")
        lines.append(f"- 当前决策：`{entry['decision']}`")
        lines.append(f"- 风险状态：`{entry['risk_status']}`")
        lines.append(f"- 建议动作：{entry['suggested_action']}")
        if entry.get("blocking_reason"):
            lines.append(f"- 阻塞原因：{entry['blocking_reason']}")
        if entry.get("target_evidence"):
            lines.append(f"- 目标证据：{entry['target_evidence']}")
        if entry.get("promotion_reason"):
            lines.append(f"- 既有炼化结论：{entry['promotion_reason']}")
        if entry.get("next_action"):
            lines.append(f"- 下一步：{entry['next_action']}")
        if entry["missing_evidence"]:
            lines.append("- 证据缺口：" + "；".join(entry["missing_evidence"]))
        lines.append("")
        lines.append("### 命中证据")
        lines.append("")
        if not entry["evidence"]:
            lines.append("未命中本地 targeted evidence。")
            lines.append("")
            continue
        for evidence in entry["evidence"]:
            label = "PR" if evidence["kind"] == "pull" else "Issue"
            lines.append(f"#### {label} #{evidence['number']}")
            lines.append("")
            lines.append(f"- 本地路径：`{evidence['path']}`")
            if evidence["title"]:
                lines.append(f"- 标题：{evidence['title']}")
            lines.append(f"- 正文摘要：{evidence['body_head']}")
            if evidence["files"]:
                lines.append("")
                lines.append("文件 / patch 摘录：")
                for file in evidence["files"]:
                    lines.append(f"- `{file['filename']}` ({file['status']}, changes={file['changes']})")
                    lines.append("")
                    lines.append("```diff")
                    lines.append(file["patch"])
                    lines.append("```")
            if evidence["review_comments"]:
                lines.append("")
                lines.append("Review comment 摘录：")
                for comment in evidence["review_comments"]:
                    lines.append(f"- `{comment['path']}`：{comment['body']}")
                    if comment["url"]:
                        lines.append(f"  来源：{comment['url']}")
                    if comment["diff_hunk"]:
                        lines.append("")
                        lines.append("```diff")
                        lines.append(comment["diff_hunk"])
                        lines.append("```")
            if evidence["conversation"]:
                lines.append("")
                lines.append("评论 / review / timeline 摘录：")
                for item in evidence["conversation"]:
                    body = item["body"] or "(无正文)"
                    lines.append(f"- `{item['event']}`：{body}")
                    if item["url"]:
                        lines.append(f"  来源：{item['url']}")
            lines.append("")
        lines.append("### 人工复核记录")
        lines.append("")
        lines.append("- 根因是否由 diff/comment 闭环：待填写")
        lines.append("- fix 类型是根因修复、workaround、support gate 还是测试放置：待填写")
        lines.append("- exact test 覆盖了什么：待填写")
        lines.append("- 没覆盖的边界：待填写")
        lines.append("- 是否更新机制页 / ledger / BITWISE_NEXT：待填写")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def default_output_path(as_json: bool) -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    suffix = "json" if as_json else "md"
    return DEFAULT_AUDIT_DIR / f"bitwise_cycle_{stamp}.{suffix}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=5, help="最多选择多少个 ledger 条目。")
    parser.add_argument("--risk-status", action="append", help="筛选 risk_status，可重复或逗号分隔。")
    parser.add_argument("--priority", action="append", help="筛选 priority，可重复或逗号分隔；默认 high。")
    parser.add_argument("--include-stable", action="store_true", help="默认跳过 stable；设置后允许 stable 进入候选。")
    parser.add_argument("--ledger", type=Path, default=LEDGER_PATH)
    parser.add_argument("--evidence-root", type=Path, default=DEFAULT_EVIDENCE_ROOT)
    parser.add_argument("--output", type=Path, help="输出路径；默认写入 audit/bitwise_cycle_<timestamp>.md。")
    parser.add_argument("--json", action="store_true", help="输出 JSON 草稿而非 Markdown，并向 stdout 打印 JSON 摘要。")
    args = parser.parse_args()

    if args.limit <= 0:
        parser.error("--limit must be positive")
    if not args.ledger.exists():
        parser.error(f"ledger not found: {args.ledger}")
    if not args.evidence_root.exists():
        parser.error(f"evidence root not found: {args.evidence_root}")

    priorities = split_values(args.priority) or {"high"}
    risk_statuses = split_values(args.risk_status)
    rows = read_csv(args.ledger)
    selected = select_rows(
        rows,
        limit=args.limit,
        priorities=priorities,
        risk_statuses=risk_statuses,
        include_stable=args.include_stable,
    )
    cycle = build_cycle(selected, args.evidence_root)

    output = args.output or default_output_path(args.json)
    output.parent.mkdir(parents=True, exist_ok=True)
    if args.json:
        output.write_text(json.dumps(cycle, ensure_ascii=False, indent=2), encoding="utf-8")
    else:
        output.write_text(render_markdown(cycle), encoding="utf-8")

    summary = {
        "status": "ok",
        "output": str(output),
        "selected": [entry["id"] for entry in cycle["entries"]],
        "evidence_root": str(args.evidence_root),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
