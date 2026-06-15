# vllm-project/vllm#27624: [CI Failure]: Model Executor Test failing on AMD due to fastsafetensors not supported

| 字段 | 值 |
| --- | --- |
| Issue | [#27624](https://github.com/vllm-project/vllm/issues/27624) |
| 状态 | closed |
| 标签 | rocm;ci-failure |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: Model Executor Test failing on AMD due to fastsafetensors not supported

### Issue 正文摘录

### Name of failing test tests/model_executor/model_loader/fastsafetensors_loader/test_fastsafetensors_loader.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Model Executor Test running on AMD CI:([example](https://buildkite.com/vllm/ci/builds/36286#019a1ead-5049-40ac-b0df-ccfaab9f34af)) We need to skip [fastsafetensors](https://github.com/foundation-model-stack/fastsafetensors) tests(introduced in https://github.com/vllm-project/vllm/pull/10647), since it's only supporting CUDA platform - this is skipped in https://github.com/vllm-project/vllm/pull/27612 ### 📝 History of failing test https://buildkite.com/vllm/ci/builds/36286#019a1ead-5049-40ac-b0df-ccfaab9f34af ### CC List. @manish-sethi @njhill

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Model Executor Test failing on AMD due to fastsafetensors not supported rocm;ci-failure ### Name of failing test tests/model_executor/model_loader/fastsafetensors_loader/test_fastsafetensors_loader.py ###
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Model Executor Test failing on AMD due to fastsafetensors not supported rocm;ci-failure ### Name of failing test tests/model_executor/model_loader/fastsafetensors_loader/test_fastsafetensors_loader.py ### Basic informat...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [CI Failure]: Model Executor Test failing on AMD due to fastsafetensors not supported rocm;ci-failure ### Name of failing test tests/model_executor/model_loader/fastsafetensors_loader/test_fastsafetensors_loader.py ###...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: safetensors_loader.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Model Executor Test running on AMD...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: Model Executor Test failing on AMD due to fastsafetensors not supported rocm;ci-failure ### Name of failing test tests/model_executor/model_loader/fastsafetensors_loader/test_fastsafetensors_loader.py ###...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
