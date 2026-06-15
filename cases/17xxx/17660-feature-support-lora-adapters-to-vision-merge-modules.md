# vllm-project/vllm#17660: [Feature]: Support LoRA adapters to vision/merge modules

| 字段 | 值 |
| --- | --- |
| Issue | [#17660](https://github.com/vllm-project/vllm/issues/17660) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support LoRA adapters to vision/merge modules

### Issue 正文摘录

### 🚀 The feature, motivation and pitch For many VLM use cases (such as object detection enabled by Qwen 2.5 VL and others) fine-tuning the vision modules is essential, so support for the full application of LoRA adapters would be really nice. The only way to simulate this behaviour with vLLM currently seems to be launching multiple different instances and switching between them with `/sleep and /wake_up` commands, which is extremely difficult to manage ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: feature request;stale ### 🚀 The feature, motivation and pitch For many VLM use cases (such as object detection enabled by Qwen 2.5 VL and others) fine-tuning the vision modules is essential, so support for the full appl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Support LoRA adapters to vision/merge modules feature request;stale ### 🚀 The feature, motivation and pitch For many VLM use cases (such as object detection enabled by Qwen 2.5 VL and others) fine-tuning the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
