# VllmWiki 炼化流程

状态：当前 wiki 构建流程说明。  
参考对象：KernelWiki 的知识库构建方式，而不是 KDA 的 kernel/算子优化流程。

## 总体流程

```text
raw issue/PR 数据
  -> cases/ source-adjacent issue 页面
  -> patterns/ 自动候选模式
  -> domains/ 子系统导航
  -> candidates/ 候选 ledger
  -> curated/ 机制知识页
  -> indexes/evidence 查询表
  -> validate/audit 质量门
```

## 各层职责

| 层 | 职责 | 当前目录 |
| --- | --- | --- |
| Source-adjacent | 保存原始 issue/PR 摘录和链接 | `cases/`、`audit/manifest.*` |
| Candidate pattern | 自动发现可能相关的问题族 | `patterns/`、`evidence/pattern_evidence.csv` |
| Domain navigation | 按 vLLM 子系统组织入口 | `domains/` |
| Candidate ledger | 记录候选 claim 的 include/defer/exclude 决策 | `candidates/` |
| Curated wiki | 写成可复用机制页 | `curated/` |
| Query/index | 提供机器可查索引 | `indexes/`、`scripts/query_vllmwiki.py` |
| Validation | 防止断链、缺文件、候选冒充结论 | `scripts/validate_vllmwiki.py`、`audit/` |

## Bitwise/Deterministic 炼化方式

bitwise/deterministic 是当前第一条重点线，但组织方式仍然是 wiki 炼化，而不是优化执行。

1. **先找候选**：用关键词和 case hints 找出 deterministic、bitwise、cache hit/miss、batch invariance、allclose、mismatch 等信号。
2. **再排队**：生成 `curated/bitwise_review_queue.md`，把 684 个候选 issue 按 cluster 和优先级排序。
3. **再入 ledger**：把最值得复核的 claim 写入 `candidates/bitwise_ledger.csv`，标注 include/defer/exclude。
4. **再读 source**：打开对应 `cases/` 页面和 linked PR，确认原文是否支持 claim。
5. **最后 curated**：只有机制、证据、边界、缺失项都写清楚，才进入 `curated/bitwise/*.md`。

## 当前六个 bitwise 机制页

- [Prefix Cache 等价](curated/bitwise/prefix_cache_equivalence.md)
- [Batch Invariance 与 Kernel Geometry](curated/bitwise/batch_invariance_kernel_geometry.md)
- [并发下的 KV Cache Identity](curated/bitwise/kv_cache_identity_concurrency.md)
- [量化与 Dtype 数值语义](curated/bitwise/quant_dtype_numerical_semantics.md)
- [Deterministic Dispatch 与 Reduction Control](curated/bitwise/deterministic_dispatch_reduction.md)
- [Bitwise 工作的验证契约](curated/bitwise/verification_contracts.md)

## 质量门

一条 bitwise claim 不能只因为关键词命中就进入 curated。它至少要说明：

- 对应 issue/PR 是什么。
- 原文证据在哪里。
- 观察到的 divergence 是什么。
- 机制解释是什么。
- 修复或验证方式是什么。
- 评论、PR detail、changed files 是否缺失。

缺证据时，应该写进 queue 或 ledger，并保持 `candidate`、`defer` 或 `blocked`。
