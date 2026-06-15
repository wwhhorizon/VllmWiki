# vllm-project/vllm#13679: [Feature]: Support for LoRA for Pooling Models

| 字段 | 值 |
| --- | --- |
| Issue | [#13679](https://github.com/vllm-project/vllm/issues/13679) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support for LoRA for Pooling Models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently vLLM does not support LoRA for Pooling models (according to #12808) I wanted to understand how can we add the support given we can use similar code structure like generation models. What all things need to be taken care if I need to add the support. Any references will be helpful. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Support for LoRA for Pooling Models feature request ### 🚀 The feature, motivation and pitch Currently vLLM does not support LoRA for Pooling models (according to #12808) I wanted to understand how can we add...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Support for LoRA for Pooling Models feature request ### 🚀 The feature, motivation and pitch Currently vLLM does not support LoRA for Pooling models (according to #12808) I wanted to understand how can we add...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
