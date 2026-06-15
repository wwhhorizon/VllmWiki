# vllm-project/vllm#21674: [Feature]: max-num-partial-prefills in V1

| 字段 | 值 |
| --- | --- |
| Issue | [#21674](https://github.com/vllm-project/vllm/issues/21674) |
| 状态 | open |
| 标签 | feature request;unstale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: max-num-partial-prefills in V1

### Issue 正文摘录

### 🚀 The feature, motivation and pitch #10235 Add support to concurrently calculate prefills of multiple requests, which allows to reduce the TTFT of shorter requests, while other longer requests also run on the same vLLM server. This feature is currently only supported in V0, but it would be very useful for me in V1, as V0 is about to deprecated. This feature should also solve #21495. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: max-num-partial-prefills in V1 feature request;unstale ### 🚀 The feature, motivation and pitch #10235 Add support to concurrently calculate prefills of multiple requests, which allows to reduce the TTFT of sh...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
