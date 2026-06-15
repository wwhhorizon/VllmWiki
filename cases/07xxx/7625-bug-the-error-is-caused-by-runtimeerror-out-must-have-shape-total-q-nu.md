# vllm-project/vllm#7625: [Bug]: The error is caused by: RuntimeError: out must have shape (total_q, num_heads, head_size_og), leading to the following error: vllm.engine.async_llm_engine.AsyncEngineDeadError: Background loop has errored already.

| 字段 | 值 |
| --- | --- |
| Issue | [#7625](https://github.com/vllm-project/vllm/issues/7625) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | runtime_err |
| Operator 关键词 | attention;cuda;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: The error is caused by: RuntimeError: out must have shape (total_q, num_heads, head_size_og), leading to the following error: vllm.engine.async_llm_engine.AsyncEngineDeadError: Background loop has errored already.

### Issue 正文摘录

### Your current environment These is the 0.5.0 environments ### 🐛 Describe the bug **1、These log files:** Traceback (most recent call last): File "/usr/local/lib/python3.10/dist-packages/uvicorn/protocols/http/httptools_impl.py", line 399, in run_asgi result = await app( # type: ignore[func-returns-value] File "/usr/local/lib/python3.10/dist-packages/uvicorn/middleware/proxy_headers.py", line 70, in __call__ return await self.app(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/fastapi/applications.py", line 1054, in __call__ await super().__call__(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/starlette/applications.py", line 123, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/starlette/middleware/errors.py", line 186, in __call__ raise exc File "/usr/local/lib/python3.10/dist-packages/starlette/middleware/errors.py", line 164, in __call__ await self.app(scope, receive, _send) File "/usr/local/lib/python3.10/dist-packages/starlette/middleware/cors.py", line 85, in __call__ await self.app(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/starlette/middleware/exce...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: lm_engine.AsyncEngineDeadError: Background loop has errored already. bug;stale ### Your current environment These is the 0.5.0 environments ### 🐛 Describe the bug **1、These log files:** Traceback (most recent call last)...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: in execute_model output = self.model_runner.execute_model(seq_group_metadata_list, File "/usr/local/lib/python3.10/dist-packages/torch/utils/_contextlib.py", line 115, in decorate_context return func(*args, **kwargs) Fi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ne/async_llm_engine.py", line 235, in step_async output = await self.model_executor.execute_model_async( File "/usr/local/lib/python3.10/dist-packages/vllm/executor/gpu_executor.py", line 117, in execute_model_async out...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ceive, sender) File "/usr/local/lib/python3.10/dist-packages/starlette/routing.py", line 756, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/starlette/routing...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ", line 529, in run_engine_loop has_requests_in_progress = await asyncio.wait_for( File "/usr/lib/python3.10/asyncio/tasks.py", line 445, in wait_for return fut.result() File "/usr/local/lib/python3.10/dist-packages/vll...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
