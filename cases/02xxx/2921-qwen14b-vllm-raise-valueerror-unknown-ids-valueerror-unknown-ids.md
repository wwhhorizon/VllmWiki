# vllm-project/vllm#2921: qwen14b+vllm raise ValueError("unknown ids") ValueError: unknown ids

| 字段 | 值 |
| --- | --- |
| Issue | [#2921](https://github.com/vllm-project/vllm/issues/2921) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> qwen14b+vllm raise ValueError("unknown ids") ValueError: unknown ids

### Issue 正文摘录

When using the vllm v0.2.4 with a large model for question answering, an error is encountered during execution. The error message indicates an issue related to unknown IDs in the tokenizer. Steps to Reproduce: Use vllm v0.2.4 with a qwen-14b-chat model for question answering. Execute the model for question answering. Expected Behavior: The model should successfully process the question and provide an answer. Actual Behavior: The following error is encountered during execution: 2024-02-19 00:30:41 | ERROR | asyncio | Exception in callback functools.partial( , request_tracker= ) handle: , request_tracker= )> Traceback (most recent call last): File "/root/miniconda3/envs/vllm/lib/python3.11/site-packages/vllm/engine/async_llm_engine.py", line 28, in _raise_exception_on_finish task.result() File "/root/miniconda3/envs/vllm/lib/python3.11/site-packages/vllm/engine/async_llm_engine.py", line 359, in run_engine_loop has_requests_in_progress = await self.engine_step() ^^^^^^^^^^^^^^^^^^^^^^^^ File "/root/miniconda3/envs/vllm/lib/python3.11/site-packages/vllm/engine/async_llm_engine.py", line 338, in engine_step request_outputs = await self.engine.step_async() ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: qwen14b+vllm raise ValueError("unknown ids") ValueError: unknown ids When using the vllm v0.2.4 with a large model for question answering, an error is encountered during execution. The error message indicates an issue re
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: 00:30:41 | ERROR | asyncio | Exception in callback functools.partial( , request_tracker= ) handle: , request_tracker= )> Traceback (most recent call last): File "/root/miniconda3/envs/vllm/lib/python3.11/site-packages/v...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: File "/root/miniconda3/envs/vllm/lib/python3.11/site-packages/starlette/routing.py", line 718, in __call__ 2024-02-19 00:30:41 | ERROR | stderr | await route.handle(scope, receive, send) 2024-02-19 00:30:41 | ERROR | st...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ge indicates an issue related to unknown IDs in the tokenizer. Steps to Reproduce: Use vllm v0.2.4 with a qwen-14b-chat model for question answering. Execute the model for question answering. Expected Behavior: The mode...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: is encountered during execution: 2024-02-19 00:30:41 | ERROR | asyncio | Exception in callback functools.partial( , request_tracker= ) handle: , request_tracker= )> Traceback (most recent call last): File "/root/minicon...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
