# vllm-project/vllm#15048: [Bug]: AttributeError: 'EmbeddingChatRequest' object has no attribute 'mm_processor_kwargs'

| 字段 | 值 |
| --- | --- |
| Issue | [#15048](https://github.com/vllm-project/vllm/issues/15048) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: AttributeError: 'EmbeddingChatRequest' object has no attribute 'mm_processor_kwargs'

### Issue 正文摘录

### Your current environment when I deploy dse-qwen2-2b-mrl-v1 embedding model, assert [Bug]: AttributeError: 'EmbeddingChatRequest' object has no attribute 'mm_processor_kwargs' File "/home/tiger/.local/lib/python3.11/site-packages/fastapi/applications.py", line 1054, in __call__ await super().__call__(scope, receive, send) File "/home/tiger/.local/lib/python3.11/site-packages/starlette/applications.py", line 112, in __call__ await self.middleware_stack(scope, receive, send) File "/home/tiger/.local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 187, in __call__ raise exc File "/home/tiger/.local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 165, in __call__ await self.app(scope, receive, _send) File "/home/tiger/.local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 85, in __call__ await self.app(scope, receive, send) File "/home/tiger/.local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 62, in __call__ await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send) File "/home/tiger/.local/lib/python3.11/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app raise exc Fi...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: mm_processor_kwargs' bug ### Your current environment when I deploy dse-qwen2-2b-mrl-v1 embedding model, assert [Bug]: AttributeError: 'EmbeddingChatRequest' object has no attribute 'mm_processor_kwargs' File "/home/tig...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: AttributeError: 'EmbeddingChatRequest' object has no attribute 'mm_processor_kwargs' bug ### Your current environment when I deploy dse-qwen2-2b-mrl-v1 embedding model, assert [Bug]: AttributeError: 'EmbeddingCha...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sender) File "/home/tiger/.local/lib/python3.11/site-packages/starlette/routing.py", line 714, in __call__ await self.middleware_stack(scope, receive, send) File "/home/tiger/.local/lib/python3.11/site-packages/starlett...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ned ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: sender) File "/home/tiger/.local/lib/python3.11/site-packages/starlette/routing.py", line 714, in __call__ await self.middleware_stack(scope, receive, send) File "/home/tiger/.local/lib/python3.11/site-packages/starlett...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
