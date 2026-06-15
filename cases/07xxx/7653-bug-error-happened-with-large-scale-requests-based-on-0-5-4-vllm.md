# vllm-project/vllm#7653: [Bug]: Error happened with Large scale requests based on 0.5.4 vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#7653](https://github.com/vllm-project/vllm/issues/7653) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 20; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Error happened with Large scale requests based on 0.5.4 vllm

### Issue 正文摘录

### Your current environment When I use `python -m vllm.entrypoints.openai.api_server` as the API request method and make a large number of requests (at least in the thousands), an error occurs. ### 🐛 Describe the bug Traceback (most recent call last): File "/data/anaconda3/lib/python3.11/site-packages/starlette/middleware/base.py", line 159, in call_next message = await recv_stream.receive() ^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/data/anaconda3/lib/python3.11/site-packages/anyio/streams/memory.py", line 101, in receive raise EndOfStream anyio.EndOfStream During handling of the above exception, another exception occurred: Traceback (most recent call last): File "/data/anaconda3/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 419, in run_asgi result = await app( # type: ignore[func-returns-value] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/data/anaconda3/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 84, in __call__ return await self.app(scope, receive, send) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/data/anaconda3/lib/python3.11/site-packages/fastapi/applications.py", line 1054, in __call__ await super().__call__(scope,...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: tte/middleware/base.py", line 191, in __call__ response = await self.dispatch_func(request, call_next) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/data/anaconda3/lib/python3.11/site-packages/vllm/entrypoints/ope...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Bug]: Error happened with Large scale requests based on 0.5.4 vllm bug ### Your current environment When I use `python -m vllm.entrypoints.openai.api_server` as the API request method and make a large number of request...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ages/anyio/streams/memory.py", line 76, in receive_nowait raise WouldBlock anyio.WouldBlock
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: , sender) File "/data/anaconda3/lib/python3.11/site-packages/starlette/routing.py", line 758, in __call__ await self.middleware_stack(scope, receive, send) File "/data/anaconda3/lib/python3.11/site-packages/starlette/ro...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Error happened with Large scale requests based on 0.5.4 vllm bug ### Your current environment When I use `python -m vllm.entrypoints.openai.api_server` as the API request method and make a large number of request...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
