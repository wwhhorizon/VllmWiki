# vllm-project/vllm#32666: [Feature]: Save the start time of the benchmark request

| 字段 | 值 |
| --- | --- |
| Issue | [#32666](https://github.com/vllm-project/vllm/issues/32666) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Save the start time of the benchmark request

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The current `vllm bench serve --save-detailed` stores data such as `ttfts`, `itls`, and `tpots`, but does not save the actual time of request startup, which makes it difficult to accurately trace the entire test process. Therefore, it is desired to also save the `start_time`. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Feature]: Save the start time of the benchmark request feature request ### 🚀 The feature, motivation and pitch The current `vllm bench serve --save-detailed` stores data such as `ttfts`, `itls`, and `tpots`, but does n...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Save the start time of the benchmark request feature request ### 🚀 The feature, motivation and pitch The current `vllm bench serve --save-detailed` stores data such as `ttfts`, `itls`, and `tpots`, but does n...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
