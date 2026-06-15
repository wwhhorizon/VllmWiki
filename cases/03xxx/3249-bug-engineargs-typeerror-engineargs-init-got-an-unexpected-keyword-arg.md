# vllm-project/vllm#3249: [bug] EngineArgs( TypeError: EngineArgs.__init__() got an unexpected keyword argument 'ray_workers_use_nsight

| 字段 | 值 |
| --- | --- |
| Issue | [#3249](https://github.com/vllm-project/vllm/issues/3249) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [bug] EngineArgs( TypeError: EngineArgs.__init__() got an unexpected keyword argument 'ray_workers_use_nsight

### Issue 正文摘录

``` python3 -c "import vllm; print(vllm.__version__)" 0.3.3 ``` when use `benchmarks/benchmark_latency.py` comes error: ``` File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/llm.py", line 91, in __init__ engine_args = EngineArgs( TypeError: EngineArgs.__init__() got an unexpected keyword argument 'ray_workers_use_nsight' ``` when use `benchmarks/benchmark_throughput.py` comes error: ``` File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/llm.py", line 91, in __init__ engine_args = EngineArgs( TypeError: EngineArgs.__init__() got an unexpected keyword argument 'enable_prefix_caching' ```

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ` python3 -c "import vllm; print(vllm.__version__)" 0.3.3 ``` when use `benchmarks/benchmark_latency.py` comes error: ``` File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/llm.py", line 91, in __init__ engi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: t an unexpected keyword argument 'ray_workers_use_nsight ``` python3 -c "import vllm; print(vllm.__version__)" 0.3.3 ``` when use `benchmarks/benchmark_latency.py` comes error: ``` File "/usr/local/lib/python3.10/dist-p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
