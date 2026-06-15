# vllm-project/vllm#11400: [RFC]: Fully SPMD Execution for Offline Inference

| 字段 | 值 |
| --- | --- |
| Issue | [#11400](https://github.com/vllm-project/vllm/issues/11400) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Fully SPMD Execution for Offline Inference

### Issue 正文摘录

### Motivation. TL;DR: Introducing a fully SPMD-style LLMEngine execution pattern to improve offline inference throughput. The RFC draft is initiated by @PeterSH6 # Background and Motivation ## Inherent dispatch overhead in single-controller paradigm For distributed offline inference, vLLM leverages a centralized controller process (e.g., Ray Driver) to broadcast the scheduler output to the workers. After workers' execution, the output is gathered from the workers to the centralized controller process to perform the next iteration scheduling. While this single-controller paradigm offers better user experience, it introduces throughput limitations. Therefore, to launch a generation call, vLLM obey the following procedure: ``` python3 offline_inference.py # launch the centralized controller process (i.e., LLMEngine) # inside the LLMEngine llm_engine.distributed_gpu_executor._run_workers('start_worker_execution_loop', ...) # execute the model # inside the _run_workers worker_outputs = [ worker.execute_method(method, *args, **kwargs) for worker in self.workers ] ``` From the code above, the `_run_workers` functions will cause unneglible overhead. Although recent proposals managed to e...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: SPMD Execution for Offline Inference RFC ### Motivation. TL;DR: Introducing a fully SPMD-style LLMEngine execution pattern to improve offline inference throughput. The RFC draft is initiated by @PeterSH6 # Background an...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: gine execution pattern to improve offline inference throughput. The RFC draft is initiated by @PeterSH6 # Background and Motivation ## Inherent dispatch overhead in single-controller paradigm For distributed offline inf...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ully SPMD-style LLMEngine execution pattern to improve offline inference throughput. The RFC draft is initiated by @PeterSH6 # Background and Motivation ## Inherent dispatch overhead in single-controller paradigm For di...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ent but also facilitates straightforward implementation of data parallelism on top of the SPMD architecture. The resulting system would be more maintainable and scalable across multiple nodes. # Major Benefits Based on...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: _executor._run_workers('start_worker_execution_loop', ...) # execute the model # inside the _run_workers worker_outputs = [ worker.execute_method(method, *args, **kwargs) for worker in self.workers ] ``` From the code a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
