# vllm-project/vllm#23816: [Bug]: multiprocessing/resource_tracker.py:279: UserWarning: resource_tracker: There appear to be 8 leaked shared_memory objects to clean up at shutdow

| 字段 | 值 |
| --- | --- |
| Issue | [#23816](https://github.com/vllm-project/vllm/issues/23816) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: multiprocessing/resource_tracker.py:279: UserWarning: resource_tracker: There appear to be 8 leaked shared_memory objects to clean up at shutdow

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug 2025-08-28 16:23:31 (EngineCore_0 pid=270) Process EngineCore_0: 2025-08-28 16:23:31 (EngineCore_0 pid=270) ERROR 08-28 01:23:31 [core.py:700] EngineCore failed to start. 2025-08-28 16:23:31 (EngineCore_0 pid=270) ERROR 08-28 01:23:31 [core.py:700] Traceback (most recent call last): 2025-08-28 16:23:31 (EngineCore_0 pid=270) ERROR 08-28 01:23:31 [core.py:700] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 691, in run_engine_core 2025-08-28 16:23:31 (EngineCore_0 pid=270) ERROR 08-28 01:23:31 [core.py:700] engine_core = EngineCoreProc(*args, **kwargs) 2025-08-28 16:23:31 (EngineCore_0 pid=270) ERROR 08-28 01:23:31 [core.py:700] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 2025-08-28 16:23:31 (EngineCore_0 pid=270) ERROR 08-28 01:23:31 [core.py:700] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 492, in __init__ 2025-08-28 16:23:31 (EngineCore_0 pid=270) ERROR 08-28 01:23:31 [core.py:700] super().__init__(vllm_config, executor_class, log_stats, 2025-08-28 16:23:31 (EngineCore_0 pid=270) ERROR 08-28 01:23:31 [core.py:700] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.p...

## 现有链接修复摘要

#23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: line 109, in run 2025-08-28 16:23:32 (APIServer pid=7) return __asyncio.run( 2025-08-28 16:23:32 (APIServer pid=7) ^^^^^^^^^^^^^^ 2025-08-28 16:23:32 (APIServer pid=7) File "/usr/lib/python3.12/asyncio/runners.py", line...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: EOF ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency #23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag Your current enviro...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: _0 pid=270) ERROR 08-28 01:23:31 [core.py:700] super().__init__(vllm_config, executor_class, log_stats, 2025-08-28 16:23:31 (EngineCore_0 pid=270) ERROR 08-28 01:23:31 [core.py:700] File "/usr/local/lib/python3.12/dist-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: e appear to be 8 leaked shared_memory objects to clean up at shutdow bug;stale ### Your current environment ### 🐛 Describe the bug 2025-08-28 16:23:31 (EngineCore_0 pid=270) Process EngineCore_0: 2025-08-28 16:23:31 (En...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#23942](https://github.com/vllm-project/vllm/pull/23942) | mentioned | 0.6 | [CI]  Add `aiter` to matching list of issue auto labeller for `rocm` tag | el: NO (0 matches) #23820: Should have ROCm label: NO (0 matches) #23816: Should have ROCm label: NO (0 matches) #23814: Should have ROCm label: NO (0 matches) #23813: Should hav |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
