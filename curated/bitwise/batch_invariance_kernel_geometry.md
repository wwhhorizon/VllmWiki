# Batch Invariance 与 Kernel Geometry

状态：curated。  
父页：[Bitwise 确定性与数值等价](README.md)。
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
| [#42670](https://github.com/vllm-project/vllm/pull/42670) | FlashInfer + CUTLASS FP4 MoE 已有 invariant code path，但 support gate 继承 `False`，导致 `VLLM_BATCH_INVARIANT=1` 不可达。PR patch 在 `FlashInferBackend.supports_batch_invariance()` 和 `CutlassExpertsFp4._supports_batch_invariance()` 显式返回 `True`；PR body 的模型级复现显示，MiniMax-M2.7-NVFP4 在 B200、TP=2、concurrency=2 下 baseline 2/2 重复失控，开启该 PR 与 `VLLM_BATCH_INVARIANT=1` 后 0/2 bad，两个并发请求 sha256 相同。 | deterministic path 不只要实现，还要被 backend selector 暴露；support gate 也是 bitwise contract 的一部分。但 PR 仍 open，且模型级复现不适合 CI，只能写成 include-with-boundary。 |
| [#33537](https://github.com/vllm-project/vllm/pull/33537) | first real request 可能受 CUDA graph、Triton JIT、cache/allocator warmup 影响；PR 增加 deterministic warmup automation，单测覆盖 warmup iteration 配置和异常处理。review 要求主线复现后，作者补充的是 TRITON_MLA 首请求 latency 稳定性，而不是 token/logprob divergence；PR 后续 stale。 | batch invariance 要覆盖冷启动和 steady state，但 warmup automation 目前只能作为 boundary/候选机制，不能写成已修复 bitwise bug。 |
| [#39096](https://github.com/vllm-project/vllm/issues/39096), [#38938](https://github.com/vllm-project/vllm/pull/38938) | SM<90 GPU 上，`VLLM_BATCH_INVARIANT=1` 与 `torch.compile` 或 CUDA graphs 组合时不能保持 batch-invariant 输出；PR #38938 将问题拆成两个修复点：`ParallelLMHead` 使用的 `UnquantizedEmbeddingMethod.apply` 漏掉 batch-invariant GEMM 路由，以及 SM<90 下 `torch.compile` + CUDA graph 组合需要 enforce-eager 边界。 | 可以 promotion 为具体机制：batch invariance 必须覆盖 final logits projection 和 compile/graph support gate。 |
| [#42513](https://github.com/vllm-project/vllm/issues/42513) | MTP eager mode 下 batch size/verification shape 差异导致 token 不同。 | candidate，需 linked fix/test review。 |

## 根因机制

Batch invariance 被破坏时，根因常常不是 sampler，而是 kernel geometry。batch composition 改变了每个 kernel 看到的 shape、expert token 分布、graph/capture 状态或 reduction order。低精度 MoE/FP4/FP8 路径中，scale layout 和 expert routing 会进一步放大这些差异。

`#42670` 补充了一个容易漏掉的层次：即使底层 backend 已经有固定 split size、禁用 split-KV 或固定 per-expert tile 的 invariant path，selector/oracle 的 support gate 仍可能让该路径完全不可达。此时问题不是“没有 deterministic kernel”，而是“deterministic kernel 没有被声明为可选能力”。

## 修复方式

1. 找出 batch composition 改变的 kernel config：`block_m`、`split_k`、tile、backend、graph capture、tokens-per-expert。
2. 在 deterministic/batch-invariant mode 下固定这些 config，或拆分 fast path 与 deterministic path。
3. 确认 support gate、backend selector、MoE oracle 都能到达 invariant path。
4. 对 quantized MoE 同时记录 scale layout、expert routing、hardware SM count 和 backend。
5. 对 support-gate fix，除了 patch kernel 本身，还要检查 `supports_batch_invariance()`、MoE expert capability、attention backend selector 和实际 engine config 是否一致。

## 验证契约

- 同一请求分别在 batch=1、混 batch、并发 prefill/decode 中输出 token 一致。
- first request、warmup 后请求、CUDA graph capture 前后都要覆盖。
- 对 low precision MoE，要同时记录 kernel config 和 strict/token equality。
- 对 `torch.compile` / CUDA graphs 问题，要区分 compiler graph、CUDA graph、kernel 本身和 test harness 的归因。
- 对 support-gate 类修复，至少要证明 invariant mode 能选到目标 backend；若只能做模型级复现，也要记录硬件、模型、TP/concurrency、backend、输出 hash 和 CI 不覆盖原因。
- 对 warmup 类修复，要分清首请求 latency 稳定、graph/JIT 编译完成和 token/logprob bitwise 稳定；三者不能互相替代。

## 适用边界

- `#27433` 是 umbrella，不直接 promotion。
- `#39096/#38938` 已能支持 final logits projection 与 SM<90 compile/graph 边界这两个具体机制；但不要外推为所有 torch.compile 场景都不支持 batch invariance。
- `#42670` 的证据集中在 MiniMax-M2-family NVFP4、FlashInfer/CUTLASS FP4 MoE 和 `VLLM_BATCH_INVARIANT=1`；PR body 也把它定位成移除一个具体噪声源的 workaround，而不是修复该 checkpoint 对低精度噪声敏感的根因。PR 仍 open/unmerged，不能写成已发布能力。
- `#33537` 的 warmup 机制合理，但本地 evidence 中缺少“无 warmup token/logprob diverge、有 warmup bitwise 收敛”的闭环；目前只能作为 cold-start serving-state 边界。
- batch invariance 与 deterministic dispatch/reduction 机制高度交叉；当根因是 split-K/atomic/autotune，应交叉写入 dispatch 页。

## 仍需补证

- 继续补充 `#38938` review comments 中关于 L4/H100 test placement、`enforce_eager` 边界和 CI 分组的细节。
- 继续拆 `#27433` 中的 umbrella 讨论，把具体 PR 映射到单独机制，不把 umbrella issue 当结论。
- 追踪 `#42670` 是否合并；最好补一个轻量 support-gate/selector test，证明 `VLLM_BATCH_INVARIANT=1` 下 FlashInfer 与 CUTLASS FP4 MoE 不再被 base-class `False` 拦截。
- 若继续推进 `#33537`，需要补 first-request token/logprob 复现矩阵，而不只是 latency benchmark。
