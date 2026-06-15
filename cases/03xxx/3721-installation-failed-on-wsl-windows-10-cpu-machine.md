# vllm-project/vllm#3721: [Installation]: failed on WSL windows 10 CPU machine

| 字段 | 值 |
| --- | --- |
| Issue | [#3721](https://github.com/vllm-project/vllm/issues/3721) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: failed on WSL windows 10 CPU machine

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Ubuntu 20.04 LTS (x86_64) GCC version: (Ubuntu 9.3.0-10ubuntu2) 9.3.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.31 Python version: 3.8.2 (default, Mar 13 2020, 10:14:16) [GCC 9.3.0] (64-bit runtime) Python platform: Linux-5.10.16.3-microsoft-standard-WSL2-x86_64-with-glibc2.29 Is CUDA available: N/A CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: N/A GPU models and configuration: Could not collect Nvidia driver version: Could not collect cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: N/A CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 39 bits physical, 48 bits virtual CPU(s): 8 On-line CPU(s) list: 0-7 Thread(s) per core: 2 Core(s) per socket: 4 Socket(s): 1 Vendor ID: GenuineIntel CPU family: 6 Model: 140 Model name: 11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz Stepping: 1 CPU MHz:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Installation]: failed on WSL windows 10 CPU machine installation ### Your current environment ```text The output of `python collect_env.py` ``` Collecting environment information... PyTorch version: N/A Is debug build:
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Ubuntu 20.04 LTS (x86_64) GCC version: (Ubuntu 9.3.0-10ubuntu2) 9.3.0 Clang ve...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: `text The output of `python collect_env.py` ``` Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Ubuntu 20.04 LTS (x86_64...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: down: Not affected Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl and seccomp Vulnerability Spectre v1: Mitigation; usercopy/swapgs barriers and __user pointer sanitization Vuln...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
