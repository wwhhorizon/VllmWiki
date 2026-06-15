# vllm-project/vllm#4783: [Usage]: How to change the batch size when testing the throughput of VLLM by running benchmark_throughput

| 字段 | 值 |
| --- | --- |
| Issue | [#4783](https://github.com/vllm-project/vllm/issues/4783) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to change the batch size when testing the throughput of VLLM by running benchmark_throughput

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Usage]: How to change the batch size when testing the throughput of VLLM by running benchmark_throughput usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: `` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: # How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: hen testing the throughput of VLLM by running benchmark_throughput usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
