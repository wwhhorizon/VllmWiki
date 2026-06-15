# vllm-project/vllm#16856: [Feature]: Support Gemma 3 QAT series

| 字段 | 值 |
| --- | --- |
| Issue | [#16856](https://github.com/vllm-project/vllm/issues/16856) |
| 状态 | open |
| 标签 | feature request;unstale |
| 评论 | 20; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support Gemma 3 QAT series

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The newly released Quantization Aware Training models can run on a single consumer GPU (3090/4090) https://ollama.com/library/gemma3 ### Alternatives Qwen 2.5 27B, currently supported by vllm. ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Feature]: Support Gemma 3 QAT series feature request;unstale ### 🚀 The feature, motivation and pitch The newly released Quantization Aware Training models can run on a single consumer GPU (3090/4090) https://ollama.com...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Support Gemma 3 QAT series feature request;unstale ### 🚀 The feature, motivation and pitch The newly released Quantization Aware Training models can run on a single consumer GPU (3090/4090) https://ollama.com...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: uest;unstale ### 🚀 The feature, motivation and pitch The newly released Quantization Aware Training models can run on a single consumer GPU (3090/4090) https://ollama.com/library/gemma3 ### Alternatives Qwen 2.5 27B, cu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Feature]: Support Gemma 3 QAT series feature request;unstale ### 🚀 The feature, motivation and pitch The newly released Quantization Aware Training models can run on a single consumer GPU (3090/4090) https://ollama.com...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
