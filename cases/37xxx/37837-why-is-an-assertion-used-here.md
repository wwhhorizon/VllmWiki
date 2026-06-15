# vllm-project/vllm#37837: Why is an assertion used here?

| 字段 | 值 |
| --- | --- |
| Issue | [#37837](https://github.com/vllm-project/vllm/issues/37837) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Why is an assertion used here?

### Issue 正文摘录

https://github.com/vllm-project/vllm/blob/43877a620bf629d3625c870ef787e590101e0518/vllm/v1/core/sched/scheduler.py#L2103 My current online test scenario is a prefill/decode separation setup. After the prefill node processes a request and forwards it to the decode node via the Proxy, the connection between the Proxy and the decode node is immediately closed, triggering a decode abort. In this scenario, when the scheduler executes _update_from_kv_xfer_finishedto update the KV state, it finds that the request's req_idis no longer in self.requests, causing an assertion failure and leading to a complete crash of the D node.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ct/vllm/blob/43877a620bf629d3625c870ef787e590101e0518/vllm/v1/core/sched/scheduler.py#L2103 My current online test scenario is a prefill/decode separation setup. After the prefill node processes a request and forwards i...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: 787e590101e0518/vllm/v1/core/sched/scheduler.py#L2103 My current online test scenario is a prefill/decode separation setup. After the prefill node processes a request and forwards it to the decode node via the Proxy, th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
