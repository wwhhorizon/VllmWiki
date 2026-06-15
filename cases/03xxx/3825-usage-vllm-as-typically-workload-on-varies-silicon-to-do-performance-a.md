# vllm-project/vllm#3825: [Usage]: vllm as typically workload on varies silicon to do performance analysis

| 字段 | 值 |
| --- | --- |
| Issue | [#3825](https://github.com/vllm-project/vllm/issues/3825) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: vllm as typically workload on varies silicon to do performance analysis

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I've built the source code and install it in my system, and started the demo on the CPU backend For NV GPU system we can use nsigth to profiler the computing progress in GPU hardware, and in CPU hardware i've tried perf top just got many JIT processes in the top monitor, for CPU system is there a much more efficient tools to monitor the performance and beheaviors to annlysis the llm on vector AVX/SVE for examples I've checked the samples code and benchmark code and found little, as using torch as backend framework, as I know torch got profiler to analysis them but how can I enable the profiler in those benchmark or examples, so far no demo code for it, is there anything missing for me? Could anyone can show me a usage demo or something may helpfull for it appreciate much

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ``` ### How would you like to use vllm I've built the source code and install it in my system, and started the demo on the CPU backend For NV GPU system we can use nsigth to profiler the computing progress in GPU hardwa...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: rted the demo on the CPU backend For NV GPU system we can use nsigth to profiler the computing progress in GPU hardware, and in CPU hardware i've tried perf top just got many JIT processes in the top monitor, for CPU sy...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: source code and install it in my system, and started the demo on the CPU backend For NV GPU system we can use nsigth to profiler the computing progress in GPU hardware, and in CPU hardware i've tried perf top just got m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: as typically workload on varies silicon to do performance analysis usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I've built the source code...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
