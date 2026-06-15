# vllm-project/vllm#43354: [CI Failure]: Quantized Models Test fails with OOM

| 字段 | 值 |
| --- | --- |
| Issue | [#43354](https://github.com/vllm-project/vllm/issues/43354) |
| 状态 | open |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Quantized Models Test fails with OOM

### Issue 正文摘录

### Name of failing test models/quantization/test_awq.py::test_awq_load (gemma4 tests) ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Tests in `models/quantization/test_awq.py::test_awq_load` (gemma4 tests) fail due to Out of Memory Errors. ### 📝 History of failing test This is a new failure ### CC List. _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [CI Failure]: Quantized Models Test fails with OOM ci-failure ### Name of failing test models/quantization/test_awq.py::test_awq_load (gemma4 tests) ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: q_load (gemma4 tests) ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Tests in `models/quantization/test...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [CI Failure]: Quantized Models Test fails with OOM ci-failure ### Name of failing test models/quantization/test_awq.py::test_awq_load (gemma4 tests) ### Basic information - [ ] Flaky test - [ ] Can reproduce locally -
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [CI Failure]: Quantized Models Test fails with OOM ci-failure ### Name of failing test models/quantization/test_awq.py::test_awq_load (gemma4 tests) ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [CI Failure]: Quantized Models Test fails with OOM ci-failure ### Name of failing test models/quantization/test_awq.py::test_awq_load (gemma4 tests) ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
