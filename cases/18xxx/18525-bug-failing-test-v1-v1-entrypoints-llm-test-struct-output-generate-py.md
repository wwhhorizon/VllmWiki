# vllm-project/vllm#18525: [Bug][Failing Test]: V1 - v1/entrypoints/llm/test_struct_output_generate.py

| 字段 | 值 |
| --- | --- |
| Issue | [#18525](https://github.com/vllm-project/vllm/issues/18525) |
| 状态 | closed |
| 标签 | bug;ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api |
| 子分类 |  |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][Failing Test]: V1 - v1/entrypoints/llm/test_struct_output_generate.py

### Issue 正文摘录

### Your current environment N/A ### 🐛 Describe the bug `v1/entrypoints/llm/test_struct_output_generate.py::test_structured_output_with_reasoning_matrices` fails on main e.g. https://buildkite.com/vllm/ci/builds/20477/steps?jid=0196f3e2-128a-409e-bafa-5d676afc9557 Stack: ``` [2025-05-21T18:59:44Z] ERROR 05-21 11:59:44 [core.py:493] EngineCore failed to start. [2025-05-21T18:59:44Z] ERROR 05-21 11:59:44 [core.py:493] Traceback (most recent call last): [2025-05-21T18:59:44Z] ERROR 05-21 11:59:44 [core.py:493] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 484, in run_engine_core [2025-05-21T18:59:44Z] ERROR 05-21 11:59:44 [core.py:493] engine_core = EngineCoreProc(*args, **kwargs) [2025-05-21T18:59:44Z] ERROR 05-21 11:59:44 [core.py:493] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [2025-05-21T18:59:44Z] ERROR 05-21 11:59:44 [core.py:493] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 383, in __init__ [2025-05-21T18:59:44Z] ERROR 05-21 11:59:44 [core.py:493] super().__init__(vllm_config, executor_class, log_stats, [2025-05-21T18:59:44Z] ERROR 05-21 11:59:44 [core.py:493] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py...

## 现有链接修复摘要

#18543 [Bugfix] Use random hidden states in dummy sampler run

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ailing Test]: V1 - v1/entrypoints/llm/test_struct_output_generate.py bug;ci-failure ### Your current environment N/A ### 🐛 Describe the bug `v1/entrypoints/llm/test_struct_output_generate.py::test_structured_output_with...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [2025-05-21T18:59:44Z] ERROR 05-21 11:59:44 [core.py:493] RuntimeError: CUDA error: an illegal memory access was encountered [2025-05-21T18:59:44Z] ERROR 05-21 11:59:44 [core.py:493] CUDA kernel errors might be asynchro...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: 5-21T18:59:44Z] ERROR 05-21 11:59:44 [core.py:493] dummy_spec_decode_metadata = SpecDecodeMetadata.make_dummy( [2025-05-21T18:59:44Z] ERROR 05-21 11:59:44 [core.py:493] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [2025-05-21T18:59:4...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: T18:59:44Z] ERROR 05-21 11:59:44 [core.py:493] super().__init__(vllm_config, executor_class, log_stats, [2025-05-21T18:59:44Z] ERROR 05-21 11:59:44 [core.py:493] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/eng...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [2025-05-21T18:59:44Z] ERROR 05-21 11:59:44 [core.py:493] dummy_spec_decode_metadata = SpecDecodeMetadata.make_dummy( [2025-05-21T18:59:44Z] ERROR 05-21 11:59:44 [core.py:493] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [2025-05-21T...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#18543](https://github.com/vllm-project/vllm/pull/18543) | closes_keyword | 0.95 | [Bugfix] Use random hidden states in dummy sampler run | FIX #18525 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
