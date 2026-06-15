# vllm-project/vllm#19623: [Feature]: Add support for multi-lora and single lora for classification tasks

| 字段 | 值 |
| --- | --- |
| Issue | [#19623](https://github.com/vllm-project/vllm/issues/19623) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add support for multi-lora and single lora for classification tasks

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Are there any plans to introduce support for multi-lora and single lora for classification tasks? I am trying to use Phi3.5 instruct model with classification head as a custom model. I also tried to add support for lora using the SupportsLoRA interface with the lora supported modules declarations but it seems to be of no use. Curious if this feature is still being considered by the vLLM team or not. If yes, what is the tentative timeline for it? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: support for multi-lora and single lora for classification tasks feature request;stale ### 🚀 The feature, motivation and pitch Are there any plans to introduce support for multi-lora and single lora for classification ta...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ingle lora for classification tasks? I am trying to use Phi3.5 instruct model with classification head as a custom model. I also tried to add support for lora using the SupportsLoRA interface with the lora supported mod...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
