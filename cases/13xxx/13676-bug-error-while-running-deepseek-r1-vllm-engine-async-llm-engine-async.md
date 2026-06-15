# vllm-project/vllm#13676: [Bug]: Error while running Deepseek-R1: vllm.engine.async_llm_engine.AsyncEngineDeadError: Task finished unexpectedly.

| 字段 | 值 |
| --- | --- |
| Issue | [#13676](https://github.com/vllm-project/vllm/issues/13676) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support |
| 子分类 | race_cond |
| Operator 关键词 | attention;cuda;kernel;operator |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error while running Deepseek-R1: vllm.engine.async_llm_engine.AsyncEngineDeadError: Task finished unexpectedly.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug While running vllm as OpenAI compatible server to server Deepseek-R1 across 2 DGX-H100 with LWS, following error happened: ``` (RayWorkerWrapper pid=570) ERROR 02-21 08:03:30 worker_base.py:581] Error executing method 'start_worker_execution_loop'. This might cause deadlock in distributed execution. (RayWorkerWrapper pid=570) ERROR 02-21 08:03:30 worker_base.py:581] Traceback (most recent call last): (RayWorkerWrapper pid=570) ERROR 02-21 08:03:30 worker_base.py:581] File "/usr/local/lib/python3.12/dist-packages/vllm/worker/worker_base.py", line 573, in execute_method (RayWorkerWrapper pid=570) ERROR 02-21 08:03:30 worker_base.py:581] return run_method(target, method, args, kwargs) (RayWorkerWrapper pid=570) ERROR 02-21 08:03:30 worker_base.py:581] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (RayWorkerWrapper pid=570) ERROR 02-21 08:03:30 worker_base.py:581] File "/usr/local/lib/python3.12/dist-packages/vllm/utils.py", line 2196, in run_method (RayWorkerWrapper pid=570) ERROR 02-21 08:03:30 worker_base.py:581] return func(*args, **kwargs) (RayWorkerWrapper pid=570) ERROR 02-21 08:03:30 worker_base.py:581] ^^^^^^^^^^^^^^^^^^^^^ (RayW...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ning vllm as OpenAI compatible server to server Deepseek-R1 across 2 DGX-H100 with LWS, following error happened: ``` (RayWorkerWrapper pid=570) ERROR 02-21 08:03:30 worker_base.py:581] Error executing method 'start_wor...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: e.async_llm_engine.AsyncEngineDeadError: Task finished unexpectedly. bug;stale ### Your current environment ### 🐛 Describe the bug While running vllm as OpenAI compatible server to server Deepseek-R1 across 2 DGX-H100 w...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ERROR 02-21 08:03:30 worker_base.py:581] RuntimeError: CUDA error: unspecified launch failure (RayWorkerWrapper pid=570) ERROR 02-21 08:03:30 worker_base.py:581] CUDA kernel errors might be asynchronously reported at so...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: e.py:581] File "/usr/local/lib/python3.12/dist-packages/vllm/attention/backends/mla/utils.py", line 457, in forward (RayWorkerWrapper pid=570) ERROR 02-21 08:03:30 worker_base.py:581] self.rotary_emb( (RayWorkerWrapper...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ntend_api;model_support attention;cuda;kernel;operator build_error;crash;mismatch env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
