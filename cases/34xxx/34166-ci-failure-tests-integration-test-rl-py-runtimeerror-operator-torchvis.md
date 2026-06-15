# vllm-project/vllm#34166: [CI Failure]: tests/integration/test_rl.py: RuntimeError: operator torchvision::nms does not exist

| 字段 | 值 |
| --- | --- |
| Issue | [#34166](https://github.com/vllm-project/vllm/issues/34166) |
| 状态 | open |
| 标签 | stale;ci-failure |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: tests/integration/test_rl.py: RuntimeError: operator torchvision::nms does not exist

### Issue 正文摘录

### Name of failing test tests/integration/test_rl.py::{test_reward_goes_up, test_reward_in_range} ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [x] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Tests fail with `RuntimeError: operator torchvision::nms does not exist`. Possibly related to pytorch 2.10 upgrade? https://github.com/vllm-project/vllm/pull/30525 ### 📝 History of failing test https://buildkite.com/vllm/ci/builds/50655#019c4134-6e4f-4251-9611-4a2a8fa7ed1d ### CC List. _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: tests/integration/test_rl.py: RuntimeError: operator torchvision::nms does not exist stale;ci-failure ### Name of failing test tests/integration/test_rl.py::{test_reward_goes_up, test_reward_in_range} ###
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: test_reward_in_range} ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [x] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Tests fail with `RuntimeError: ope...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ion/test_rl.py::{test_reward_goes_up, test_reward_in_range} ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [x] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ation/test_rl.py: RuntimeError: operator torchvision::nms does not exist stale;ci-failure ### Name of failing test tests/integration/test_rl.py::{test_reward_goes_up, test_reward_in_range} ### Basic information - [ ] Fl...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: tests/integration/test_rl.py: RuntimeError: operator torchvision::nms does not exist stale;ci-failure ### Name of failing test tests/integration/test_rl.py::{test_reward_goes_up, test_reward_in_range} ###...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
