# vllm-project/vllm#5732: [Bug]: asyncio.exceptions.CancelledError asyncio.exceptions.TimeoutError

| 字段 | 值 |
| --- | --- |
| Issue | [#5732](https://github.com/vllm-project/vllm/issues/5732) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: asyncio.exceptions.CancelledError asyncio.exceptions.TimeoutError

### Issue 正文摘录

### Your current environment Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 10 (buster) (x86_64) GCC version: (Debian 8.3.0-6) 8.3.0 Clang version: Could not collect CMake version: version 3.29.5 Libc version: glibc-2.28 Python version: 3.10.9 (main, Mar 1 2023, 18:23:06) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-78-generic-x86_64-with-glibc2.28 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A800-SXM4-80GB GPU 1: NVIDIA A800-SXM4-80GB GPU 2: NVIDIA A800-SXM4-80GB GPU 3: NVIDIA A800-SXM4-80GB Nvidia driver version: 525.125.06 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 46 bits physical, 57 bits virtual CPU(s): 128 On-line CPU(s) list: 0-127 Thread(s) per core: 2 Core(s) per socket: 32 Socket(s): 2 NUMA node(s): 2 Vendor ID: GenuineIntel CPU family: 6 Model: 106 Model name: Intel(R)...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Bug]: asyncio.exceptions.CancelledError asyncio.exceptions.TimeoutError bug;stale ### Your current environment Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: onment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 10 (buster) (x86_64) GCC version: (Debian 8.3.0-6) 8.3.0 Cla...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: utError bug;stale ### Your current environment Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Lin...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ansformers==3.0.1 [pip3] torch==2.3.0 [pip3] transformers==4.41.2 [pip3] triton==2.3.0 [conda] blas 1.0 mkl [conda] mkl 2021.4.0 h06a4308_640 [conda] mkl-service 2.4.0 py310h7f8727e_0 [c
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ]: asyncio.exceptions.CancelledError asyncio.exceptions.TimeoutError bug;stale ### Your current environment Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyT...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
