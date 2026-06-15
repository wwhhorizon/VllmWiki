# vllm-project/vllm#33816: [CI Failure]: Quantized Models Test in `tests/models/quantization/test_gptq_marlin.py::test_models[5-32-bfloat16-model2]`

| 字段 | 值 |
| --- | --- |
| Issue | [#33816](https://github.com/vllm-project/vllm/issues/33816) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Quantized Models Test in `tests/models/quantization/test_gptq_marlin.py::test_models[5-32-bfloat16-model2]`

### Issue 正文摘录

### Name of failing test `tests/models/quantization/test_gptq_marlin.py::test_models[5-32-bfloat16-model2]` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test The test fails because the `gptq` backend is producing nans, which doesn't match the correct `gptq_marlin` backend ``` E AssertionError: Test0: E Matched tokens: [] E gptq: '' {0: Logprob(logprob=nan, rank=2, decoded_token=' '), 1: Logprob(logprob=nan, rank=1, decoded_token=' '), 2: Logprob(logprob=nan, rank=3, decoded_token=' '), 4: Logprob(logprob=nan, rank=4, decoded_token=' '), 3: Logprob(logprob=nan, rank=5, decoded_token=' ')} E gptq_marlin: '**Key features:**\n\n- **High-throughput inference:** Enables inference of LLMs at inference rates of up to 100 billion inferences per second.' {688: Logprob(logprob=-1.143240213394165, rank=1, decoded_token='**'), 1718: Logprob(logprob=-1.643240213394165, rank=2, decoded_token='It'), 235272: Logprob(logprob=-1.830740213394165, rank=3, decoded_token='v'), 651: Logprob(logprob=-2.830740213394165, rank=4, decoded_token='The'), 4471: Logprob(logprob=-2.955740213394165, rank...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: Quantized Models Test in `tests/models/quantization/test_gptq_marlin.py::test_models[5-32-bfloat16-model2]` ci-failure ### Name of failing test `tests/models/quantization/test_gptq_marlin.py::test_models[5-
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [CI Failure]: Quantized Models Test in `tests/models/quantization/test_gptq_marlin.py::test_models[5-32-bfloat16-model2]` ci-failure ### Name of failing test `tests/models/quantization/test_gptq_marlin.py::test_models[5...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [CI Failure]: Quantized Models Test in `tests/models/quantization/test_gptq_marlin.py::test_models[5-32-bfloat16-model2]` ci-failure ### Name of failing test `tests/models/quantization/test_gptq_marlin.py::test_models[5...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [CI Failure]: Quantized Models Test in `tests/models/quantization/test_gptq_marlin.py::test_models[5-32-bfloat16-model2]` ci-failure ### Name of failing test `tests/models/quantization/test_gptq_marlin.py::test_models[5...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rs`) ### 🧪 Describe the failing test The test fails because the `gptq` backend is producing nans, which doesn't match the correct `gptq_marlin` backend ``` E AssertionError: Test0: E Matched tokens: [] E gptq: '' {0: Lo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
