"""Generate the first VllmWiki from local vLLM issue/PR data.

The generator deliberately keeps evidence close to every conclusion.  It reads
the raw issue/PR bodies, the existing classification tables, and issue-PR links,
then emits a navigable markdown wiki plus machine-readable ledgers for audits.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "all" / "data"
OUT = ROOT / "VllmWiki"


WORK_AREA_NAMES = {
    "attention_kv_cache": "Attention 与 KV Cache",
    "moe": "MoE",
    "quantization": "量化与低精度",
    "gemm_linear": "GEMM 与 Linear Kernel",
    "sampling_logits": "采样与 Logits",
    "activation_norm": "激活与归一化",
    "model_support": "模型支持",
    "scheduler_memory": "调度与内存",
    "distributed_parallel": "分布式与并行",
    "frontend_api": "前端与 Serving API",
    "multimodal_vlm": "多模态与 VLM",
    "speculative_decoding": "投机解码",
    "ci_build": "CI、构建与打包",
    "hardware_porting": "硬件适配",
    "uncategorized": "未分类",
}


PATTERNS = {
    "bitwise_determinism_equivalence": {
        "title": "Bitwise 确定性与数值等价",
        "definition": "在 batch size、prefix-cache 命中/未命中、backend 选择、分布式形态和低精度 kernel 变化时，保持完全一致或接近完全一致的输出等价。",
        "keywords": [
            "bitwise", "deterministic", "non-deterministic", "nondeterministic",
            "reproducible", "reproduce", "same output", "different output",
            "numerical", "numeric", "mismatch", "allclose", "assert_close",
            "torch.allclose", "accuracy", "precision", "divergence", "drift",
            "batch invariance", "cache-hit", "cache hit", "cache-miss", "cache miss",
        ],
    },
    "backend_routing_fallback": {
        "title": "Backend 路由与 Fallback",
        "definition": "在 FlashAttention、FlashInfer、CUTLASS、Triton、ROCm/AITER 等执行 backend 之间进行选择、保护或 fallback。",
        "keywords": [
            "backend", "fallback", "flashattention", "flash attention", "flashinfer",
            "cutlass", "aiter", "triton", "routing", "dispatch", "fa3",
        ],
    },
    "metadata_layout_contract": {
        "title": "Metadata 与 Layout 契约",
        "definition": "修复传给 kernel 的 block table、slot mapping、LSE、stride、cache group、page size 或 attention metadata 中的语义漂移。",
        "keywords": [
            "metadata", "layout", "block", "slot", "stride", "lse", "page size",
            "page_size", "cache group", "mapping", "contiguous",
        ],
    },
    "dtype_quantization_path": {
        "title": "Dtype、量化与 Scale 路径",
        "definition": "让 dtype 转换、FP8/FP4/NVFP4/MXFP4/INT4/TQ4 量化、scale、packing 与 dequantization 显式且可测试。",
        "keywords": [
            "fp8", "fp4", "nvfp4", "mxfp4", "int4", "tq4", "quant", "scale",
            "dequant", "dtype", "bf16", "bfloat16", "float16", "float32",
        ],
    },
    "kv_cache_capacity_offload": {
        "title": "KV Cache 容量、压缩与 Offload",
        "definition": "调整 KV cache sizing、compression、offload、block identity、allocation 或 fit check，避免 OOM、死锁或精度损失。",
        "keywords": [
            "kv cache", "kv-cache", "cache capacity", "offload", "prefix cache",
            "block table", "cache dtype", "cache block", "gpu memory", "oom",
        ],
    },
    "moe_gemm_routing": {
        "title": "MoE、GEMM 与 Expert Routing",
        "definition": "优化或修正 grouped GEMM、expert routing、top-k、permute/unpermute、all-gather payload 与 MoE kernel dispatch。",
        "keywords": [
            "moe", "expert", "grouped gemm", "gemm", "topk", "top-k", "permute",
            "unpermute", "all-gather", "router", "routing",
        ],
    },
    "scheduler_request_lifecycle": {
        "title": "Scheduler 与请求状态生命周期",
        "definition": "修复 request admission、waiting queue、prefill/decode 切换、投机解码状态或 stale buffer。",
        "keywords": [
            "scheduler", "waiting", "deadlock", "request", "prefill", "decode",
            "spec decode", "speculative", "draft", "stale", "queue",
        ],
    },
    "hardware_arch_guard": {
        "title": "硬件架构 Guard",
        "definition": "根据 CUDA/ROCm 版本、SM 架构、GPU 家族、编译目标或 vendor backend 支持情况约束行为。",
        "keywords": [
            "cuda", "rocm", "hip", "sm", "blackwell", "hopper", "ampere",
            "b200", "h100", "a100", "mi300", "mi300x", "rtx", "arch",
            "ptxas", "capability",
        ],
    },
    "build_dependency_packaging": {
        "title": "构建、依赖与打包",
        "definition": "处理构建失败、wheel、依赖 pin、ABI/linker 错误、CI 镜像或安装兼容性问题。",
        "keywords": [
            "build", "compile", "cmake", "wheel", "glibc", "install", "dependency",
            "import", "undefined symbol", "link", "ci", "docker", "version",
        ],
    },
    "model_format_adapter": {
        "title": "模型格式与 Adapter 路径",
        "definition": "适配模型格式、Hugging Face layout、多模态输入、config 解析或模型专属执行路径。",
        "keywords": [
            "model", "hf", "huggingface", "format", "qwen", "llama", "gemma",
            "internvl", "gpt-oss", "multimodal", "vlm", "config",
        ],
    },
    "verification_benchmarking": {
        "title": "验证与 Benchmark",
        "definition": "增加或解释测试、benchmark 证据、回归检查、eval、确定性检查或性能 baseline。",
        "keywords": [
            "test", "benchmark", "regression", "throughput", "latency", "tpot",
            "accuracy", "deterministic", "eval", "profile", "profiling",
        ],
    },
}


@dataclass
class IssueRecord:
    number: int
    title: str
    url: str
    state: str
    labels: str
    body: str
    comments_count: int
    created_at: str
    updated_at: str
    source: str = "raw_issue_body"


@dataclass
class CaseRecord:
    number: int
    title: str
    url: str
    state: str
    primary_category: str
    matched_categories: str
    work_area: str
    sub_category: str
    operator_keywords: str
    symptom: str
    root_cause_hint: str
    solution_summary: str
    solution_type: str
    linked_prs: str
    hardware_scope: str
    needs_manual_review: str
    summary: str


@dataclass
class PrRecord:
    number: int
    title: str
    url: str
    state: str
    merged: str
    body: str
    summary: str
    primary_category: str
    work_area: str
    solution_type: str
    hardware_scope: str
    operator_keywords: str


@dataclass
class PatternHit:
    pattern: str
    issue_number: int | None = None
    pr_number: int | None = None
    score: int = 0
    evidence: str = ""
    source: str = ""


def read_jsonl(path: Path) -> Iterable[dict]:
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                yield json.loads(line)


def read_csv(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def count_lines(path: Path) -> int:
    with path.open("rb") as handle:
        return sum(1 for _ in handle)


def clean_text(text: str | None) -> str:
    if not text:
        return ""
    text = re.sub(r"\r\n?", "\n", text)
    text = re.sub(r"<details>.*?</details>", " ", text, flags=re.I | re.S)
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def split_multi(value: str | None) -> list[str]:
    if not value:
        return []
    parts = re.split(r"[;,]", str(value))
    return [p.strip() for p in parts if p.strip()]


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value or "item"


def truncate(value: str, limit: int = 180) -> str:
    value = re.sub(r"\s+", " ", value or "").strip()
    if len(value) <= limit:
        return value
    return value[: limit - 1].rstrip() + "..."


def markdown_escape(value: str | None) -> str:
    value = str(value or "")
    return value.replace("|", "\\|").replace("\n", " ")


def first_snippet(text: str, keywords: list[str], window: int = 220) -> str:
    lowered = text.lower()
    best = None
    for keyword in keywords:
        idx = lowered.find(keyword.lower())
        if idx >= 0 and (best is None or idx < best):
            best = idx
    if best is None:
        return truncate(text, window)
    start = max(0, best - window // 3)
    end = min(len(text), best + window)
    return truncate(text[start:end], window)


def load_issues() -> dict[int, IssueRecord]:
    issues = {}
    for obj in read_jsonl(DATA / "raw" / "issues_raw.jsonl"):
        labels = ";".join(label.get("name", "") for label in obj.get("labels") or [])
        issues[int(obj["number"])] = IssueRecord(
            number=int(obj["number"]),
            title=obj.get("title") or "",
            url=obj.get("html_url") or "",
            state=obj.get("state") or "",
            labels=labels,
            body=clean_text(obj.get("body")),
            comments_count=int(obj.get("comments") or 0),
            created_at=obj.get("created_at") or "",
            updated_at=obj.get("updated_at") or "",
        )
    return issues


def load_cases() -> dict[int, CaseRecord]:
    cases = {}
    for row in read_csv(DATA / "tables" / "cases.csv"):
        number = int(row.get("number") or row.get("issue_number") or 0)
        cases[number] = CaseRecord(
            number=number,
            title=row.get("title") or "",
            url=row.get("html_url") or row.get("url") or "",
            state=row.get("state") or "",
            primary_category=row.get("primary_category") or "",
            matched_categories=row.get("matched_categories") or "",
            work_area=row.get("work_area") or "",
            sub_category=row.get("sub_category") or "",
            operator_keywords=row.get("operator_keywords") or "",
            symptom=row.get("symptom") or "",
            root_cause_hint=row.get("root_cause_hint") or "",
            solution_summary=row.get("solution_summary") or "",
            solution_type=row.get("solution_type") or "",
            linked_prs=row.get("linked_prs") or "",
            hardware_scope=row.get("hardware_scope") or "",
            needs_manual_review=row.get("needs_manual_review") or "",
            summary=row.get("summary") or "",
        )
    return cases


def load_prs() -> dict[int, PrRecord]:
    raw = {}
    for obj in read_jsonl(DATA / "raw" / "prs_raw.jsonl"):
        raw[int(obj["number"])] = clean_text(obj.get("body"))
    prs = {}
    for row in read_csv(DATA / "tables" / "prs.csv"):
        number = int(row.get("pr_number") or 0)
        prs[number] = PrRecord(
            number=number,
            title=row.get("title") or "",
            url=row.get("url") or f"https://github.com/vllm-project/vllm/pull/{number}",
            state=row.get("state") or "",
            merged=row.get("merged") or "",
            body=raw.get(number, ""),
            summary=row.get("summary") or "",
            primary_category=row.get("primary_category") or "",
            work_area=row.get("work_area") or "",
            solution_type=row.get("solution_type") or "",
            hardware_scope=row.get("hardware_scope") or "",
            operator_keywords=row.get("operator_keywords") or "",
        )
    return prs


def load_links() -> dict[int, list[dict]]:
    links = defaultdict(list)
    for row in read_csv(DATA / "tables" / "issue_pr_links.csv"):
        try:
            issue_number = int(row.get("issue_number") or 0)
            pr_number = int(row.get("pr_number") or 0)
        except ValueError:
            continue
        if issue_number and pr_number:
            row["pr_number"] = pr_number
            links[issue_number].append(row)
    return links


def score_patterns(text: str) -> list[tuple[str, int, str]]:
    lowered = text.lower()
    hits = []
    for key, spec in PATTERNS.items():
        matched = [kw for kw in spec["keywords"] if kw.lower() in lowered]
        if matched:
            hits.append((key, len(matched), first_snippet(text, matched)))
    hits.sort(key=lambda item: (-item[1], item[0]))
    return hits


def issue_text(issue: IssueRecord, case: CaseRecord | None) -> str:
    parts = [issue.title, issue.labels, issue.body]
    if case:
        parts.extend([
            case.primary_category,
            case.work_area,
            case.operator_keywords,
            case.symptom,
            case.root_cause_hint,
            case.solution_summary,
            case.summary,
        ])
    return "\n".join(p for p in parts if p)


def pr_text(pr: PrRecord) -> str:
    return "\n".join([
        pr.title,
        pr.body,
        pr.summary,
        pr.work_area,
        pr.operator_keywords,
        pr.solution_type,
    ])


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def case_slug(number: int, title: str) -> str:
    return f"{number}-{slugify(title)[:70]}.md"


def build_case_page(
    issue: IssueRecord,
    case: CaseRecord | None,
    links: list[dict],
    prs: dict[int, PrRecord],
    pattern_hits: list[tuple[str, int, str]],
) -> str:
    title = case.title if case else issue.title
    lines = [
        f"# vllm-project/vllm#{issue.number}: {title}",
        "",
        "| 字段 | 值 |",
        "| --- | --- |",
        f"| Issue | [#{issue.number}]({issue.url}) |",
        f"| 状态 | {markdown_escape(issue.state)} |",
        f"| 标签 | {markdown_escape(issue.labels)} |",
        f"| 评论 | {issue.comments_count}; 本地原始数据只有评论数量，没有评论正文 |",
    ]
    if case:
        lines.extend([
            f"| 一级分类 | {markdown_escape(case.primary_category)} |",
            f"| 工作域 | {markdown_escape(case.work_area)} |",
            f"| 子分类 | {markdown_escape(case.sub_category)} |",
            f"| Operator 关键词 | {markdown_escape(case.operator_keywords)} |",
            f"| 症状 | {markdown_escape(case.symptom)} |",
            f"| 根因提示 | {markdown_escape(case.root_cause_hint)} |",
            f"| 硬件范围 | {markdown_escape(case.hardware_scope)} |",
            f"| 需要人工复核 | {markdown_escape(case.needs_manual_review)} |",
        ])
    lines.extend(["", "## 源证据", ""])
    lines.append("### Issue 标题")
    lines.append("")
    lines.append(f"> {markdown_escape(issue.title)}")
    lines.append("")
    lines.append("### Issue 正文摘录")
    lines.append("")
    excerpt = truncate(issue.body, 1200) or "_本地原始数据中没有 issue 正文。_"
    lines.append(excerpt)
    lines.append("")
    if case and case.solution_summary:
        lines.append("## 现有链接修复摘要")
        lines.append("")
        lines.append(case.solution_summary)
        lines.append("")
    if pattern_hits:
        lines.append("## 候选优化模式")
        lines.append("")
        for key, score, evidence in pattern_hits[:5]:
            spec = PATTERNS[key]
            lines.append(f"- [{spec['title']}](../patterns/{key}.md) - 分数 {score}: {evidence}")
        lines.append("")
    if links:
        lines.append("## 关联 PR 证据")
        lines.append("")
        lines.append("| PR | 链接类型 | 置信度 | PR 标题 | 证据 |")
        lines.append("| --- | --- | ---: | --- | --- |")
        for link in links[:20]:
            pr_number = int(link["pr_number"])
            pr = prs.get(pr_number)
            pr_title = pr.title if pr else ""
            pr_url = pr.url if pr else f"https://github.com/vllm-project/vllm/pull/{pr_number}"
            lines.append(
                f"| [#{pr_number}]({pr_url}) | {markdown_escape(link.get('link_type'))} | "
                f"{markdown_escape(link.get('confidence'))} | {markdown_escape(pr_title)} | "
                f"{markdown_escape(truncate(link.get('evidence') or '', 220))} |"
            )
        lines.append("")
    lines.append("## Wiki 抽取状态")
    lines.append("")
    if issue.comments_count and not links:
        lines.append("- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。")
    if not case:
        lines.append("- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。")
    if case and not case.solution_summary and not links:
        lines.append("- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。")
    lines.append("- 后续迭代应在可用时读取完整讨论评论。")
    return "\n".join(lines)


def build_pattern_page(
    key: str,
    issue_hits: list[PatternHit],
    pr_hits: list[PatternHit],
    cases: dict[int, CaseRecord],
    issues: dict[int, IssueRecord],
    prs: dict[int, PrRecord],
) -> str:
    spec = PATTERNS[key]
    category_counter = Counter()
    work_counter = Counter()
    for hit in issue_hits:
        if hit.issue_number in cases:
            case = cases[hit.issue_number]
            category_counter.update(split_multi(case.primary_category))
            work_counter.update(split_multi(case.work_area))
    lines = [
        f"# {spec['title']}",
        "",
        spec["definition"],
        "",
        "## 优化或修复的对象",
        "",
        "- 正确性：防止静默错误输出、崩溃、非确定性、stale metadata 或不受支持的 backend 使用。",
        "- 性能：让请求保持在预期的优化 backend 上，或移除热路径重复开销。",
        "- 可运维性：增加显式 guard、fallback、测试或依赖约束，让失败原因可理解。",
        "",
        "## 常见信号",
        "",
        ", ".join(f"`{kw}`" for kw in spec["keywords"]),
        "",
        "## 分布",
        "",
        f"- Issue 证据命中：{len(issue_hits)}",
        f"- PR 证据命中：{len(pr_hits)}",
        f"- 高频分类：{', '.join(f'{k}={v}' for k, v in category_counter.most_common(5)) or 'n/a'}",
        f"- 高频工作域：{', '.join(f'{k}={v}' for k, v in work_counter.most_common(8)) or 'n/a'}",
        "",
        "## 代表性 Issue 证据",
        "",
        "| Issue | 标题 | 分类 | 工作域 | 证据 |",
        "| --- | --- | --- | --- | --- |",
    ]
    for hit in sorted(issue_hits, key=lambda item: (-item.score, item.issue_number or 0))[:40]:
        if hit.issue_number is None:
            continue
        issue = issues[hit.issue_number]
        case = cases.get(hit.issue_number)
        case_path = f"../cases/{hit.issue_number // 1000:02d}xxx/{case_slug(hit.issue_number, issue.title)}"
        lines.append(
            f"| [#{hit.issue_number}]({case_path}) | {markdown_escape(issue.title)} | "
            f"{markdown_escape(case.primary_category if case else '')} | "
            f"{markdown_escape(case.work_area if case else '')} | {markdown_escape(hit.evidence)} |"
        )
    lines.extend(["", "## 代表性 PR 证据", "", "| PR | 标题 | 工作域 | 证据 |", "| --- | --- | --- | --- |"])
    for hit in sorted(pr_hits, key=lambda item: (-item.score, item.pr_number or 0))[:40]:
        if hit.pr_number is None or hit.pr_number not in prs:
            continue
        pr = prs[hit.pr_number]
        lines.append(
            f"| [#{hit.pr_number}]({pr.url}) | {markdown_escape(pr.title)} | "
            f"{markdown_escape(pr.work_area)} | {markdown_escape(hit.evidence)} |"
        )
    lines.extend([
        "",
        "## 后续迭代抽取规则",
        "",
        "- 在把候选证据提升为最终 lesson 前，必须读取关联 issue 正文和 PR 正文。",
        "- 表格字段只能作为路由提示；根因和方案需要源文本或 maintainer/PR 证据支持。",
        "- 依赖评论的结论，在评论正文抓取前必须标记为不完整。",
    ])
    return "\n".join(lines)


def build_domain_page(
    work_area: str,
    case_numbers: list[int],
    cases: dict[int, CaseRecord],
    issues: dict[int, IssueRecord],
    pattern_by_issue: dict[int, list[tuple[str, int, str]]],
) -> str:
    title = WORK_AREA_NAMES.get(work_area, work_area)
    category_counter = Counter()
    symptom_counter = Counter()
    root_counter = Counter()
    pattern_counter = Counter()
    for number in case_numbers:
        case = cases[number]
        category_counter.update(split_multi(case.primary_category))
        symptom_counter.update(split_multi(case.symptom))
        root_counter.update(split_multi(case.root_cause_hint))
        pattern_counter.update(key for key, _, _ in pattern_by_issue.get(number, [])[:3])
    lines = [
        f"# {title}",
        "",
        f"工作域键：`{work_area}`",
        "",
        "## 范围",
        "",
        f"- 候选 issue case 数：{len(case_numbers)}",
        f"- 高频分类：{', '.join(f'{k}={v}' for k, v in category_counter.most_common(5)) or 'n/a'}",
        f"- 高频症状：{', '.join(f'{k}={v}' for k, v in symptom_counter.most_common(8)) or 'n/a'}",
        f"- 高频根因提示：{', '.join(f'{k}={v}' for k, v in root_counter.most_common(8)) or 'n/a'}",
        "",
        "## 主要优化模式",
        "",
    ]
    for key, count in pattern_counter.most_common(10):
        lines.append(f"- [{PATTERNS[key]['title']}](../patterns/{key}.md): {count}")
    lines.extend(["", "## 代表性 Case", "", "| Issue | 标题 | 分类 | 症状 | 证据 |", "| --- | --- | --- | --- | --- |"])
    ranked = sorted(
        case_numbers,
        key=lambda number: (
            -len(pattern_by_issue.get(number, [])),
            -issues[number].comments_count,
            number,
        ),
    )
    for number in ranked[:80]:
        issue = issues[number]
        case = cases[number]
        evidence = pattern_by_issue.get(number, [])
        snippet = evidence[0][2] if evidence else truncate(issue.body, 180)
        case_path = f"../cases/{number // 1000:02d}xxx/{case_slug(number, issue.title)}"
        lines.append(
            f"| [#{number}]({case_path}) | {markdown_escape(issue.title)} | "
            f"{markdown_escape(case.primary_category)} | {markdown_escape(case.symptom)} | "
            f"{markdown_escape(snippet)} |"
        )
    lines.extend([
        "",
        "## 说明",
        "",
        "- 本页由原始 issue 正文和分类提示生成。",
        "- 计数只用于导航；只有检查关联 case 与 PR 证据后，才能提升结论。",
    ])
    return "\n".join(lines)


def main() -> None:
    source_paths = {
        "issues_raw": DATA / "raw" / "issues_raw.jsonl",
        "prs_raw": DATA / "raw" / "prs_raw.jsonl",
        "cases_csv": DATA / "tables" / "cases.csv",
        "prs_csv": DATA / "tables" / "prs.csv",
        "issue_pr_links_csv": DATA / "tables" / "issue_pr_links.csv",
    }
    raw_counts = {name: count_lines(path) for name, path in source_paths.items()}
    issues = load_issues()
    cases = load_cases()
    prs = load_prs()
    links = load_links()

    pattern_by_issue: dict[int, list[tuple[str, int, str]]] = {}
    pattern_issue_hits: dict[str, list[PatternHit]] = defaultdict(list)
    pattern_pr_hits: dict[str, list[PatternHit]] = defaultdict(list)
    domain_cases: dict[str, list[int]] = defaultdict(list)

    for number, issue in issues.items():
        case = cases.get(number)
        hits = score_patterns(issue_text(issue, case))
        pattern_by_issue[number] = hits
        for key, score, evidence in hits:
            pattern_issue_hits[key].append(PatternHit(key, issue_number=number, score=score, evidence=evidence, source="raw_issue_body+case_hints"))
        if case:
            areas = split_multi(case.work_area) or ["uncategorized"]
            for area in areas:
                domain_cases[area].append(number)

    for number, pr in prs.items():
        for key, score, evidence in score_patterns(pr_text(pr)):
            pattern_pr_hits[key].append(PatternHit(key, pr_number=number, score=score, evidence=evidence, source="raw_pr_body+pr_table"))

    for key in PATTERNS:
        write(
            OUT / "patterns" / f"{key}.md",
            build_pattern_page(key, pattern_issue_hits[key], pattern_pr_hits[key], cases, issues, prs),
        )

    for work_area, numbers in sorted(domain_cases.items()):
        write(
            OUT / "domains" / f"{work_area}.md",
            build_domain_page(work_area, numbers, cases, issues, pattern_by_issue),
        )

    case_rows = []
    for number, issue in sorted(issues.items()):
        case = cases.get(number)
        folder = OUT / "cases" / f"{number // 1000:02d}xxx"
        rel = f"cases/{number // 1000:02d}xxx/{case_slug(number, issue.title)}"
        write(folder / case_slug(number, issue.title), build_case_page(issue, case, links.get(number, []), prs, pattern_by_issue.get(number, [])))
        case_rows.append({
            "issue_number": number,
            "title": issue.title,
            "url": issue.url,
            "state": issue.state,
            "labels": issue.labels,
            "comments_count": issue.comments_count,
            "in_case_table": bool(case),
            "wiki_page": rel,
            "primary_category": case.primary_category if case else "",
            "work_area": case.work_area if case else "",
            "symptom": case.symptom if case else "",
            "root_cause_hint": case.root_cause_hint if case else "",
            "linked_prs": case.linked_prs if case else "",
            "comment_body_status": "missing" if issue.comments_count else "not_applicable",
            "top_patterns": ";".join(key for key, _, _ in pattern_by_issue.get(number, [])[:5]),
        })

    write_csv(
        OUT / "indexes" / "issues.csv",
        case_rows,
        [
            "issue_number", "title", "url", "state", "labels", "comments_count",
            "in_case_table", "wiki_page", "primary_category", "work_area", "symptom",
            "root_cause_hint", "linked_prs", "comment_body_status", "top_patterns",
        ],
    )

    pr_rows = []
    for number, pr in sorted(prs.items()):
        pr_rows.append({
            "pr_number": number,
            "title": pr.title,
            "url": pr.url,
            "state": pr.state,
            "merged": pr.merged,
            "primary_category": pr.primary_category,
            "work_area": pr.work_area,
            "solution_type": pr.solution_type,
            "hardware_scope": pr.hardware_scope,
            "operator_keywords": pr.operator_keywords,
            "top_patterns": ";".join(hit.pattern for hit in sorted(pattern_pr_hits_for_pr(pattern_pr_hits, number), key=lambda h: -h.score)[:5]),
        })
    write_csv(
        OUT / "indexes" / "prs.csv",
        pr_rows,
        [
            "pr_number", "title", "url", "state", "merged", "primary_category",
            "work_area", "solution_type", "hardware_scope", "operator_keywords", "top_patterns",
        ],
    )

    evidence_rows = []
    for key in PATTERNS:
        for hit in pattern_issue_hits[key]:
            evidence_rows.append({
                "pattern": key,
                "source_type": "issue",
                "source_number": hit.issue_number,
                "score": hit.score,
                "source": hit.source,
                "evidence": hit.evidence,
            })
        for hit in pattern_pr_hits[key]:
            evidence_rows.append({
                "pattern": key,
                "source_type": "pr",
                "source_number": hit.pr_number,
                "score": hit.score,
                "source": hit.source,
                "evidence": hit.evidence,
            })
    write_csv(
        OUT / "evidence" / "pattern_evidence.csv",
        evidence_rows,
        ["pattern", "source_type", "source_number", "score", "source", "evidence"],
    )

    manifest = build_manifest(source_paths, raw_counts, issues, cases, prs, links, case_rows, evidence_rows)
    write(OUT / "audit" / "manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2))
    write(OUT / "audit" / "manifest.md", build_manifest_markdown(manifest))
    write(OUT / "README.md", build_home(issues, cases, prs, links, domain_cases, pattern_issue_hits, pattern_pr_hits, raw_counts))
    write(OUT / "METHODOLOGY.md", build_methodology())
    write(OUT / "QUALITY_GATE.md", build_quality_gate(len(issues), len(cases), len(prs)))


def pattern_pr_hits_for_pr(pattern_pr_hits: dict[str, list[PatternHit]], pr_number: int) -> list[PatternHit]:
    result = []
    for hits in pattern_pr_hits.values():
        result.extend(hit for hit in hits if hit.pr_number == pr_number)
    return result


def build_home(
    issues: dict[int, IssueRecord],
    cases: dict[int, CaseRecord],
    prs: dict[int, PrRecord],
    links: dict[int, list[dict]],
    domain_cases: dict[str, list[int]],
    pattern_issue_hits: dict[str, list[PatternHit]],
    pattern_pr_hits: dict[str, list[PatternHit]],
    raw_counts: dict[str, int],
) -> str:
    state_counter = Counter(issue.state for issue in issues.values())
    category_counter = Counter(case.primary_category for case in cases.values() if case.primary_category)
    comment_missing = sum(1 for issue in issues.values() if issue.comments_count)
    linked_issues = sum(1 for issue_links in links.values() if issue_links)
    lines = [
        "# VllmWiki",
        "",
        "VllmWiki 是一个从 `vllm-project/vllm` issue 与 PR 语料炼化出的 source-backed 工程知识库。",
        "项目效仿 KernelWiki 的组织方式，把原始材料拆成 source-adjacent 页面、候选模式、领域导航、curated 机制页、索引和质量门。",
        "",
        "## 项目概览",
        "",
        "| 项 | 数量 / 状态 |",
        "| --- | ---: |",
        f"| 原始 issue JSONL 行数 | {raw_counts['issues_raw']:,} |",
        f"| 去重 issue 数 | {len(issues):,} |",
        f"| 原始 PR JSONL 行数 | {raw_counts['prs_raw']:,} |",
        f"| 去重 PR 表行数 | {len(prs):,} |",
        f"| Operator/kernel 候选 issue 数 | {len(cases):,} |",
        f"| 本地 issue-PR 链接 issue 数 | {linked_issues:,} |",
        f"| 有评论计数但缺评论正文的 issue 数 | {comment_missing:,} |",
        f"| Issue 状态 | {', '.join(f'{k}={v:,}' for k, v in state_counter.most_common())} |",
        f"| Case 分类 | {', '.join(f'{k}={v:,}' for k, v in category_counter.most_common())} |",
        "",
        "## 文件树分工",
        "",
        "```text",
        "VllmWiki/",
        "├── cases/                 # 每个 issue 的 source-adjacent 页面",
        "├── patterns/              # 自动候选模式页，负责聚类而非定论",
        "├── domains/               # 按 vLLM 子系统组织的导航页",
        "├── curated/               # 人工/agent 复核后的机制知识页",
        "│   └── bitwise/           # bitwise/deterministic 六个机制页",
        "├── candidates/            # 候选 claim ledger，记录 include/defer/exclude",
        "├── data/                  # schema、tag、alias、version claim",
        "├── evidence/              # 自动抽取的 pattern evidence 表",
        "├── indexes/               # issue / PR 索引表",
        "├── audit/                 # manifest 与每轮迭代审计报告",
        "└── scripts/               # 生成、查询、验证和迭代脚本",
        "```",
        "",
        "## 关键入口",
        "",
        "- [BITWISE_DETERMINISTIC.md](BITWISE_DETERMINISTIC.md)：当前重点主线，解释 bitwise/deterministic 的目标、产物和阅读顺序。",
        "- [WIKI_REFINEMENT_FLOW.md](WIKI_REFINEMENT_FLOW.md)：VllmWiki 如何效仿 KernelWiki 做知识炼化。",
        "- [KERNELWIKI_REFINEMENT_NOTES.md](KERNELWIKI_REFINEMENT_NOTES.md)：KernelWiki 的 source/wiki/queries/schema/ledger/validate 构建方式。",
        "- [WIKI_IMPLEMENTATION.md](WIKI_IMPLEMENTATION.md)：当前实现层次与证据规则。",
        "- [QUALITY_GATE.md](QUALITY_GATE.md)：质量门与防偷懒规则。",
        "",
        "## 常用命令",
        "",
        "```powershell",
        "python scripts\\query_vllmwiki.py bitwise --kind issue --limit 5",
        "python scripts\\get_page.py 33123 --follow-sources",
        "python scripts\\grep_wiki.py \"deterministic prefix\" --only wiki",
        "python scripts\\validate_vllmwiki.py",
        "python scripts\\run_vllmwiki_iteration.py",
        "```",
        "",
        "## 阅读路线",
        "",
        "1. 先从根目录概览文档理解项目结构。",
        "2. 如果关注当前主线，直接进入 [BITWISE_DETERMINISTIC.md](BITWISE_DETERMINISTIC.md)。",
        "3. 查具体 issue 时进入 `cases/`，查问题族时进入 `patterns/`，查子系统时进入 `domains/`。",
        "4. 只有 `curated/` 和 `candidates/` 中带证据状态的内容才接近可复用知识；自动聚类只作为候选导航。",
    ]
    return "\n".join(lines)


def build_methodology() -> str:
    return """# 方法论

## 源数据层

- 原始 issue 正文：`all/data/raw/issues_raw.jsonl`
- 原始 PR 正文：`all/data/raw/prs_raw.jsonl`
- 分类提示：`all/data/tables/cases.csv` 与 `all/data/tables/prs.csv`
- Issue-PR 链接提示：`all/data/tables/issue_pr_links.csv`

## 抽取原则

本 wiki 将证据和推断分开。

- 证据：标题/正文摘录、PR 描述、linked PR 证据字符串、URL。
- 路由提示：category、work area、symptom、root-cause hint、hardware scope、operator keywords。
- 推断：候选优化 pattern、代表性 case 排名、领域级 lesson。

## 为什么第一版使用候选 Pattern

本地数据集包含 issue 和 PR 正文，但没有讨论评论正文。很多最终 resolution 存在于评论里，所以生成器会把依赖评论的 case 标记为不完整，而不是假装已经知道最终根因。

## 迭代计划

1. 从所有原始 issue 和 PR 构建 source-backed 骨架。
2. 优先处理有 linked PR、高评论数、高 pattern 分数或 manual-review 标记的 case。
3. 抓取/阅读讨论评论和 PR review 上下文。
4. 只有在源证据确认根因与修复后，才把候选 pattern 提升为 curated lesson。
5. 保留 `evidence/pattern_evidence.csv` 作为所有提升结论的审计 ledger。
"""


def build_quality_gate(issue_count: int, case_count: int, pr_count: int) -> str:
    return f"""# 质量门

## 覆盖率门

- 原始 issue 覆盖目标：{issue_count:,} 个 issue 出现在 `indexes/issues.csv` 中。
- Operator/kernel case 覆盖目标：{case_count:,} 个去重 case 有生成 case 页或索引行。
- PR 覆盖目标：{pr_count:,} 个 PR 出现在 `indexes/prs.csv` 中。
- `indexes/issues.csv` 的每一行都必须有存在的 `wiki_page`。

## 证据门

一个 wiki lesson 被视为 curated 前，必须具备：

- 至少一个源 issue 或 PR URL。
- 来自 issue body、PR body 或已抓取评论的源正文摘录。
- 明确的抽取来源：raw body、PR body、comment 或 manual review。
- 置信状态：candidate、reviewed 或 curated。
- 清楚地区分 symptom、suspected root cause、confirmed root cause 和 fix。

## 防偷懒门

- 不要把只来自表格的结论提升为 curated lesson。
- 没有源证据时，不要把 `root_cause_hint` 当成根因。
- 不要只根据 `closed` 状态推断修复。
- 对有评论的 issue，在评论正文抓取完成或明确标记不可用前，不要总结成完整结论。
- 不要因为共享关键词就合并无关 issue family。
- 除非页面明确写着 `reviewed` 或 `curated`，否则把本 wiki 内容视为 `candidate`。

## 采样门

每轮迭代中，每个领域页都应：

- 复核分数最高的 20 个 case。
- 至少复核 10 个 linked-PR case。
- 至少复核 10 个 open issue。
- 至少复核 10 个高评论数但缺失评论正文的 issue。
- 记录 false positive 并更新 pattern 规则。

## 完整性标签

- `candidate`：由 raw body 和表格提示生成。
- `reviewed`：人类/agent 已阅读完整源 issue 和 linked PR body。
- `curated`：在 reviewed 基础上检查了评论或 maintainer resolution，并写成稳定 lesson。
- `blocked`：需要源评论或外部数据，但当前缺失。
"""


def build_manifest(
    source_paths: dict[str, Path],
    raw_counts: dict[str, int],
    issues: dict[int, IssueRecord],
    cases: dict[int, CaseRecord],
    prs: dict[int, PrRecord],
    links: dict[int, list[dict]],
    case_rows: list[dict],
    evidence_rows: list[dict],
) -> dict:
    missing_pages = [row["issue_number"] for row in case_rows if not row.get("wiki_page") or not (OUT / row["wiki_page"]).exists()]
    return {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "candidate_snapshot",
        "sources": {
            name: {
                "path": str(path),
                "line_count": raw_counts[name],
                "sha256": file_sha256(path),
            }
            for name, path in source_paths.items()
        },
        "coverage": {
            "unique_issues": len(issues),
            "unique_cases": len(cases),
            "unique_prs": len(prs),
            "issues_with_links": sum(1 for value in links.values() if value),
            "index_issue_rows": len(case_rows),
            "pattern_evidence_rows": len(evidence_rows),
            "missing_issue_pages": len(missing_pages),
            "issues_with_missing_comment_bodies": sum(1 for issue in issues.values() if issue.comments_count),
        },
        "known_limits": [
            "本地没有 issue 评论正文；带评论的 issue 仍应保持 candidate 或 blocked。",
            "没有 pull-request detail 数据时，PR 表中的 merge state 不能作为可靠 merge 证明。",
            "Pattern 证据在人工复核前只是基于关键词的候选证据。",
            "本地 case 表里的 root_cause 为空；根因需要源文本或 PR/comment 证据支持。",
        ],
    }


def build_manifest_markdown(manifest: dict) -> str:
    lines = [
        "# 构建 Manifest",
        "",
        f"状态：`{manifest['status']}`",
        f"生成时间 UTC：`{manifest['generated_at_utc']}`",
        "",
        "## 源文件",
        "",
        "| 源 | 行数 | SHA256 | 路径 |",
        "| --- | ---: | --- | --- |",
    ]
    for name, info in manifest["sources"].items():
        lines.append(f"| `{name}` | {info['line_count']:,} | `{info['sha256']}` | `{info['path']}` |")
    lines.extend(["", "## 覆盖率", "", "| 指标 | 值 |", "| --- | ---: |"])
    for key, value in manifest["coverage"].items():
        lines.append(f"| `{key}` | {value:,} |")
    lines.extend(["", "## 已知限制", ""])
    lines.extend(f"- {item}" for item in manifest["known_limits"])
    return "\n".join(lines)


if __name__ == "__main__":
    main()
