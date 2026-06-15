# vllm-project/vllm#5729: [Bug]: asyncio.exceptions.CancelledError  asyncio.exceptions.TimeoutError

| 字段 | 值 |
| --- | --- |
| Issue | [#5729](https://github.com/vllm-project/vllm/issues/5729) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: asyncio.exceptions.CancelledError  asyncio.exceptions.TimeoutError

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug ERROR: Exception in ASGI application Traceback (most recent call last): File "/root/anaconda3/envs/vllm/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 506, in engine_step request_outputs = await self.engine.step_async() File "/root/anaconda3/envs/vllm/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 235, in step_async output = await self.model_executor.execute_model_async( File "/root/anaconda3/envs/vllm/lib/python3.10/site-packages/vllm/executor/distributed_gpu_executor.py", line 166, in execute_model_async return await self._driver_execute_model_async(execute_model_req) File "/root/anaconda3/envs/vllm/lib/python3.10/site-packages/vllm/executor/multiproc_gpu_executor.py", line 149, in _driver_execute_model_async return await self.driver_exec_model(execute_model_req) asyncio.exceptions.CancelledError During handling of the above exception, another exception occurred: Traceback (most recent call last): File "/root/anaconda3/envs/vllm/lib/python3.10/asyncio/tasks.py", line 456, in wait_for return fut.result() asyncio.exceptions.CancelledError...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: File "/root/anaconda3/envs/vllm/lib/python3.10/site-packages/starlette/routing.py", line 756, in __call__ await self.middleware_stack(scope, receive, send) File "/root/anaconda3/envs/vllm/lib/python3.10/site-packages/st...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: asyncio.exceptions.CancelledError asyncio.exceptions.TimeoutError bug ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug ERROR: Exception in ASGI application Tra...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ne/async_llm_engine.py", line 235, in step_async output = await self.model_executor.execute_model_async( File "/root/anaconda3/envs/vllm/lib/python3.10/site-packages/vllm/executor/distributed_gpu_executor.py", line 166,...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: File "/root/anaconda3/envs/vllm/lib/python3.10/site-packages/starlette/routing.py", line 756, in __call__ await self.middleware_stack(scope, receive, send) File "/root/anaconda3/envs/vllm/lib/python3.10/site-packages/st...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: -packages/vllm/engine/async_llm_engine.py", line 506, in engine_step request_outputs = await self.engine.step_async() File "/root/anaconda3/envs/vllm/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 2...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
