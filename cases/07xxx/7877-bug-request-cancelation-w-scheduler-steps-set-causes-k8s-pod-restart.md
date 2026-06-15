# vllm-project/vllm#7877: [Bug]: Request Cancelation w/ Scheduler Steps Set Causes K8s Pod Restart

| 字段 | 值 |
| --- | --- |
| Issue | [#7877](https://github.com/vllm-project/vllm/issues/7877) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Request Cancelation w/ Scheduler Steps Set Causes K8s Pod Restart

### Issue 正文摘录

### Your current environment I am running K8s vLLM OpenAI compatible server on version 0.5.5. The client was a locust load test. ### 🐛 Describe the bug ```bash INFO: 10.65.62.6:37396 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error ERROR: Exception in ASGI application Traceback (most recent call last): File "/usr/local/lib/python3.10/dist-packages/uvicorn/protocols/http/httptools_impl.py", line 401, in run_asgi result = await app( # type: ignore[func-returns-value] File "/usr/local/lib/python3.10/dist-packages/uvicorn/middleware/proxy_headers.py", line 70, in __call__ return await self.app(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/fastapi/applications.py", line 1054, in __call__ await super().__call__(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/starlette/applications.py", line 123, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/starlette/middleware/errors.py", line 186, in __call__ raise exc File "/usr/local/lib/python3.10/dist-packages/starlette/middleware/errors.py", line 164, in __call__ await self.app(scope, receive, _send) File "/usr/local/lib/python3...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Request Cancelation w/ Scheduler Steps Set Causes K8s Pod Restart bug ### Your current environment I am running K8s vLLM OpenAI compatible server on version 0.5.5. The client was a locust load test. ### 🐛 Describ...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ceive, sender) File "/usr/local/lib/python3.10/dist-packages/starlette/routing.py", line 754, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/starlette/routing...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: r current environment I am running K8s vLLM OpenAI compatible server on version 0.5.5. The client was a locust load test. ### 🐛 Describe the bug ```bash INFO: 10.65.62.6:37396 - "POST /v1/chat/completions HTTP/1.1" 500...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ceive, sender) File "/usr/local/lib/python3.10/dist-packages/starlette/routing.py", line 754, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/starlette/routing...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
