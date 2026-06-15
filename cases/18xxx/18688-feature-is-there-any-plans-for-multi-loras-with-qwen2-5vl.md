# vllm-project/vllm#18688: [Feature]: Is there any plans for multi loras with Qwen2.5vl ?

| 字段 | 值 |
| --- | --- |
| Issue | [#18688](https://github.com/vllm-project/vllm/issues/18688) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Is there any plans for multi loras with Qwen2.5vl ?

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I have a lot of finetune lora by qwen2.5vl, but a warning appeared during runtime vLLM currently only supports adding LoRA to language model May I ask if you have any plans to solve this recently？ ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Is there any plans for multi loras with Qwen2.5vl ? feature request ### 🚀 The feature, motivation and pitch I have a lot of finetune lora by qwen2.5vl, but a warning appeared during runtime vLLM currently onl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Is there any plans for multi loras with Qwen2.5vl ? feature request ### 🚀 The feature, motivation and pitch I have a lot of finetune lora by qwen2.5vl, but a warning appeared during runtime vLLM currently onl...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
