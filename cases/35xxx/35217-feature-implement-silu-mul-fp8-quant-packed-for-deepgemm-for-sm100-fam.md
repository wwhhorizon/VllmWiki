# vllm-project/vllm#35217: [Feature]: Implement silu_mul_fp8_quant_packed for deepgemm for sm100 families

| 字段 | 值 |
| --- | --- |
| Issue | [#35217](https://github.com/vllm-project/vllm/issues/35217) |
| 状态 | open |
| 标签 | feature request;stale;model-bash |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Implement silu_mul_fp8_quant_packed for deepgemm for sm100 families

### Issue 正文摘录

### 🚀 The feature, motivation and pitch On blackwell family when using deepgemm blockscaled fp8 backend. We currently launch separate kernel for `silu_and_mul` activation and 'fp8_quant' which is not efficient. It is good to implement fused kernel for this type of operation and later add them into the compilation fusion pass. https://github.com/vllm-project/vllm/blob/f5972a872fa3fabd94b7a6c6f031f4b5bcee2b2d/vllm/model_executor/layers/fused_moe/deep_gemm_moe.py#L201-L211 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Feature]: Implement silu_mul_fp8_quant_packed for deepgemm for sm100 families feature request;stale;model-bash ### 🚀 The feature, motivation and pitch On blackwell family when using deepgemm blockscaled fp8 backend. We...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Feature]: Implement silu_mul_fp8_quant_packed for deepgemm for sm100 families feature request;stale;model-bash ### 🚀 The feature, motivation and pitch On blackwell family when using deepgemm blockscaled fp8 backend. We...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ation and pitch On blackwell family when using deepgemm blockscaled fp8 backend. We currently launch separate kernel for `silu_and_mul` activation and 'fp8_quant' which is not efficient. It is good to implement fused ke...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Feature]: Implement silu_mul_fp8_quant_packed for deepgemm for sm100 families feature request;stale;model-bash ### 🚀 The feature, motivation and pitch On blackwell family when using deepgemm blockscaled fp8 backend. We...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: lement silu_mul_fp8_quant_packed for deepgemm for sm100 families feature request;stale;model-bash ### 🚀 The feature, motivation and pitch On blackwell family when using deepgemm blockscaled fp8 backend. We currently lau...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
