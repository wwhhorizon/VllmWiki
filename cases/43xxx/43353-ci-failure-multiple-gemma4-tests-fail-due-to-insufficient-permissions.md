# vllm-project/vllm#43353: [CI Failure]: Multiple Gemma4 tests fail due to insufficient permissions

| 字段 | 值 |
| --- | --- |
| Issue | [#43353](https://github.com/vllm-project/vllm/issues/43353) |
| 状态 | open |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Multiple Gemma4 tests fail due to insufficient permissions

### Issue 正文摘录

### Name of failing test models/multimodal/generation/test_common.py::test_single_image_models (gemma4 tests) ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Multiple tests fail with ``` Failed with vllm.third_party.pynvml.NVMLError_NoPermission: Insufficient Permissions ``` ### 📝 History of failing test This is a new failure ### CC List. _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [CI Failure]: Multiple Gemma4 tests fail due to insufficient permissions ci-failure ### Name of failing test models/multimodal/generation/test_common.py::test_single_image_models (gemma4 tests) ### Basic information - [...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: models (gemma4 tests) ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Multiple tests fail with ``` Faile...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [CI Failure]: Multiple Gemma4 tests fail due to insufficient permissions ci-failure ### Name of failing test models/multimodal/generation/test_common.py::test_single_image_models (gemma4 tests) ### Basic information -
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [CI Failure]: Multiple Gemma4 tests fail due to insufficient permissions ci-failure ### Name of failing test models/multimodal/generation/test_common.py::test_single_image_models (gemma4 tests) ### Basic information - [...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: Multiple Gemma4 tests fail due to insufficient permissions ci-failure ### Name of failing test models/multimodal/generation/test_common.py::test_single_image_models (gemma4 tests) ### Basic information - [...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
