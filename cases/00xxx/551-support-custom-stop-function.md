# vllm-project/vllm#551: Support custom stop function?

| 字段 | 值 |
| --- | --- |
| Issue | [#551](https://github.com/vllm-project/vllm/issues/551) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Support custom stop function?

### Issue 正文摘录

Consider supporting a function as a `stop` argument. This will speed up some generation use cases, such as stopping when an answer matches in evaluation.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Support custom stop function? feature request Consider supporting a function as a `stop` argument. This will speed up some generation use cases, such as stopping when an answer matches in evaluation.
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: up some generation use cases, such as stopping when an answer matches in evaluation.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
