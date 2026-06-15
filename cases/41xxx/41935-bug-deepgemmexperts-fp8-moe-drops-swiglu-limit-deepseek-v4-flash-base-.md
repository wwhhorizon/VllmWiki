# vllm-project/vllm#41935: [Bug]: DeepGemmExperts FP8 MoE drops swiglu_limit (DeepSeek-V4-Flash-Base produces glitch tokens)

| 字段 | 值 |
| --- | --- |
| Issue | [#41935](https://github.com/vllm-project/vllm/issues/41935) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: DeepGemmExperts FP8 MoE drops swiglu_limit (DeepSeek-V4-Flash-Base produces glitch tokens)

### Issue 正文摘录

### Your current environment Problem exists on the latest main. ### 🐛 Describe the bug `DeepGemmExperts._act_mul_quant` https://github.com/vllm-project/vllm/blob/6e6d182d18dbe5c81c9c9058a5571241f649ae7b/vllm/model_executor/layers/fused_moe/experts/deep_gemm_moe.py#L195 on the FP8 MoE path discards the model's `swiglu_limit`. The sister class `DeepGemmFP4Experts` https://github.com/vllm-project/vllm/blob/6e6d182d18dbe5c81c9c9058a5571241f649ae7b/vllm/model_executor/layers/fused_moe/experts/deep_gemm_moe.py#L431 correctly propagates `gemm1_clamp_limit` to its silu_mul kernel, but the FP8 variant does not. For DeepSeek-V4-Flash-Base (swiglu_limit=10), routed-expert SwiGLU outputs go unbounded, leading to rare-vocab tokens (e.g. id 83480 ")Skip", ) winning argmax at clause boundaries. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: DeepGemmExperts FP8 MoE drops swiglu_limit (DeepSeek-V4-Flash-Base produces glitch tokens) bug ### Your current environment Problem exists on the latest main. ### 🐛 Describe the bug `DeepGemmExperts._act_mul_quan...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: DeepGemmExperts FP8 MoE drops swiglu_limit (DeepSeek-V4-Flash-Base produces glitch tokens) bug ### Your current environment Problem exists on the latest main. ### 🐛 Describe the bug `DeepGemmExperts._act_mul_quan...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: es. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: com/vllm-project/vllm/blob/6e6d182d18dbe5c81c9c9058a5571241f649ae7b/vllm/model_executor/layers/fused_moe/experts/deep_gemm_moe.py#L195 on the FP8 MoE path discards the model's `swiglu_limit`. The sister class `DeepGemmF...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: glitch tokens) bug ### Your current environment Problem exists on the latest main. ### 🐛 Describe the bug `DeepGemmExperts._act_mul_quant` https://github.com/vllm-project/vllm/blob/6e6d182d18dbe5c81c9c9058a5571241f649ae...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
