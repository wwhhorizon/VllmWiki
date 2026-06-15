# vllm-project/vllm#27844: [CI Failure]: AMD structured outputs tests OOM with @pytest.mark.skip_global_cleanup

| 字段 | 值 |
| --- | --- |
| Issue | [#27844](https://github.com/vllm-project/vllm/issues/27844) |
| 状态 | closed |
| 标签 | rocm;ci-failure |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting |
| 子分类 | memory |
| Operator 关键词 | cuda;operator |
| 症状 | build_error;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: AMD structured outputs tests OOM with @pytest.mark.skip_global_cleanup

### Issue 正文摘录

### Name of failing test tests/v1/entrypoints/llm/test_struct_output_generate.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Structured outputs tests were added in https://github.com/vllm-project/vllm/pull/12388 with `@pytest.mark.skip_global_cleanup` to speed up testing time, however this is causing tests OOMs on AMD CI specifically. ([example](https://buildkite.com/vllm/amd-ci/builds/736#019a3390-9acd-43ae-9496-9deeed1db4d8)) ``` 2025-10-30 05:48:54 UTC | (EngineCore_DP0 pid=3997) ERROR 10-30 05:48:54 [core.py:779] self.driver_worker.init_device() -- | -- | 2025-10-30 05:48:54 UTC | (EngineCore_DP0 pid=3997) ERROR 10-30 05:48:54 [core.py:779] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/worker/worker_base.py", line 308, in init_device | 2025-10-30 05:48:54 UTC | (EngineCore_DP0 pid=3997) ERROR 10-30 05:48:54 [core.py:779] self.worker.init_device() # type: ignore | 2025-10-30 05:48:54 UTC | (EngineCore_DP0 pid=3997) ERROR 10-30 05:48:54 [core.py:779] ^^^^^^^^^^^^^^^^^^^^^^^^^ | 2025-10-30 05:48:54 UTC | (EngineCore_DP0 pid=3997) ERROR 10-30 05:48:54 [cor...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [CI Failure]: AMD structured outputs tests OOM with @pytest.mark.skip_global_cleanup rocm;ci-failure ### Name of failing test tests/v1/entrypoints/llm/test_struct_output_generate.py ### Basic information - [ ] Flaky te
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: : AMD structured outputs tests OOM with @pytest.mark.skip_global_cleanup rocm;ci-failure ### Name of failing test tests/v1/entrypoints/llm/test_struct_output_generate.py ### Basic information - [ ] Flaky test - [x] Can...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [CI Failure]: AMD structured outputs tests OOM with @pytest.mark.skip_global_cleanup rocm;ci-failure ### Name of failing test tests/v1/entrypoints/llm/test_struct_output_generate.py ### Basic information - [ ] Flaky tes...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ct_output_generate.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Structured outputs tests were adde...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: st tests/v1/entrypoints/llm/test_struct_output_generate.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
