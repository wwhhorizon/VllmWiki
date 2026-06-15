# vllm-project/vllm#1476: AssertionError   assert output == other_output

| 字段 | 值 |
| --- | --- |
| Issue | [#1476](https://github.com/vllm-project/vllm/issues/1476) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;model_support |
| 子分类 | debug |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> AssertionError   assert output == other_output

### Issue 正文摘录

model: Qwen-7B-Chat cuda: 12.2 vllm: 0.2.1 GPU: 2 T4 async_llm_engine.py:134] Aborted request 2f0244c5636145e8bf9a59e7b4063657. 2023-10-26 18:11:35 | ERROR | stderr | ERROR: Exception in ASGI application 2023-10-26 18:11:35 | ERROR | stderr | Traceback (most recent call last): 2023-10-26 18:11:35 | ERROR | stderr | File "/opt/jiuyindanao/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 28, in _raise_exception_on_finish 2023-10-26 18:11:35 | ERROR | stderr | task.result() 2023-10-26 18:11:35 | ERROR | stderr | File "/opt/jiuyindanao/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 351, in run_engine_loop 2023-10-26 18:11:35 | ERROR | stderr | has_requests_in_progress = await self.engine_step() 2023-10-26 18:11:35 | ERROR | stderr | File "/opt/jiuyindanao/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 330, in engine_step 2023-10-26 18:11:35 | ERROR | stderr | request_outputs = await self.engine.step_async() 2023-10-26 18:11:35 | ERROR | stderr | File "/opt/jiuyindanao/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 191, in step_async 2023-10-26 18:11:35 | ERROR | stderr | output = await self._run_workers_...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: stderr | File "/opt/jiuyindanao/lib/python3.10/site-packages/starlette/routing.py", line 718, in __call__ 2023-10-26 18:11:35 | ERROR | stderr | await route.handle(scope, receive, send) 2023-10-26 18:11:35 | ERROR | std...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: AssertionError assert output == other_output model: Qwen-7B-Chat cuda: 12.2 vllm: 0.2.1 GPU: 2 T4 async_llm_engine.py:134] Aborted request 2f0244c5636145e8bf9a59e7b4063657. 2023-10-26 18:11:35 | ERROR | stderr | ERROR:...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: File "/opt/jiuyindanao/lib/python3.10/site-packages/anyio/_backends/_asyncio.py", line 597, in __aexit__ 2023-10-26 18:11:35 | ERROR | stderr | raise exceptions[0] 2023-10-26 18:11:35 | ERROR | stderr | File "/opt/jiuyi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: AssertionError assert output == other_output model: Qwen-7B-Chat cuda: 12.2 vllm: 0.2.1 GPU: 2 T4 async_llm_engine.py:134] Aborted request 2f0244c5636145e8bf9a59e7b4063657. 2023-10-26 18:11:35 | ERROR | stderr | ERROR:...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: stderr | File "/opt/jiuyindanao/lib/python3.10/site-packages/starlette/routing.py", line 718, in __call__ 2023-10-26 18:11:35 | ERROR | stderr | await route.handle(scope, receive, send) 2023-10-26 18:11:35 | ERROR | std...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
