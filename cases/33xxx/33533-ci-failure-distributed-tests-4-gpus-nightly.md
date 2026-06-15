# vllm-project/vllm#33533: [CI Failure]: Distributed Tests (4 GPUs) [Nightly]

| 字段 | 值 |
| --- | --- |
| Issue | [#33533](https://github.com/vllm-project/vllm/issues/33533) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Distributed Tests (4 GPUs) [Nightly]

### Issue 正文摘录

### Name of failing test `torchrun --nproc-per-node=4 distributed/test_torchrun_example.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Fails to start (seems to be a NCCL hang) https://buildkite.com/vllm/ci/builds/49464#019c1801-a6c3-47a4-9890-f1b805ca12b3 ### 📝 History of failing test Failing since thursday nightly ### CC List. _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Distributed Tests (4 GPUs) [Nightly] ci-failure ### Name of failing test `torchrun --nproc-per-node=4 distributed/test_torchrun_example.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce local
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: _torchrun_example.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Fails to start (seems to be a NCCL...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: un --nproc-per-node=4 distributed/test_torchrun_example.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: Distributed Tests (4 GPUs) [Nightly] ci-failure ### Name of failing test `torchrun --nproc-per-node=4 distributed/test_torchrun_example.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locall...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
