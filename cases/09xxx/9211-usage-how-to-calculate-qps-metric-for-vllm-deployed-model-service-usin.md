# vllm-project/vllm#9211: [Usage]: How to Calculate QPS Metric for vllm-Deployed Model Service Using Raw Query in Prometheus?

| 字段 | 值 |
| --- | --- |
| Issue | [#9211](https://github.com/vllm-project/vllm/issues/9211) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to Calculate QPS Metric for vllm-Deployed Model Service Using Raw Query in Prometheus?

### Issue 正文摘录

I want to know the concurrency of requests for my online model service deployed via vllm. How can I use a Raw query in Prometheus to calculate the QPS metric?

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ric for vllm-Deployed Model Service Using Raw Query in Prometheus? usage;stale I want to know the concurrency of requests for my online model service deployed via vllm. How can I use a Raw query in Prometheus to calcula...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: How to Calculate QPS Metric for vllm-Deployed Model Service Using Raw Query in Prometheus? usage;stale I want to know the concurrency of requests for my online model service deployed via vllm. How can I use a R...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
