# vllm-project/vllm#28061: [CI Failure]: ci-infra is broken at approximately noon Nov, 4, 2025

| 字段 | 值 |
| --- | --- |
| Issue | [#28061](https://github.com/vllm-project/vllm/issues/28061) |
| 状态 | closed |
| 标签 | stale;ci-failure |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: ci-infra is broken at approximately noon Nov, 4, 2025

### Issue 正文摘录

### Name of failing test bootstrap.sh ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Apparently a bad queue name "arm64_cpu_queue_premerge" is mentioned in the test definition. ### 📝 History of failing test noon (Central Time Zone) November, 4, 2025 ### CC List. Apparently a bad queue name "arm64_cpu_queue_premerge" is mentioned in the test definition.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [CI Failure]: ci-infra is broken at approximately noon Nov, 4, 2025 stale;ci-failure ### Name of failing test bootstrap.sh ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libr...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ng test bootstrap.sh ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Apparently a bad queue name "arm64_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [CI Failure]: ci-infra is broken at approximately noon Nov, 4, 2025 stale;ci-failure ### Name of failing test bootstrap.sh ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external lib
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 025 stale;ci-failure ### Name of failing test bootstrap.sh ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: at approximately noon Nov, 4, 2025 stale;ci-failure ### Name of failing test bootstrap.sh ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
