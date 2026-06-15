# vllm-project/vllm#29599: [Bug]: Tests failure for PrithviMAE model

| 字段 | 值 |
| --- | --- |
| Issue | [#29599](https://github.com/vllm-project/vllm/issues/29599) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Tests failure for PrithviMAE model

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Prithvi MAE related tests are failing on main locally but on CI they seem to pass. ``` pytest tests/models/test_initialization.py::test_can_initialize_small_subset[PrithviGeoSpatialMAE] ``` ``` pytest tests/models/multimodal/pooling/test_prithvi_mae.py::test_models_image[mgazz/Prithvi-EO-2.0-300M-TL-Sen1Floods11] ``` Output ``` ... File ".../python3.12/site-packages/torch/nn/modules/conv.py", line 712, in _conv_forward return F.conv3d( ^^^^^^^^^ torch.AcceleratorError: CUDA error: device-side assert triggered Search for `cudaErrorAssert' in https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__TYPES.html for more information. CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect. [0;36m(EngineCore_DP0 pid=2283430)[0;0m 2025-11-27 09:46:31,105 - INFO - autotuner.py:256 - flashinfer.jit: [Autotuner]: Autotuning process starts ... [0;36m(EngineCore_DP0 pid=2283430)[0;0m 2025-11-27 09:46:31,720 - INFO - autotuner.py:262 - flashinfer.jit: [Autotuner]: Autotuning process ends /pytorch/aten/src/ATen/native/cuda/IndexKernelUtils.cu:16: vectorized_gather_kernel: b...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Tests failure for PrithviMAE model bug ### Your current environment ### 🐛 Describe the bug Prithvi MAE related tests are failing on main locally but on CI they seem to pass. ``` pytest tests/models/test_initializ...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: be the bug Prithvi MAE related tests are failing on main locally but on CI they seem to pass. ``` pytest tests/models/test_initialization.py::test_can_initialize_small_subset[PrithviGeoSpatialMAE] ``` ``` pytest tests/m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ss. ``` pytest tests/models/test_initialization.py::test_can_initialize_small_subset[PrithviGeoSpatialMAE] ``` ``` pytest tests/models/multimodal/pooling/test_prithvi_mae.py::test_models_image[mgazz/Prithvi-EO-2.0-300M-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 0 pid=2283430)[0;0m 2025-11-27 09:46:31,105 - INFO - autotuner.py:256 - flashinfer.jit: [Autotuner]: Autotuning process starts ... [0;36m(EngineCore_DP0 pid=2283430)[0;0m 2025-11-27 09:46:31,720 - INFO - autotuner.py...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: n/src/ATen/native/cuda/IndexKernelUtils.cu:16: vectorized_gather_kernel: block: [12,3,0], thread: [128,0,0] Assertion `ind >=0 && ind =0 && ind =0 && ind =0 && ind =0 && ind =0 && ind =0 && ind =0 && ind =0 && ind < ind...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
