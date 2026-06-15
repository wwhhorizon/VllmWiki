# vllm-project/vllm#8998: [Usage]: Not able to run LLMEngine in two sequential tests using pytest

| 字段 | 值 |
| --- | --- |
| Issue | [#8998](https://github.com/vllm-project/vllm/issues/8998) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Not able to run LLMEngine in two sequential tests using pytest

### Issue 正文摘录

### Your current environment ```text Collecting environment information... WARNING 10-01 11:59:43 cuda.py:22] You are using a deprecated `pynvml` package. Please install `nvidia-ml-py` instead. See https://pypi.org/project/pynvml for more information. PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 24.04.1 LTS (x86_64) GCC version: (Ubuntu 13.2.0-23ubuntu4) 13.2.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.39 Python version: 3.12.3 (main, Sep 11 2024, 14:17:37) [GCC 13.2.0] (64-bit runtime) Python platform: Linux-6.8.0-41-generic-x86_64-with-glibc2.39 Is CUDA available: True CUDA runtime version: 12.0.140 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 4090 GPU 1: NVIDIA GeForce RTX 4090 Nvidia driver version: 535.183.06 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 43 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 16 On-line CPU(s) list: 0-15 Vendor ID: AuthenticA...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: 11:59:43 cuda.py:22] You are using a deprecated `pynvml` package. Please install `nvidia-ml-py` instead. See https://pypi.org/project/pynvml for more information. PyTorch version: 2.4.0+cu121 Is debug build: False CUDA...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: nt ```text Collecting environment information... WARNING 10-01 11:59:43 cuda.py:22] You are using a deprecated `pynvml` package. Please install `nvidia-ml-py` instead. See https://pypi.org/project/pynvml for more inform...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: age;stale ### Your current environment ```text Collecting environment information... WARNING 10-01 11:59:43 cuda.py:22] You are using a deprecated `pynvml` package. Please install `nvidia-ml-py` instead. See https://pyp...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: e]: Not able to run LLMEngine in two sequential tests using pytest usage;stale ### Your current environment ```text Collecting environment information... WARNING 10-01 11:59:43 cuda.py:22] You are using a deprecated `py...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rch==2.4.0 [pip3] torchvision==0.19.0 [pip3] transformers==4.44.2 [pip3] triton==3.0.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.5.5@09c7792610ada9f88bbf87d32b472d...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
