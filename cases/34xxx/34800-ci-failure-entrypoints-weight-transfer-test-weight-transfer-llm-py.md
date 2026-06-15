# vllm-project/vllm#34800: [CI Failure]: entrypoints/weight_transfer/test_weight_transfer_llm.py

| 字段 | 值 |
| --- | --- |
| Issue | [#34800](https://github.com/vllm-project/vllm/issues/34800) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: entrypoints/weight_transfer/test_weight_transfer_llm.py

### Issue 正文摘录

### Name of failing test `entrypoints/weight_transfer/test_weight_transfer_llm.py::test_init_weight_transfer_engine_calls_engine` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Looks like the issue is that the patch `with patch( "vllm.v1.worker.gpu_worker.WeightTransferEngineFactory.create_engine", mock_create_engine, )` doesn't work (might be because of spawning?) and not `MockWeightTransferEngine` is created. ``` FAILED entrypoints/weight_transfer/test_weight_transfer_llm.py::test_init_weight_transfer_engine_calls_engine - Exception: Call to collective_rpc method failed: Invalid init_info for NCCLWeightTransferEngine: NCCLWeightTransferInitInfo.__init__() got an unexpected keyword argument 'test_param' -- [2026-02-18T07:23:18Z] FAILED entrypoints/weight_transfer/test_weight_transfer_llm.py::test_update_weights_calls_engine - Exception: Call to collective_rpc method failed: Invalid init_info for NCCLWeightTransferEngine: NCCLWeightTransferInitInfo.__init__() got an unexpected keyword argument 'test_param' [2026-02-18T07:23:18Z] FAILED entrypoints/weight_transfer/tes...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: entrypoints/weight_transfer/test_weight_transfer_llm.py ci-failure ### Name of failing test `entrypoints/weight_transfer/test_weight_transfer_llm.py::test_init_weight_transfer_engine_calls_engine` ### Basi
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: _engine_calls_engine` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Looks like the issue is that the p...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: sfer_llm.py::test_init_weight_transfer_engine_calls_engine` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: entrypoints/weight_transfer/test_weight_transfer_llm.py ci-failure ### Name of failing test `entrypoints/weight_transfer/test_weight_transfer_llm.py::test_init_weight_transfer_engine_calls_engine` ### Basi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
