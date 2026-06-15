# vllm-project/vllm#34284: [CI Failure]: Metrics - Tracing Test - Race Condition Between gRPC and OpenTelemetry Threads?

| 字段 | 值 |
| --- | --- |
| Issue | [#34284](https://github.com/vllm-project/vllm/issues/34284) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Metrics - Tracing Test - Race Condition Between gRPC and OpenTelemetry Threads?

### Issue 正文摘录

### Name of failing test pytest -v -s v1/tracing ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test The "Metrics Tracing (2GPU)" fails with a `segmentation fault` on CI run https://buildkite.com/vllm/ci/builds/50888 (nightly) I can't reproduce this test locally. ### 📝 History of failing test Started failing today, Feb 10 2026 - https://buildkite.com/vllm/ci/builds/50888 ### CC List. _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Metrics - Tracing Test - Race Condition Between gRPC and OpenTelemetry Threads? ci-failure ### Name of failing test pytest -v -s v1/tracing ### Basic information - [ ] Flaky test - [ ] Can reproduce local
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: test -v -s v1/tracing ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test The "Metrics Tracing (2GPU)" fails...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: i-failure ### Name of failing test pytest -v -s v1/tracing ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: Metrics - Tracing Test - Race Condition Between gRPC and OpenTelemetry Threads? ci-failure ### Name of failing test pytest -v -s v1/tracing ### Basic information - [ ] Flaky test - [ ] Can reproduce locall...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
