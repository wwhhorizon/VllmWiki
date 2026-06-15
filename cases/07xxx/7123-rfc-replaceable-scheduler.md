# vllm-project/vllm#7123: [RFC]: Replaceable Scheduler

| 字段 | 值 |
| --- | --- |
| Issue | [#7123](https://github.com/vllm-project/vllm/issues/7123) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Replaceable Scheduler

### Issue 正文摘录

### Motivation. The default scheduler is functioning well for the basic use case of serving with maximum throughput. There are still some use cases in which we prioritize other metrics before maximum throughput, for example maintaining fairness between different users. I specifically have a use case in which I have an application that uses vLLM, and tries to maintain fairness between requests of different users of the application. By making the scheduler component more abstract and replaceable (perhaps also pluginable) we can allow such use case without having to change the scheduler logic to support each of these use cases. ### Proposed Change. I propose 2 different solutions, one of which may be hard to implement, but allows anyone to implement any scheduling logic they wish without changing any other core logic. The other is simple to implement but doesn't allow full control of the scheduler logic, and the other may be harder to implement but . ### Solution 1 - Scheduler plugins This solution requires defining an abstract base class of a scheduler, and allowing to pass the desired scheduler implementation file path as a CLI argument (or an environment variable). This idea could...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [RFC]: Replaceable Scheduler RFC;stale ### Motivation. The default scheduler is functioning well for the basic use case of serving with maximum throughput. There are still some use cases in which we prioritize other met...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: oughput, for example maintaining fairness between different users. I specifically have a use case in which I have an application that uses vLLM, and tries to maintain fairness between requests of different users of the...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: duler is functioning well for the basic use case of serving with maximum throughput. There are still some use cases in which we prioritize other metrics before maximum throughput, for example maintaining fairness betwee...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
