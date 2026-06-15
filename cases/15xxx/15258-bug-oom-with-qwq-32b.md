# vllm-project/vllm#15258: [Bug]: OOM with QwQ-32B

| 字段 | 值 |
| --- | --- |
| Issue | [#15258](https://github.com/vllm-project/vllm/issues/15258) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: OOM with QwQ-32B

### Issue 正文摘录

### Your current environment The output of `python collect_env.py` ```INFO 03-21 08:37:46 [__init__.py:256] Automatically detected platform cpu. Collecting environment information... PyTorch version: 2.6.0+cpu Is debug build: False CUDA used to build PyTorch: Could not collect ROCM used to build PyTorch: N/A OS: Ubuntu 24.04.2 LTS (x86_64) GCC version: (Ubuntu 12.3.0-17ubuntu1) 12.3.0 Clang version: 18.1.3 (1ubuntu1) CMake version: version 3.31.6 Libc version: glibc-2.39 Python version: 3.12.9 | packaged by Anaconda, Inc. | (main, Feb 6 2025, 18:56:27) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-6.8.0-55-generic-x86_64-with-glibc2.39 Is CUDA available: False CUDA runtime version: 12.0.140 CUDA_MODULE_LOADING set to: N/A GPU models and configuration: GPU 0: NVIDIA GeForce RTX 3060 Nvidia driver version: 560.35.05 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 88 On-line CPU(s) list: 0-87 Vendor ID: GenuineIntel Model name: Intel(R) Xeon(R) CPU E5-2696 v4 @ 2.20GHz CPU fa...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: lly detected platform cpu. Collecting environment information... PyTorch version: 2.6.0+cpu Is debug build: False CUDA used to build PyTorch: Could not collect ROCM used to build PyTorch: N/A OS: Ubuntu 24.04.2 LTS (x86...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: ironment information... PyTorch version: 2.6.0+cpu Is debug build: False CUDA used to build PyTorch: Could not collect ROCM used to build PyTorch: N/A OS: Ubuntu 24.04.2 LTS (x86_64) GCC version: (Ubuntu 12.3.0-17ubuntu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: __.py:256] Automatically detected platform cpu. Collecting environment information... PyTorch version: 2.6.0+cpu Is debug build: False CUDA used to build PyTorch: Could not collect ROCM used to build PyTorch: N/A OS: Ub...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Vulnerability Meltdown: Mitigation; PTI Vulnerability Mmio stale data: Mitigation; Clear CPU buffers; SMT vulnerable Vulnerability Reg file data sampling: Not affected Vulnerability Retbleed: Not affected Vulnerability...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: u [pip3] torchvision==0.21.0+cpu [pip3] transformers==4.50.0.dev0 [pip3] triton==3.2.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] pyzmq 26.3.0 pypi_0 pypi [conda] torch 2.6.0+cpu

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
