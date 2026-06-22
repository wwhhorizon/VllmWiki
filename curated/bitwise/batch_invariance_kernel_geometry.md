# Batch Invariance 与 Kernel Geometry

状态：curated。
父页：[Bitwise 确定性与数值等价](README.md)。
范围：同一请求在单独运行、混 batch、并发 prefill/decode、first request 与 warmup 后的输出等价。

## TL;DR

Batch invariance 要求同一请求不因同 batch 的其他请求而改变 token、logprob 或 KV 语义。常见根因是 batch composition 改变 kernel geometry、attention path、MoE tile、quantized matmul config 或 graph/warmup 状态。`VLLM_BATCH_INVARIANT=1` 只有在 selector、support gate 和最终 kernel path 都可达时才有意义。open workaround 和 support-gate 项保留在 [next.md](next.md)。

## 机制解释

batch composition 改变每个 kernel 看到的 shape、expert token 分布、graph/capture 状态或 reduction order。低精度 MoE、FP4/FP8、cascade attention、FlashInfer CTA tile 和 quantization auto-conversion 都可能把这种差异放大。

因此 batch-invariant 修复不只是“加一个全局开关”。每个 backend 或 quantization path 都要证明最终 dispatch 的 kernel family、split 参数、tile 或 support gate 被固定。

<!-- 稳定证据区禁止出现 open/defer/include_with_boundary；此类对象仅可进入"边界与反例"段或 next.md -->

## 稳定证据

- upstream id: [#36488](https://github.com/vllm-project/vllm/pull/36488)
  - upstream status: merged PR
  - claim level: stable
  - direct evidence: MXFP4 MoE `matmul_ogs` 原本按 tokens-per-expert 和 SM count 动态选择 `block_m`/`split_k`；PR 传入 `enforce_bitwise_invariance=True`。
  - mechanism: batch-invariant flag 必须传到实际 kernel config 层。
  - boundary: 同时属于 quant/dtype 机制，不代表所有 MoE backend 都已覆盖。

- upstream id: [#39096](https://github.com/vllm-project/vllm/issues/39096), [#38938](https://github.com/vllm-project/vllm/pull/38938)
  - upstream status: issue plus PR evidence
  - claim level: stable mechanism
  - direct evidence: SM<90 上 BI mode 与 `torch.compile` / CUDA graphs 组合失败；PR 将 final logits projection 和 compile/graph support gate 拆开处理。
  - mechanism: batch invariance 必须覆盖 final logits projection 和 compile/graph 边界。
  - boundary: 不外推为所有 `torch.compile` 场景都不支持 batch invariance。

- upstream id: [#32561](https://github.com/vllm-project/vllm/pull/32561)
  - upstream status: merged PR
  - claim level: stable
  - direct evidence: cascade attention 会按 batch shape 条件性启用，造成 logprob 差异；merged patch 在 BI mode 下禁用该优化。
  - mechanism: 条件性 attention 优化必须被 gate，或证明启用条件与同 batch 其他请求无关。
  - boundary: PR 讨论把 FlashInfer chunked prefill、MoE、AWQ 留作独立后续边界。

- upstream id: [#38670](https://github.com/vllm-project/vllm/pull/38670)
  - upstream status: merged PR
  - claim level: stable
  - direct evidence: AWQ 在 BI mode 下绕开 AWQ_Marlin，回到 dequant + `torch.matmul`，让 deterministic override 接管。
  - mechanism: quantization auto-conversion 也是 batch-invariant contract 的一部分。
  - boundary: 不能宣称 AWQ_Marlin fused kernel 本身已 deterministic。

- upstream id: [#33688](https://github.com/vllm-project/vllm/pull/33688)
  - upstream status: merged PR
  - claim level: stable
  - direct evidence: TRITON_ATTN 在 BI mode 下强制 decode 走 2D kernel，before/after logprob test 从失败到通过。
  - mechanism: backend support gate 要证明最终 kernel family 固定，而不只是 backend 名称可运行。
  - boundary: 证据集中在 B200、TRITON_ATTN、GPT-OSS/Qwen 测试；不覆盖 MLA/FlashInfer。

## 边界与反例

- `#27433` 是 umbrella，不直接 promotion。
- `#42670` 是 open support-gate workaround：它说明 deterministic path 可能不可达，但不能写成 checkpoint root-cause 修复或 landed ability。
- `#33537` 目前只有 warmup/latency 边界，缺 token/logprob divergence before/after。
- `#42513/#42518` 当前是 eager-vs-BI 契约边界：eager 模式下 MTP/spec decode 与 non-MTP 的 attention GEMM 数值路径可能通过 verification batch geometry 分叉，并经 KV 放大到 token 分叉；当前未发现 linked fix 或 selective patch，属于 batch-invariant 契约边界。
- batch invariance 与 dispatch/reduction 交叉；当根因是 split-K、atomic 或 autotune，应链接到 [Deterministic Dispatch 与 Reduction Control](deterministic_dispatch_reduction.md)。

## Evidence appendix

长证据表、support-gate matrix 和补证记录见 [evidence_appendix/batch_invariance_kernel_geometry.md](evidence_appendix/batch_invariance_kernel_geometry.md)。
