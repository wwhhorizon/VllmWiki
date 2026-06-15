# vllm-project/vllm#19786: [Bug]: 使用vllm0.7.3对Qwen2.5VL-7b有时会报错

| 字段 | 值 |
| --- | --- |
| Issue | [#19786](https://github.com/vllm-project/vllm/issues/19786) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: 使用vllm0.7.3对Qwen2.5VL-7b有时会报错

### Issue 正文摘录

### Your current environment vllm0.7.3 ### 🐛 Describe the bug 启动模型：vllm serve /Qwen/Qwen2___5-VL-7B-Instruct/ --trust-remote-code --served-model-name vl_model --gpu-memory-utilization 0.9 --port 8000 请求的时候有时是正常的，有时是错误的，错误的报错内容为await app(scope, receive, sender) File "/.local/lib/python3.10/site-packages/starlette/routing.py", line 715, in __call__ await self.middleware_stack(scope, receive, send) File "/.local/lib/python3.10/site-packages/starlette/routing.py", line 735, in app await route.handle(scope, receive, send) File "/.local/lib/python3.10/site-packages/starlette/routing.py", line 288, in handle await self.app(scope, receive, send) File "/.local/lib/python3.10/site-packages/starlette/routing.py", line 76, in app await wrap_app_handling_exceptions(app, request)(scope, receive, send) File "/.local/lib/python3.10/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app raise exc File "/.local/lib/python3.10/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app await app(scope, receive, sender) File "/.local/lib/python3.10/site-packages/starlette/routing.py", line 73, in app response = await f(request) File "/.local/lib/python3.10/site-packages/f...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: 使用vllm0.7.3对Qwen2.5VL-7b有时会报错 bug;stale ### Your current environment vllm0.7.3 ### 🐛 Describe the bug 启动模型：vllm serve /Qwen/Qwen2___5-VL-7B-Instruct/ --trust-remote-code --served-model-name vl_model --gpu-memory-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: 使用vllm0.7.3对Qwen2.5VL-7b有时会报错 bug;stale ### Your current environment vllm0.7.3 ### 🐛 Describe the bug 启动模型：vllm serve /Qwen/Qwen2___5-VL-7B-Instruct/ --trust-remote-code --served-model-name vl_model --gpu-memory-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: receive, sender) File "/.local/lib/python3.10/site-packages/starlette/routing.py", line 715, in __call__ await self.middleware_stack(scope, receive, send) File "/.local/lib/python3.10/site-packages/starlette/routing.py"...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: /vllm/entrypoints/chat_utils.py", line 482, in modality: await asyncio.gather(*items) File "/.conda/envs/weitiao/lib/python3.10/site-packages/vllm/multimodal/utils.py", line 202, in fetch_image_async return await self.l...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 题呀？ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
