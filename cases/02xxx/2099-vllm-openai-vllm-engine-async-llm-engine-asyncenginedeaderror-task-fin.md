# vllm-project/vllm#2099: 命令行启动vllm服务，openai调用报错；vllm.engine.async_llm_engine.AsyncEngineDeadError: Task finished unexpectedly

| 字段 | 值 |
| --- | --- |
| Issue | [#2099](https://github.com/vllm-project/vllm/issues/2099) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> 命令行启动vllm服务，openai调用报错；vllm.engine.async_llm_engine.AsyncEngineDeadError: Task finished unexpectedly

### Issue 正文摘录

Traceback (most recent call last): File "/home/house365ai/.local/lib/python3.10/site-packages/uvicorn/protocols/http/httptools_impl.py", line 426, in run_asgi result = await app( # type: ignore[func-returns-value] File "/home/house365ai/.local/lib/python3.10/site-packages/uvicorn/middleware/proxy_headers.py", line 84, in __call__ return await self.app(scope, receive, send) File "/home/house365ai/.conda/envs/vllm11/lib/python3.10/site-packages/fastapi/applications.py", line 1106, in __call__ await super().__call__(scope, receive, send) File "/home/house365ai/.conda/envs/vllm11/lib/python3.10/site-packages/starlette/applications.py", line 122, in __call__ await self.middleware_stack(scope, receive, send) File "/home/house365ai/.conda/envs/vllm11/lib/python3.10/site-packages/starlette/middleware/errors.py", line 184, in __call__ raise exc File "/home/house365ai/.conda/envs/vllm11/lib/python3.10/site-packages/starlette/middleware/errors.py", line 162, in __call__ await self.app(scope, receive, _send) File "/home/house365ai/.conda/envs/vllm11/lib/python3.10/site-packages/starlette/middleware/cors.py", line 83, in __call__ await self.app(scope, receive, send) File "/home/house365ai/.con...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ome/house365ai/.conda/envs/vllm11/lib/python3.10/site-packages/starlette/routing.py", line 718, in __call__ await route.handle(scope, receive, send) File "/home/house365ai/.conda/envs/vllm11/lib/python3.10/site-packages...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ome/house365ai/.conda/envs/vllm11/lib/python3.10/site-packages/starlette/routing.py", line 718, in __call__ await route.handle(scope, receive, send) File "/home/house365ai/.conda/envs/vllm11/lib/python3.10/site-packages...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: te-packages/starlette/routing.py", line 66, in app response = await func(request) File "/home/house365ai/.conda/envs/vllm11/lib/python3.10/site-packages/fastapi/routing.py", line 274, in app raw_response = await run_end...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
