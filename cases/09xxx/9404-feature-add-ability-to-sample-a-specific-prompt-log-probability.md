# vllm-project/vllm#9404: [Feature]: Add ability to sample a specific prompt log probability

| 字段 | 值 |
| --- | --- |
| Issue | [#9404](https://github.com/vllm-project/vllm/issues/9404) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add ability to sample a specific prompt log probability

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We want to be able to sample specific prompt log probabilities (not all of them). Current sampling parameters will return every log probability. However, if we could pass in a list, or even `first-ten` or `last-ten` options, it'd help a ton. We are currently limited by #5907 and believe that giving the ability to sample specific logprobs will help us get past that issue. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: eature]: Add ability to sample a specific prompt log probability feature request;stale ### 🚀 The feature, motivation and pitch We want to be able to sample specific prompt log probabilities (not all of them). Current sa...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature]: Add ability to sample a specific prompt log probability feature request;stale ### 🚀 The feature, motivation and pitch We want to be able to sample specific prompt log probabilities (not all of them). Current...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
