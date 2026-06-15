# vllm-project/vllm#4980: [Installation]: failed installation with pip

| 字段 | 值 |
| --- | --- |
| Issue | [#4980](https://github.com/vllm-project/vllm/issues/4980) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: failed installation with pip

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 8.4.0-3ubuntu2) 8.4.0 Clang version: Could not collect CMake version: version 3.16.3 Libc version: glibc-2.31 Python version: 3.9.19 (main, May 6 2024, 19:43:03) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-106-generic-x86_64-with-glibc2.31 Is CUDA available: N/A CUDA runtime version: 12.2.140 CUDA_MODULE_LOADING set to: N/A GPU models and configuration: GPU 0: Quadro RTX 8000 GPU 1: Quadro RTX 8000 Nvidia driver version: 535.161.08 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: N/A CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 46 bits physical, 48 bits virtual CPU(s): 72 On-line CPU(s) list: 0-71 Thread(s) per core: 2 Core(s) per socket: 18 Socket(s): 2 NUMA node(s): 2 Vendor ID: GenuineIntel CPU family: 6 Model: 85 Model name: Intel(R) Xeon(R) Gold 6240 CPU @ 2.60GHz Stepping: 7 CPU MHz: 2600.000 CPU max MHz: 3900.0000 CPU m...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Installation]: failed installation with pip installation ### Your current environment ```text Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to b
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: ting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 8.4.0-3ubuntu2) 8.4.0 Clang v...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: tallation ### Your current environment ```text Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_6...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: cies ... done Getting requirements to build wheel ... done Preparing metadata (pyproject.toml) ... done Collecting cmake>=3.21 (from vllm) Using cached cmake-3.29.3-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: on3.12/site-packages (from vllm) (1.26.4) Requirement already satisfied: requests in /opt/conda/lib/python3.12/site-packages (from vllm) (2.31.0) Collecting py-cpuinfo (from vllm) Using cached py_cpuinfo-9.0.0-py3-none-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
