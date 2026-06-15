# vllm-project/vllm#7019: [Bug]: TypeError: LLMEngine._add_processed_request() missing 1 required positional argument: 'prompt_adapter_request'

| 字段 | 值 |
| --- | --- |
| Issue | [#7019](https://github.com/vllm-project/vllm/issues/7019) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: TypeError: LLMEngine._add_processed_request() missing 1 required positional argument: 'prompt_adapter_request'

### Issue 正文摘录

### Your current environment docker: v0.5.2 model: DeepSeek-Coder-V2-Lite-Instruct device: 4090 driver: DeepSeek-Coder-V2-Lite-Instruct ### 🐛 Describe the bug 2024-08-01T14:54:38.899270162+08:00 ERROR 08-01 14:54:38 async_llm_engine.py:55] Engine background task failed 2024-08-01T14:54:38.899292484+08:00 ERROR 08-01 14:54:38 async_llm_engine.py:55] Traceback (most recent call last): 2024-08-01T14:54:38.899295858+08:00 ERROR 08-01 14:54:38 async_llm_engine.py:55] File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 45, in _log_task_completion 2024-08-01T14:54:38.899298559+08:00 ERROR 08-01 14:54:38 async_llm_engine.py:55] return_value = task.result() 2024-08-01T14:54:38.899300936+08:00 ERROR 08-01 14:54:38 async_llm_engine.py:55] File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 614, in run_engine_loop 2024-08-01T14:54:38.899303228+08:00 ERROR 08-01 14:54:38 async_llm_engine.py:55] result = task.result() 2024-08-01T14:54:38.899305613+08:00 ERROR 08-01 14:54:38 async_llm_engine.py:55] File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 542, in engine_step 2024-08-01T14:54:38.899308296...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 01738485+08:00 File "/usr/local/lib/python3.10/dist-packages/starlette/routing.py", line 756, in __call__ 2024-08-01T14:54:38.901740598+08:00 await self.middleware_stack(scope, receive, send) 2024-08-01T14:54:38.9017428...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: nal argument: 'prompt_adapter_request' bug ### Your current environment docker: v0.5.2 model: DeepSeek-Coder-V2-Lite-Instruct device: 4090 driver: DeepSeek-Coder-V2-Lite-Instruct ### 🐛 Describe the bug 2024-08-01T14:54:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: prompt_adapter_request' bug ### Your current environment docker: v0.5.2 model: DeepSeek-Coder-V2-Lite-Instruct device: 4090 driver: DeepSeek-Coder-V2-Lite-Instruct ### 🐛 Describe the bug 2024-08-01T14:54:38.899270162+08...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: 01738485+08:00 File "/usr/local/lib/python3.10/dist-packages/starlette/routing.py", line 756, in __call__ 2024-08-01T14:54:38.901740598+08:00 await self.middleware_stack(scope, receive, send) 2024-08-01T14:54:38.9017428...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: TypeError: LLMEngine._add_processed_request() missing 1 required positional argument: 'prompt_adapter_request' bug ### Your current environment docker: v0.5.2 model: DeepSeek-Coder-V2-Lite-Instruct device: 4090 d...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
