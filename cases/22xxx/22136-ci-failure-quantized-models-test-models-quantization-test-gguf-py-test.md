# vllm-project/vllm#22136: [CI Failure]: Quantized Models Test - models/quantization/test_gguf.py::test_models

| 字段 | 值 |
| --- | --- |
| Issue | [#22136](https://github.com/vllm-project/vllm/issues/22136) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Quantized Models Test - models/quantization/test_gguf.py::test_models

### Issue 正文摘录

### Name of failing test Quantized Models Test - models/quantization/test_gguf.py::test_models ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Error message: ``` | [2025-08-02T17:58:21Z] FAILED models/quantization/test_gguf.py::test_models[1-5-32-half-model0] - OSError: It looks like the config file at '/fsx/hf_cache/hub/models--Qwen--Qwen2.5-1.5B-Instruct-GGUF/snapshots/91cad51170dc346986eccefdc2dd33a9da36ead9/qwen2.5-1.5b-instruct-q6_k.gguf' is not a valid JSON file. | [2025-08-02T17:58:21Z] FAILED models/quantization/test_gguf.py::test_models[1-5-32-half-model1] - OSError: It looks like the config file at '/fsx/hf_cache/hub/models--bartowski--Phi-3.5-mini-instruct-GGUF/snapshots/6d70da17e749a471ccb62ade694486011a75cda3/Phi-3.5-mini-instruct-IQ4_XS.gguf' is not a valid JSON file. | [2025-08-02T17:58:21Z] FAILED models/quantization/test_gguf.py::test_models[1-5-32-half-model2] - OSError: It looks like the config file at '/fsx/hf_cache/hub/models--QuantFactory--gpt2-large-GGUF/snapshots/16ed8338c8e0d67ad6d47f776b2de9bf28338d27/gpt2-large.Q4_K_M.gguf' is not a valid JS...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [CI Failure]: Quantized Models Test - models/quantization/test_gguf.py::test_models ci-failure ### Name of failing test Quantized Models Test - models/quantization/test_gguf.py::test_models ### Basic information - [ ] F...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: _gguf.py::test_models ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Error message: ``` | [2025-08-02T1...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [CI Failure]: Quantized Models Test - models/quantization/test_gguf.py::test_models ci-failure ### Name of failing test Quantized Models Test - models/quantization/test_gguf.py::test_models ### Basic information - [ ]
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [CI Failure]: Quantized Models Test - models/quantization/test_gguf.py::test_models ci-failure ### Name of failing test Quantized Models Test - models/quantization/test_gguf.py::test_models ### Basic information - [ ] F...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: Quantized Models Test - models/quantization/test_gguf.py::test_models ci-failure ### Name of failing test Quantized Models Test - models/quantization/test_gguf.py::test_models ### Basic information - [ ] F...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
