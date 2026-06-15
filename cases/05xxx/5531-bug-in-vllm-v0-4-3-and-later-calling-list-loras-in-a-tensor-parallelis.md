# vllm-project/vllm#5531: [Bug]: In vLLM v0.4.3 and later, calling list_loras() in a tensor parallelism situation causes the system to hang.

| 字段 | 值 |
| --- | --- |
| Issue | [#5531](https://github.com/vllm-project/vllm/issues/5531) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;scheduler_memory;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: In vLLM v0.4.3 and later, calling list_loras() in a tensor parallelism situation causes the system to hang.

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux Type "help", "copyright", "credits" or "license" for more information. >>> quit Use quit() or Ctrl-D (i.e. EOF) to exit >>> quit() root@vllm-0-4-3-predictor-00001-deployment-54797fd955-p7b8g:/vllm-workspace# python3 collect_env.py Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.29.5 Libc version: glibc-2.35 Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.4.0-65-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB Nvidia driver version: 535.86.10 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_6...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ce# python3 collect_env.py Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC ve...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: ug]: In vLLM v0.4.3 and later, calling list_loras() in a tensor parallelism situation causes the system to hang. bug ### Your current environment ```text The output of `python collect_env.py` Python 3.10.12 (main, Nov 2...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: .0] on linux Type "help", "copyright", "credits" or "license" for more information. >>> quit Use quit() or Ctrl-D (i.e. EOF) to exit >>> quit() root@vllm-0-4-3-predictor-00001-deployment-54797fd955-p7b8g:/vllm-workspace...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: down: Not affected Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl and seccomp Vulnerability Spectre v1: Mitigation; usercopy/swapgs barriers and __user pointer sanitization Vuln...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: nccl-cu12==2.20.5 [pip3] torch==2.3.0 [pip3] transformers==4.41.2 [pip3] triton==2.3.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.4.3 vLLM Build Flags: CUDA Archs:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
