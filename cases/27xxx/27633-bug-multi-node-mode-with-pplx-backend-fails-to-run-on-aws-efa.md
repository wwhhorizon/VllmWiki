# vllm-project/vllm#27633: [Bug]: Multi-node mode with pplx backend fails to run on AWS EFA

| 字段 | 值 |
| --- | --- |
| Issue | [#27633](https://github.com/vllm-project/vllm/issues/27633) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Multi-node mode with pplx backend fails to run on AWS EFA

### Issue 正文摘录

### Your current environment Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version : 14.0.0-1ubuntu1.1 CMake version : version 4.1.0 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.13.5 | packaged by Anaconda, Inc. | (main, Jun 12 2025, 16:09:02) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-6.8.0-1036-aws-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.8.93 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA H200 GPU 1: NVIDIA H200 GPU 2: NVIDIA H200 GPU 3: NVIDIA H200 GPU 4: NVIDIA H200 GPU 5: NVIDIA H200 GPU 6: NVIDIA H200 GPU 7: NVIDIA H200 Nvidia driver version : 570.172.08 cuDNN version : Could not collect HIP runti...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version : 14.0.0-1ubuntu1.1 CMake version : version 4.1.0 Libc version : glibc-2.35 ================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.13.5 |...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: AWS EFA bug;stale ### Your current environment Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: Multi-node mode with pplx backend fails to run on AWS EFA bug;stale ### Your current environment Collecting environment information... ============================== System Info ============================== OS
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: abric-based, NOT InfiniBand - **Configuration**: Data Parallel (DP) with Expert Parallelism (EP) ## Reproduce ### Working Configuration (for comparison) ```bash # This works perfectly export VLLM_ALL2ALL_BACKEND=allgath...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
