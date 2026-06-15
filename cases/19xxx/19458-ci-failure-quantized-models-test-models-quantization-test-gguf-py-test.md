# vllm-project/vllm#19458: [CI Failure]: Quantized Models Test - models/quantization/test_gguf.py::test_models[1-5-32-half-model0]

| 字段 | 值 |
| --- | --- |
| Issue | [#19458](https://github.com/vllm-project/vllm/issues/19458) |
| 状态 | closed |
| 标签 | stale;ci-failure |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Quantized Models Test - models/quantization/test_gguf.py::test_models[1-5-32-half-model0]

### Issue 正文摘录

### Name of failing test `models/quantization/test_gguf.py::test_models[1-5-32-half-model0]` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test This specific Llama 1B GGUF model test has been failing consistently in multiple PRs https://buildkite.com/vllm/ci/builds/21800/steps/waterfall?jid=01975af4-f581-4d43-a1e5-7175d960b2b7#01975af4-f581-4d43-a1e5-7175d960b2b7/212-6971 ``` [2025-06-10T18:40:56Z] FAILED models/quantization/test_gguf.py::test_models[1-5-32-half-model0] - AssertionError: Test0: [2025-06-10T18:40:56Z] Matched tokens: [4897, 596, 4495, 13, 650, 4178, 44, 13656, 369] [2025-06-10T18:40:56Z] original: "That's correct. VLLM stands for Vision and Language Model, which is a type of large language model designed for both inference and serving. It's a" {31541: Logprob(logprob=-1.6094070672988892, rank=1, decoded_token='ĠVision'), 28968: Logprob(logprob=-2.0000319480895996, rank=2, decoded_token='ĠVari'), 8519: Logprob(logprob=-2.5000319480895996, rank=3, decoded_token='ĠVideo'), 21382: Logprob(logprob=-2.6562819480895996, rank=4, decoded_token='ĠVirtual'), 20796:...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [CI Failure]: Quantized Models Test - models/quantization/test_gguf.py::test_models[1-5-32-half-model0] stale;ci-failure ### Name of failing test `models/quantization/test_gguf.py::test_models[1-5-32-half-model0]` ### B...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Quantized Models Test - models/quantization/test_gguf.py::test_models[1-5-32-half-model0] stale;ci-failure ### Name of failing test `models/quantization/test_gguf.py::test_models[1-5-32-half-model0]` ### B
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Test - models/quantization/test_gguf.py::test_models[1-5-32-half-model0] stale;ci-failure ### Name of failing test `models/quantization/test_gguf.py::test_models[1-5-32-half-model0]` ### Basic information - [x] Flaky te...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [CI Failure]: Quantized Models Test - models/quantization/test_gguf.py::test_models[1-5-32-half-model0] stale;ci-failure ### Name of failing test `models/quantization/test_gguf.py::test_models[1-5-32-half-model0]` ### B...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [1-5-32-half-model0]` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test This specific Llama 1B GGUF model...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
