# vllm-project/vllm#27916: [Feature]: Does the latest version support LoRa for visual models?

| 字段 | 值 |
| --- | --- |
| Issue | [#27916](https://github.com/vllm-project/vllm/issues/27916) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Does the latest version support LoRa for visual models?

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When I loaded the QWEN2.5-VL model fine-tuned by LoRa using vllm version 0.8.4, I encountered the following prompt: > Regarding multimodal models, vLLM currently only supports adding LoRA to language model, visual.blocks.31.mlp.up_proj will be ignored. I found an issue https://github.com/vllm-project/vllm/issues/26422 with a similar problem, but it seems the PR hasn't been merged into master. How can I enable loading visual-side LORA parameters and using VLLM to accelerate inference? Looking forward to your reply ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: Does the latest version support LoRa for visual models? feature request ### 🚀 The feature, motivation and pitch When I loaded the QWEN2.5-VL model fine-tuned by LoRa using vllm version 0.8.4, I encountered th...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature]: Does the latest version support LoRa for visual models? feature request ### 🚀 The feature, motivation and pitch When I loaded the QWEN2.5-VL model fine-tuned by LoRa using vllm version 0.8.4, I encountered th...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: dels, vLLM currently only supports adding LoRA to language model, visual.blocks.31.mlp.up_proj will be ignored. I found an issue https://github.com/vllm-project/vllm/issues/26422 with a similar problem, but it seems the...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: eature]: Does the latest version support LoRa for visual models? feature request ### 🚀 The feature, motivation and pitch When I loaded the QWEN2.5-VL model fine-tuned by LoRa using vllm version 0.8.4, I encountered the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
