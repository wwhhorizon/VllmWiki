# 对 Kernel 优化的约束

状态：curated bridge。
父页：[Bitwise 确定性与数值等价](README.md)。
范围：把 bitwise / deterministic 结论翻译成后续 kernel 优化时必须保留的不变量；本文不是 kernel 优化方法论，也不替代各机制页的证据。

## TL;DR

很多 bitwise issue 最后都落到 kernel dispatch、tiling、reduction、metadata 或 dtype path。后续做 kernel 优化时，不能只比较吞吐和宽松 tolerance，还要明确优化是否改变同一请求的执行几何、累加顺序、cache 身份或验证契约。允许存在更快但非 bitwise 的路径，但必须和 deterministic / batch-invariant 路径显式分离。

## 机制解释

kernel 优化需要保留的核心不变量包括：固定 reduction order、固定 batch-sensitive geometry、autotune candidate 先证数值等价、metadata 来源单一、cache identity 完整、dtype/reference boundary 明确、selector/support gate 同步，以及测试保护对象明确。

这些约束来自各机制页的稳定结论，本文只做工程化摘要，不新增独立 claim。

## 稳定证据

- upstream id: [#25194](https://github.com/vllm-project/vllm/issues/25194), [#25197](https://github.com/vllm-project/vllm/pull/25197)
- upstream status: merged PR
- claim level: stable
- direct evidence: 不稳定 autotune candidate 被移除。
- mechanism: autotune 空间不是纯性能空间。
- boundary: 新 candidate 仍需单独 exact 或 strict-tolerance 证据。

- upstream id: [#35183](https://github.com/vllm-project/vllm/pull/35183)
- upstream status: merged PR
- claim level: stable
- direct evidence: deterministic store-then-reduce 与 fast `atomicAdd` path 被拆开。
- mechanism: fast path 可以存在，但不能复用 deterministic correctness claim。
- boundary: 性能 opt-in path 要有独立语义。

- upstream id: [#36488](https://github.com/vllm-project/vllm/pull/36488), [#40408](https://github.com/vllm-project/vllm/pull/40408)
- upstream status: merged PRs
- claim level: stable family
- direct evidence: MXFP4 MoE 与 Cutlass FP8 都要求 BI mode 下 config 不随 `M`、tokens-per-expert 或 batch composition 改变。
- mechanism: low-precision fast kernel 能进入 BI 的前提是 fixed-config。
- boundary: 后续 tuning 重新依赖 shape 时要重跑 bitwise 验证。

- upstream id: [#41651](https://github.com/vllm-project/vllm/issues/41651), [#42650](https://github.com/vllm-project/vllm/pull/42650)
- upstream status: merged PR
- claim level: stable
- direct evidence: attention metadata 从 model-wide head count 改为 served layer shape。
- mechanism: plan/scratch/tile budget 必须和 runtime tensor 同源。
- boundary: 不覆盖其他 FP8 scale 或 grouping key 问题。

## 边界与反例

- 本文只总结已有 bitwise 主线约束；新 kernel 结论必须先进入对应机制页和 ledger。
- 性能优化可以提供 fast path，但必须显式 opt-in、说明边界并独立测试。
- kernel test 不能只用 semantic output 或宽松 `allclose` 支撑 bitwise claim。

## Evidence appendix

本文是桥接页，没有独立 appendix。详细证据分别见：

- [Dispatch / Reduction appendix](evidence_appendix/deterministic_dispatch_reduction.md)
- [Batch / Kernel Geometry appendix](evidence_appendix/batch_invariance_kernel_geometry.md)
- [Quant / Dtype appendix](evidence_appendix/quant_dtype_numerical_semantics.md)
- [KV Cache Identity appendix](evidence_appendix/kv_cache_identity_concurrency.md)
- [Verification Contracts appendix](evidence_appendix/verification_contracts.md)
