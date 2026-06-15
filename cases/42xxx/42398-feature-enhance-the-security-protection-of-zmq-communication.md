# vllm-project/vllm#42398: [Feature]: Enhance the security protection of ZMQ communication

| 字段 | 值 |
| --- | --- |
| Issue | [#42398](https://github.com/vllm-project/vllm/issues/42398) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Enhance the security protection of ZMQ communication

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When we use data parallelism, the ZMQ port is exposed externally. If it receives some data starting with an int type at this time, the service is very likely to crash, and the error is “ msgspec.ValidationError: Expected `array`, got `int` ”. If possible, it is hoped that some validation logic can be added to improve the stability of the service. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: quest ### 🚀 The feature, motivation and pitch When we use data parallelism, the ZMQ port is exposed externally. If it receives some data starting with an int type at this time, the service is very likely to crash, and t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Enhance the security protection of ZMQ communication feature request ### 🚀 The feature, motivation and pitch When we use data parallelism, the ZMQ port is exposed externally. If it receives some data starting...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
