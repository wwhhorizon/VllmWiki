# vllm-project/vllm#18890: [Bug]: vllm启动模型后使用openai格式请求传base64值有问题

| 字段 | 值 |
| --- | --- |
| Issue | [#18890](https://github.com/vllm-project/vllm/issues/18890) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm启动模型后使用openai格式请求传base64值有问题

### Issue 正文摘录

### Your current environment 使用vllm0.7.3部署的qwen2.5vl-7b模型，使用openai格式请求接口。 方法1是在代码中读取本地文件然后转base64传入大模型中，正常。 方法2是将本地图片转换好的base64直接传入大模型中，报错。 下面是我传入的图片，请问是什么问题？ ![Image](https://github.com/user-attachments/assets/db40eee5-5de0-4c9a-9d15-6b266469b766) ### 🐛 Describe the bug ERROR: Exception in ASGI application Traceback (most recent call last): File ".local/lib/python3.10/site-packages/uvicorn/protocols/http/httptools_impl.py", line 409, in run_asgi result = await app( # type: ignore[func-returns-value] File ".local/lib/python3.10/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__ return await self.app(scope, receive, send) File ".local/lib/python3.10/site-packages/fastapi/applications.py", line 1054, in __call__ await super().__call__(scope, receive, send) File ".local/lib/python3.10/site-packages/starlette/applications.py", line 112, in __call__ await self.middleware_stack(scope, receive, send) File ".local/lib/python3.10/site-packages/starlette/middleware/errors.py", line 187, in __call__ raise exc File ".local/lib/python3.10/site-packages/starlette/middleware/errors.py", line 165, in __call__ await self.app(scope, receive, _send) File ".local/lib/python3.10/...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: vllm启动模型后使用openai格式请求传base64值有问题 bug;stale ### Your current environment 使用vllm0.7.3部署的qwen2.5vl-7b模型，使用openai格式请求接口。 方法1是在代码中读取本地文件然后转base64传入大模型中，正常。 方法2是将本地图片转换好的base64直接传入大模型中，报错。 下面是我传入的图片，请问是什么问题？ ![Image](h...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nai格式请求传base64值有问题 bug;stale ### Your current environment 使用vllm0.7.3部署的qwen2.5vl-7b模型，使用openai格式请求接口。 方法1是在代码中读取本地文件然后转base64传入大模型中，正常。 方法2是将本地图片转换好的base64直接传入大模型中，报错。 下面是我传入的图片，请问是什么问题？ ![Image](https://github.com/use...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: , receive, sender) File ".local/lib/python3.10/site-packages/starlette/routing.py", line 715, in __call__ await self.middleware_stack(scope, receive, send) File ".local/lib/python3.10/site-packages/starlette/routing.py"...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: /vllm/entrypoints/chat_utils.py", line 482, in modality: await asyncio.gather(*items) File ".conda/envs/weitiao/lib/python3.10/site-packages/vllm/multimodal/utils.py", line 202, in fetch_image_async return await self.lo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: e ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
