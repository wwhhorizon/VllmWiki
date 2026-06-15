# vllm-project/vllm#5177: [Bug]: Incorrect Example for the Inference with Prefix 

| 字段 | 值 |
| --- | --- |
| Issue | [#5177](https://github.com/vllm-project/vllm/issues/5177) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Incorrect Example for the Inference with Prefix 

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.29.3 Libc version: glibc-2.35 Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.15.0-97-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.2.140 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100 80GB PCIe GPU 1: NVIDIA A100 80GB PCIe GPU 2: NVIDIA A100 80GB PCIe GPU 3: NVIDIA A100 80GB PCIe Nvidia driver version: 535.161.07 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 48 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 48 On-line CPU(s) list: 0-47 Vendor ID: AuthenticAMD Model name: AMD EPYC 7443 24-Core Processor CPU family: 25 Model: 1 Thread(s) per core: 1 Core(s) per socket: 24 Socket(s): 2 Stepping: 1 Frequency boost:...

## 现有链接修复摘要

#5180 [Bugfix]: Fix issues related to prefix caching example (#5177)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: Inference with Prefix bug ### Your current environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC vers...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: True CUDA runtime version: 12.2.140 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100 80GB PCIe GPU 1: NVIDIA A100 80GB PCIe GPU 2: NVIDIA A100 80GB PCIe GPU 3: NVIDIA A100 80GB PCIe Nvid...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: d_ppin arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold v_vmsave_vmload vgif v_spec_ctrl umip pku ospke vaes vpclmulqdq rdpid overflow_recov succor smca Virtualizat...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: rt LLM, SamplingParams from time import time prefix = ( "You are an expert school principal, skilled in effectively managing " "faculty and staff. Draft 10-15 questions for a potential first grade " "Head Teacher for my...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#5180](https://github.com/vllm-project/vllm/pull/5180) | closes_keyword | 0.95 | [Bugfix]: Fix issues related to prefix caching example (#5177) | FIX #5177 This PR fixes two issues of [prefix inference example](https://github.com/vllm-project/vllm/blob/main/examples/offline_inference_with_prefix.py) described in the afor |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
