# vllm-project/vllm#4853: [Usage]: How to determine how many concurrent requests can be supported in an acceptable time duration with demo api server?

| 字段 | 值 |
| --- | --- |
| Issue | [#4853](https://github.com/vllm-project/vllm/issues/4853) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to determine how many concurrent requests can be supported in an acceptable time duration with demo api server?

### Issue 正文摘录

### Your current environment Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.4 LTS (x86_64) GCC version: (Ubuntu 11.2.0-19ubuntu1) 11.2.0 Clang version: Could not collect CMake version: version 3.27.9 Libc version: glibc-2.35 Python version: 3.11.0 (main, Mar 1 2023, 18:26:19) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.1.66 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA RTX 6000 Ada Generation GPU 1: NVIDIA RTX 6000 Ada Generation GPU 2: NVIDIA RTX 6000 Ada Generation GPU 3: NVIDIA RTX 6000 Ada Generation Nvidia driver version: 535.171.04 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: 架构： x86_64 CPU 运行模式： 32-bit, 64-bit 字节序： Little Endian Address sizes: 48 bits physical, 48 bits virtual CPU: 64 在线 CPU 列表： 0-63 每个核的线程数： 2 每个座的核数： 32 座： 1 NUMA 节点： 1 厂商 ID： AuthenticAMD CPU 系列： 25 型号： 8 型号名称： AMD Ryzen Threadripper PRO 5975WX 32-Cores 步进： 2 Frequency boost: enabled...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: Your current environment Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.4 LTS (x86_64) GCC vers...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: onment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.4 LTS (x86_64) GCC version: (Ubuntu 11.2.0-19ubuntu1) 11.2.0 Cla...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: rver? usage;stale ### Your current environment Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.4...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Usage]: How to determine how many concurrent requests can be supported in an acceptable time duration with demo api server? usage;stale ### Your current environment Collecting environment information... PyTorch version...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 2.1.2 [pip3] torchmetrics==1.3.0.post0 [pip3] torchvision==0.16.2 [pip3] triton==2.1.0 [conda] numpy 1.26.2 pypi_0 pypi [conda] nvidia-nccl-cu11 2.14.3 pypi_0 pypi [conda] nvidia-nccl-cu12 2.18.1

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
