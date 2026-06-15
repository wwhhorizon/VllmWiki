# vllm-project/vllm#34617: [CI Failure]: `v1/e2e/test_spec_decode.py::test_ngram_and_suffix_correctness`

| 字段 | 值 |
| --- | --- |
| Issue | [#34617](https://github.com/vllm-project/vllm/issues/34617) |
| 状态 | open |
| 标签 | stale;ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: `v1/e2e/test_spec_decode.py::test_ngram_and_suffix_correctness`

### Issue 正文摘录

### Name of failing test `v1/e2e/test_spec_decode.py::test_ngram_and_suffix_correctness` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test `FAILED v1/e2e/test_spec_decode.py::test_ngram_and_suffix_correctness[speculative_config1] - assert 52 >= 66` May be flaky ### 📝 History of failing test https://buildkite.com/vllm/ci/builds/51738/tests?sid=019c6541-0084-46c5-b830-4ff83a80dd92&tab=output&group_by=test ### CC List. _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [CI Failure]: `v1/e2e/test_spec_decode.py::test_ngram_and_suffix_correctness` stale;ci-failure ### Name of failing test `v1/e2e/test_spec_decode.py::test_ngram_and_suffix_correctness` ### Basic information - [x] Flaky t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: `v1/e2e/test_spec_decode.py::test_ngram_and_suffix_correctness` stale;ci-failure ### Name of failing test `v1/e2e/test_spec_decode.py::test_ngram_and_suffix_correctness` ### Basic information - [x] Flaky
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: e2e/test_spec_decode.py::test_ngram_and_suffix_correctness` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: d_suffix_correctness` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test `FAILED v1/e2e/test_spec_decode.py...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: `v1/e2e/test_spec_decode.py::test_ngram_and_suffix_correctness` stale;ci-failure ### Name of failing test `v1/e2e/test_spec_decode.py::test_ngram_and_suffix_correctness` ### Basic information - [x] Flaky t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
