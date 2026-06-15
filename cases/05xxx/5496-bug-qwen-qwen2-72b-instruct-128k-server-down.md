# vllm-project/vllm#5496: [Bug]: Qwen/Qwen2-72B-Instruct 128k server down 

| 字段 | 值 |
| --- | --- |
| Issue | [#5496](https://github.com/vllm-project/vllm/issues/5496) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen/Qwen2-72B-Instruct 128k server down 

### Issue 正文摘录

### Your current environment PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu Jammy Jellyfish (development branch) (x86_64) GCC version: Could not collect Clang version: Could not collect CMake version: version 3.29.5 Libc version: glibc-2.35 Python version: 3.10.14 (main, May 6 2024, 19:42:50) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.10.134-15.al8.x86_64-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L20 GPU 1: NVIDIA L20 GPU 2: NVIDIA L20 GPU 3: NVIDIA L20 GPU 4: NVIDIA L20 GPU 5: NVIDIA L20 GPU 6: NVIDIA L20 GPU 7: NVIDIA L20 Nvidia driver version: 535.161.07 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 52 bits physical, 57 bits virtual Byte Order: Little Endian CPU(s): 128 On-line CPU(s) list: 0-127 Vendor ID: GenuineIntel Model name: Intel(R) Xeon(R) Gold 6462C CPU family: 6 Model: 143 Thread(s) per core: 2 Core(s) per socket: 32 Sock...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: struct 128k server down bug;stale ### Your current environment PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu Jammy Jellyfish (development...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: current environment PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu Jammy Jellyfish (development branch) (x86_64) GCC version: Could not col...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen/Qwen2-72B-Instruct 128k server down bug;stale ### Your current environment PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu Jammy...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: nccl-cu12==2.20.5 [pip3] torch==2.3.0 [pip3] transformers==4.41.2 [pip3] triton==2.3.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-nccl-cu12 2.20.5 pypi_0 pypi [conda] torch 2.3.0
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Qwen/Qwen2-72B-Instruct 128k server down bug;stale ### Your current environment PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu Jammy...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
