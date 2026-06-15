# vllm-project/vllm#10319: [Installation]: Request to include vllm==0.6.2 for cuda 11.8

| 字段 | 值 |
| --- | --- |
| Issue | [#10319](https://github.com/vllm-project/vllm/issues/10319) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Request to include vllm==0.6.2 for cuda 11.8

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py`: Collecting environment information... PyTorch version: 2.4.0+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Rocky Linux release 8.6 (Green Obsidian) (x86_64) GCC version: (GCC) 8.5.0 20210514 (Red Hat 8.5.0-10) Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.28 Python version: 3.10.15 (main, Oct 3 2024, 07:27:34) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-4.18.0-372.9.1.el8.x86_64-x86_64-with-glibc2.28 Is CUDA available: True CUDA runtime version: 11.8.89 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Tesla V100-PCIE-32GB GPU 1: Tesla V100-PCIE-32GB Nvidia driver version: 515.105.01 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian CPU(s): 52 On-line CPU(s) list: 0-51 Thread(s) per core: 1 Core(s) per socket: 26 Socket(s): 2 NUMA node(s): 2 Vendor ID: GenuineIntel CPU family: 6 Model: 85 Model name: Intel(R) Xeon(R) Gold 6230R CPU @ 2.10GHz S...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Installation]: Request to include vllm==0.6.2 for cuda 11.8 installation;stale ### Your current environment ```text The output of `python collect_env.py`: Collecting environment information... PyTorch version: 2.4.0+cu1
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Installation]: Request to include vllm==0.6.2 for cuda 11.8 installation;stale ### Your current environment ```text The output of `python collect_env.py`: Collecting environment information... PyTorch version: 2.4.0+cu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ```text The output of `python collect_env.py`: Collecting environment information... PyTorch version: 2.4.0+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Rocky Linux re...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Installation]: Request to include vllm==0.6.2 for cuda 11.8 installation;stale ### Your current environment ```text The output of `python collect_env.py`: Collecting environment information... PyTorch version: 2.4.0+cu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: u118 [pip3] torchvision==0.19.0+cu118 [pip3] transformers==4.46.2 [pip3] triton==3.0.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-cublas-cu11 11.11.3.6 pypi_0 pypi [conda] nvidia-cuda-cupti-cu11 11.8.87

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
