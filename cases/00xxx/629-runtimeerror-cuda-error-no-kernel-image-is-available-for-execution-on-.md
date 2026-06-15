# vllm-project/vllm#629: RuntimeError: CUDA error: no kernel image is available for execution on the device

| 字段 | 值 |
| --- | --- |
| Issue | [#629](https://github.com/vllm-project/vllm/issues/629) |
| 状态 | closed |
| 标签 |  |
| 评论 | 33; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api |
| 子分类 |  |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> RuntimeError: CUDA error: no kernel image is available for execution on the device

### Issue 正文摘录

Error: RuntimeError: CUDA error: no kernel image is available for execution on the device CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1. Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. nvcc -V Copyright (c) 2005-2022 NVIDIA Corporation Built on Tue_May__3_18:49:52_PDT_2022 Cuda compilation tools, release 11.7, V11.7.64 Build cuda_11.7.r11.7/compiler.31294372_0 conda list: cudatoolkit-dev 11.7.0 cudatoolkit 11.7.0 torch 2.0.1+cu117 nvidia-smi A100 80G NVIDIA-SMI 470.141.03 Driver Version: 470.141.03 CUDA Version: 11.4 how to solve this problem? thanks!

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ght be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1. Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. nvcc -V Copyright (c) 2005-2022 NVIDIA Corporation Built on Tue_May__3_18:49:5...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: RuntimeError: CUDA error: no kernel image is available for execution on the device Error: RuntimeError: CUDA error: no kernel image is available for execution on the device CUDA kernel errors might be asynchronously rep...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: oblem? thanks! correctness ci_build;frontend_api cuda;kernel build_error;mismatch env_dependency Error:
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ace below might be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1. Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. nvcc -V Copyright (c) 2005-2022 NVIDIA Corporation Built on Tue_Ma...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
