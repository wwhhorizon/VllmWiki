# vllm-project/vllm#1083: Feature request: add prometheus exporter

| 字段 | 值 |
| --- | --- |
| Issue | [#1083](https://github.com/vllm-project/vllm/issues/1083) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Feature request: add prometheus exporter

### Issue 正文摘录

I think it would be great to add `/metrics` route for api using prometheus client. This will help vllm be more “end to end” product Some metrics I think will be great: - Total request count - Total failure count with error type as label - buckets of latency - Total generated tokens - Total input tokens Those are the main I can think of right now. Pleased to get some more

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Feature request: add prometheus exporter I think it would be great to add `/metrics` route for api using prometheus client. This will help vllm be more “end to end” product Some metrics I think will be great: - Total re...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: equest count - Total failure count with error type as label - buckets of latency - Total generated tokens - Total input tokens Those are the main I can think of right now. Pleased to get some more

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
