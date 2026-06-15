# vllm-project/vllm#33153: [CI Failure]: Blackwell Test failed for cudaErrorDevicesUnavailable

| 字段 | 值 |
| --- | --- |
| Issue | [#33153](https://github.com/vllm-project/vllm/issues/33153) |
| 状态 | closed |
| 标签 | stale;ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;quantization |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;quantization |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: Blackwell Test failed for cudaErrorDevicesUnavailable

### Issue 正文摘录

### Name of failing test tests/kernels/quantization/test_cutlass_scaled_mm.py ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test https://buildkite.com/vllm/ci/builds/48532/steps/canvas?sid=019bfb99-f4a9-4df1-8782-b3bd4df7f19f ``` > a = to_fp8(torch.randn((m, k), device=device)) -- E torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable E Search for `cudaErrorDevicesUnavailable' in https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__TYPES.html for more information. E CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect. E For debugging consider passing CUDA_LAUNCH_BLOCKING=1 E Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. tests/kernels/quantization/test_cutlass_scaled_mm.py:80: AcceleratorError ``` Another test failure with `cudaErrorDevicesUnavailable` in https://buildkite.com/vllm/ci/builds/48537/steps/canvas?sid=019bfbb4-382c-4d65-9b5b-bd8d0d00f25b `Blackwell Fusion and Compile Tests` https://github.com/vllm-project/vllm/pull/32224#issuecomme...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [CI Failure]: Blackwell Test failed for cudaErrorDevicesUnavailable stale;ci-failure ### Name of failing test tests/kernels/quantization/test_cutlass_scaled_mm.py ### Basic information - [x] Flaky test - [ ] Can reprod
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [CI Failure]: Blackwell Test failed for cudaErrorDevicesUnavailable stale;ci-failure ### Name of failing test tests/kernels/quantization/test_cutlass_scaled_mm.py ### Basic information - [x] Flaky test - [ ] Can reprodu...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: icesUnavailable stale;ci-failure ### Name of failing test tests/kernels/quantization/test_cutlass_scaled_mm.py ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g....
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: _cutlass_scaled_mm.py ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test https://buildkite.com/vllm/ci/buil...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: test tests/kernels/quantization/test_cutlass_scaled_mm.py ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing tes...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
