# vllm-project/vllm#44335: [Installation]: libcudart.so.13 required when torch-backend=cu129 on vllm v0.22.0

| 字段 | 值 |
| --- | --- |
| Issue | [#44335](https://github.com/vllm-project/vllm/issues/44335) |
| 状态 | open |
| 标签 | installation |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: libcudart.so.13 required when torch-backend=cu129 on vllm v0.22.0

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` $ python collect_env.py Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.4 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.11.0+cu129 Is debug build : False CUDA used to build PyTorch : 12.9 ROCM used to build PyTorch : N/A XPU used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (main, Mar 23 2026, 19:04:32) [GCC 13.3.0] (64-bit runtime) Python platform : Linux-6.14.0-34-generic-x86_64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : Could not collect CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA RTX 5000 Ada Generation Laptop GPU Nvidia driver version : 575.64.03 cuDNN version : Could not collect HIP runtime version : N/A...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Installation]: libcudart.so.13 required when torch-backend=cu129 on vllm v0.22.0 installation ### Your current environment ```text The output of `python collect_env.py` ``` $ python collect_env.py Collecting environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Installation]: libcudart.so.13 required when torch-backend=cu129 on vllm v0.22.0 installation ### Your current environment ```text The output of `python collect_env.py` ``` $ python collect_env.py Collecting environmen...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Installation]: libcudart.so.13 required when torch-backend=cu129 on vllm v0.22.0 installation ### Your current environment ```text The output of `python collect_env.py` ``` $ python collect_env.py Collecting environmen...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: hon collect_env.py` ``` $ python collect_env.py Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.4 LTS (x86_64) GCC version : (Ubuntu 13.3...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Reg file data sampling: Mitigation; Clear Register File Vulnerability Retbleed: Not affected Vulnerability Spec rstack overf...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
