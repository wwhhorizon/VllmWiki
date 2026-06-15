# vllm-project/vllm#41579: [CI Failure]:  mi300_1: DeepSeek V2-Lite Prefetch Offload Accuracy (H100-MI300)

| 字段 | 值 |
| --- | --- |
| Issue | [#41579](https://github.com/vllm-project/vllm/issues/41579) |
| 状态 | closed |
| 标签 | rocm;ci-failure |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]:  mi300_1: DeepSeek V2-Lite Prefetch Offload Accuracy (H100-MI300)

### Issue 正文摘录

### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi300_1-deepseek-v2-lite-prefetch-offload-accuracy-h100-mi300 && export VLLM_ALLOW_DEPRECATED_BEAM_SEARCH=1 && cd /vllm-workspace && bash .buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_prefetch_offload.sh 0.25 200 8030` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` + python3 - Traceback (most recent call last): File " ", line 3, in AssertionError: deepseek-ai/DeepSeek-V2-Lite prefetch_offload accuracy 0.015 ``` ### 📝 History of failing test - Current streak start: 2026-05-02 - First failure in 60d window: 2026-04-21 - Last successful nightly: 2026-05-01 - Break frequency (60d, pass↔fail flips): 2 - Latest nightly date: 2026-05-03 - Latest build(s): [amd-ci #8177](https://buildkite.com/vllm/amd-ci/builds/8177) - Latest hardware status: `mi300_1`=fail

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [CI Failure]: mi300_1: DeepSeek V2-Lite Prefetch Offload Accuracy (H100-MI300) rocm;ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi300_1-deepseek-v2-lite-prefetch-offloa...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: [CI Failure]: mi300_1: DeepSeek V2-Lite Prefetch Offload Accuracy (H100-MI300) rocm;ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi300_1-deepseek-v2-lite-prefetch-offloa...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi300_1: DeepSeek V2-Lite Prefetch Offload Accuracy (H100-MI300) rocm;ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi300_1-deepseek-v2-lite-prefetch-offloa
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [CI Failure]: mi300_1: DeepSeek V2-Lite Prefetch Offload Accuracy (H100-MI300) rocm;ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi300_1-deepseek-v2-lite-prefetch-offloa...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [CI Failure]: mi300_1: DeepSeek V2-Lite Prefetch Offload Accuracy (H100-MI300) rocm;ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi300_1-deepseek-v2-lite-prefetch-offloa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
