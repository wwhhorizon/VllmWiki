# Batch Invariance 与 Kernel Geometry

状态：curated。  
父页：[Bitwise 确定性与数值等价](../bitwise_determinism.md)。

## 契约

同一个请求的输出不应因为其他无关请求进入同一个 batch 而改变。batch composition 可以改变吞吐、排队和调度，但不能改变 deterministic decoding 的可见 token。

## 机制

Batch invariance 被破坏时，根因常常不是 sampler，而是 kernel geometry：tokens-per-expert、batch size、sequence grouping 改变 `block_m`、`split_k`、tile choice、graph capture 或 backend path。低精度 MoE/FP4/FP8 路径中，scale layout 和 expert routing 会进一步放大这些差异。

## Source Evidence

| Source | 证据 | 炼化结论 |
| --- | --- | --- |
| [#27433](https://github.com/vllm-project/vllm/issues/27433) | batch invariant umbrella issue，已抓取 59 条评论和 177 条 timeline event。 | 这是索引入口，不应作为单条 curated measure。 |
| [#36488](https://github.com/vllm-project/vllm/pull/36488) | MXFP4 MoE `matmul_ogs` 根据 tokens-per-expert 和 SM count 动态选择 `block_m`/`split_k`；PR 传入 `enforce_bitwise_invariance=True` 固定参数。 | batch invariant mode 必须传到实际 kernel config 层。 |
| [#42670](https://github.com/vllm-project/vllm/pull/42670) | FlashInfer + CUTLASS FP4 MoE 已有 invariant code path，但 support gate 继承 `False`，导致 `VLLM_BATCH_INVARIANT=1` 不可达。 | deterministic path 不只要实现，还要被 backend selector 暴露。 |
| [#33537](https://github.com/vllm-project/vllm/pull/33537) | first real request 可能受 CUDA graph、Triton JIT、cache/allocator warmup 影响；PR 增加 deterministic warmup automation。 | batch invariance 要覆盖冷启动和 steady state。 |
| [#39096](https://github.com/vllm-project/vllm/issues/39096) | torch.compile/CUDA graphs 在 SM<90 上打破 batch invariance。 | 保持 defer，需要继续确认 linked PR 和 exact failing config。 |
| [#42513](https://github.com/vllm-project/vllm/issues/42513) | MTP eager mode 下 batch size/verification shape 差异导致 token 不同。 | candidate，需 linked fix/test review。 |

## Fix Pattern

1. 找出 batch composition 改变的 kernel config：`block_m`、`split_k`、tile、backend、graph capture、tokens-per-expert。
2. 在 deterministic/batch-invariant mode 下固定这些 config，或拆分 fast path 与 deterministic path。
3. 确认 support gate、backend selector、MoE oracle 都能到达 invariant path。
4. 测试同一请求在单独运行、混 batch、并发 prefill/decode、first request 和 warmup 后的输出。
5. 对 quantized MoE 同时记录 scale layout、expert routing 和 hardware SM count。

## Open Review Queue

下一轮优先拆 `#27433` 中的 umbrella 讨论，把具体 PR 映射到单独机制，不把 umbrella issue 当结论。
