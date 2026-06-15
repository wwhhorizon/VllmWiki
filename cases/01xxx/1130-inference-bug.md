# vllm-project/vllm#1130: inference Bug

| 字段 | 值 |
| --- | --- |
| Issue | [#1130](https://github.com/vllm-project/vllm/issues/1130) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> inference Bug

### Issue 正文摘录

问题描述： 使用vllm进行gpt2推理，输入prompt为空会触发以下error，之后任何请求都不会出结果，除非重启服务；不仅是这个场景，其他情况下触发这个error也会出现相同情况 Problem Description: When using vllm for gpt2 inference, if the input prompt is empty, it triggers the following error, and thereafter no request will yield results unless the service is restarted. This situation occurs not only in this scenario but also in other cases where this error is triggered. error: ERROR: Exception in ASGI application Traceback (most recent call last): File "/home/ubuntu/anaconda3/envs/lyra/lib/python3.9/site-packages/uvicorn/protocols/http/h11_impl.py", line 407, in run_asgi result = await app( # type: ignore[func-returns-value] File "/home/ubuntu/anaconda3/envs/lyra/lib/python3.9/site-packages/uvicorn/middleware/proxy_headers.py", line 78, in __call__ return await self.app(scope, receive, send) File "/home/ubuntu/anaconda3/envs/lyra/lib/python3.9/site-packages/fastapi/applications.py", line 270, in __call__ await super().__call__(scope, receive, send) File "/home/ubuntu/anaconda3/envs/lyra/lib/python3.9/site-packages/starlette/applications.py", line 124, in __call__ await self.middleware_stack(scope, receive, send) File "/home/ubuntu/anaconda3/envs/lyra/lib/pytho...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: "/home/ubuntu/anaconda3/envs/lyra/lib/python3.9/site-packages/starlette/routing.py", line 706, in __call__ await route.handle(scope, receive, send) File "/home/ubuntu/anaconda3/envs/lyra/lib/python3.9/site-packages/star...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: nput prompt is empty, it triggers the following error, and thereafter no request will yield results unless the service is restarted. This situation occurs not only in this scenario but also in other cases where this err...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ntu/anaconda3/envs/lyra/lib/python3.9/site-packages/anyio/_backends/_asyncio.py", line 597, in __aexit__ raise exceptions[0] File "/home/ubuntu/anaconda3/envs/lyra/lib/python3.9/site-packages/starlette/responses.py", li...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: "/home/ubuntu/anaconda3/envs/lyra/lib/python3.9/site-packages/starlette/routing.py", line 706, in __call__ await route.handle(scope, receive, send) File "/home/ubuntu/anaconda3/envs/lyra/lib/python3.9/site-packages/star...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
