# vllm-project/vllm#41989: [CI Failure]:  mi300_1: Quantized Models Test

| 字段 | 值 |
| --- | --- |
| Issue | [#41989](https://github.com/vllm-project/vllm/issues/41989) |
| 状态 | open |
| 标签 | ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;quantization |
| 子分类 |  |
| Operator 关键词 | quantization |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]:  mi300_1: Quantized Models Test

### Issue 正文摘录

### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi300_1-quantized-models-test && export VLLM_ALLOW_DEPRECATED_BEAM_SEARCH=1 && cd /vllm-workspace/tests && pytest -v -s models/quantization` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Exited with status 139 (soft failed) Link: https://buildkite.com/vllm/amd-ci/builds/8279/canvas?sid=019e0105-dcaa-41ef-b8a3-c4987192a08a&tab=output ### 📝 History of failing test - Current streak start: 2026-04-23 - First failure in 60d window: 2026-04-23 - Last successful nightly: 2026-04-22 - Break frequency (60d, pass↔fail flips): 1 - Latest nightly date: 2026-05-07 - Latest build(s): [amd-ci #8279](https://buildkite.com/vllm/amd-ci/builds/8279) - Latest hardware status: `mi300_1`=fail

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [CI Failure]: mi300_1: Quantized Models Test ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi300_1-quantized-models-test && export VLLM_ALLOW_DEPRECATED_BEAM_SEARCH=1 &&...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: mi300_1: Quantized Models Test ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi300_1-quantized-models-test && export VLLM_ALLOW_DEPRECATED_BEAM_SEARCH=1 &&
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [CI Failure]: mi300_1: Quantized Models Test ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi300_1-quantized-models-test && export VLLM_ALLOW_DEPRECATED_BEAM_SEARCH=1 &&...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: models/quantization` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Exited with status 139 (soft failed...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [CI Failure]: mi300_1: Quantized Models Test ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi300_1-quantized-models-test && export VLLM_ALLOW_DEPRECATED_BEAM_SEARCH=1 &&...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
