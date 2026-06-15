# vllm-project/vllm#34814: [CI Failure]: models/test_initialization.py::test_can_initialize_large_subset[InternS1ProForConditionalGeneration]

| 字段 | 值 |
| --- | --- |
| Issue | [#34814](https://github.com/vllm-project/vllm/issues/34814) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: models/test_initialization.py::test_can_initialize_large_subset[InternS1ProForConditionalGeneration]

### Issue 正文摘录

### Name of failing test `models/test_initialization.py::test_can_initialize_large_subset[InternS1ProForConditionalGeneration]` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` assert routing_weights.shape[-1] % self.n_groups == 0, ( AssertionError: 2 cannot be divided by 8 ``` ### 📝 History of failing test https://buildkite.com/vllm/ci/builds/52052/steps/canvas?jid=019c6f8d-c546-4165-8d8f-fbbd93e602ce Triggered after [PR](https://github.com/vllm-project/vllm/pull/33600) ### CC List. _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: models/test_initialization.py::test_can_initialize_large_subset[InternS1ProForConditionalGeneration] ci-failure ### Name of failing test `models/test_initialization.py::test_can_initialize_large_subset[Inte
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [CI Failure]: models/test_initialization.py::test_can_initialize_large_subset[InternS1ProForConditionalGeneration] ci-failure ### Name of failing test `models/test_initialization.py::test_can_initialize_large_subset[Int...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` assert routing_weights.shape[-1] % self.n_groups == 0, ( AssertionError: 2 cannot be divided by 8 ``` ### 📝 History of failing test https://buildkite.com/v...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: nditionalGeneration]` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` assert routing_weights.shape[-...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` assert routing_weights.shape[-1] % self.n_groups == 0, ( AssertionError: 2 cannot be divided by 8 ``` ### 📝 History of failing test https://buildkite.com/v...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
