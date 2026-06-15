# vllm-project/vllm#1380: AsyncEngineDeadError: Task finished unexpectedly

| 字段 | 值 |
| --- | --- |
| Issue | [#1380](https://github.com/vllm-project/vllm/issues/1380) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> AsyncEngineDeadError: Task finished unexpectedly

### Issue 正文摘录

Hey! I've been facing the following error with the latest version of vllm. The stacktrace is below: > INFO: 127.0.0.1:52238 - "POST /generate HTTP/1.1" 500 Internal Server Error ERROR: Exception in ASGI application Traceback (most recent call last): File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 28, in _raise_exception_on_finish task.result() File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 351, in run_engine_loop has_requests_in_progress = await self.engine_step() File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 330, in engine_step request_outputs = await self.engine.step_async() File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 191, in step_async output = await self._run_workers_async( File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 228, in _run_workers_async assert output == other_output AssertionError > The above exception was the direct cause of the following exception: > Traceback (most recent call last): File "/usr/local/lib/python3.10/dist-packages/uvicorn/protocols/http/httptools_impl.py", lin...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: AsyncEngineDeadError: Task finished unexpectedly bug Hey! I've been facing the following error with the latest version of vllm. The stacktrace is below: > INFO: 127.0.0.1:52238 - "POST /generate HTTP/1.1" 500 Internal S...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: , receive, send) File "/usr/local/lib/python3.10/dist-packages/starlette/routing.py", line 718, in __call__ await route.handle(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/starlette/routing.py", l...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: stack trace above for the actual cause. I am using vLLM inside Docker, CUDA version is "11.8.0", torch version is 2.0.1+cu118 development ci_build;frontend_api cuda crash env_dependency Hey! I've been facing the followi...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: , receive, send) File "/usr/local/lib/python3.10/dist-packages/starlette/routing.py", line 718, in __call__ await route.handle(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/starlette/routing.py", l...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: kages/vllm/engine/async_llm_engine.py", line 351, in run_engine_loop has_requests_in_progress = await self.engine_step() File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 330, in engin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
