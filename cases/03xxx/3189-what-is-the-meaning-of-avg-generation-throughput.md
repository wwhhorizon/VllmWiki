# vllm-project/vllm#3189: What is the meaning of [Avg generation throughput]

| 字段 | 值 |
| --- | --- |
| Issue | [#3189](https://github.com/vllm-project/vllm/issues/3189) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> What is the meaning of [Avg generation throughput]

### Issue 正文摘录

I want to check how many tokens the server has generated during a time period. I notice there are two throughput metrics, the `Avg prompt throughput` and the `Avg generation throughput`. I guess the `Avg generation throughput` is `returned token length` divides the `time period`, is that right? If I want to know the token throughput of the server, I can just ignore the prompt throughput, right?

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: What is the meaning of [Avg generation throughput] stale I want to check how many tokens the server has generated during a time period. I notice there are two throughput metrics, the `Avg prompt throughput` and the `Avg...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: What is the meaning of [Avg generation throughput] stale I want to check how many tokens the server has generated during a time period. I notice there are two throughput metrics, the `Avg prompt throughput` and the `Avg...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
