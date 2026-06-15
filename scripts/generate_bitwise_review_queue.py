"""Build a focused review queue for bitwise/numerical-equivalence work."""

from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
WIKI = ROOT / "VllmWiki"
DATA = ROOT / "all" / "data"


CLUSTERS = {
    "prefix_cache_equivalence": [
        "prefix caching", "prefix cache", "cache hit", "cache-hit",
        "cache miss", "cache-miss", "full prefill", "partial prefill",
    ],
    "batch_invariance": [
        "batch invariance", "batch-invariant", "batch invariant",
        "VLLM_BATCH_INVARIANT", "batch size", "same prompt", "concurrency",
    ],
    "kernel_autotune_reduction": [
        "autotuner", "auto-tuning", "autotune", "atomicadd", "atomicAdd",
        "reduction", "accumulation order", "split_k", "block_m", "tiling",
        "cublas", "tensile", "rocblas", "hipblas", "triton",
    ],
    "kv_identity_concurrency": [
        "kv cache", "kv block", "block allocator", "offload", "slot",
        "slot mapping", "wrong block", "stale", "corrupt", "concurrent",
    ],
    "quant_dtype_semantics": [
        "fp8", "fp4", "nvfp4", "mxfp4", "int4", "gptq", "awq",
        "dtype", "bf16", "float8", "scale", "dequant", "rmsnorm",
    ],
    "verification_contract": [
        "bitwise", "torch.equal", "allclose", "assert_close", "rtol",
        "atol", "test", "benchmark", "logprob", "argmax", "greedy",
    ],
    "backend_specific_drift": [
        "flashinfer", "flashattention", "flash attention", "rocm_attn",
        "aiter", "cutlass", "marlin", "machete", "backend", "fallback",
    ],
}

SIGNALS = [
    "bitwise", "deterministic", "non-deterministic", "nondeterministic",
    "batch invariance", "batch invariant", "same output", "different output",
    "cache hit", "cache miss", "numeric", "numerical", "divergence", "drift",
    "argmax", "temperature=0", "temperature 0", "torch.equal", "allclose",
    "assert_close", "rtol", "atol", "accuracy", "precision", "mismatch",
]


def read_csv(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def read_jsonl(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                yield json.loads(line)


def clean(text: str | None) -> str:
    text = text or ""
    text = re.sub(r"\r\n?", "\n", text)
    text = re.sub(r"<details>.*?</details>", " ", text, flags=re.I | re.S)
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def truncate(text: str, limit: int = 260) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "..."


def snippet(text: str) -> str:
    low = text.lower()
    idx = -1
    for signal in SIGNALS:
        loc = low.find(signal.lower())
        if loc >= 0 and (idx < 0 or loc < idx):
            idx = loc
    if idx < 0:
        idx = 0
    return truncate(text[max(0, idx - 90): idx + 380])


def cluster_text(text: str) -> tuple[list[str], int]:
    low = text.lower()
    clusters = []
    score = 0
    for name, kws in CLUSTERS.items():
        hits = [kw for kw in kws if kw.lower() in low]
        if hits:
            clusters.append(name)
            score += len(hits)
    score += sum(2 for signal in SIGNALS if signal.lower() in low)
    return clusters or ["unclustered_bitwise"], score


def strict_signal_score(text: str) -> int:
    low = text.lower()
    strong = [
        "bitwise", "batch invariance", "batch invariant", "deterministic",
        "non-deterministic", "nondeterministic", "same output",
        "different output", "cache hit", "cache miss", "argmax",
        "temperature=0", "temperature 0", "torch.equal", "allclose",
        "assert_close", "numerical divergence", "numeric divergence",
    ]
    return sum(1 for signal in strong if signal.lower() in low)


def main() -> None:
    issues_index = {int(r["issue_number"]): r for r in read_csv(WIKI / "indexes" / "issues.csv")}
    pattern_rows = [
        r for r in read_csv(WIKI / "evidence" / "pattern_evidence.csv")
        if r["pattern"] == "bitwise_determinism_equivalence"
    ]
    issue_evidence = defaultdict(list)
    pr_evidence = defaultdict(list)
    for row in pattern_rows:
        number = int(row["source_number"])
        if row["source_type"] == "issue":
            issue_evidence[number].append(row)
        else:
            pr_evidence[number].append(row)

    raw_issue_bodies = {}
    for obj in read_jsonl(DATA / "raw" / "issues_raw.jsonl"):
        number = int(obj["number"])
        if number in issue_evidence:
            raw_issue_bodies[number] = clean((obj.get("title") or "") + "\n" + (obj.get("body") or ""))

    queue = []
    for number, evidence_rows in issue_evidence.items():
        idx = issues_index.get(number, {})
        body = raw_issue_bodies.get(number, "")
        evidence_text = " ".join(row.get("evidence") or "" for row in evidence_rows[:5])
        strict_text = " ".join([idx.get("title", ""), body])
        if strict_signal_score(strict_text) < 1:
            continue
        text = " ".join([idx.get("title", ""), idx.get("work_area", ""), evidence_text, body])
        clusters, signal_score = cluster_text(text)
        if signal_score < 4:
            continue
        linked_pr_count = len([p for p in re.split(r"[;,\s]+", idx.get("linked_prs", "")) if p.strip()])
        comments = int(idx.get("comments_count") or 0)
        priority = signal_score + min(comments, 12) + linked_pr_count * 4
        if "correctness" in idx.get("primary_category", ""):
            priority += 5
        queue.append({
            "issue_number": number,
            "title": idx.get("title", ""),
            "url": idx.get("url", ""),
            "priority": priority,
            "clusters": ";".join(clusters),
            "comments_count": comments,
            "linked_prs": idx.get("linked_prs", ""),
            "work_area": idx.get("work_area", ""),
            "evidence": snippet(text),
            "wiki_page": idx.get("wiki_page", ""),
        })

    queue.sort(key=lambda row: (-row["priority"], row["issue_number"]))
    out_csv = WIKI / "curated" / "bitwise_review_queue.csv"
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "issue_number", "title", "url", "priority", "clusters", "comments_count",
        "linked_prs", "work_area", "evidence", "wiki_page",
    ]
    with out_csv.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(queue)

    by_cluster = defaultdict(list)
    for row in queue:
        for cluster in row["clusters"].split(";"):
            by_cluster[cluster].append(row)

    lines = [
        "# Bitwise 复核队列",
        "",
        "状态：候选复核队列。行按原始源证据排序；提升前必须阅读源 issue/PR。",
        "",
        f"队列 issue 总数：{len(queue):,}",
        "",
        "## Cluster 计数",
        "",
        "| Cluster | 数量 |",
        "| --- | ---: |",
    ]
    for cluster, rows in sorted(by_cluster.items(), key=lambda item: (-len(item[1]), item[0])):
        lines.append(f"| `{cluster}` | {len(rows):,} |")
    lines.extend(["", "## 各 Cluster 的 Top Issue", ""])
    for cluster, rows in sorted(by_cluster.items(), key=lambda item: (-len(item[1]), item[0])):
        lines.extend([f"### {cluster}", "", "| Issue | 优先级 | 关联 PR | 证据 |", "| --- | ---: | --- | --- |"])
        for row in rows[:20]:
            lines.append(
                f"| [#{row['issue_number']}]({row['url']}) {row['title'].replace('|', '/')} | "
                f"{row['priority']} | {row['linked_prs'].replace('|', '/')} | {row['evidence'].replace('|', '/')} |"
            )
        lines.append("")
    (WIKI / "curated" / "bitwise_review_queue.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
