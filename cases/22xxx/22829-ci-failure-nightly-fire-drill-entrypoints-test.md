# vllm-project/vllm#22829: [CI Failure][NIGHTLY FIRE DRILL]: Entrypoints Test

| 字段 | 值 |
| --- | --- |
| Issue | [#22829](https://github.com/vllm-project/vllm/issues/22829) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure][NIGHTLY FIRE DRILL]: Entrypoints Test

### Issue 正文摘录

### Name of failing test test_openapi_stateless ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test TBU ### 📝 History of failing test https://buildkite.com/vllm/ci/builds/26788#0198a196-b375-4423-be1a-61257fca9d9f ### CC List. @wseaton

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure][NIGHTLY FIRE DRILL]: Entrypoints Test ci-failure ### Name of failing test test_openapi_stateless ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g.
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: est_openapi_stateless ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test TBU ### 📝 History of failing test...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ci-failure ### Name of failing test test_openapi_stateless ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure][NIGHTLY FIRE DRILL]: Entrypoints Test ci-failure ### Name of failing test test_openapi_stateless ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. b...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
