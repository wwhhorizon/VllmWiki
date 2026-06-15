# vllm-project/vllm#4900: [Usage]: Profiling Prefill and Decode Phases Separately

| 字段 | 值 |
| --- | --- |
| Issue | [#4900](https://github.com/vllm-project/vllm/issues/4900) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Profiling Prefill and Decode Phases Separately

### Issue 正文摘录

### Your current environment I'm attempting to independently measure the performance (e.g., latency, throughput, etc.) of the prefill and decode phases. Is there a way to achieve this? I have noticed a few benchmarks that measure end-to-end throughput and latency but do not provide separate metrics for each phase. I would greatly appreciate any guidance on profiling these two phases separately. ### How would you like to use vllm _No response_

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Usage]: Profiling Prefill and Decode Phases Separately usage;stale ### Your current environment I'm attempting to independently measure the performance (e.g., latency, throughput, etc.) of the prefill and decode phases...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Usage]: Profiling Prefill and Decode Phases Separately usage;stale ### Your current environment I'm attempting to independently measure the performance (e.g., latency, throughput, etc.) of the prefill and decode phases...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ut do not provide separate metrics for each phase. I would greatly appreciate any guidance on profiling these two phases separately. ### How would you like to use vllm _No response_

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
