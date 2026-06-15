# vllm-project/vllm#27956: [Feature]: awq marlin performs poorly when dealing with long inputs

| 字段 | 值 |
| --- | --- |
| Issue | [#27956](https://github.com/vllm-project/vllm/issues/27956) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: awq marlin performs poorly when dealing with long inputs

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When using awq-marlin, the performance of prefill is very poor, while the decoding performance is relatively good. Is this known? Are there any optimization methods？ ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ature]: awq marlin performs poorly when dealing with long inputs feature request;stale ### 🚀 The feature, motivation and pitch When using awq-marlin, the performance of prefill is very poor, while the decoding performan...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
