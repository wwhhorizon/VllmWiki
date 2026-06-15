# vllm-project/vllm#4882: [Usage]: why can't I  set gpu nums while use "tensor_parallel_size"?

| 字段 | 值 |
| --- | --- |
| Issue | [#4882](https://github.com/vllm-project/vllm/issues/4882) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: why can't I  set gpu nums while use "tensor_parallel_size"?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I notice there is a annotation, but why ``` # Apply batch inference for all input data. ds = ds.map_batches( LLMPredictor, # Set the concurrency to the number of LLM instances. concurrency=10, # Specify the number of GPUs required per LLM instance. # NOTE: Do NOT set `num_gpus` when using vLLM with tensor-parallelism # (i.e., `tensor_parallel_size`). num_gpus=1, # Specify the batch size for inference. batch_size=32, ) ```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: concurrency to the number of LLM instances. concurrency=10, # Specify the number of GPUs required per LLM instance. # NOTE: Do NOT set `num_gpus` when using vLLM with tensor-parallelism # (i.e., `tensor_parallel_size`)....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: . # NOTE: Do NOT set `num_gpus` when using vLLM with tensor-parallelism # (i.e., `tensor_parallel_size`). num_gpus=1, # Specify the batch size for inference. batch_size=32, ) ```
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: sage]: why can't I set gpu nums while use "tensor_parallel_size"? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I notice there is a annotat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
