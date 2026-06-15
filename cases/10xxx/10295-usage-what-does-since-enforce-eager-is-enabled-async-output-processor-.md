# vllm-project/vllm#10295: [Usage]: What does "since, enforce-eager is enabled, async output processor cannot be used" mean exactly?

| 字段 | 值 |
| --- | --- |
| Issue | [#10295](https://github.com/vllm-project/vllm/issues/10295) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: What does "since, enforce-eager is enabled, async output processor cannot be used" mean exactly?

### Issue 正文摘录

### Your current environment vllm docker, async openai client ### How would you like to use vllm When using enforce-eager, I get the message that "async output processor cannot be used". What exactly does this mean for my requests and the performance? I am using the async openai client. lets say I sent 50 requests with a concurrency of 25. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: r is enabled, async output processor cannot be used" mean exactly? usage;stale ### Your current environment vllm docker, async openai client ### How would you like to use vllm When using enforce-eager, I get the message...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ot be used" mean exactly? usage;stale ### Your current environment vllm docker, async openai client ### How would you like to use vllm When using enforce-eager, I get the message that "async output processor cannot be u...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 25. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
