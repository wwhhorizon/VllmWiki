# vllm-project/vllm#917: once occur error the inference will stuck

| 字段 | 值 |
| --- | --- |
| Issue | [#917](https://github.com/vllm-project/vllm/issues/917) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> once occur error the inference will stuck

### Issue 正文摘录

service is running got the following error: ``` openai.error.Timeout: Request timed out: HTTPConnectionPool(host='172.26.1.30', port=8000): Read timed out. (read timeout=600) ``` ``` ERROR: Exception in ASGI application Traceback (most recent call last): File "/usr/local/lib/python3.8/dist-packages/uvicorn/protocols/http/h11_impl.py", line 408, in run_asgi result = await app( # type: ignore[func-returns-value] File "/usr/local/lib/python3.8/dist-packages/uvicorn/middleware/proxy_headers.py", line 84, in __call__ return await self.app(scope, receive, send) File "/usr/local/lib/python3.8/dist-packages/fastapi/applications.py", line 292, in __call__ await super().__call__(scope, receive, send) File "/usr/local/lib/python3.8/dist-packages/starlette/applications.py", line 122, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.8/dist-packages/starlette/middleware/errors.py", line 184, in __call__ raise exc File "/usr/local/lib/python3.8/dist-packages/starlette/middleware/errors.py", line 162, in __call__ await self.app(scope, receive, _send) File "/usr/local/lib/python3.8/dist-packages/starlette/middleware/cors.py", line 83, in __call__ await sel...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: to_tokens return self._convert_id_to_token(ids) File "/root/.cache/huggingface/modules/transformers_modules/Qwen-7B-Chat/tokenization_qwen.py", line 198, in _convert_id_to_token raise ValueError("unknown ids") ValueErro...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: k service is running got the following error: ``` openai.error.Timeout: Request timed out: HTTPConnectionPool(host='172.26.1.30', port=8000): Read timed out. (read timeout=600) ``` ``` ERROR: Exception in ASGI applicati...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: receive, send) File "/usr/local/lib/python3.8/dist-packages/starlette/routing.py", line 718, in __call__ await route.handle(scope, receive, send) File "/usr/local/lib/python3.8/dist-packages/starlette/routing.py", line...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: receive, send) File "/usr/local/lib/python3.8/dist-packages/starlette/routing.py", line 718, in __call__ await route.handle(scope, receive, send) File "/usr/local/lib/python3.8/dist-packages/starlette/routing.py", line...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
