# Batch Invariance 与 Kernel Geometry

状态：reviewed seed page。  
父页：[Bitwise 确定性与数值等价](../bitwise_determinism.md)

## 契约

同一个请求的输出不应因为无关请求进入同一个 batch 而改变。batch composition 可以改变吞吐与调度，但不能改变 deterministic decoding 的可见 token。

## 机制

Batch invariance 经常被 kernel geometry 打破：

- tokens-per-expert、batch size、sequence grouping 改变 `block_m`、`split_k` 或 tile choice。
- cuBLAS/Triton/CUTLASS/FlashInfer 可能为不同 shape 选择不同算法。
- 不同 reduction order 或 atomic path 会产生不同舍入。
- 低精度 MoE/FP4/FP8 路径中，scale layout 与 expert routing 会放大微小差异。

## Curated Case

| Case | 观察 | 优化/修复 |
| --- | --- | --- |
| [#27433](https://github.com/vllm-project/vllm/issues/27433) | Batch Invariant feature 与 performance optimization umbrella | candidate umbrella：需要拆成具体 PR/机制 |
| [#36488](https://github.com/vllm-project/vllm/pull/36488) | MXFP4 MoE `matmul_ogs` 动态选择 `block_m`/`split_k` | 将 `VLLM_BATCH_INVARIANT` 传入 kernel config，强制稳定参数 |
| [#42670](https://github.com/vllm-project/vllm/pull/42670) | FlashInfer + CUTLASS FP4 MoE invariant path 被 support gate 阻断 | 声明已有 invariant backend 支持，使 deterministic 路径可达 |
| [#39096](https://github.com/vllm-project/vllm/issues/39096) | torch.compile/CUDA graphs 在 SM<90 上打破 batch invariance | candidate：需要审计 linked PR 与 exact failing config |
| [#42513](https://github.com/vllm-project/vllm/issues/42513) | MTP eager mode 下 batch size 差异导致 token 不同 | candidate：kernel selection/graph capture 可能锁定或改变算法 |

## Fix Pattern

1. 找出 batch composition 改变的 kernel config：`block_m`、`split_k`、tile、backend、graph capture。
2. 在 deterministic/batch-invariant mode 下固定这些 config。
3. 如果固定代价太高，拆分 fast path 与 deterministic path。
4. 测试同一请求在单独运行、混 batch、并发 prefill/decode 下是否一致。

## Open Review Queue

使用 [bitwise_review_queue.csv](../bitwise_review_queue.csv) 中 cluster 为 `batch_invariance` 的行。
