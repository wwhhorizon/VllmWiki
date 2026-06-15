# vllm-project/vllm#10764: [Bug]: idefics3 doesn't stream

| 字段 | 值 |
| --- | --- |
| Issue | [#10764](https://github.com/vllm-project/vllm/issues/10764) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: idefics3 doesn't stream

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Trying to stream with Idefics3-based models (both `Idefics3-8B-Llama3` and `SmolVLM`), I immediately get this traceback: ``` INFO 11-28 22:33:35 preprocess.py:215] Your model uses the legacy input pipeline instead of the new multi-modal processor. Please note that the legacy pipeline will be removed in a future release. For more details, see: https://github.com/vllm-project/vllm/issues/10114 INFO 11-28 22:33:35 engine.py:285] Aborted request chatcmpl-9aaf2452b75e4c54bc0b21685e6149d5. ERROR: Exception in ASGI application + Exception Group Traceback (most recent call last): | File "/home/jeff/.virtualenvs/vllm312/lib/python3.12/site-packages/starlette/middleware/base.py", line 188, in __call__ | await response(scope, wrapped_receive, send) | File "/home/jeff/.virtualenvs/vllm312/lib/python3.12/site-packages/starlette/middleware/base.py", line 222, in __call__ | async for chunk in self.body_iterator: | File "/home/jeff/.virtualenvs/vllm312/lib/python3.12/site-packages/starlette/middleware/base.py", line 179, in body_stream | raise app_exc | File "/home/jeff/.virtualenvs/vllm312/lib/python3.12/site...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: "/home/jeff/.virtualenvs/vllm312/lib/python3.12/site-packages/starlette/routing.py", line 715, in __call__ | await self.middleware_stack(scope, receive, send) | File "/home/jeff/.virtualenvs/vllm312/lib/python3.12/site-...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: f/.virtualenvs/vllm312/lib/python3.12/site-packages/anyio/_backends/_asyncio.py", line 763, in __aexit__ | raise BaseExceptionGroup( | ExceptionGroup: unhandled errors in a TaskGroup (1 sub-exception) +-+---------------...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ing to stream with Idefics3-based models (both `Idefics3-8B-Llama3` and `SmolVLM`), I immediately get this traceback: ``` INFO 11-28 22:33:35 preprocess.py:215] Your model uses the legacy input pipeline instead of the n...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: idefics3 doesn't stream bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Trying to stream with Idefics3-based models (both `Idefics3-8B-Llama3` and `SmolVLM`), I immedia...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: "/home/jeff/.virtualenvs/vllm312/lib/python3.12/site-packages/starlette/routing.py", line 715, in __call__ | await self.middleware_stack(scope, receive, send) | File "/home/jeff/.virtualenvs/vllm312/lib/python3.12/site-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
