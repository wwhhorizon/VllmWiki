# vllm-project/vllm#7349: [Bug]: internvl2-8b提问无限循环

| 字段 | 值 |
| --- | --- |
| Issue | [#7349](https://github.com/vllm-project/vllm/issues/7349) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: internvl2-8b提问无限循环

### Issue 正文摘录

### Your current environment 环境信息 wsl2 ubuntu22.04 Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.30.2 Libc version: glibc-2.35 Python version: 3.11.9 (main, Apr 19 2024, 16:48:06) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.153.1-microsoft-standard-WSL2-x86_64-with-glibc2.35 Is CUDA available: False CUDA runtime version: 12.1.66 CUDA_MODULE_LOADING set to: N/A GPU models and configuration: Could not collect Nvidia driver version: Could not collect cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 48 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 16 On-line CPU(s) list: 0-15 Vendor ID: AuthenticAMD Model name: AMD Ryzen 7 5700X 8-Core Processor CPU family: 25 Model: 33 Thread(s) per core: 2 Core(s) per socket: 8 Socket(s): 1 Stepping: 2 BogoMIPS: 6787.23 Flags: fpu vme de p...

## 现有链接修复摘要

#7354 [VLM][Doc] Add `stop_token_ids` to InternVL example

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: 环境信息 wsl2 ubuntu22.04 Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: internvl2-8b提问无限循环 bug ### Your current environment 环境信息 wsl2 ubuntu22.04 Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to bui...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: onment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Mitigation; safe RET, no microcode Vulnerability Spec store...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rch==2.4.0 [pip3] torchvision==0.19.0 [pip3] transformers==4.44.0 [pip3] triton==3.0.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-nccl-cu12 2.20.5 pypi_0 pypi [conda] pyzmq 26.1.0

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#7354](https://github.com/vllm-project/vllm/pull/7354) | closes_keyword | 0.95 | [VLM][Doc] Add `stop_token_ids` to InternVL example | FIX #7349 (*link existing issues this PR will resolve*) **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <details> <!-- inside |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
