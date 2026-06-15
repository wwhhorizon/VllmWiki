# vllm-project/vllm#15147: [Bug]: Error running ShieldGemma: 'guideline' is undefined

| 字段 | 值 |
| --- | --- |
| Issue | [#15147](https://github.com/vllm-project/vllm/issues/15147) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: Error running ShieldGemma: 'guideline' is undefined

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am trying to run ShieldGemma 2B in a vllm server deployed in Modal. The server correctly starts and I can make a few requests like checking the available models, but every request to `v1/chat/completions` results in the following error: ``` ERROR: Exception in ASGI application + Exception Group Traceback (most recent call last): | File "/usr/local/lib/python3.12/site-packages/starlette/_utils.py", line 76, in collapse_excgroups | yield | File "/usr/local/lib/python3.12/site-packages/starlette/middleware/base.py", line 174, in __call__ | async with anyio.create_task_group() as task_group: | ^^^^^^^^^^^^^^^^^^^^^^^^^ | File "/usr/local/lib/python3.12/site-packages/anyio/_backends/_asyncio.py", line 772, in __aexit__ | raise BaseExceptionGroup( | ExceptionGroup: unhandled errors in a TaskGroup (1 sub-exception) +-+---------------- 1 ---------------- | Traceback (most recent call last): | File "/usr/local/lib/python3.12/site-packages/uvicorn/protocols/http/httptools_impl.py", line 409, in run_asgi | result = await app( # type: ignore[func-returns-value] | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ | File "/usr/local/lib/python3...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: ^^^^^^^^^^^^^ | File "/usr/local/lib/python3.12/site-packages/anyio/_backends/_asyncio.py", line 772, in __aexit__ | raise BaseExceptionGroup( | ExceptionGroup: unhandled errors in a TaskGroup (1 sub-exception) +-+-----...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: | File "/usr/local/lib/python3.12/site-packages/anyio/_backends/_asyncio.py", line 772, in __aexit__ | raise BaseExceptionGroup( | ExceptionGroup: unhandled errors in a TaskGroup (1 sub-exception) +-+---------------- 1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Error running ShieldGemma: 'guideline' is undefined bug;stale ### Your current environment ### 🐛 Describe the bug I am trying to run ShieldGemma 2B in a vllm server deployed in Modal. The server correctly starts...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: yet ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: Error running ShieldGemma: 'guideline' is undefined bug;stale ### Your current environment ### 🐛 Describe the bug I am trying to run ShieldGemma 2B in a vllm server deployed in Modal. The server correctly starts...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
