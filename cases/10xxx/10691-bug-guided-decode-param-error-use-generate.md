# vllm-project/vllm#10691: [Bug]: guided decode param error use /generate

| 字段 | 值 |
| --- | --- |
| Issue | [#10691](https://github.com/vllm-project/vllm/issues/10691) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: guided decode param error use /generate

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug use guided decoding through /generate get the following error: Traceback (most recent call last): File "/opt/conda/lib/python3.10/asyncio/events.py", line 80, in _run self._context.run(self._callback, *self._args) File "/opt/conda/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 67, in _log_task_completion raise AsyncEngineDeadError( vllm.engine.async_llm_engine.AsyncEngineDeadError: Task finished unexpectedly. This should never happen! Please open an issue on Github. See stack trace above for the actual cause. INFO: 127.0.0.1:56644 - "POST /generate HTTP/1.1" 500 Internal Server Error ERROR: Exception in ASGI application Traceback (most recent call last): File "/opt/conda/lib/python3.10/site-packages/uvicorn/protocols/http/httptools_impl.py", line 401, in run_asgi result = await app( # type: ignore[func-returns-value] File "/opt/conda/lib/python3.10/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__ return await self.app(scope, receive, send) File "/opt/conda/lib/python3.10/site-packages/fastapi/applications.py", line 1054, in __call__ await super().__c...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ceive, sender) File "/opt/conda/lib/python3.10/site-packages/starlette/routing.py", line 715, in __call__ await self.middleware_stack(scope, receive, send) File "/opt/conda/lib/python3.10/site-packages/starlette/routing...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: Traceback (most recent call last): File "/opt/conda/lib/python3.10/asyncio/events.py", line 80, in _run self._context.run(self._callback, *self._args) File "/opt/conda/lib/python3.10/site-packages/vllm/engine/async_llm_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: .py ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: guided decode param error use /generate bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug use guided decoding through /generate get the following error: Traceback (most r...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ecode param error use /generate bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug use guided decoding through /generate get the following error: Traceback (most recent call last...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
