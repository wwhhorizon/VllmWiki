# vllm-project/vllm#2706: The echo parameters and request logs seem to have some issues in vLLM v0.3.0 version (/v1/completions)

| 字段 | 值 |
| --- | --- |
| Issue | [#2706](https://github.com/vllm-project/vllm/issues/2706) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> The echo parameters and request logs seem to have some issues in vLLM v0.3.0 version (/v1/completions)

### Issue 正文摘录

In vLLM v0.3.0 version, logprobs appears to have expired. My personal guess is that it's due to the Pydantic version. In Pydantic2 version, use model_ dump() method doesn't seem to handle logprops very well. ![question](https://github.com/vllm-project/vllm/assets/49606519/986f5dc2-5559-405d-a84b-99ca1c58c16a) ```shell ERROR: Exception in ASGI application Traceback (most recent call last): File "/usr/local/lib/python3.10/dist-packages/uvicorn/protocols/http/httptools_impl.py", line 419, in run_asgi result = await app( # type: ignore[func-returns-value] File "/usr/local/lib/python3.10/dist-packages/uvicorn/middleware/proxy_headers.py", line 84, in __call__ return await self.app(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/fastapi/applications.py", line 1054, in __call__ await super().__call__(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/starlette/applications.py", line 123, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/starlette/middleware/errors.py", line 186, in __call__ raise exc File "/usr/local/lib/python3.10/dist-packages/starlette/middleware/errors.py", line 164, in __c...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: uess is that it's due to the Pydantic version. In Pydantic2 version, use model_ dump() method doesn't seem to handle logprops very well. ![question](https://github.com/vllm-project/vllm/assets/49606519/986f5dc2-5559-405...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: The echo parameters and request logs seem to have some issues in vLLM v0.3.0 version (/v1/completions) stale In vLLM v0.3.0 version, logprobs appears to have expired. My personal guess is that it's due to the Pydantic v...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ceive, sender) File "/usr/local/lib/python3.10/dist-packages/starlette/routing.py", line 762, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/starlette/routing...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: echo parameters and request logs seem to have some issues in vLLM v0.3.0 version (/v1/completions) stale In vLLM v0.3.0 version, logprobs appears to have expired. My personal guess is that it's due to the Pydantic versi...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ceive, sender) File "/usr/local/lib/python3.10/dist-packages/starlette/routing.py", line 762, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/starlette/routing...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
