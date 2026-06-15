# vllm-project/vllm#34943: [CI Failure]: AMD Samplers Test (mi325_1)

| 字段 | 值 |
| --- | --- |
| Issue | [#34943](https://github.com/vllm-project/vllm/issues/34943) |
| 状态 | closed |
| 标签 | rocm;ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting |
| 子分类 |  |
| Operator 关键词 | kernel |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: AMD Samplers Test (mi325_1)

### Issue 正文摘录

### Name of failing test distributed/test_ca_buffer_sharing.py, distributed/test_multiproc_executor.py, distributed/test_torchrun_example.py , distributed/test_torchrun_example_moe.py, kernels/helion/test_utils.py, plugins_tests/test_stats_logger_plugins.py, v1/kv_connector/nixl_integration/test_edge_cases.py ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Multiple errors - looks environmental. Please take a look at https://buildkite.com/vllm/ci/builds/52218#019c74b4-5f36-4358-a577-34e29f305932 ### 📝 History of failing test Started failing https://buildkite.com/vllm/ci/builds/52052 (Feb 18) ### CC List. cc @tjtanaa can you please take a look or point to someone please. Thanks 🙌

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: AMD Samplers Test (mi325_1) rocm;ci-failure ### Name of failing test distributed/test_ca_buffer_sharing.py, distributed/test_multiproc_executor.py, distributed/test_torchrun_example.py , distributed/test_t
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: n/test_edge_cases.py ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Multiple errors - looks environment...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [CI Failure]: AMD Samplers Test (mi325_1) rocm;ci-failure ### Name of failing test distributed/test_ca_buffer_sharing.py, distributed/test_multiproc_executor.py, distributed/test_torchrun_example.py , distributed/test_t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ns.py, v1/kv_connector/nixl_integration/test_edge_cases.py ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: distributed/test_torchrun_example.py , distributed/test_torchrun_example_moe.py, kernels/helion/test_utils.py, plugins_tests/test_stats_logger_plugins.py, v1/kv_connector/nixl_integration/test_edge_cases.py ### Basic in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
