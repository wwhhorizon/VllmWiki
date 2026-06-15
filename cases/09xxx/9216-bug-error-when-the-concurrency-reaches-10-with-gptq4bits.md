# vllm-project/vllm#9216: [Bug]: error when the concurrency reaches 10 with gptq4bits

| 字段 | 值 |
| --- | --- |
| Issue | [#9216](https://github.com/vllm-project/vllm/issues/9216) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: error when the concurrency reaches 10 with gptq4bits

### Issue 正文摘录

### Your current environment vllm 6.0 ### Model Input Dumps _No response_ ### 🐛 Describe the bug ```Traceback (most recent call last): File "/usr/local/lib/python3.10/dist-packages/uvicorn/protocols/http/httptools_impl.py", line 411, in run_asgi result = await app( # type: ignore[func-returns-value] File "/usr/local/lib/python3.10/dist-packages/uvicorn/middleware/proxy_headers.py", line 69, in __call__ return await self.app(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/fastapi/applications.py", line 1054, in __call__ await super().__call__(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/starlette/applications.py", line 113, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/starlette/middleware/errors.py", line 187, in __call__ raise exc File "/usr/local/lib/python3.10/dist-packages/starlette/middleware/errors.py", line 165, in __call__ await self.app(scope, receive, _send) File "/usr/local/lib/python3.10/dist-packages/starlette/middleware/exceptions.py", line 62, in __call__ await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send) File "/usr/local/lib/python3.10/dist...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: error when the concurrency reaches 10 with gptq4bits bug;stale ### Your current environment vllm 6.0 ### Model Input Dumps _No response_ ### 🐛 Describe the bug ```Traceback (most recent call last): File "/usr/loc...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ceive, sender) File "/usr/local/lib/python3.10/dist-packages/starlette/routing.py", line 715, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/starlette/routing...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Bug]: error when the concurrency reaches 10 with gptq4bits bug;stale ### Your current environment vllm 6.0 ### Model Input Dumps _No response_ ### 🐛 Describe the bug ```Traceback (most recent call last): File "/usr/loc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 10 with gptq4bits bug;stale ### Your current environment vllm 6.0 ### Model Input Dumps _No response_ ### 🐛 Describe the bug ```Traceback (most recent call last): File "/usr/local/lib/python3.10/dist-packages/uvicorn/pr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
