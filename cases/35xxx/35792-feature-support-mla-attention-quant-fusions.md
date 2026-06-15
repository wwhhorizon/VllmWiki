# vllm-project/vllm#35792: [Feature]: Support MLA attention + quant fusions

| 字段 | 值 |
| --- | --- |
| Issue | [#35792](https://github.com/vllm-project/vllm/issues/35792) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support MLA attention + quant fusions

### Issue 正文摘录

### 🚀 The feature, motivation and pitch A sub-task from [[Performance]: Custom fused kernel tracking](https://github.com/vllm-project/vllm/issues/25179), to add fusion support for MLA attention + quant. TODOs: - [x] Phase 1: understand current MLA code - [x] Phase 1: mla attention + quant fusion pass pattern for - [x] static fp8/nvfp4: #36205 - [x] group fp8: #38877 - [ ] Phase 2: Add output quant support in following case: | Kernel path | Static FP8 (`kFp8StaticTensorSym`) | NVFP4 (`kNvfp4Dynamic`) | Per-group FP8 (`kFp8DynamicTokenSym`) | |---|---|---|---| | `forward_mha`(has_context=False) see below | | | | - FlashInfer (trtllm ragged)* | - 🟡 FI: support fp8 output - 🟡 (blocked) PR: #40304 | - 🟡 FI: support fp8 output - 🔴 vllm update callsite | 🔴 | | - FlashInfer (cutlass, blackwell)* | - 🟡 FI: flashinfer-ai/flashinfer/pull/3177 - 🔴 vllm update callsite | 🔴 | 🔴 | | - CuDNN | 🔴 | 🔴 | 🔴 | | - FlashAttn | - 🟢 kernel: [#135](https://github.com/vllm-project/flash-attention/pull/135) - 🟡 wiring: [#43050](https://github.com/vllm-project/vllm/pull/43050) | 🔴 | 🔴 | | `forward_mha`(has_context=True), output quant for `merge_attn_states` (#33097) | - 🟢 kernel: #36518 - 🟡 wiring: #40908 |...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Feature]: Support MLA attention + quant fusions feature request ### 🚀 The feature, motivation and pitch A sub-task from [[Performance]: Custom fused kernel tracking](https://github.com/vllm-project/vllm/issues/25179),...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: --|---|---|---| | `forward_mha`(has_context=False) see below | | | | - FlashInfer (trtllm ragged)* | - 🟡 FI: support fp8 output - 🟡 (blocked) PR: #40304 | - 🟡 FI: support fp8 output - 🔴 vllm update callsite | 🔴 | | - Fl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rt fp8 output - 🔴 vllm update callsite | 🔴 | | - FlashInfer (cutlass, blackwell)* | - 🟡 FI: flashinfer-ai/flashinfer/pull/3177 - 🔴 vllm update callsite | 🔴 | 🔴 | | - CuDNN | 🔴 | 🔴 | 🔴 | | - FlashAttn | - 🟢 kernel: [#135...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: `kFp8DynamicTokenSym`) | |---|---|---|---| | `forward_mha`(has_context=False) see below | | | | - FlashInfer (trtllm ragged)* | - 🟡 FI: support fp8 output - 🟡 (blocked) PR: #40304 | - 🟡 FI: support fp8 output - 🔴 vllm u...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: #36518 - 🟡 wiring: #40908 | 🟡 | - 🟡 kernel: #40930 | | `forward_mqa`: GEMM/BMM kernel with output quant for `_v_up_proj` | 🟡 PR #36297 | TBD | 🟡 PR #36297 | (Legend: 🟢 supported / 🟡 in progress / 🔴 not started) *Flashin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
