# vllm-project/vllm#32607: [CI Failure][Nightly 1-18]: Test Models Distirbuted

| 字段 | 值 |
| --- | --- |
| Issue | [#32607](https://github.com/vllm-project/vllm/issues/32607) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure][Nightly 1-18]: Test Models Distirbuted

### Issue 正文摘录

### Name of failing test `basic_correctness/test_basic_correctness.py::test_models_distributed[True-facebook/opt-125m-mp--A100-extra_env7]` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test https://buildkite.com/vllm/ci/builds/47580 Invalid str comparison: ```bash E AssertionError: Test6: -- E hf: 'Explain the cultural significance of the Mona Lisa painting, and how its perception might vary in Western versus Eastern societies.\n\nThe Mona Lisa' E vllm: "Explain the cultural significance of the Mona Lisa painting, and how its perception might vary in Western versus Eastern societies.\n\nI'm not sure" ``` ### 📝 History of failing test Never failed before: - https://buildkite.com/organizations/vllm/analytics/suites/ci-1/tests/0a9c3a2d-948d-8f6c-b83c-d73c1d2a5ffa?branch=main&query=test_models_distributed%5BTrue-facebook%2Fopt-125m-mp--A100-extra_env7%5D ### CC List. _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [CI Failure][Nightly 1-18]: Test Models Distirbuted ci-failure ### Name of failing test `basic_correctness/test_basic_correctness.py::test_models_distributed[True-facebook/opt-125m-mp--A100-extra_env7]` ### Basic inform...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure][Nightly 1-18]: Test Models Distirbuted ci-failure ### Name of failing test `basic_correctness/test_basic_correctness.py::test_models_distributed[True-facebook/opt-125m-mp--A100-extra_env7]` ### Basic inform
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: mp--A100-extra_env7]` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test https://buildkite.com/vllm/ci/buil...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: basic_correctness.py::test_models_distributed[True-facebook/opt-125m-mp--A100-extra_env7]` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure][Nightly 1-18]: Test Models Distirbuted ci-failure ### Name of failing test `basic_correctness/test_basic_correctness.py::test_models_distributed[True-facebook/opt-125m-mp--A100-extra_env7]` ### Basic inform...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
