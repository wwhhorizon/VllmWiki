# vllm-project/vllm#11629: [Bug]: VLLM - Getting a 500 Internal Error when calling /v1/chat/completions with an image_url

| 字段 | 值 |
| --- | --- |
| Issue | [#11629](https://github.com/vllm-project/vllm/issues/11629) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: VLLM - Getting a 500 Internal Error when calling /v1/chat/completions with an image_url

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I'm doing a POST /v1/chat/completions with the following body ``` { "model": "meta-llama/Llama-3.3-70B-Instruct", "messages": [ { "role": "user", "content": [ { "type": "text", "text": "What is in this image?" }, { "type": "image_url", "image_url": {"url": "data:image/jpeg;base64, >>>"} } ] } ] } ``` I'm getting a "**500 Internal Server Error**" I've got the same result with several model supporting Vision. Here are the logs of the container: ``` INFO: 10.42.3.225:0 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error ERROR: Exception in ASGI application + Exception Group Traceback (most recent call last): | File "/usr/local/lib/python3.12/dist-packages/starlette/_utils.py", line 76, in collapse_excgroups | yield | File "/usr/local/lib/python3.12/dist-packages/starlette/middleware/base.py", line 186, in __call__ | async with anyio.create_task_group() as task_group: | ^^^^^^^^^^^^^^^^^^^^^^^^^ | File "/usr/local/lib/python3.12/dist-packages/anyio/_backends/_asyncio.py", line 763, in __aexit__ | raise BaseExceptionGroup( | ExceptionGroup: unhandled errors in a TaskGroup (1 sub-ex...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ^^^^^^^^^^^^^ | File "/usr/local/lib/python3.12/dist-packages/anyio/_backends/_asyncio.py", line 763, in __aexit__ | raise BaseExceptionGroup( | ExceptionGroup: unhandled errors in a TaskGroup (1 sub-exception) +-+-----...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: t/completions with an image_url bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I'm doing a POST /v1/chat/completions with the following body ``` { "model": "meta-llama/L...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: | File "/usr/local/lib/python3.12/dist-packages/anyio/_backends/_asyncio.py", line 763, in __aexit__ | raise BaseExceptionGroup( | ExceptionGroup: unhandled errors in a TaskGroup (1 sub-exception) +-+---------------- 1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: sender) | File "/usr/local/lib/python3.12/dist-packages/starlette/routing.py", line 715, in __call__ | await self.middleware_stack(scope, receive, send) | File "/usr/local/lib/python3.12/dist-packages/starlette/routing....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
