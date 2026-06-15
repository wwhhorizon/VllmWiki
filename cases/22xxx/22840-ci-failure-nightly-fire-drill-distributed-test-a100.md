# vllm-project/vllm#22840: [CI Failure][NIGHTLY FIRE DRILL]: Distributed Test - A100

| 字段 | 值 |
| --- | --- |
| Issue | [#22840](https://github.com/vllm-project/vllm/issues/22840) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure][NIGHTLY FIRE DRILL]: Distributed Test - A100

### Issue 正文摘录

### Name of failing test torchrun --nproc_per_node=2 distributed/test_ca_buffer_sharing.py ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test some issue with CustomAllReduce.free_shared_buffer ### 📝 History of failing test https://buildkite.com/vllm/ci/builds/26788#0198a196-b3a3-4aea-bbe8-232079738347 ### CC List. cc @ilmarkov

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure][NIGHTLY FIRE DRILL]: Distributed Test - A100 ci-failure ### Name of failing test torchrun --nproc_per_node=2 distributed/test_ca_buffer_sharing.py ### Basic information - [ ] Flaky test - [ ] Can reproduce
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: _ca_buffer_sharing.py ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test some issue with CustomAllReduce.fr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [CI Failure][NIGHTLY FIRE DRILL]: Distributed Test - A100 ci-failure ### Name of failing test torchrun --nproc_per_node=2 distributed/test_ca_buffer_sharing.py ### Basic information - [ ] Flaky test - [ ] Can reproduce...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: un --nproc_per_node=2 distributed/test_ca_buffer_sharing.py ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure][NIGHTLY FIRE DRILL]: Distributed Test - A100 ci-failure ### Name of failing test torchrun --nproc_per_node=2 distributed/test_ca_buffer_sharing.py ### Basic information - [ ] Flaky test - [ ] Can reproduce...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
