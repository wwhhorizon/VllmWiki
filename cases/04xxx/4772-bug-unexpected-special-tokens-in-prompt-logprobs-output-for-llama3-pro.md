# vllm-project/vllm#4772: [Bug]: Unexpected Special Tokens in prompt_logprobs Output for Llama3 Prompt

| 字段 | 值 |
| --- | --- |
| Issue | [#4772](https://github.com/vllm-project/vllm/issues/4772) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unexpected Special Tokens in prompt_logprobs Output for Llama3 Prompt

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: version 3.29.0 Libc version: glibc-2.31 Python version: 3.8.19 (default, Mar 20 2024, 19:58:24) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.4.0-162-generic-x86_64-with-glibc2.17 Is CUDA available: True CUDA runtime version: 11.6.124 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A40 GPU 1: NVIDIA A40 GPU 2: NVIDIA A40 GPU 3: NVIDIA A40 GPU 4: NVIDIA A40 GPU 5: NVIDIA A40 GPU 6: NVIDIA A40 GPU 7: NVIDIA A40 Nvidia driver version: 525.105.17 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 52 bits physical, 57 bits virtual CPU(s): 128 On-line CPU(s) list: 0-127 Thread(s) per core: 2 Core(s) per socket: 32 Socket(s): 2 NUMA node(s): 2 Vendor ID: GenuineIntel CPU fami...

## 现有链接修复摘要

#6223 [ BugFix ] Prompt Logprobs Detokenization

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug]: Unexpected Special Tokens in prompt_logprobs Output for Llama3 Prompt bug ### Your current environment ```text The output of `python collect_env.py` ``` PyTorch version: 2.3.0+cu121 Is debug build: False CUDA use...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: n collect_env.py` ``` PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Unexpected Special Tokens in prompt_logprobs Output for Llama3 Prompt bug ### Your current environment ```text The output of `python collect_env.py` ``` PyTorch version: 2.3.0+cu121 Is debug build: False CUDA use...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Mitigation; Clear CPU buffers; SMT vulnerable Vulnerability Retbleed: Not affected Vulnerability Spec store bypass: Mitigation; Speculative Store...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rch==2.3.0 [pip3] torch_geometric==2.5.2 [pip3] torchaudio==2.3.0 [pip3] triton==2.3.0 [pip3] vllm-nccl-cu12==2.18.1.0.4.0 [conda] numpy 1.24.4 pypi_0 pypi [conda] nvidia-nccl-cu12 2.20.5 pypi_0 pypi [conda] torch

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#6223](https://github.com/vllm-project/vllm/pull/6223) | closes_keyword | 0.95 | [ BugFix ] Prompt Logprobs Detokenization | FIX #4772 FIX #5334 FIX #5872 **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <details> <!-- inside this <details> section |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
