# vllm-project/vllm#43345: [CI Failure]: no logical_output_size in CutlassFP8ScaledMMLinearKernel

| 字段 | 值 |
| --- | --- |
| Issue | [#43345](https://github.com/vllm-project/vllm/issues/43345) |
| 状态 | open |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: no logical_output_size in CutlassFP8ScaledMMLinearKernel

### Issue 正文摘录

### Name of failing test tests/kernels/quantization/test_cutlass_scaled_mm.py::test_cutlass_fp8_gemm_padded ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Test fails for multiple sets of parameters with the message ``` AttributeError: 'CutlassFP8ScaledMMLinearKernel' object has no attribute 'logical_output_size' ``` ### 📝 History of failing test New nightly failure ### CC List. _No response_

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [CI Failure]: no logical_output_size in CutlassFP8ScaledMMLinearKernel ci-failure ### Name of failing test tests/kernels/quantization/test_cutlass_scaled_mm.py::test_cutlass_fp8_gemm_padded ### Basic information - [ ] F...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [CI Failure]: no logical_output_size in CutlassFP8ScaledMMLinearKernel ci-failure ### Name of failing test tests/kernels/quantization/test_cutlass_scaled_mm.py::test_cutlass_fp8_gemm_padded ### Basic information - [ ] F...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: tlass_fp8_gemm_padded ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Test fails for multiple sets of pa...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [CI Failure]: no logical_output_size in CutlassFP8ScaledMMLinearKernel ci-failure ### Name of failing test tests/kernels/quantization/test_cutlass_scaled_mm.py::test_cutlass_fp8_gemm_padded ### Basic information - [ ]
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ion/test_cutlass_scaled_mm.py::test_cutlass_fp8_gemm_padded ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
