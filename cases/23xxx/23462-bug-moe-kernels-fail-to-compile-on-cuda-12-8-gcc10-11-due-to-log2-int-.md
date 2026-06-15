# vllm-project/vllm#23462: [Bug]:MOE kernels fail to compile on CUDA 12.8 (GCC10/11) due to log2(int) overload ambiguity

| 字段 | 值 |
| --- | --- |
| Issue | [#23462](https://github.com/vllm-project/vllm/issues/23462) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;moe |
| 子分类 | env_compat |
| Operator 关键词 | cuda;kernel;moe |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:MOE kernels fail to compile on CUDA 12.8 (GCC10/11) due to log2(int) overload ambiguity

### Issue 正文摘录

## Problem Summary When building vLLM from source with CUDA 12.8 and GCC 10/11, the build fails during compilation of the Mixture of Experts (MOE) CUDA kernels. This prevents vLLM from completing installation and loading GPU-accelerated extensions. The failure occurs at build-time, before any models can be run. ## Environment * **System**: Cloud GPU instance with NVIDIA A100-SXM4-40GB * **OS**: Ubuntu 22.04 LTS * **CUDA Version**: 12.8 * **PyTorch Version**: 2.7.1 (pip, cu128) * **Python Version**: 3.10.12 * **GCC Version**: 10.5.0 (also tried GCC 11) * **vLLM Version**: Latest v1 snapshot from main (`0.10.2.dev113+g26d1ec60b.d20250821`) * **CMake Version**: 4.1 ## Reproducibility Instructions Fresh Instance. ```bash # Update system sudo apt-get update && sudo apt-get upgrade -y # Verify CUDA installation nvidia-smi # Expect CUDA Version: 12.8 nvcc --version # Expect release 12.8 # Install system dependencies sudo apt-get install -y \ git python3.10 python3.10-venv python3.10-dev \ build-essential ninja-build # Clone vLLM repository cd ~ git clone https://github.com/vllm-project/vllm.git cd vllm # Create virtual environment python3.10 -m venv .venv source .venv/bin/activate # Upgr...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug]:MOE kernels fail to compile on CUDA 12.8 (GCC10/11) due to log2(int) overload ambiguity bug;stale ## Problem Summary When building vLLM from source with CUDA 12.8 and GCC 10/11, the build fails during compilation...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]:MOE kernels fail to compile on CUDA 12.8 (GCC10/11) due to log2(int) overload ambiguity bug;stale ## Problem Summary When building vLLM from source with CUDA 12.8 and GCC 10/11, the build fails during compilation...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: [Bug]:MOE kernels fail to compile on CUDA 12.8 (GCC10/11) due to log2(int) overload ambiguity bug;stale ## Problem Summary When building vLLM from source with CUDA 12.8 and GCC 10/11, the build fails during compilation...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: GPU-accelerated extensions. The failure occurs at build-time, before any models can be run. ## Environment * **System**: Cloud GPU instance with NVIDIA A100-SXM4-40GB * **OS**: Ubuntu 22.04 LTS * **CUDA Version**: 12.8...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: compile on CUDA 12.8 (GCC10/11) due to log2(int) overload ambiguity bug;stale ## Problem Summary When building vLLM from source with CUDA 12.8 and GCC 10/11, the build fails during compilation of the Mixture of Experts...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
