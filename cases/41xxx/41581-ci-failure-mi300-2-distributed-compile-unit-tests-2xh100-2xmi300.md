# vllm-project/vllm#41581: [CI Failure]:  mi300_2: Distributed Compile Unit Tests (2xH100-2xMI300)

| 字段 | 值 |
| --- | --- |
| Issue | [#41581](https://github.com/vllm-project/vllm/issues/41581) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]:  mi300_2: Distributed Compile Unit Tests (2xH100-2xMI300)

### Issue 正文摘录

### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi300_2-distributed-compile-unit-tests-2xh100-2xmi300 && export VLLM_ALLOW_DEPRECATED_BEAM_SEARCH=1 && cd /vllm-workspace/ && export VLLM_TEST_CLEAN_GPU_MEMORY=1 && VLLM_TEST_CLEAN_GPU_MEMORY=1 pytest -v -s tests/compile/passes/distributed/test_async_tp.py && pytest -v -s tests/compile/passes/distributed/test_sequence_parallelism.py && pytest -v -s tests/compile/passes/distributed/test_tp2_ar_rms.py::test_tp2_ar_rms_fusions` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test There are shards that collect 0 items. ### 📝 History of failing test - Current streak start: 2026-05-02 - First failure in 60d window: 2026-05-02 - Last successful nightly: 2026-05-01 - Break frequency (60d, pass↔fail flips): 1 - Latest nightly date: 2026-05-03 - Latest build(s): [amd-ci #8177](https://buildkite.com/vllm/amd-ci/builds/8177) - Latest hardware status: `mi300_2`=fail

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [CI Failure]: mi300_2: Distributed Compile Unit Tests (2xH100-2xMI300) ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi300_2-distributed-compile-unit-tests-2xh100-2xmi300...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: mi300_2: Distributed Compile Unit Tests (2xH100-2xMI300) ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi300_2-distributed-compile-unit-tests-2xh100-2xmi300
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: t_tp2_ar_rms_fusions` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test There are shards that collect 0 it...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: es/distributed/test_tp2_ar_rms.py::test_tp2_ar_rms_fusions` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: mi300_2: Distributed Compile Unit Tests (2xH100-2xMI300) ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi300_2-distributed-compile-unit-tests-2xh100-2xmi300...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
