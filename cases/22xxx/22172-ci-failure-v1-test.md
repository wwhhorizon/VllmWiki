# vllm-project/vllm#22172: [CI Failure]: V1 Test

| 字段 | 值 |
| --- | --- |
| Issue | [#22172](https://github.com/vllm-project/vllm/issues/22172) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: V1 Test

### Issue 正文摘录

### Name of failing test v1/entrypoints/openai/test_completion.py::test_batch_completions[server1-facebook/opt-125m] ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test This test fails semi-consistently in CI but passes locally. Maybe related to kernels? ### 📝 History of failing test https://buildkite.com/organizations/vllm/analytics/suites/ci-1/tests/e0037ea8-753f-8000-938f-d772ab07343e?branch=main&period=7days ### CC List. cc @mgoin @Isotr0py

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: V1 Test ci-failure ### Name of failing test v1/entrypoints/openai/test_completion.py::test_batch_completions[server1-facebook/opt-125m] ### Basic information - [x] Flaky test - [ ] Can reproduce locally -
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: r1-facebook/opt-125m] ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test This test fails semi-consistently...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: etion.py::test_batch_completions[server1-facebook/opt-125m] ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: V1 Test ci-failure ### Name of failing test v1/entrypoints/openai/test_completion.py::test_batch_completions[server1-facebook/opt-125m] ### Basic information - [x] Flaky test - [ ] Can reproduce locally -...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
