# vllm-project/vllm#40644: [CI Failure]: mi250_1: Basic Models Tests (Other)

| 字段 | 值 |
| --- | --- |
| Issue | [#40644](https://github.com/vllm-project/vllm/issues/40644) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: mi250_1: Basic Models Tests (Other)

### Issue 正文摘录

### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi250_1-basic-models-tests-other && export VLLM_ALLOW_DEPRECATED_BEAM_SEARCH=1 && cd /vllm-workspace/tests && pytest -v -s models/test_terratorch.py models/test_transformers.py models/test_registry.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test - Latest nightly date: 2026-04-22 - Latest build(s): [amd-ci #7880](https://buildkite.com/vllm/amd-ci/builds/7880) - Latest hardware status: `mi250_1`=fail ### 📝 History of failing test - Current streak start: 2026-04-16 - First failure in 60d window: 2026-04-16 - Last successful nightly: 2026-04-15

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: asic Models Tests (Other) ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi250_1-basic-models-tests-other && export VLLM_ALLOW_DEPRECATED_BEAM_SEARCH=1 && cd /vllm-workspa...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi250_1: Basic Models Tests (Other) ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi250_1-basic-models-tests-other && export VLLM_ALLOW_DEPRECATED_BEAM_SEARC
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [CI Failure]: mi250_1: Basic Models Tests (Other) ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi250_1-basic-models-tests-other && export VLLM_ALLOW_DEPRECATED_BEAM_SEAR...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: els/test_registry.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test - Latest nightly date: 2026-04-22...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: mi250_1: Basic Models Tests (Other) ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi250_1-basic-models-tests-other && export VLLM_ALLOW_DEPRECATED_BEAM_SEAR...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
