# vllm-project/vllm#7262: [Bug]: stream_options.include_usage being retrieved on every chunk

| 字段 | 值 |
| --- | --- |
| Issue | [#7262](https://github.com/vllm-project/vllm/issues/7262) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: stream_options.include_usage being retrieved on every chunk

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.5.0.dev20240726+rocm6.1 Is debug build: False CUDA used to build PyTorch: N/A ROCM used to build PyTorch: 6.1.40091-a8dbc0c19 OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: 17.0.0 (https://github.com/RadeonOpenCompute/llvm-project roc-6.1.2 24193 669db884972e769450470020c06a6f132a8a065b) CMake version: version 3.30.2 Libc version: glibc-2.31 Python version: 3.9.19 (main, May 6 2024, 19:43:03) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-117-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: AMD Instinct MI100 (gfx908:sramecc+:xnack-) Nvidia driver version: Could not collect cuDNN version: Could not collect HIP runtime version: 6.1.40093 MIOpen runtime version: 3.1.0 Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 48 bits physical, 48 bits virtual CPU(s): 16 On-line CPU(s) list: 0-15 Thread(s) per core: 1 Core(s) per socket: 16 Socket(s): 1 NUMA node(s): 1 Vendor ID: AuthenticAMD CP...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: trieved on every chunk bug ### Your current environment ```text PyTorch version: 2.5.0.dev20240726+rocm6.1 Is debug build: False CUDA used to build PyTorch: N/A ROCM used to build PyTorch: 6.1.40091-a8dbc0c19 OS: Ubuntu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ### Your current environment ```text PyTorch version: 2.5.0.dev20240726+rocm6.1 Is debug build: False CUDA used to build PyTorch: N/A ROCM used to build PyTorch: 6.1.40091-a8dbc0c19 OS: Ubuntu 20.04.6 LTS (x86_64) GCC v...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: AMD Instinct MI100 (gfx908:sramecc+:xnack-) Nvidia driver version: Could not collect cuDNN version: Could not collect HIP...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ed Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Reg file data sampling: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Mitigation;...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: tensions==1.0.0 [pip3] numpy==1.26.4 [pip3] optree==0.9.1 [pip3] pytorch-triton-rocm==3.0.0+21eae954ef [pip3] pyzmq==26.1.0 [pip3] torch==2.5.0.dev20240726+rocm6.1 [pip3] torchvision==0.20.0.dev20240726+rocm6.1 [pip3] t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
