# vllm-project/vllm#40637: [CI Failure]: Kernels FusedMoE Layer Test (2 H100s): test_moe_layer.py::test_moe_layer

| 字段 | 值 |
| --- | --- |
| Issue | [#40637](https://github.com/vllm-project/vllm/issues/40637) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Kernels FusedMoE Layer Test (2 H100s): test_moe_layer.py::test_moe_layer

### Issue 正文摘录

### Name of failing test FAILED kernels/moe/test_moe_layer.py::test_moe_layer[False-deepep_high_throughput-2-1-True] - torch.multiprocessing.spawn.ProcessExitedException: process 0 terminated with signal SIGABRT FAILED kernels/moe/test_moe_layer.py::test_moe_layer[False-deepep_low_latency-2-1-True] - torch.multiprocessing.spawn.ProcessExitedException: process 0 terminated with signal SIGABRT ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test https://buildkite.com/vllm/ci/builds/62456#019db5a5-fc65-4fe3-bcd4-62ead4870367 ```bash =================================================================== short test summary info ==================================================================== -- FAILED kernels/moe/test_moe_layer.py::test_moe_layer[False-deepep_high_throughput-2-1-True] - torch.multiprocessing.spawn.ProcessExitedException: process 0 terminated with signal SIGABRT FAILED kernels/moe/test_moe_layer.py::test_moe_layer[False-deepep_low_latency-2-1-True] - torch.multiprocessing.spawn.ProcessExitedException: process 0 terminated with signal SIGABRT ===================...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [CI Failure]: Kernels FusedMoE Layer Test (2 H100s): test_moe_layer.py::test_moe_layer ci-failure ### Name of failing test FAILED kernels/moe/test_moe_layer.py::test_moe_layer[False-deepep_high_throughput-2-1-True] - to...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Kernels FusedMoE Layer Test (2 H100s): test_moe_layer.py::test_moe_layer ci-failure ### Name of failing test FAILED kernels/moe/test_moe_layer.py::test_moe_layer[False-deepep_high_throughput-2-1-True] - tor
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: d with signal SIGABRT ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test https://buildkite.com/vllm/ci/buil...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [CI Failure]: Kernels FusedMoE Layer Test (2 H100s): test_moe_layer.py::test_moe_layer ci-failure ### Name of failing test FAILED kernels/moe/test_moe_layer.py::test_moe_layer[False-deepep_high_throughput-2-1-True] - to...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: of failing test FAILED kernels/moe/test_moe_layer.py::test_moe_layer[False-deepep_high_throughput-2-1-True] - torch.multiprocessing.spawn.ProcessExitedException: process 0 terminated with signal SIGABRT FAILED kernels/m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
