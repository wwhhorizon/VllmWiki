# vllm-project/vllm#20192: [CI Failure]: Quantization Test - tests/quantization/test_fp8.py::test_scaled_fp8_quant

| 字段 | 值 |
| --- | --- |
| Issue | [#20192](https://github.com/vllm-project/vllm/issues/20192) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Quantization Test - tests/quantization/test_fp8.py::test_scaled_fp8_quant

### Issue 正文摘录

### Name of failing test `tests/quantization/test_fp8.py::test_scaled_fp8_quant` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test After https://github.com/vllm-project/vllm/pull/20076 fixed the assert to always check for per-tensor scales in the static scaled_fp8_quant case, this test `tests/quantization/test_fp8.py::test_scaled_fp8_quant` started failing https://buildkite.com/vllm/ci/builds/22749#0197ad88-59ca-41d0-9692-2bb3f5c6dca3 ### 📝 History of failing test After https://github.com/vllm-project/vllm/pull/20076 ### CC List. _No response_

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [CI Failure]: Quantization Test - tests/quantization/test_fp8.py::test_scaled_fp8_quant ci-failure ### Name of failing test `tests/quantization/test_fp8.py::test_scaled_fp8_quant` ### Basic information - [ ] Flaky test...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Quantization Test - tests/quantization/test_fp8.py::test_scaled_fp8_quant ci-failure ### Name of failing test `tests/quantization/test_fp8.py::test_scaled_fp8_quant` ### Basic information - [ ] Flaky test
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: est_scaled_fp8_quant` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test After https://github.com/vllm-proj...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: st `tests/quantization/test_fp8.py::test_scaled_fp8_quant` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: Quantization Test - tests/quantization/test_fp8.py::test_scaled_fp8_quant ci-failure ### Name of failing test `tests/quantization/test_fp8.py::test_scaled_fp8_quant` ### Basic information - [ ] Flaky test...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
