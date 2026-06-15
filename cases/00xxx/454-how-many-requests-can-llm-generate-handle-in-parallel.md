# vllm-project/vllm#454: How many requests can `llm.generate` handle in parallel?

| 字段 | 值 |
| --- | --- |
| Issue | [#454](https://github.com/vllm-project/vllm/issues/454) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How many requests can `llm.generate` handle in parallel?

### Issue 正文摘录

To run benchmarks, should I add all prompts to the `llm.generate` class at once, let the engine queue and schedule, or add them in small batches?

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: How many requests can `llm.generate` handle in parallel? To run benchmarks, should I add all prompts to the `llm.generate` class at once, let the engine queue and schedule, or add them in small batches?
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nerate` class at once, let the engine queue and schedule, or add them in small batches?
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: How many requests can `llm.generate` handle in parallel? To run benchmarks, should I add all prompts to the `llm.generate` class at once, let the engine queue and schedule, or add them in small batches?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
