# vllm-project/vllm#32057: [Feature][DSR1 NVFP4 Model Bash]: FlashInfer Quantize Op

| 字段 | 值 |
| --- | --- |
| Issue | [#32057](https://github.com/vllm-project/vllm/issues/32057) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][DSR1 NVFP4 Model Bash]: FlashInfer Quantize Op

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We currently run a flashinfer quantize op https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/quantization/utils/flashinfer_fp4_moe.py#L290-L294 This is much slower than the vllm native op ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Feature][DSR1 NVFP4 Model Bash]: FlashInfer Quantize Op feature request ### 🚀 The feature, motivation and pitch We currently run a flashinfer quantize op https://github.com/vllm-project/vllm/blob/main/vllm/model_execut...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Feature][DSR1 NVFP4 Model Bash]: FlashInfer Quantize Op feature request ### 🚀 The feature, motivation and pitch We currently run a flashinfer quantize op https://github.com/vllm-project/vllm/blob/main/vllm/model_execut...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature][DSR1 NVFP4 Model Bash]: FlashInfer Quantize Op feature request ### 🚀 The feature, motivation and pitch We currently run a flashinfer quantize op https://github.com/vllm-project/vllm/blob/main/vllm/model_execut...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: m/blob/main/vllm/model_executor/layers/quantization/utils/flashinfer_fp4_moe.py#L290-L294 This is much slower than the vllm native op ### Alternatives _No response_ ### Additional context _No response_ ### Before submit...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
