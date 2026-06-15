# vllm-project/vllm#22941: [Performance]: Run Arctic embedding benchmarks with V0 and V1

| 字段 | 值 |
| --- | --- |
| Issue | [#22941](https://github.com/vllm-project/vllm/issues/22941) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Run Arctic embedding benchmarks with V0 and V1

### Issue 正文摘录

### Arctic Embedding Benchmark As part of RFC https://github.com/vllm-project/vllm/issues/21796, we want to run the [Artic embedding benchmarks](https://github.com/snowflakedb/ArcticInference/tree/main/benchmark/embedding) to replicate the results in their [blog post](https://www.snowflake.com/en/engineering-blog/embedding-inference-arctic-16x-faster/).

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: run the [Artic embedding benchmarks](https://github.com/snowflakedb/ArcticInference/tree/main/benchmark/embedding) to replicate the results in their [blog post](https://www.snowflake.com/en/engineering-blog/embedding-in...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Performance]: Run Arctic embedding benchmarks with V0 and V1 performance;stale ### Arctic Embedding Benchmark As part of RFC https://github.com/vllm-project/vllm/issues/21796, we want to run the [Artic embedding benchma...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Performance]: Run Arctic embedding benchmarks with V0 and V1 performance;stale ### Arctic Embedding Benchmark As part of RFC https://github.com/vllm-project/vllm/issues/21796, we want to run the [Artic embedding benchm...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
