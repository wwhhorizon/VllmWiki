# vllm-project/vllm#13840: [Feature]: Add CLI Commands for Benchmarking

| 字段 | 值 |
| --- | --- |
| Issue | [#13840](https://github.com/vllm-project/vllm/issues/13840) |
| 状态 | closed |
| 标签 | good first issue;feature request |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add CLI Commands for Benchmarking

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently the `vllm` commands has support for `serve|chat|complete`, while the benchmark commands lives in https://github.com/vllm-project/vllm/tree/main/benchmarks. It would be great to have commands such as following ``` vllm benchmark-throughput vllm benchmark-latency vllm benchmark-serving ``` ### Alternatives Status quo. ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Feature]: Add CLI Commands for Benchmarking good first issue;feature request ### 🚀 The feature, motivation and pitch Currently the `vllm` commands has support for `serve|chat|complete`, while the benchmark commands liv...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Add CLI Commands for Benchmarking good first issue;feature request ### 🚀 The feature, motivation and pitch Currently the `vllm` commands has support for `serve|chat|complete`, while the benchmark commands liv...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
