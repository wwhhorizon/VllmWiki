# vllm-project/vllm#8147: [Performance]: The impact of CPU on vLLM performance is significant.

| 字段 | 值 |
| --- | --- |
| Issue | [#8147](https://github.com/vllm-project/vllm/issues/8147) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: The impact of CPU on vLLM performance is significant.

### Issue 正文摘录

### Proposal to improve performance We used the same GPU on two machines but different CPUs. The following experimental conclusions were drawn: Experimental results: The GPU is 3090, and the CPU was upgraded from Xeon Gold 6240 to i9-12900k. The impact is as follows. a. vLLM achieved a 3.8x speedup in the agent scenario. b. TGi achieved a 1.23x speedup in the agent scenario. c. vLLM still has latency issues, but the time has been reduced to 100ms (previously 300ms). e. GPU utilization has increased from 70% to 90%. From the stress test data, it is evident that vLLM heavily relies on the performance of the CPU. What are the main factors affecting CPU performance, and how can they be optimized?

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: b. TGi achieved a 1.23x speedup in the agent scenario. c. vLLM still has latency issues, but the time has been reduced to 100ms (previously 300ms). e. GPU utilization has increased from 70% to 90%. From the stress test...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ance]: The impact of CPU on vLLM performance is significant. performance;stale ### Proposal to improve performance We used the same GPU on two machines but different CPUs. The following experimental conclusions were dra...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
