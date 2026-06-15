# vllm-project/vllm#29440: [CI Failure]: torch.compile cache are reused across unittests.

| 字段 | 值 |
| --- | --- |
| Issue | [#29440](https://github.com/vllm-project/vllm/issues/29440) |
| 状态 | open |
| 标签 | torch.compile;keep-open;ci-failure |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: torch.compile cache are reused across unittests.

### Issue 正文摘录

### Name of failing test test_basic_correctness.py ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test We are seeing test failures on PyTorch CI (running against pinned vllm nightly and torch trunk): https://github.com/pytorch/pytorch/actions/runs/19645318969/job/56265977952?pr=16649 The root cause of these failures are due to the fact that when we compile a model for a specific test, we later reuse the cache dir in another test and sometimes this "cache sharing across unittest cases" will expose cache bugs accidentally when these is caching bug. Although this behavior accidentally expose cache bugs, this is not ideal because when such a failure happens, we have no idea it's a caching issue and will spend time debugging something else. Ideally this should be broken down into 2 pieces: 1. Some dedicated test for testing against caching config changes. 2. Each test should have isolated caching env. To be noted that, pytorch once test everything with single shared cache dir, which results in a lot of flakiness in the CI and later we realized testing in isolation is more impo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: torch.compile cache are reused across unittests. torch.compile;keep-open;ci-failure ### Name of failing test test_basic_correctness.py ### Basic information - [x] Flaky test - [ ] Can reproduce locally -
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: failure ### Name of failing test test_basic_correctness.py ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [CI Failure]: torch.compile cache are reused across unittests. torch.compile;keep-open;ci-failure ### Name of failing test test_basic_correctness.py ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: _basic_correctness.py ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test We are seeing test failures on PyT...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ve no idea it's a caching issue and will spend time debugging something else. Ideally this should be broken down into 2 pieces: 1. Some dedicated test for testing against caching config changes. 2. Each test should have...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
