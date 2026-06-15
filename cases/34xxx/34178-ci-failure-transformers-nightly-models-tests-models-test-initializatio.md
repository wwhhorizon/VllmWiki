# vllm-project/vllm#34178: [CI Failure]: Transformers Nightly Models, tests/models/test_initialization.py

| 字段 | 值 |
| --- | --- |
| Issue | [#34178](https://github.com/vllm-project/vllm/issues/34178) |
| 状态 | open |
| 标签 | stale;ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Transformers Nightly Models, tests/models/test_initialization.py

### Issue 正文摘录

### Name of failing test tests/models/test_initialization.py::{test_can_initialize_small_subset. test_can_initialize_large_subset} ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test A large number of testpoints fail. See logs here: https://buildkite.com/vllm/ci/builds/50655#019c4134-6e9e-4a98-a858-5365c8d3b4a9 ### 📝 History of failing test Seen failing on 2/9/26 nightly run. ### CC List. _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Transformers Nightly Models, tests/models/test_initialization.py stale;ci-failure ### Name of failing test tests/models/test_initialization.py::{test_can_initialize_small_subset. test_can_initialize_large_s
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [CI Failure]: Transformers Nightly Models, tests/models/test_initialization.py stale;ci-failure ### Name of failing test tests/models/test_initialization.py::{test_can_initialize_small_subset. test_can_initialize_large_...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: tialize_large_subset} ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test A large number of testpoints fail....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: failing test tests/models/test_initialization.py::{test_can_initialize_small_subset. test_can_initialize_large_subset} ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external librarie...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ilure]: Transformers Nightly Models, tests/models/test_initialization.py stale;ci-failure ### Name of failing test tests/models/test_initialization.py::{test_can_initialize_small_subset. test_can_initialize_large_subset...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
