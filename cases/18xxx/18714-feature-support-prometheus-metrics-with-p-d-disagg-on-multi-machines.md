# vllm-project/vllm#18714: [Feature]: Support Prometheus Metrics with P/D disagg on multi-machines

| 字段 | 值 |
| --- | --- |
| Issue | [#18714](https://github.com/vllm-project/vllm/issues/18714) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support Prometheus Metrics with P/D disagg on multi-machines

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I noticed that the existing Prometheus metrics cannot function properly in multi-machine deployments, as the RequestStatsUpdate class requires stats to be generated from a single machine. This creates observability problem in xPyD disaggregate deployment scenarios. To address this, I plan to add support for multi-machine observability in V1. ### Alternatives As an alternative solutions, I'm using logging to collection metrics where P and D nodes output separately, then aggregating and computing them through cloud logging services (such as Tencent Cloud CLS or Google Cloud Logging). ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: e]: Support Prometheus Metrics with P/D disagg on multi-machines feature request;stale ### 🚀 The feature, motivation and pitch I noticed that the existing Prometheus metrics cannot function properly in multi-machine dep...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
