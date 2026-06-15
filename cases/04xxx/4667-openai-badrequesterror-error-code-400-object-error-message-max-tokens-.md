# vllm-project/vllm#4667: openai.BadRequestError: Error code: 400 - {'object': 'error', 'message': 'max_tokens must be at least 1, got -186.', 'type': 'BadRequestError', 'param': None, 'code': 400}

| 字段 | 值 |
| --- | --- |
| Issue | [#4667](https://github.com/vllm-project/vllm/issues/4667) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> openai.BadRequestError: Error code: 400 - {'object': 'error', 'message': 'max_tokens must be at least 1, got -186.', 'type': 'BadRequestError', 'param': None, 'code': 400}

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug ERROR: Exception in ASGI application Traceback (most recent call last): File "/usr/local/lib/python3.8/dist-packages/uvicorn/protocols/http/httptools_impl.py", line 426, in run_asgi result = await app( # type: ignore[func-returns-value] File "/usr/local/lib/python3.8/dist-packages/uvicorn/middleware/proxy_headers.py", line 84, in __call__ return await self.app(scope, receive, send) File "/usr/local/lib/python3.8/dist-packages/fastapi/applications.py", line 1106, in __call__ await super().__call__(scope, receive, send) File "/usr/local/lib/python3.8/dist-packages/starlette/applications.py", line 122, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.8/dist-packages/starlette/middleware/errors.py", line 184, in __call__ raise exc File "/usr/local/lib/python3.8/dist-packages/starlette/middleware/errors.py", line 162, in __call__ await self.app(scope, receive, _send) File "/usr/local/lib/python3.8/dist-packages/starlette/middleware/cors.py", line 91, in __call__ await self.simple_response(scope, receive, send, request_headers=headers) File "/us...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: receive, send) File "/usr/local/lib/python3.8/dist-packages/starlette/routing.py", line 718, in __call__ await route.handle(scope, receive, send) File "/usr/local/lib/python3.8/dist-packages/starlette/routing.py", line...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ve)) File "/usr/local/lib/python3.8/dist-packages/anyio/_backends/_asyncio.py", line 597, in __aexit__ raise exceptions[0] File "/usr/local/lib/python3.8/dist-packages/starlette/responses.py", line 273, in wrap await fu...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: receive, send) File "/usr/local/lib/python3.8/dist-packages/starlette/routing.py", line 718, in __call__ await route.handle(scope, receive, send) File "/usr/local/lib/python3.8/dist-packages/starlette/routing.py", line...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: openai.BadRequestError: Error code: 400 - {'object': 'error', 'message': 'max_tokens must be at least 1, got -186.', 'type': 'BadRequestError', 'param': None, 'code': 400} bug ### Your current environment ```text The ou...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
