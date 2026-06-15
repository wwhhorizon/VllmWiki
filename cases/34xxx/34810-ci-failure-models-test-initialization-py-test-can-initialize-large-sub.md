# vllm-project/vllm#34810: [CI Failure]: models/test_initialization.py::test_can_initialize_large_subset[H2OVLChatModel]

| 字段 | 值 |
| --- | --- |
| Issue | [#34810](https://github.com/vllm-project/vllm/issues/34810) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: models/test_initialization.py::test_can_initialize_large_subset[H2OVLChatModel]

### Issue 正文摘录

### Name of failing test `models/test_initialization.py::test_can_initialize_large_subset[H2OVLChatModel]` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` TypeError: _LazyConfigMapping.__init__() missing 1 required positional argument: 'mapping' ``` ### 📝 History of failing test https://buildkite.com/vllm/ci/builds/52052/steps/canvas?jid=019c6f8d-c524-48e4-bbd8-dff962e89889 ### CC List. _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [CI Failure]: models/test_initialization.py::test_can_initialize_large_subset[H2OVLChatModel] ci-failure ### Name of failing test `models/test_initialization.py::test_can_initialize_large_subset[H2OVLChatModel]` ### Bas...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: models/test_initialization.py::test_can_initialize_large_subset[H2OVLChatModel] ci-failure ### Name of failing test `models/test_initialization.py::test_can_initialize_large_subset[H2OVLChatModel]` ### Bas
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: bset[H2OVLChatModel]` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` TypeError: _LazyConfigMapping....
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ansformers`) ### 🧪 Describe the failing test ``` TypeError: _LazyConfigMapping.__init__() missing 1 required positional argument: 'mapping' ``` ### 📝 History of failing test https://buildkite.com/vllm/ci/builds/52052/st...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: models/test_initialization.py::test_can_initialize_large_subset[H2OVLChatModel] ci-failure ### Name of failing test `models/test_initialization.py::test_can_initialize_large_subset[H2OVLChatModel]` ### Bas...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
