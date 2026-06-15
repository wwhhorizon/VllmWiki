# vllm-project/vllm#1966: Latency benchmark script is broken

| 字段 | 值 |
| --- | --- |
| Issue | [#1966](https://github.com/vllm-project/vllm/issues/1966) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Latency benchmark script is broken

### Issue 正文摘录

Got the following error: ``` Traceback (most recent call last): File "/workdir/workspace/vllm/benchmarks/benchmark_latency.py", line 127, in main(args) File "/workdir/workspace/vllm/benchmarks/benchmark_latency.py", line 75, in main latencies.append(run_to_completion(profile=False)) TypeError: main. .run_to_completion() got an unexpected keyword argument 'profile' ```

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: Latency benchmark script is broken Got the following error: ``` Traceback (most recent call last): File "/workdir/workspace/vllm/benchmarks/benchmark_latency.py", line 127, in main(args) File "/workdir/workspac
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: rkspace/vllm/benchmarks/benchmark_latency.py", line 75, in main latencies.append(run_to_completion(profile=False)) TypeError: main. .run_to_completion() got an unexpected keyword argument 'profile' ```
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: y.py", line 75, in main latencies.append(run_to_completion(profile=False)) TypeError: main. .run_to_completion() got an unexpected keyword argument 'profile' ```

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
