# vllm-project/vllm#21254: [Feature]: Raise proper HTTP error with details for multimodal input url fetch error

| 字段 | 值 |
| --- | --- |
| Issue | [#21254](https://github.com/vllm-project/vllm/issues/21254) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Raise proper HTTP error with details for multimodal input url fetch error

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In openai online serving mode, when a user sends a chat message with unreachable multimodal(e.g. image/audio/...) urls, vllm server returns a 500 Internal Server Error due to lack of proper error handling for multimodal input fetch stage: ```txt INFO: 127.0.0.1:39126 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error ERROR: Exception in ASGI application Traceback (most recent call last): File "/app/.venv/lib/python3.10/site-packages/uvicorn/protocols/http/httptools_impl.py", line 409, in run_asgi result = await app( # type: ignore[func-returns-value] File "/app/.venv/lib/python3.10/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__ return await self.app(scope, receive, send) File "/app/.venv/lib/python3.10/site-packages/fastapi/applications.py", line 1054, in __call__ await super().__call__(scope, receive, send) File "/app/.venv/lib/python3.10/site-packages/starlette/applications.py", line 112, in __call__ await self.middleware_stack(scope, receive, send) File "/app/.venv/lib/python3.10/site-packages/starlette/middleware/errors.py", line 187, in __call__ raise exc File "/app/.venv/lib/python3.10/site-packa...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: per HTTP error with details for multimodal input url fetch error feature request;stale ### 🚀 The feature, motivation and pitch In openai online serving mode, when a user sends a chat message with unreachable multimodal(...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ceive, sender) File "/app/.venv/lib/python3.10/site-packages/starlette/routing.py", line 714, in __call__ await self.middleware_stack(scope, receive, send) File "/app/.venv/lib/python3.10/site-packages/starlette/routing...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: /vllm/entrypoints/chat_utils.py", line 605, in modality: await asyncio.gather(*items) File "/app/.venv/lib/python3.10/site-packages/vllm/multimodal/utils.py", line 227, in fetch_image_async return await self.load_from_u...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ge='Not Found', url='http://example.com/nonexistant_image.jpg' ``` This blocks a chance for the user to easily find the root cause of the error (it is often the case that the user simply made a typo in their image url o...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
