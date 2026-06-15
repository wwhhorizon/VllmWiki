# vllm-project/vllm#26422: [Feature]: Adding Lora on visual blocks of multimodal models

| 字段 | 值 |
| --- | --- |
| Issue | [#26422](https://github.com/vllm-project/vllm/issues/26422) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Adding Lora on visual blocks of multimodal models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hello, I have trained Qwen 2.5 VL 7B on all multimodal layers with Lora but when I try to load my adapter with vLLM I have : Regarding multimodal models, vLLM currently only supports adding LoRA to language model Do you know when LoRA will be added to visual layers also ? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: Adding Lora on visual blocks of multimodal models feature request ### 🚀 The feature, motivation and pitch Hello, I have trained Qwen 2.5 VL 7B on all multimodal layers with Lora but when I try to load my adap...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Feature]: Adding Lora on visual blocks of multimodal models feature request ### 🚀 The feature, motivation and pitch Hello, I have trained Qwen 2.5 VL 7B on all multimodal layers with Lora but when I try to load my adap...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Adding Lora on visual blocks of multimodal models feature request ### 🚀 The feature, motivation and pitch Hello, I have trained Qwen 2.5 VL 7B on all multimodal layers with Lora but when I try to load my adap...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
