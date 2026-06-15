# vllm-project/vllm#22902: [CI Failure]: `test_async_llm_dp` causes hang and 3 hour timeout in CI

| 字段 | 值 |
| --- | --- |
| Issue | [#22902](https://github.com/vllm-project/vllm/issues/22902) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: `test_async_llm_dp` causes hang and 3 hour timeout in CI

### Issue 正文摘录

### Name of failing test v1/test_async_llm_dp.py ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test The test doesn't actually seem to fail in CI but it seems to hang and the test times out after 3 hours. Locally, I cannot reproduce the hang but the test is flaky and sometimes fails (will update shortly with the error). I have verified that if we skip this test, the Distributed Test (2 GPUs) is now passing. ### 📝 History of failing test TBD ### CC List. _No response_

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: /test_async_llm_dp.py ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test The test doesn't actually seem to...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [CI Failure]: `test_async_llm_dp` causes hang and 3 hour timeout in CI ci-failure ### Name of failing test v1/test_async_llm_dp.py ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by exte
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: i-failure ### Name of failing test v1/test_async_llm_dp.py ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: `test_async_llm_dp` causes hang and 3 hour timeout in CI ci-failure ### Name of failing test v1/test_async_llm_dp.py ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by exter...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
