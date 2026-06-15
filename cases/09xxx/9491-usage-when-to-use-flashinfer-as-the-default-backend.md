# vllm-project/vllm#9491: [Usage]: When to use flashinfer as the default backend

| 字段 | 值 |
| --- | --- |
| Issue | [#9491](https://github.com/vllm-project/vllm/issues/9491) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;hardware_porting |
| 子分类 |  |
| Operator 关键词 | attention;cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: When to use flashinfer as the default backend

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.30.0 Libc version: glibc-2.35 Python version: 3.10.12 (main, Mar 22 2024, 16:50:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.4.0-171-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB GPU 2: NVIDIA A100-SXM4-80GB GPU 3: NVIDIA A100-SXM4-80GB GPU 4: NVIDIA A100-SXM4-80GB GPU 5: NVIDIA A100-SXM4-80GB GPU 6: NVIDIA A100-SXM4-80GB GPU 7: NVIDIA A100-SXM4-80GB ### How would you like to use vllm I have read the flashinfer blog post and excited with its great performance., but i'm confused with why vllm not taking flashinfer as the default attention backend, and the performance blog post of vllm 0.6.0 is also not running with flashinfer. Is there any usage of when to use flashinfer a...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: t environment ```text The output of `python collect_env.py` ``` PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: n collect_env.py` ``` PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Usage]: When to use flashinfer as the default backend usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyT...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB GPU 2: NVIDIA A100-SXM4-80GB GPU 3: NVIDIA A100-SXM4-80GB GPU 4...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: here any usage of when to use flashinfer as the backend or some official benchmark of the scenarios where flashinfer is much better than FA2, thanks ### Before submitting a new issue... - [X] Make sure you already searc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
