# vllm-project/vllm#13659: [Installation]:Error while deploying Deepseek-R1 671B with AMD 8xMi300x

| 字段 | 值 |
| --- | --- |
| Issue | [#13659](https://github.com/vllm-project/vllm/issues/13659) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
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

> [Installation]:Error while deploying Deepseek-R1 671B with AMD 8xMi300x

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` INFO 02-21 08:47:36 __init__.py:179] Automatically detected platform rocm. WARNING 02-21 08:47:36 rocm.py:34] `fork` method is not supported by ROCm. VLLM_WORKER_MULTIPROC_METHOD is overridden to `spawn` instead. Collecting environment information... PyTorch version: 2.7.0a0+git3a58512 Is debug build: False CUDA used to build PyTorch: N/A ROCM used to build PyTorch: 6.3.42133-1b9c17779 OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: 18.0.0git (https://github.com/RadeonOpenCompute/llvm-project roc-6.3.1 24491 1e0fda770a2079fbd71e4b70974d74f62fd3af10) CMake version: version 3.31.4 Libc version: glibc-2.35 Python version: 3.12.8 (main, Dec 4 2024, 08:54:12) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.15.0-130-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: AMD Instinct MI300X (gfx942:sramecc+:xnack-) Nvidia driver version: Could not collect cuDNN version: Could not collect HIP runtime version: 6.3.42133 MIOpen runtime version: 3.3.0 Is XNNPACK...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: [Installation]:Error while deploying Deepseek-R1 671B with AMD 8xMi300x installation;stale ### Your current environment ```text The output of `python collect_env.py` INFO 02-21 08:47:36 __init__.py:179] Automatically de
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: [Installation]:Error while deploying Deepseek-R1 671B with AMD 8xMi300x installation;stale ### Your current environment ```text The output of `python collect_env.py` INFO 02-21 08:47:36 __init__.py:179] Automatically de...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: TIPROC_METHOD is overridden to `spawn` instead. Collecting environment information... PyTorch version: 2.7.0a0+git3a58512 Is debug build: False CUDA used to build PyTorch: N/A ROCM used to build PyTorch: 6.3.42133-1b9c1...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: n]:Error while deploying Deepseek-R1 671B with AMD 8xMi300x installation;stale ### Your current environment ```text The output of `python collect_env.py` INFO 02-21 08:47:36 __init__.py:179] Automatically detected platf...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [pip3] torchvision==0.19.1a0+6194369 [pip3] transformers==4.48.1 [pip3] triton==3.2.0+gite5be006a [conda] Could not collect ROCM Version: 6.3.42133-1b9c17779 Neuron SDK Version: N/A vLLM Version: 0.6.7.dev220+g84f5d47b...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
