# vllm-project/vllm#13885: [Feature]: Any plan run deepseek-r1 fp8 on Ampere gpu

| 字段 | 值 |
| --- | --- |
| Issue | [#13885](https://github.com/vllm-project/vllm/issues/13885) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Any plan run deepseek-r1 fp8 on Ampere gpu

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I notice the core reason of vllm can not deployment deepseek-r1 fp8 model is `Marlin doesn't support block-wise fp8`. So, What are the possible approaches to run the DeepSeek R1 FP8 on Ampere architecture GPU ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: Any plan run deepseek-r1 fp8 on Ampere gpu feature request ### 🚀 The feature, motivation and pitch I notice the core reason of vllm can not deployment deepseek-r1 fp8 model is `Marlin doesn't support block-wi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Feature]: Any plan run deepseek-r1 fp8 on Ampere gpu feature request ### 🚀 The feature, motivation and pitch I notice the core reason of vllm can not deployment deepseek-r1 fp8 model is `Marlin doesn't support block-wi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: vllm can not deployment deepseek-r1 fp8 model is `Marlin doesn't support block-wise fp8`. So, What are the possible approaches to run the DeepSeek R1 FP8 on Ampere architecture GPU ### Alternatives _No response_ ### Add...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: tch I notice the core reason of vllm can not deployment deepseek-r1 fp8 model is `Marlin doesn't support block-wise fp8`. So, What are the possible approaches to run the DeepSeek R1 FP8 on Ampere architecture GPU ### Al...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Any plan run deepseek-r1 fp8 on Ampere gpu feature request ### 🚀 The feature, motivation and pitch I notice the core reason of vllm can not deployment deepseek-r1 fp8 model is `Marlin doesn't support block-wi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
