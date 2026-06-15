# vllm-project/vllm#6887: [Bug]: dag teardown error AttributeError: 'Worker' object has no attribute 'core_worker'

| 字段 | 值 |
| --- | --- |
| Issue | [#6887](https://github.com/vllm-project/vllm/issues/6887) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: dag teardown error AttributeError: 'Worker' object has no attribute 'core_worker'

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug command: `python benchmarks/benchmark_throughput.py --input-len 100 --output-len 100 --num-prompts 100 --model facebook/opt-125m -tp 2 --distributed-executor-backend ray` error: ```text 2024-07-28 22:30:36,078 INFO compiled_dag_node.py:1202 -- Tearing down compiled DAG Exception ignored in: Traceback (most recent call last): File "/data/youkaichao/vllm/vllm/executor/ray_gpu_executor.py", line 396, in __del__ self.forward_dag.teardown() File "/data/youkaichao/miniconda/envs/vllm/lib/python3.9/site-packages/ray/dag/compiled_dag_node.py", line 1402, in teardown monitor.teardown(wait=True) File "/data/youkaichao/miniconda/envs/vllm/lib/python3.9/site-packages/ray/dag/compiled_dag_node.py", line 1204, in teardown outer._dag_submitter.close() File "/data/youkaichao/miniconda/envs/vllm/lib/python3.9/site-packages/ray/experimental/channel/common.py", line 383, in close self._output_channel.close() File "/data/youkaichao/miniconda/envs/vllm/lib/python3.9/site-packages/ray/experimental/channel/shared_memory_channel.py", line 629, in close channel.close() File "/data/youkaichao/miniconda/env...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: f `python collect_env.py` ``` ### 🐛 Describe the bug command: `python benchmarks/benchmark_throughput.py --input-len 100 --output-len 100 --num-prompts 100 --model facebook/opt-125m -tp 2 --distributed-executor-backend...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: --num-prompts 100 --model facebook/opt-125m -tp 2 --distributed-executor-backend ray` error: ```text 2024-07-28 22:30:36,078 INFO compiled_dag_node.py:1202 -- Tearing down compiled DAG Exception ignored in: Traceback (m...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: uted-executor-backend ray` error: ```text 2024-07-28 22:30:36,078 INFO compiled_dag_node.py:1202 -- Tearing down compiled DAG Exception ignored in: Traceback (most recent call last): File "/data/youkaichao/vllm/vllm/exe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: benchmark_throughput.py --input-len 100 --output-len 100 ``` cc @ruisearch42 @rkooo567 @stephanie-wang
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: hmark_throughput.py --input-len 100 --output-len 100 --num-prompts 100 --model facebook/opt-125m -tp 2 --distributed-executor-backend ray` error: ```text 2024-07-28 22:30:36,078 INFO compiled_dag_node.py:1202 -- Tearing...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
