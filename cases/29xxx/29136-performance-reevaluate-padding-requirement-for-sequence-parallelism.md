# vllm-project/vllm#29136: [Performance]: Reevaluate padding requirement for Sequence Parallelism

| 字段 | 值 |
| --- | --- |
| Issue | [#29136](https://github.com/vllm-project/vllm/issues/29136) |
| 状态 | open |
| 标签 | performance;torch.compile;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Reevaluate padding requirement for Sequence Parallelism

### Issue 正文摘录

### Proposal to improve performance Currently, we pad `num_tokens` to a multiple of TP (SP) size when Sequence Parallelism (SP) is enabled. However, we should benchmark to see the performance reduction in padding num_tokens and compare it to just manually padding with `-num_tokens % tp_size` around the sequence parallel section, or by doing uneven work across TP ranks by manipulating the sizes returned by `reduce_scatter` (more complicated but theoretically the best performance). ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Performance]: Reevaluate padding requirement for Sequence Parallelism performance;torch.compile;stale ### Proposal to improve performance Currently, we pad `num_tokens` to a multiple of TP (SP) size when Sequence Paral...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Performance]: Reevaluate padding requirement for Sequence Parallelism performance;torch.compile;stale ### Proposal to improve performance Currently, we pad `num_tokens` to a multiple of TP (SP) size when Sequence Paral...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: eevaluate padding requirement for Sequence Parallelism performance;torch.compile;stale ### Proposal to improve performance Currently, we pad `num_tokens` to a multiple of TP (SP) size when Sequence Parallelism (SP) is e...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: e padding requirement for Sequence Parallelism performance;torch.compile;stale ### Proposal to improve performance Currently, we pad `num_tokens` to a multiple of TP (SP) size when Sequence Parallelism (SP) is enabled....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
