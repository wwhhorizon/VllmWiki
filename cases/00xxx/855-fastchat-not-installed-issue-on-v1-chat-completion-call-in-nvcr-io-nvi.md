# vllm-project/vllm#855: "FastChat not installed" issue on /v1/chat/completion call in nvcr.io/nvidia/pytorch:22.12-py3 container.

| 字段 | 值 |
| --- | --- |
| Issue | [#855](https://github.com/vllm-project/vllm/issues/855) |
| 状态 | closed |
| 标签 |  |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> "FastChat not installed" issue on /v1/chat/completion call in nvcr.io/nvidia/pytorch:22.12-py3 container.

### Issue 正文摘录

An interesting one. I can run `python -m vllm.entrypoints.openai.api_server --model facebook/opt-125m` without issue, and /completion calls work fine. However, when I make a /chat/completion call, I receive the following: ` INFO: ::1:38566 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error ERROR: Exception in ASGI application Traceback (most recent call last): File "/usr/local/lib/python3.8/dist-packages/uvicorn/protocols/http/h11_impl.py", line 408, in run_asgi result = await app( # type: ignore[func-returns-value] File "/usr/local/lib/python3.8/dist-packages/uvicorn/middleware/proxy_headers.py", line 84, in __call__ return await self.app(scope, receive, send) File "/usr/local/lib/python3.8/dist-packages/fastapi/applications.py", line 289, in __call__ await super().__call__(scope, receive, send) File "/usr/local/lib/python3.8/dist-packages/starlette/applications.py", line 122, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.8/dist-packages/starlette/middleware/errors.py", line 184, in __call__ raise exc File "/usr/local/lib/python3.8/dist-packages/starlette/middleware/errors.py", line 162, in __call__ await self.app(scope,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: "FastChat not installed" issue on /v1/chat/completion call in nvcr.io/nvidia/pytorch:22.12-py3 container. An interesting one. I can run `python -m vllm.entrypoints.openai.api_server --model facebook/opt-125m` without is...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: receive, send) File "/usr/local/lib/python3.8/dist-packages/starlette/routing.py", line 718, in __call__ await route.handle(scope, receive, send) File "/usr/local/lib/python3.8/dist-packages/starlette/routing.py", line...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: resting one. I can run `python -m vllm.entrypoints.openai.api_server --model facebook/opt-125m` without issue, and /completion calls work fine. However, when I make a /chat/completion call, I receive the following: ` IN...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: receive, send) File "/usr/local/lib/python3.8/dist-packages/starlette/routing.py", line 718, in __call__ await route.handle(scope, receive, send) File "/usr/local/lib/python3.8/dist-packages/starlette/routing.py", line...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ackages/starlette/routing.py", line 66, in app response = await func(request) File "/usr/local/lib/python3.8/dist-packages/fastapi/routing.py", line 273, in app raw_response = await run_endpoint_function( File "/usr/loc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
