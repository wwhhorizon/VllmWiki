# vllm-project/vllm#41291: [Refactor] Merge `select_gpt_oss_mxfp4_moe_backend` and `select_mxfp4_moe_backend`

| 字段 | 值 |
| --- | --- |
| Issue | [#41291](https://github.com/vllm-project/vllm/issues/41291) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Refactor] Merge `select_gpt_oss_mxfp4_moe_backend` and `select_mxfp4_moe_backend`

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ## Summary The current MXFP4 MoE backend selection logic has two separate functions: - `select_gpt_oss_mxfp4_moe_backend()` - uses `_get_priority_backends_for_gpt_oss()` (BF16 backends) - `select_mxfp4_moe_backend()` - uses `_get_priority_backends()` (MXFP8/DeepGEMM backends) These two functions share significant code duplication and could potentially be merged into a unified selector. ## Context From PR #40860 review discussion: https://github.com/vllm-project/vllm/pull/40860#discussion_r3148773753 The functions differ primarily in: 1. The priority backend list they iterate over 2. The activation key handling (BF16 vs MXFP8/FP8) ## Proposed Solution Merge into a single `select_mxfp4_moe_backend()` function. Accepts `activation_key` parameter or quantization_config parameter to map to proper backend. ## Related Files - `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py` - `vllm/model_executor/layers/quantization/mxfp4.py` - `vllm/model_executor/layers/quantization/quark/quark_moe.py` cc @mgoin @robertgshaw2-redhat @zyongye @ivanium ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Refactor] Merge `select_gpt_oss_mxfp4_moe_backend` and `select_mxfp4_moe_backend` feature request ### 🚀 The feature, motivation and pitch ## Summary The current MXFP4 MoE backend selection logic has two separate functi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: _backend()` function. Accepts `activation_key` parameter or quantization_config parameter to map to proper backend. ## Related Files - `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py` - `vllm/model_executor/layers...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Refactor] Merge `select_gpt_oss_mxfp4_moe_backend` and `select_mxfp4_moe_backend` feature request ### 🚀 The feature, motivation and pitch ## Summary The current MXFP4 MoE backend selection logic has two separate functi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Refactor] Merge `select_gpt_oss_mxfp4_moe_backend` and `select_mxfp4_moe_backend` feature request ### 🚀 The feature, motivation and pitch ## Summary The current MXFP4 MoE backend selection logic has two separate functi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
