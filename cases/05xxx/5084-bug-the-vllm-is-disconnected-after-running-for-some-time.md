# vllm-project/vllm#5084: [Bug]: The vllm is disconnected after running for some time

| 字段 | 值 |
| --- | --- |
| Issue | [#5084](https://github.com/vllm-project/vllm/issues/5084) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 29; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting |
| 子分类 | env_compat |
| Operator 关键词 | cuda;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: The vllm is disconnected after running for some time

### Issue 正文摘录

### Your current environment PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.2 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0 Clang version: Could not collect CMake version: version 3.29.3 Libc version: glibc-2.31 Python version: 3.8.19 (default, Mar 20 2024, 19:58:24) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.8.0-43-generic-x86_64-with-glibc2.17 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A800 80GB PCIe GPU 1: NVIDIA A800 80GB PCIe Versions of relevant libraries: [pip3] numpy==1.24.4 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] torch==2.3.0 [pip3] triton==2.3.0 [pip3] vllm_nccl_cu12==2.18.1.0.4.0 [conda] numpy 1.24.4 pypi_0 pypi [conda] nvidia-nccl-cu12 2.20.5 pypi_0 pypi [conda] torch 2.3.0 pypi_0 pypi [conda] triton 2.3.0 pypi_0 pypi [conda] vllm-nccl-cu12 2.18.1.0.4.0 pypi_0 pypiROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.4.2 vLLM Build Flags: CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled ### 🐛 Describe the bug Error executing method start...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ed after running for some time bug ### Your current environment PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.2 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: current environment PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.2 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: Your current environment PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.2 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A800 80GB PCIe GPU 1: NVIDIA A800 80GB PCIe Versions of relevant libraries: [pip3] numpy==1.24.4 [pip3] nvi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ug Error executing method start_worker_execution_loop. This might cause deadlock in distributed execution. [36m(RayWorkerWrapper pid=3957362)[0m ERROR 05-28 16:05:41 worker_base.py:146] Traceback (most recent call las...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
