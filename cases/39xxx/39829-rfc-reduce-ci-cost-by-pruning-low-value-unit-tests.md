# vllm-project/vllm#39829: [RFC]: Reduce CI Cost by Pruning Low-Value Unit Tests

| 字段 | 值 |
| --- | --- |
| Issue | [#39829](https://github.com/vllm-project/vllm/issues/39829) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Reduce CI Cost by Pruning Low-Value Unit Tests

### Issue 正文摘录

### Motivation. Our CI unit test suite continues to grow, and the cost of a full CI run grows with it. While comprehensive coverage is important, not all unit tests provide enough signal to justify their runtime and maintenance cost. The goal of this RFC is not to weaken test quality, but to improve the signal-to-cost ratio of our CI unit tests while preserving confidence in important behaviors and regressions. ### Proposed Change. From my understanding, we can choose to update: 1. tests cover outdated functionality 2. tests rely on overly exhaustive parameter combinations ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [RFC]: Reduce CI Cost by Pruning Low-Value Unit Tests RFC ### Motivation. Our CI unit test suite continues to grow, and the cost of a full CI run grows with it. While comprehensive coverage is important, not all unit te...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [RFC]: Reduce CI Cost by Pruning Low-Value Unit Tests RFC ### Motivation. Our CI unit test suite continues to grow, and the cost of a full CI run grows with it. While comprehensive coverage is important, not all unit te...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
