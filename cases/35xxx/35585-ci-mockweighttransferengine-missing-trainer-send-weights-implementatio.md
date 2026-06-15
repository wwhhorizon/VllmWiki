# vllm-project/vllm#35585: [CI] MockWeightTransferEngine missing trainer_send_weights implementation

| 字段 | 值 |
| --- | --- |
| Issue | [#35585](https://github.com/vllm-project/vllm/issues/35585) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI] MockWeightTransferEngine missing trainer_send_weights implementation

### Issue 正文摘录

## Name of failing test - `entrypoints/weight_transfer/test_weight_transfer_llm.py::test_init_weight_transfer_engine_calls_engine` - `entrypoints/weight_transfer/test_weight_transfer_llm.py::test_update_weights_calls_engine` - `entrypoints/weight_transfer/test_weight_transfer_llm.py::test_full_weight_transfer_flow` ## Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries **Affected jobs:** Entrypoints Unit Tests **Category:** test ## Describe the failing test Test mock class MockWeightTransferEngine is incomplete, missing implementation for abstract method 'trainer_send_weights'. When weight transfer tests instantiate the mock in WeightTransferEngineFactory.create_engine(), Python raises TypeError because abstract base class requirements are not met. This prevents weight transfer tests from running. ``` TypeError: Can't instantiate abstract class MockWeightTransferEngine without an implementation for abstract method 'trainer_send_weights' ``` ## Relevant builds - [Build #53738](https://buildkite.com/vllm/ci/builds/53738) (405f28d3) - [Entrypoints Unit Tests](https://buildkite.com/vllm/ci/builds/53738#019ca1d5-66d2-4bb4-a02d-74bbcd409152)...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI] MockWeightTransferEngine missing trainer_send_weights implementation ci-failure ## Name of failing test - `entrypoints/weight_transfer/test_weight_transfer_llm.py::test_init_weight_transfer_engine_calls_engine` - `e
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: _weight_transfer_flow` ## Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries **Affected jobs:** Entrypoints Unit Tests **Category:** test ## Describe the failing test Test...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: test_weight_transfer_llm.py::test_full_weight_transfer_flow` ## Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries **Affected jobs:** Entrypoints Unit Tests **Category:** t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: issing trainer_send_weights implementation ci-failure ## Name of failing test - `entrypoints/weight_transfer/test_weight_transfer_llm.py::test_init_weight_transfer_engine_calls_engine` - `entrypoints/weight_transfer/tes...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
