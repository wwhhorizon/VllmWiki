# vllm-project/vllm#34637: [CI Failure]:  mi325_1: Entrypoints Integration Test (API Server 2)

| 字段 | 值 |
| --- | --- |
| Issue | [#34637](https://github.com/vllm-project/vllm/issues/34637) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]:  mi325_1: Entrypoints Integration Test (API Server 2)

### Issue 正文摘录

### Name of failing test `pytest -s -v entrypoints/instrumentator/test_metrics.py::test_abort_metrics_reset[-text]` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test There was a recent regression in this TG. This is expected to be green in our next nightly run after: https://github.com/vllm-project/vllm/pull/34566 ### 📝 History of failing test https://buildkite.com/vllm/amd-ci/builds/4802/steps/canvas?sid=019c653f-d83d-4f99-8af1-e12ce7c2a656&tab=output

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi325_1: Entrypoints Integration Test (API Server 2) ci-failure ### Name of failing test `pytest -s -v entrypoints/instrumentator/test_metrics.py::test_abort_metrics_reset[-text]` ### Basic information -
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [CI Failure]: mi325_1: Entrypoints Integration Test (API Server 2) ci-failure ### Name of failing test `pytest -s -v entrypoints/instrumentator/test_metrics.py::test_abort_metrics_reset[-text]` ### Basic information - [...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: metrics_reset[-text]` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test There was a recent regression in t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: umentator/test_metrics.py::test_abort_metrics_reset[-text]` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
