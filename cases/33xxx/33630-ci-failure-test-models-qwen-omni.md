# vllm-project/vllm#33630: [CI Failure]: Test Models (Qwen OMni)

| 字段 | 值 |
| --- | --- |
| Issue | [#33630](https://github.com/vllm-project/vllm/issues/33630) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Test Models (Qwen OMni)

### Issue 正文摘录

### Name of failing test `FAILED models/test_initialization.py::test_can_initialize_large_subset` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test https://buildkite.com/vllm/ci/builds/49657#019c20a3-411d-452f-a178-fc74d3e4dfff FAILED models/test_initialization.py::test_can_initialize_large_subset[Qwen3OmniMoeForConditionalGeneration] - KeyError: 'audio' ### 📝 History of failing test ? ### CC List. cc @DarkLight1337

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [CI Failure]: Test Models (Qwen OMni) ci-failure ### Name of failing test `FAILED models/test_initialization.py::test_can_initialize_large_subset` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ]...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Test Models (Qwen OMni) ci-failure ### Name of failing test `FAILED models/test_initialization.py::test_can_initialize_large_subset` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: tialize_large_subset` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test https://buildkite.com/vllm/ci/buil...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: models/test_initialization.py::test_can_initialize_large_subset[Qwen3OmniMoeForConditionalGeneration] - KeyError: 'audio' ### 📝 History of failing test ? ### CC List. cc @DarkLight1337
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: Test Models (Qwen OMni) ci-failure ### Name of failing test `FAILED models/test_initialization.py::test_can_initialize_large_subset` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ]...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
