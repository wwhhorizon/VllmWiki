# vllm-project/vllm#7300: [Bug]: EfficientQAT GPTQ Does load but does not output through api

| 字段 | 值 |
| --- | --- |
| Issue | [#7300](https://github.com/vllm-project/vllm/issues/7300) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: EfficientQAT GPTQ Does load but does not output through api

### Issue 正文摘录

### Your current environment ```text ERROR: Exception in ASGI application Traceback (most recent call last): File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/rpc/client.py", line 232, in generate message = await socket.recv() ^^^^^^^^^^^^^^^^^^^ asyncio.exceptions.CancelledError During handling of the above exception, another exception occurred: Traceback (most recent call last): File "/usr/local/lib/python3.12/dist-packages/uvicorn/protocols/http/httptools_impl.py", line 399, in run_asgi result = await app( # type: ignore[func-returns-value] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/uvicorn/middleware/proxy_headers.py", line 70, in __call__ return await self.app(scope, receive, send) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/fastapi/applications.py", line 1054, in __call__ await super().__call__(scope, receive, send) File "/usr/local/lib/python3.12/dist-packages/starlette/applications.py", line 123, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.12/dist-packages/starlette/middleware/errors.py", line 186, in __call__ raise exc...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: routing.py", line 77, in app await wrap_app_handling_exceptions(app, request)(scope, receive, send) File "/usr/local/lib/python3.12/dist-packages/starlette/_exception_handler.py", line 64, in wrapped_app raise exc File...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ceive, sender) File "/usr/local/lib/python3.12/dist-packages/starlette/routing.py", line 756, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.12/dist-packages/starlette/routing...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: EfficientQAT GPTQ Does load but does not output through api bug ### Your current environment ```text ERROR: Exception in ASGI application Traceback (most recent call last): File "/usr/local/lib/python3.12/dist-pa...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ing. When closing vllm it does output the error above. It is using this quantization https://github.com/OpenGVLab/EfficientQAT Hope this is workable, been experimenting a lot with vllm really love it! Thank you for your...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ut [ChenMnZ/Mistral-Large-Instruct-2407-EfficientQAT-w2g64-GPTQ](https://huggingface.co/ChenMnZ/Mistral-Large-Instruct-2407-EfficientQAT-w2g64-GPTQ) in vllm it does load completely. But when you post a message it keeps...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
