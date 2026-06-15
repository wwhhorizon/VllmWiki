# vllm-project/vllm#521: datatype overflow

| 字段 | 值 |
| --- | --- |
| Issue | [#521](https://github.com/vllm-project/vllm/issues/521) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> datatype overflow

### Issue 正文摘录

When setting num-batched-tokens > 8k (I am working with a 12k model) it seems like there is a datatype overflow in the attention layer. Here is the error I receive: ``` Traceback (most recent call last): File "/home/paperspace/.pyenv/versions/3.10.12/lib/python3.10/site-packages/uvicorn/protocols/http/h11_impl.py", line 408, in run_asgi result = await app( # type: ignore[func-returns-value] File "/home/paperspace/.pyenv/versions/3.10.12/lib/python3.10/site-packages/uvicorn/middleware/proxy_headers.py", line 84, in __call__ return await self.app(scope, receive, send) File "/home/paperspace/.pyenv/versions/3.10.12/lib/python3.10/site-packages/fastapi/applications.py", line 289, in __call__ await super().__call__(scope, receive, send) File "/home/paperspace/.pyenv/versions/3.10.12/lib/python3.10/site-packages/starlette/applications.py", line 122, in __call__ await self.middleware_stack(scope, receive, send) File "/home/paperspace/.pyenv/versions/3.10.12/lib/python3.10/site-packages/starlette/middleware/errors.py", line 184, in __call__ raise exc File "/home/paperspace/.pyenv/versions/3.10.12/lib/python3.10/site-packages/starlette/middleware/errors.py", line 162, in __call__ await sel...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: /model_executor/models/mpt.py", line 202, in forward hidden_states = block( File "/home/paperspace/.pyenv/versions/3.10.12/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1501, in _call_impl return forwar...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: aperspace/.pyenv/versions/3.10.12/lib/python3.10/site-packages/starlette/routing.py", line 718, in __call__ await route.handle(scope, receive, send) File "/home/paperspace/.pyenv/versions/3.10.12/lib/python3.10/site-pac...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ``` Traceback (most recent call last): File "/home/paperspace/.pyenv/versions/3.10.12/lib/python3.10/site-packages/uvicorn/protocols/http/h11_impl.py", line 408, in run_asgi result = await app( # type: ignore[func-retur...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: erflow bug When setting num-batched-tokens > 8k (I am working with a 12k model) it seems like there is a datatype overflow in the attention layer. Here is the error I receive: ``` Traceback (most recent call last): File...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: aperspace/.pyenv/versions/3.10.12/lib/python3.10/site-packages/starlette/routing.py", line 718, in __call__ await route.handle(scope, receive, send) File "/home/paperspace/.pyenv/versions/3.10.12/lib/python3.10/site-pac...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
