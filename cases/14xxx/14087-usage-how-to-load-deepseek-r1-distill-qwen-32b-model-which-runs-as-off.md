# vllm-project/vllm#14087: [Usage]: How to load DeepSeek-R1-Distill-Qwen-32B model which runs as offline batch inference

| 字段 | 值 |
| --- | --- |
| Issue | [#14087](https://github.com/vllm-project/vllm/issues/14087) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to load DeepSeek-R1-Distill-Qwen-32B model which runs as offline batch inference

### Issue 正文摘录

### Your current environment I want to run DeepSeek-R1-Distill-Qwen-32B model as offline batch inference. I only have CPUs (no GPU). I also need to provide Hugging Face cache directory, Hugging Face token, and max tokens. Could you please provide a sample of how to put those parameters in LLM class or its initialize function? ```text The output of `python collect_env.py` INFO 03-01 20:14:34 __init__.py:183] Automatically detected platform cpu. Collecting environment information... PyTorch version: 2.5.1+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 24.04.1 LTS (x86_64) GCC version: (Ubuntu 12.3.0-17ubuntu1) 12.3.0 Clang version: Could not collect CMake version: version 3.31.4 Libc version: glibc-2.39 Python version: 3.12.3 (main, Feb 4 2025, 14:48:35) [GCC 13.3.0] (64-bit runtime) Python platform: Linux-5.15.167.4-microsoft-standard-WSL2-x86_64-with-glibc2.39 Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Archite...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: lly detected platform cpu. Collecting environment information... PyTorch version: 2.5.1+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 24.04.1 LTS (x86_64) GCC vers...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ironment information... PyTorch version: 2.5.1+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 24.04.1 LTS (x86_64) GCC version: (Ubuntu 12.3.0-17ubuntu1) 12.3.0 Cla...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: How to load DeepSeek-R1-Distill-Qwen-32B model which runs as offline batch inference usage;stale ### Your current environment I want to run DeepSeek-R1-Distill-Qwen-32B model as offline batch inference. I only...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ek-R1-Distill-Qwen-32B model which runs as offline batch inference usage;stale ### Your current environment I want to run DeepSeek-R1-Distill-Qwen-32B model as offline batch inference. I only have CPUs (no GPU). I also...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: environment information... PyTorch version: 2.5.1+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 24.04.1 LTS (x86_64) GCC version: (Ubuntu 12.3.0-17ubuntu1) 12.3.0...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
