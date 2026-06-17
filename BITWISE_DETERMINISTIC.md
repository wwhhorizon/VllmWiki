# Bitwise / Deterministic 主线

状态：当前优先炼化方向。  
目标：把 vLLM issue/PR 中和 deterministic decoding、bitwise equality、batch invariance、prefix-cache equivalence、KV cache identity、dtype/quantization drift 相关的问题，整理成可复用的中文工程知识。

## 这条主线在解决什么

在 vLLM 里，同一个 prompt、同一个模型、同样 `temperature=0`，仍可能因为执行路径变化产生不同输出：

- prefix cache hit / miss 走了不同 prefill 几何；
- batch composition 改变 kernel shape、graph capture 状态或 reduction order；
- backend dispatch、autotune、split-K、atomic reduction 选择了不同路径；
- FP8/FP4/MXFP4 等 dtype 与 scale layout 不一致；
- 并发、LoRA、offload 或 block reuse 破坏 KV cache identity；
- verification 使用过宽的 `allclose`，没有真正约束 bitwise 行为。

这类问题不是普通性能问题，而是 correctness contract 问题。

## 当前结论层

| 产物 | 作用 |
| --- | --- |
| [curated/bitwise_determinism.md](curated/bitwise_determinism.md) | bitwise/deterministic 的 canonical 总览 |
| [curated/bitwise/](curated/bitwise/) | 六个机制页，承载长期结论 |
| [BITWISE_EVIDENCE_SYNTHESIS.md](BITWISE_EVIDENCE_SYNTHESIS.md) | 第一轮 targeted evidence 综合 |
| [candidates/bitwise_ledger.csv](candidates/bitwise_ledger.csv) | include/defer/exclude claim 账本 |

本地可再生材料不提交到 GitHub，包括 `cases/`、`patterns/`、`domains/`、`indexes/`、`evidence/` 和 review queue。需要核对原始证据时，优先使用仓库外的 `E:\Vllm-Issue\all\data\targeted\bitwise`。

## 六个机制页

- [Prefix Cache 等价](curated/bitwise/prefix_cache_equivalence.md)
- [Batch Invariance 与 Kernel Geometry](curated/bitwise/batch_invariance_kernel_geometry.md)
- [并发下的 KV Cache Identity](curated/bitwise/kv_cache_identity_concurrency.md)
- [量化与 Dtype 数值语义](curated/bitwise/quant_dtype_numerical_semantics.md)
- [Deterministic Dispatch 与 Reduction Control](curated/bitwise/deterministic_dispatch_reduction.md)
- [Bitwise 工作的验证契约](curated/bitwise/verification_contracts.md)

## 推荐阅读顺序

1. 先读 [curated/bitwise_determinism.md](curated/bitwise_determinism.md)，建立全局图。
2. 再读六个机制页，理解每类问题的触发条件、根因机制、修复方式和验证契约。
3. 查看 [BITWISE_EVIDENCE_SYNTHESIS.md](BITWISE_EVIDENCE_SYNTHESIS.md)，了解第一轮证据如何支撑这些机制。
4. 用 [candidates/bitwise_ledger.csv](candidates/bitwise_ledger.csv) 区分已经纳入结论、暂缓和仍需补证的 claim。

## 当前证据状态

- targeted bitwise evidence 已补到 `E:\Vllm-Issue\all\data\targeted\bitwise`。
- 第一轮 evidence index 覆盖 785 个 issue JSON、242 个 PR JSON、676 个带评论 issue、240 个带 changed files PR。
- `curated/` 是当前 GitHub 仓库中的结论层；自动分类和本地生成索引只能作为导航。

## 当前边界

- `BITWISE_EVIDENCE_SYNTHESIS.md` 是第一轮综合，不是最终全集。
- `candidates/bitwise_ledger.csv` 中 `defer` 的条目不能被当作 curated 结论。
- umbrella issue、无 linked fix 的 issue、只有关键词命中的旧 issue，仍应保持 `candidate` 或 `defer`。
- 后续新结论应优先下沉到六个机制页，而不是继续增加根目录文档。
