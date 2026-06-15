# vllm-project/vllm#5600: [Feature]: support Qwen2 embedding

| 字段 | 值 |
| --- | --- |
| Issue | [#5600](https://github.com/vllm-project/vllm/issues/5600) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: support Qwen2 embedding

### Issue 正文摘录

### 🚀 The feature, motivation and pitch in the Mteb leaderboard, the current best embedding model is `Alibaba-NLP/gte-Qwen2-7B-instruct`. However, using the embedding endpoint on it returns the following error currently: ```python INFO: 127.0.0.1:46414 - "POST /v1/embeddings HTTP/1.1" 500 Internal Server Error ERROR: Exception in ASGI application Traceback (most recent call last): File "/usr/local/lib/python3.10/dist-packages/uvicorn/protocols/http/httptools_impl.py", line 399, in run_asgi result = await app( # type: ignore[func-returns-value] File "/usr/local/lib/python3.10/dist-packages/uvicorn/middleware/proxy_headers.py", line 70, in __call__ return await self.app(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/fastapi/applications.py", line 1054, in __call__ await super().__call__(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/starlette/applications.py", line 123, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/starlette/middleware/errors.py", line 186, in __call__ raise exc File "/usr/local/lib/python3.10/dist-packages/starlette/middleware/errors.py", line 164, in __call__ aw...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: support Qwen2 embedding feature request;stale ### 🚀 The feature, motivation and pitch in the Mteb leaderboard, the current best embedding model is `Alibaba-NLP/gte-Qwen2-7B-instruct`. However, using the embed...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: support Qwen2 embedding feature request;stale ### 🚀 The feature, motivation and pitch in the Mteb leaderboard, the current best embedding model is `Alibaba-NLP/gte-Qwen2-7B-instruct`. However, using the embed...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ceive, sender) File "/usr/local/lib/python3.10/dist-packages/starlette/routing.py", line 756, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/starlette/routing...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ", line 532, in run_engine_loop has_requests_in_progress = await asyncio.wait_for( File "/usr/lib/python3.10/asyncio/tasks.py", line 445, in wait_for return fut.result() File "/usr/local/lib/python3.10/dist-packages/vll...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: in execute_model output = self.model_runner.execute_model(seq_group_metadata_list, File "/usr/local/lib/python3.10/dist-packages/torch/utils/_contextlib.py", line 115, in decorate_context return func(*args, **kwargs) Fi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
