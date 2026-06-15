# vllm-project/vllm#12061: [Feature]: When will vllm support predicted outputs?

| 字段 | 值 |
| --- | --- |
| Issue | [#12061](https://github.com/vllm-project/vllm/issues/12061) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: When will vllm support predicted outputs?

### Issue 正文摘录

### 🚀 The feature, motivation and pitch **Predicted Outputs** Reduce latency for model responses where much of the response is known ahead of time. https://platform.openai.com/docs/guides/predicted-outputs I want to use it in a code editing scenario, which can significantly improve performance. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: When will vllm support predicted outputs? feature request;stale ### 🚀 The feature, motivation and pitch **Predicted Outputs** Reduce latency for model responses where much of the response is known ahead of ti...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: le ### 🚀 The feature, motivation and pitch **Predicted Outputs** Reduce latency for model responses where much of the response is known ahead of time. https://platform.openai.com/docs/guides/predicted-outputs I want to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: feature, motivation and pitch **Predicted Outputs** Reduce latency for model responses where much of the response is known ahead of time. https://platform.openai.com/docs/guides/predicted-outputs I want to use it in a c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
