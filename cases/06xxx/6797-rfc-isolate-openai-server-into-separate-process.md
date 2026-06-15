# vllm-project/vllm#6797: [RFC]: Isolate OpenAI Server Into Separate Process

| 字段 | 值 |
| --- | --- |
| Issue | [#6797](https://github.com/vllm-project/vllm/issues/6797) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 27; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Isolate OpenAI Server Into Separate Process

### Issue 正文摘录

### Motivation. Currently, the OpenAI API server and AsyncLLMEngine share the same asyncio event loop. This means that the API server and the CPU components of the AsyncLLMEngine contend for the same resources. Below, we have a chart of Llama-3-8B running ShareGPT at QPS=10 on an H100. We can see time is split into three buckets: - Light blue → this is overlapped GPU execution time (call of execute_model) - Orange → this is CPU execution time in the LLM engine - All else → this is API server time - `execute_model` does not block the asyncio event loop as it is run in run_in_execuctor https://github.com/vllm-project/vllm/blob/d92b3c5cdef59533347ac714a70274f186943019/vllm/executor/gpu_executor.py#L143 - So, we believe that some GPU time is currently already overlapped with the API server ### Proposed Change. Enable better overlapping of the API server and `AsyncLLMEngine` via multiprocessing by spitting into two processes that communicate over gRPC with `protobufs`. This is roughly the architecture used by TGI (though TGI has more items in the server than we are proposing here. ### Initial Goal - Write protobuf API to roughly match AsyncLLMEngine `generate()` method, separate API se...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: s. Below, we have a chart of Llama-3-8B running ShareGPT at QPS=10 on an H100. We can see time is split into three buckets: - Light blue → this is overlapped GPU execution time (call of execute_model) - Orange → this is...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: e_model) - Orange → this is CPU execution time in the LLM engine - All else → this is API server time - `execute_model` does not block the asyncio event loop as it is run in run_in_execuctor https://github.com/vllm-proj...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: AsyncLLMEngine contend for the same resources. Below, we have a chart of Llama-3-8B running ShareGPT at QPS=10 on an H100. We can see time is split into three buckets: - Light blue → this is overlapped GPU execution tim...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Currently, the OpenAI API server and AsyncLLMEngine share the same asyncio event loop. This means that the API server and the CPU components of the AsyncLLMEngine contend for the same resources. Below, we have a chart o...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ly to the stream returned by this method. Cancellations can be mapped to request aborts ### Follow Ups Move items that currently run inside `AsyncLLMEngine` into the API Server for better overlap with the GPU - Make nec...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
