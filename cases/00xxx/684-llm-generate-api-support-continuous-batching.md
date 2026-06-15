# vllm-project/vllm#684: "llm.generate()" API support Continuous Batching?

| 字段 | 值 |
| --- | --- |
| Issue | [#684](https://github.com/vllm-project/vllm/issues/684) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> "llm.generate()" API support Continuous Batching?

### Issue 正文摘录

In my understanding, Continuous Batching is a trade-off between request latency and throughput, it can return the results of the completed request in time instead of waiting all requests of a batch. But it is seemingly that the “llm.generate()” API alaways wait all requests of a batch have been completed before return. ![image](https://github.com/vllm-project/vllm/assets/63448337/f33747b2-0447-496b-beb2-bbe4ae2fb177)

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: atching? In my understanding, Continuous Batching is a trade-off between request latency and throughput, it can return the results of the completed request in time instead of waiting all requests of a batch. But it is s...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: In my understanding, Continuous Batching is a trade-off between request latency and throughput, it can return the results of the completed request in time instead of waiting all requests of a batch. But it is seemingly...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
