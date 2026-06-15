# vllm-project/vllm#23088: [Feature]: Support for AIDC-AI/Ovis2.5-9B enable_thinking_budget and thinking_budget

| 字段 | 值 |
| --- | --- |
| Issue | [#23088](https://github.com/vllm-project/vllm/issues/23088) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support for AIDC-AI/Ovis2.5-9B enable_thinking_budget and thinking_budget

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Models with thinking have shown to improve accuracy. But sometimes they think too much and go into a loop of "wait". Ovis2.5 9B has introduced a new approach with their enable_thinking_budget and thinking_budget kwargs which would allow us reduce inference time yet allow for some improvements in accuracy by benefiting from the thinking process. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: or AIDC-AI/Ovis2.5-9B enable_thinking_budget and thinking_budget feature request;stale ### 🚀 The feature, motivation and pitch Models with thinking have shown to improve accuracy. But sometimes they think too much and g...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: eature, motivation and pitch Models with thinking have shown to improve accuracy. But sometimes they think too much and go into a loop of "wait". Ovis2.5 9B has introduced a new approach with their enable_thinking_budge...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: eature, motivation and pitch Models with thinking have shown to improve accuracy. But sometimes they think too much and go into a loop of "wait". Ovis2.5 9B has introduced a new approach with their enable_thinking_budge...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ng_budget feature request;stale ### 🚀 The feature, motivation and pitch Models with thinking have shown to improve accuracy. But sometimes they think too much and go into a loop of "wait". Ovis2.5 9B has introduced a ne...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
