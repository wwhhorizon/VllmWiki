# vllm-project/vllm#15418: [Feature]: Limit thinking tokens

| 字段 | 值 |
| --- | --- |
| Issue | [#15418](https://github.com/vllm-project/vllm/issues/15418) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Limit thinking tokens

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Is there plan to support an option (e.g., `max_thinking_tokens`) to limit the thinking tokens for reasoning models? Perhaps both a minimum and a maximum limit would be useful. This is an example of one approach to achieving this: https://simonwillison.net/2025/Jan/22/r1py/ ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Limit thinking tokens feature request;stale ### 🚀 The feature, motivation and pitch Is there plan to support an option (e.g., `max_thinking_tokens`) to limit the thinking tokens for reasoning models? Perhaps...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: (e.g., `max_thinking_tokens`) to limit the thinking tokens for reasoning models? Perhaps both a minimum and a maximum limit would be useful. This is an example of one approach to achieving this: https://simonwillison.ne...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
