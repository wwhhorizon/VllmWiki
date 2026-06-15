# vllm-project/vllm#9304: [Bug]: Hermes 2 Pro Tool parser could not locate tool call start/end tokens in the tokenizer!

| 字段 | 值 |
| --- | --- |
| Issue | [#9304](https://github.com/vllm-project/vllm/issues/9304) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Hermes 2 Pro Tool parser could not locate tool call start/end tokens in the tokenizer!

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug glm-4-9b-chat, MiniCPM3-4B, llama3.1 tool-call-parser set hermes occur this error! ``` ERROR: Exception in ASGI application Traceback (most recent call last): File "/usr/local/lib/python3.10/dist-packages/starlette/responses.py", line 257, in __call__ await wrap(partial(self.listen_for_disconnect, receive)) File "/usr/local/lib/python3.10/dist-packages/starlette/responses.py", line 253, in wrap await func() File "/usr/local/lib/python3.10/dist-packages/starlette/responses.py", line 230, in listen_for_disconnect message = await receive() File "/usr/local/lib/python3.10/dist-packages/uvicorn/protocols/http/httptools_impl.py", line 555, in receive await self.message_event.wait() File "/usr/lib/python3.10/asyncio/locks.py", line 214, in wait await fut asyncio.exceptions.CancelledError: Cancelled by cancel scope 7fd9d0252d70 During handling of the above exception, another exception occurred: + Exception Group Traceback (most recent call last): | File "/usr/local/lib/python3.10/dist-packages/uvicorn/protocols/http/httptools_impl.py", line 401, in run_asgi | result = await app( # type: ignore[func-ret...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: e, sender) | File "/usr/local/lib/python3.10/dist-packages/starlette/routing.py", line 715, in __call__ | await self.middleware_stack(scope, receive, send) | File "/usr/local/lib/python3.10/dist-packages/starlette/routi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: tokens in the tokenizer! bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug glm-4-9b-chat, MiniCPM3-4B, llama3.1 tool-call-parser set hermes occur this error! ``` ERROR: Ex...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: parser could not locate tool call start/end tokens in the tokenizer! bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug glm-4-9b-chat, MiniCPM3-4B, llama3.1 tool-call-parse...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: eive await self.message_event.wait() File "/usr/lib/python3.10/asyncio/locks.py", line 214, in wait await fut asyncio.exceptions.CancelledError: Cancelled by cancel scope 7fd9d0252d70 During handling of the above except...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
