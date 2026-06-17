# Batch Invariance 与 Kernel Geometry

状态：curated。  
父页：[Bitwise 确定性与数值等价](../bitwise_determinism.md)。  
范围：同一请求在单独运行、混 batch、并发 prefill/decode、first request 与 warmup 后的输出等价。

## 问题定义

同一个请求的输出不应因为其他无关请求进入同一个 batch 而改变。batch composition 可以改变吞吐、排队和调度，但不能改变 deterministic decoding 的可见 token。

## 典型触发条件

- tokens-per-expert、batch size、sequence grouping 改变 MoE/GEMM kernel config。
- `block_m`、`split_k`、tile choice、backend path 或 graph capture 状态随 batch composition 改变。
- FP4/FP8/MXFP4 MoE 路径中，scale layout、expert routing 和低精度累加放大差异。
- first real request 触发 CUDA graph、Triton JIT、allocator/cache warmup。
- SM<90 上 `torch.compile` 或 CUDA graphs 与 batch-invariant mode 组合出现 strict equality 失败。

## 代表证据

| Source | 证据事实 | 炼化结论 |
| --- | --- | --- |
| [#27433](https://github.com/vllm-project/vllm/issues/27433) | batch invariant umbrella issue，已抓取大量评论和 timeline。 | 这是索引入口，不应作为单条 curated measure。 |
| [#36488](https://github.com/vllm-project/vllm/pull/36488) | MXFP4 MoE `matmul_ogs` 根据 tokens-per-expert 和 SM count 动态选择 `block_m`/`split_k`；PR 传入 `enforce_bitwise_invariance=True` 固定参数。 | batch invariant mode 必须传到实际 kernel config 层。 |
| [#42670](https://github.com/vllm-project/vllm/pull/42670) | FlashInfer + CUTLASS FP4 MoE 已有 invariant code path，但 support gate 继承 `False`，导致 `VLLM_BATCH_INVARIANT=1` 不可达。 | deterministic path 不只要实现，还要被 backend selector 暴露。 |
| [#33537](https://github.com/vllm-project/vllm/pull/33537) | first real request 可能受 CUDA graph、Triton JIT、cache/allocator warmup 影响；PR 增加 deterministic warmup automation。 | batch invariance 要覆盖冷启动和 steady state。 |
| [#39096](https://github.com/vllm-project/vllm/issues/39096) | SM<90 GPU 上，`VLLM_BATCH_INVARIANT=1` 与 `torch.compile` 或 CUDA graphs 组合时不能保持 batch-invariant 输出；issue 同时指出单独的 compiled RMSNorm 在 L4 上可 bitwise equal。 | 保持 defer，需要确认 linked PR、exact failing config 和根因归属。 |
| [#42513](https://github.com/vllm-project/vllm/issues/42513) | MTP eager mode 下 batch size/verification shape 差异导致 token 不同。 | candidate，需 linked fix/test review。 |

## 根因机制

Batch invariance 被破坏时，根因常常不是 sampler，而是 kernel geometry。batch composition 改变了每个 kernel 看到的 shape、expert token 分布、graph/capture 状态或 reduction order。低精度 MoE/FP4/FP8 路径中，scale layout 和 expert routing 会进一步放大这些差异。

## 修复方式

1. 找出 batch composition 改变的 kernel config：`block_m`、`split_k`、tile、backend、graph capture、tokens-per-expert。
2. 在 deterministic/batch-invariant mode 下固定这些 config，或拆分 fast path 与 deterministic path。
3. 确认 support gate、backend selector、MoE oracle 都能到达 invariant path。
4. 对 quantized MoE 同时记录 scale layout、expert routing、hardware SM count 和 backend。

## 验证契约

- 同一请求分别在 batch=1、混 batch、并发 prefill/decode 中输出 token 一致。
- first request、warmup 后请求、CUDA graph capture 前后都要覆盖。
- 对 low precision MoE，要同时记录 kernel config 和 strict/token equality。
- 对 `torch.compile` / CUDA graphs 问题，要区分 compiler graph、CUDA graph、kernel 本身和 test harness 的归因。

## 适用边界

- `#27433` 是 umbrella，不直接 promotion。
- `#39096` 仍处于 defer：已有强问题描述，但缺 linked PR 与 exact failing config 的闭环。
- batch invariance 与 deterministic dispatch/reduction 机制高度交叉；当根因是 split-K/atomic/autotune，应交叉写入 dispatch 页。

## 仍需补证

- 审计 `#39096` 的 linked PR `#38938`、失败配置和最终修复边界。
- 继续拆 `#27433` 中的 umbrella 讨论，把具体 PR 映射到单独机制，不把 umbrella issue 当结论。
