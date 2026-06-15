# vllm-project/vllm#12401: [Bug]: AsyncEngineDeadError during inference of two vllm engine on single gpu

| 字段 | 值 |
| --- | --- |
| Issue | [#12401](https://github.com/vllm-project/vllm/issues/12401) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AsyncEngineDeadError during inference of two vllm engine on single gpu

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Getting this error while running two vllm instances (Async Engine) on the same GPU instance. ``` ERROR 01-24 10:22:07 async_llm_engine.py:68] Engine background task failed ERROR 01-24 10:22:07 async_llm_engine.py:68] Traceback (most recent call last): ERROR 01-24 10:22:07 async_llm_engine.py:68] File "/usr/local/lib/python3.9/dist-packages/vllm/engine/async_llm_engine.py", line 58, in _log_task_completion ERROR 01-24 10:22:07 async_llm_engine.py:68] return_value = task.result() ERROR 01-24 10:22:07 async_llm_engine.py:68] File "/usr/local/lib/python3.9/dist-packages/vllm/engine/async_llm_engine.py", line 888, in run_engine_loop ERROR 01-24 10:22:07 async_llm_engine.py:68] result = task.result() ERROR 01-24 10:22:07 async_llm_engine.py:68] File "/usr/local/lib/python3.9/dist-packages/vllm/engine/async_llm_engine.py", line 811, in engine_step ERROR 01-24 10:22:07 async_llm_engine.py:68] request_outputs = await self.engine.step_async(virtual_engine) ERROR 01-24 10:22:07 async_llm_engine.py:68] File "/usr/local/lib/python3.9/dist-packages/vllm/engine/async_llm_engine.py", line 353, in step_async ER...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: -24 10:22:07 - fm - VerifyLegal - development - ERROR - 1:MainThread:asyncio:run:44 - Exception in callback functools.partial( , error_callback= >) handle: , error_callback= >)> - {"_ray_timestamp_ns": 17377141271352013...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: yncEngineDeadError during inference of two vllm engine on single gpu bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Getting this error while running two vllm instances...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: vllm engine on single gpu bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Getting this error while running two vllm instances (Async Engine) on the same GPU instance. ``...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
