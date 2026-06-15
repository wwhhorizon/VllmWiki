# vllm-project/vllm#43000: [CI Failure]: Acceptance length issue in the Speculators Correctness group

| 字段 | 值 |
| --- | --- |
| Issue | [#43000](https://github.com/vllm-project/vllm/issues/43000) |
| 状态 | open |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Acceptance length issue in the Speculators Correctness group

### Issue 正文摘录

### Name of failing test tests/v1/spec_decode/test_speculators_correctness.py::test_speculators_correctness[peagle] ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` E AssertionError: PEagle speculators acceptance length too low: 1.74 = 1.816 ``` ### 📝 History of failing test According to the CI dashboard this test has been failing 100% of the time since [f887aa1a53](https://github.com/vllm-project/vllm/commit/f887aa1a53e273d90ac537fcd399504f70aff2c7). https://buildkite.com/vllm/ci/builds/66298 ### CC List. @LucasWilkinson @MatthewBonanni @benchislett

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Acceptance length issue in the Speculators Correctness group ci-failure ### Name of failing test tests/v1/spec_decode/test_speculators_correctness.py::test_speculators_correctness[peagle] ### Basic informa
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: s_correctness[peagle] ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` E AssertionError: PEagle specu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: lators_correctness.py::test_speculators_correctness[peagle] ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ors Correctness group ci-failure ### Name of failing test tests/v1/spec_decode/test_speculators_correctness.py::test_speculators_correctness[peagle] ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ssue in the Speculators Correctness group ci-failure ### Name of failing test tests/v1/spec_decode/test_speculators_correctness.py::test_speculators_correctness[peagle] ### Basic information - [ ] Flaky test - [x] Can r...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
