# Bitwise / Deterministic 主线

状态：当前优先炼化方向。  
目标：从 vLLM issue/PR 中提炼 deterministic decoding、bitwise equality、batch invariance、prefix-cache equivalence、KV cache identity、dtype/quantization drift 等问题的可复用知识。

## 这条主线在解决什么

在 vLLM 里，同一个 prompt、同一个模型、同样 `temperature=0`，仍可能因为以下因素产生不同输出：

- prefix cache hit / miss 走了不同 prefill 路径；
- batch composition 改变了 kernel shape 或 reduction order；
- backend dispatch、autotune、split-K、atomic reduction 选择了不同路径；
- FP8/FP4/MXFP4 等 dtype 与 scale layout 不一致；
- 并发、LoRA、offload 或 block reuse 破坏了 KV cache identity；
- verification 使用了过宽的 `allclose`，没有真正约束 bitwise 行为。

这类问题不是普通性能问题，而是 correctness contract 问题。

## 当前产物

| 产物 | 作用 |
| --- | --- |
| [curated/bitwise_determinism.md](curated/bitwise_determinism.md) | bitwise/deterministic 总览页 |
| [curated/bitwise/](curated/bitwise/) | 六个机制页 |
| [curated/bitwise_review_queue.md](curated/bitwise_review_queue.md) | 684 条候选 issue 的复核队列 |
| [candidates/bitwise_ledger.csv](candidates/bitwise_ledger.csv) | 重点 claim 的 include/defer/exclude ledger |
| [patterns/bitwise_determinism_equivalence.md](patterns/bitwise_determinism_equivalence.md) | 自动聚类出的 bitwise 候选证据 |
| [BITWISE_EVIDENCE_SYNTHESIS.md](BITWISE_EVIDENCE_SYNTHESIS.md) | 第一轮 source-backed 机制综合 |

## 六个机制页

- [Prefix Cache 等价](curated/bitwise/prefix_cache_equivalence.md)
- [Batch Invariance 与 Kernel Geometry](curated/bitwise/batch_invariance_kernel_geometry.md)
- [并发下的 KV Cache Identity](curated/bitwise/kv_cache_identity_concurrency.md)
- [量化与 Dtype 数值语义](curated/bitwise/quant_dtype_numerical_semantics.md)
- [Deterministic Dispatch 与 Reduction Control](curated/bitwise/deterministic_dispatch_reduction.md)
- [Bitwise 工作的验证契约](curated/bitwise/verification_contracts.md)

## 推荐阅读顺序

1. 先读 [curated/bitwise_determinism.md](curated/bitwise_determinism.md) 建立全局图。
2. 再读六个机制页，理解 recurring root mechanisms。
3. 查看 [candidates/bitwise_ledger.csv](candidates/bitwise_ledger.csv)，区分 include/defer/exclude。
4. 从本地生成的 `curated/bitwise_review_queue.csv` 选下一批 issue 深读。
5. 回到本地 `cases/` 页面或 `all/data/targeted/bitwise` JSON 核对原始 issue/PR 证据。

## 当前证据状态

- targeted bitwise evidence 已补到 `E:\Vllm-Issue\all\data\targeted\bitwise`。
- 当前 evidence index 覆盖 785 个 issue JSON、242 个 PR JSON、676 个带评论 issue、240 个带 changed files PR。
- 第一轮综合见 [BITWISE_EVIDENCE_SYNTHESIS.md](BITWISE_EVIDENCE_SYNTHESIS.md)。

## 当前边界

- 本地 `evidence/bitwise_sources.csv` 的 `mechanism_guess` 是自动分类，只能作为导航。
- `patterns/` 是候选聚类，不能当作最终结论。
- `curated/` 中的机制页仍应持续补充 source excerpt、边界和验证证据。
- umbrella issue、无 linked fix 的 issue、只有关键词命中的旧 issue 仍应保持 `candidate` 或 `defer`。
