# vllm-project/vllm#2278: Can we perform prompt evaluation and token generation in parallel？

| 字段 | 值 |
| --- | --- |
| Issue | [#2278](https://github.com/vllm-project/vllm/issues/2278) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Can we perform prompt evaluation and token generation in parallel？

### Issue 正文摘录

Can we perform prompt evaluation and token generation in parallel？We need to pause decoding when accept a new request in the current scheduling policy.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: token generation in parallel？We need to pause decoding when accept a new request in the current scheduling policy.
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Can we perform prompt evaluation and token generation in parallel？ Can we perform prompt evaluation and token generation in parallel？We need to pause decoding when accept a new request in the current scheduling policy.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
