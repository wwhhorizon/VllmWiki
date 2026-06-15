# vllm-project/vllm#6888: [Performance]: tracking ray dag plus spmd performance

| 字段 | 值 |
| --- | --- |
| Issue | [#6888](https://github.com/vllm-project/vllm/issues/6888) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: tracking ray dag plus spmd performance

### Issue 正文摘录

### Proposal to improve performance On the current main: ```shell $ python benchmarks/benchmark_throughput.py --input-len 100 --output-len 100 --num-prompts 100 --model facebook/opt-125m -tp 2 --distributed-executor-backend ray Throughput: 101.53 requests/s, 20305.47 tokens/s ``` With ray dag and spmd worker: ```shell $ export VLLM_USE_RAY_SPMD_WORKER=1; export VLLM_USE_RAY_COMPILED_DAG=1 $ python benchmarks/benchmark_throughput.py --input-len 100 --output-len 100 --num-prompts 100 --model facebook/opt-125m -tp 2 --distributed-executor-backend ray Throughput: 41.17 requests/s, 8234.22 tokens/s ``` The goal is to make the latter as fast as the former, so that we can use spmd worker by default. ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ```

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: Proposal to improve performance On the current main: ```shell $ python benchmarks/benchmark_throughput.py --input-len 100 --output-len 100 --num-prompts 100 --model facebook/opt-125m -tp 2 --distributed-executor-backend...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Performance]: tracking ray dag plus spmd performance performance;stale ### Proposal to improve performance On the current main: ```shell $ python benchmarks/benchmark_throughput.py --input-len 100 --output-len 100 --nu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: --num-prompts 100 --model facebook/opt-125m -tp 2 --distributed-executor-backend ray Throughput: 101.53 requests/s, 20305.47 tokens/s ``` With ray dag and spmd worker: ```shell $ export VLLM_USE_RAY_SPMD_WORKER=1; expor...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: rker: ```shell $ export VLLM_USE_RAY_SPMD_WORKER=1; export VLLM_USE_RAY_COMPILED_DAG=1 $ python benchmarks/benchmark_throughput.py --input-len 100 --output-len 100 --num-prompts 100 --model facebook/opt-125m -tp 2 --dis...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: hmark_throughput.py --input-len 100 --output-len 100 --num-prompts 100 --model facebook/opt-125m -tp 2 --distributed-executor-backend ray Throughput: 101.53 requests/s, 20305.47 tokens/s ``` With ray dag and spmd worker...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
