# vllm-project/vllm#186: Langchain passes `prompt` as a `list` instead of `str`

| 字段 | 值 |
| --- | --- |
| Issue | [#186](https://github.com/vllm-project/vllm/issues/186) |
| 状态 | closed |
| 标签 | good first issue;feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Langchain passes `prompt` as a `list` instead of `str`

### Issue 正文摘录

As mentioned in the title [this simple example](https://python.langchain.com/docs/get_started/quickstart#llms) passes a list instead of a str. Raw request: ![image](https://github.com/vllm-project/vllm/assets/47108366/197b6dc3-a5b0-49f5-9568-2739de1fbd93) Error Message: `INFO: 127.0.0.1:44226 - "POST /v1/completions HTTP/1.1" 500 Internal Server Error ERROR: Exception in ASGI application Traceback (most recent call last): File "/home/aipath/repo/local-agent/.venv/lib/python3.10/site-packages/uvicorn/protocols/http/httptools_impl.py", line 435, in run_asgi result = await app( # type: ignore[func-returns-value] File "/home/aipath/repo/local-agent/.venv/lib/python3.10/site-packages/uvicorn/middleware/proxy_headers.py", line 78, in __call__ return await self.app(scope, receive, send) File "/home/aipath/repo/local-agent/.venv/lib/python3.10/site-packages/fastapi/applications.py", line 282, in __call__ await super().__call__(scope, receive, send) File "/home/aipath/repo/local-agent/.venv/lib/python3.10/site-packages/starlette/applications.py", line 122, in __call__ await self.middleware_stack(scope, receive, send) File "/home/aipath/repo/local-agent/.venv/lib/python3.10/site-packages/st...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ome/aipath/repo/local-agent/.venv/lib/python3.10/site-packages/starlette/routing.py", line 718, in __call__ await route.handle(scope, receive, send) File "/home/aipath/repo/local-agent/.venv/lib/python3.10/site-packages...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: equest.json()) File "pydantic/main.py", line 341, in pydantic.main.BaseModel.__init__ pydantic.error_wrappers.ValidationError: 1 validation error for CompletionRequest prompt str type expected (type=type_error.str) `
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ome/aipath/repo/local-agent/.venv/lib/python3.10/site-packages/starlette/routing.py", line 718, in __call__ await route.handle(scope, receive, send) File "/home/aipath/repo/local-agent/.venv/lib/python3.10/site-packages...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: in passes `prompt` as a `list` instead of `str` good first issue;feature request As mentioned in the title [this simple example](https://python.langchain.com/docs/get_started/quickstart#llms) passes a list instead of a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
