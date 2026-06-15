# vllm-project/vllm#22831: [CI Failure][NIGHTLY FIRE DRILL]: Distributed Tests (4GPUs)

| 字段 | 值 |
| --- | --- |
| Issue | [#22831](https://github.com/vllm-project/vllm/issues/22831) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure][NIGHTLY FIRE DRILL]: Distributed Tests (4GPUs)

### Issue 正文摘录

### Name of failing test v1/test_async_llm_dp.py::test_load ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test the test is hanging ### 📝 History of failing test https://buildkite.com/vllm/ci/builds/26788#0198a196-b376-4e2b-8420-3b9e85b48a54 ### CC List. _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure][NIGHTLY FIRE DRILL]: Distributed Tests (4GPUs) ci-failure ### Name of failing test v1/test_async_llm_dp.py::test_load ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by exte
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: _llm_dp.py::test_load ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test the test is hanging ### 📝 History...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ## Name of failing test v1/test_async_llm_dp.py::test_load ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure][NIGHTLY FIRE DRILL]: Distributed Tests (4GPUs) ci-failure ### Name of failing test v1/test_async_llm_dp.py::test_load ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by exter...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
