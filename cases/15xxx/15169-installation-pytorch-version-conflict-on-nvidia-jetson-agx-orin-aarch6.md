# vllm-project/vllm#15169: [Installation]: PyTorch Version Conflict on NVIDIA Jetson AGX Orin (aarch64) with CUDA 12.6

| 字段 | 值 |
| --- | --- |
| Issue | [#15169](https://github.com/vllm-project/vllm/issues/15169) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: PyTorch Version Conflict on NVIDIA Jetson AGX Orin (aarch64) with CUDA 12.6

### Issue 正文摘录

### Your current environment I am using NVIDIA Jetson AGX Orin 64GB Developer Kit with CUDA 12.6 and Triton Server base Docker container. Here is my env: - Device: NVIDIA Jetson AGX Orin 64GB Developer Kit (aarch64 architecture) - Base Docker container: `nvcr.io/nvidia/tritonserver:24.12-py3` - Triton Server Version: 2.53.0 - CUDA Version: 12.6 Here is result of collect_env.py **after all steps taken to reproduce the issues**. ```text INFO 03-19 22:03:37 [__init__.py:256] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.6.0+cu126 Is debug build: False CUDA used to build PyTorch: 12.6 ROCM used to build PyTorch: N/A OS: Ubuntu 24.04.1 LTS (aarch64) GCC version: (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version: 18.1.3 (1ubuntu1) CMake version: Could not collect Libc version: glibc-2.39 Python version: 3.12.3 (main, Nov 6 2024, 18:32:19) [GCC 13.2.0] (64-bit runtime) Python platform: Linux-5.15.0-1013-nvidia-tegra-igx-aarch64-with-glibc2.39 Is CUDA available: True CUDA runtime version: 12.6.85 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Orin (nvgpu) Nvidia driver version: 540.4.0 cuDNN version: Probably one of...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Installation]: PyTorch Version Conflict on NVIDIA Jetson AGX Orin (aarch64) with CUDA 12.6 installation ### Your current environment I am using NVIDIA Jetson AGX Orin 64GB Developer Kit with CUDA 12.6 and Triton Server
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Installation]: PyTorch Version Conflict on NVIDIA Jetson AGX Orin (aarch64) with CUDA 12.6 installation ### Your current environment I am using NVIDIA Jetson AGX Orin 64GB Developer Kit with CUDA 12.6 and Triton Server...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: _.py:256] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.6.0+cu126 Is debug build: False CUDA used to build PyTorch: 12.6 ROCM used to build PyTorch: N/A OS: Ubuntu 24.04....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Not affected Vulnerability Spec store bypass: Mitigation; Sp...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: I am using NVIDIA Jetson AGX Orin 64GB Developer Kit with CUDA 12.6 and Triton Server base Docker container. Here is my env: - Device: NVIDIA Jetson AGX Orin 64GB Developer Kit (aarch64 architecture) - Base Docker conta...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
