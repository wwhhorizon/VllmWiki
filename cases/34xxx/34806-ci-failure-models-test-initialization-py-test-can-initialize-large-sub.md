# vllm-project/vllm#34806: [CI Failure]: models/test_initialization.py::test_can_initialize_large_subset[EagleMiniCPMForCausalLM]

| 字段 | 值 |
| --- | --- |
| Issue | [#34806](https://github.com/vllm-project/vllm/issues/34806) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: models/test_initialization.py::test_can_initialize_large_subset[EagleMiniCPMForCausalLM]

### Issue 正文摘录

### Name of failing test `models/test_initialization.py::test_can_initialize_large_subset[EagleMiniCPMForCausalLM]`` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test During `dummy_run`: ``` TypeError: EagleMiniCPMForCausalLM.forward() got an unexpected keyword argument 'inputs_embeds' ``` ### 📝 History of failing test https://buildkite.com/vllm/ci/builds/52052/steps/canvas?jid=019c6f8d-c545-4f0c-93a5-f519bdfd8ace ### CC List. @huangyuxiang03

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: models/test_initialization.py::test_can_initialize_large_subset[EagleMiniCPMForCausalLM] ci-failure ### Name of failing test `models/test_initialization.py::test_can_initialize_large_subset[EagleMiniCPMForC
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [CI Failure]: models/test_initialization.py::test_can_initialize_large_subset[EagleMiniCPMForCausalLM] ci-failure ### Name of failing test `models/test_initialization.py::test_can_initialize_large_subset[EagleMiniCPMFor...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: MiniCPMForCausalLM]`` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test During `dummy_run`: ``` TypeError:...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: models/test_initialization.py::test_can_initialize_large_subset[EagleMiniCPMForCausalLM] ci-failure ### Name of failing test `models/test_initialization.py::test_can_initialize_large_subset[EagleMiniCPMFor...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
