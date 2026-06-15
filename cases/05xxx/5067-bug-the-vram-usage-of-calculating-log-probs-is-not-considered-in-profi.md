# vllm-project/vllm#5067: [Bug]: The VRAM usage of calculating log_probs is not considered in profile run

| 字段 | 值 |
| --- | --- |
| Issue | [#5067](https://github.com/vllm-project/vllm/issues/5067) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: The VRAM usage of calculating log_probs is not considered in profile run

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.29.3 Libc version: glibc-2.35 Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-6.9.1-arch1-1-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.4.131 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 4070 Ti SUPER Nvidia driver version: 550.78 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 24 On-line CPU(s) list: 0-23 Vendor ID: GenuineIntel Model name: 13th Gen Intel(R) Core(TM) i7-13700K CPU family: 6 Model: 183 Thread(s) per core: 2 Core(s) per socket: 16 Socket(s): 1 Stepping: 1 CPU max MHz: 5400....

## 现有链接修复摘要

#5355 [Bugfix] Take the VRAM usage of prompt_logprobs into account

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: f `python collect_env.py` Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ```text The output of `python collect_env.py` Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: nvironment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 1...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: VRAM usage of calculating log_probs is not considered in profile run bug;stale ### Your current environment ```text The output of `python collect_env.py` Collecting environment information... PyTorch version: 2.3.0+cu12...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#5355](https://github.com/vllm-project/vllm/pull/5355) | closes_keyword | 0.95 | [Bugfix] Take the VRAM usage of prompt_logprobs into account | FIX #5067 FIX #1532 FIX #5147 FIX #5274 FIX #5550 --- <details> <!-- inside this <details> section, markdown rendering does not work, so we use raw html here. --> <summ |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
