# vllm-project/vllm#13081: TypeError: '>' not supported between instances of 'int' and 'NoneType'

| 字段 | 值 |
| --- | --- |
| Issue | [#13081](https://github.com/vllm-project/vllm/issues/13081) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> TypeError: '>' not supported between instances of 'int' and 'NoneType'

### Issue 正文摘录

### Your current environment DEBUG:root:Received request JSON: {'query': '给我讲一篇故事', 'chat_aim': True, 'userId': 'admin', 'history': [], 'gradio': True, 'system': 'You are a helpful assistant.'} [] INFO: 192.168.100.43:55564 - "POST /stream_chat HTTP/1.1" 200 OK ERROR: Exception in ASGI application Traceback (most recent call last): File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/starlette/responses.py", line 265, in __call__ await wrap(partial(self.listen_for_disconnect, receive)) File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/starlette/responses.py", line 261, in wrap await func() File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/starlette/responses.py", line 238, in listen_for_disconnect message = await receive() File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/uvicorn/protocols/http/httptools_impl.py", line 568, in receive await self.message_event.wait() File "/root/miniconda3/envs/vllm/lib/python3.10/asyncio/locks.py", line 214, in wait await fut asyncio.exceptions.CancelledError: Cancelled by cancel scope 7f48d7a76470 During handling of the above exception, another exception occurred: + Exception Group Traceback (most rece...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/starlette/routing.py", line 756, in __call__ | await self.middleware_stack(scope, receive, send) | File "/root/miniconda3/envs/vllm/lib/python3.10/site-packa...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ssage_event.wait() File "/root/miniconda3/envs/vllm/lib/python3.10/asyncio/locks.py", line 214, in wait await fut asyncio.exceptions.CancelledError: Cancelled by cancel scope 7f48d7a76470 During handling of the above ex...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ing ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: response | async for chunk in self.body_iterator: | File "/qwen/code/vllm/test1.py", line 136, in streaming_resp | async for item in generater: | File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/vllm/engine...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/starlette/routing.py", line 756, in __call__ | await self.middleware_stack(scope, receive, send) | File "/root/miniconda3/envs/vllm/lib/python3.10/site-packa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
