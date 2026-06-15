# vllm-project/vllm#2197: vllm.engine.async_llm_engine.AsyncEngineDeadError

| 字段 | 值 |
| --- | --- |
| Issue | [#2197](https://github.com/vllm-project/vllm/issues/2197) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> vllm.engine.async_llm_engine.AsyncEngineDeadError

### Issue 正文摘录

2023-12-19 18:11:16 | ERROR | stderr | 2023-12-19 18:11:16 | ERROR | stderr | The above exception was the direct cause of the following exception: 2023-12-19 18:11:16 | ERROR | stderr | 2023-12-19 18:11:16 | ERROR | stderr | Traceback (most recent call last): 2023-12-19 18:11:16 | ERROR | stderr | File "/root/miniconda3/envs/pytorch21/lib/python3.10/site-packages/uvicorn/protocols/http/httptools_impl.py", line 426, in run_asgi 2023-12-19 18:11:16 | ERROR | stderr | result = await app( # type: ignore[func-returns-value] 2023-12-19 18:11:16 | ERROR | stderr | File "/root/miniconda3/envs/pytorch21/lib/python3.10/site-packages/uvicorn/middleware/proxy_headers.py", line 84, in __call__ 2023-12-19 18:11:16 | ERROR | stderr | return await self.app(scope, receive, send) 2023-12-19 18:11:16 | ERROR | stderr | File "/root/miniconda3/envs/pytorch21/lib/python3.10/site-packages/fastapi/applications.py", line 1106, in __call__ 2023-12-19 18:11:16 | ERROR | stderr | await super().__call__(scope, receive, send) 2023-12-19 18:11:16 | ERROR | stderr | File "/root/miniconda3/envs/pytorch21/lib/python3.10/site-packages/starlette/applications.py", line 122, in __call__ 2023-12-19 18:11:16 | ERROR | s...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: "/root/miniconda3/envs/pytorch21/lib/python3.10/site-packages/starlette/routing.py", line 718, in __call__ 2023-12-19 18:11:16 | ERROR | stderr | await route.handle(scope, receive, send) 2023-12-19 18:11:16 | ERROR | st...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: iconda3/envs/pytorch21/lib/python3.10/site-packages/anyio/_backends/_asyncio.py", line 597, in __aexit__ 2023-12-19 18:11:16 | ERROR | stderr | raise exceptions[0] 2023-12-19 18:11:16 | ERROR | stderr | File "/root/mini...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: "/root/miniconda3/envs/pytorch21/lib/python3.10/site-packages/starlette/routing.py", line 718, in __call__ 2023-12-19 18:11:16 | ERROR | stderr | await route.handle(scope, receive, send) 2023-12-19 18:11:16 | ERROR | st...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: in generate_stream 2023-12-19 18:11:16 | ERROR | stderr | async for request_output in results_generator: 2023-12-19 18:11:16 | ERROR | stderr | File "/root/vllm-gptq/vllm/engine/async_llm_engine.py", line 435, in genera...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
