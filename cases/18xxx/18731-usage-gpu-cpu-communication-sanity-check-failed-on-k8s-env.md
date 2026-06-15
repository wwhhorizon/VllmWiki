# vllm-project/vllm#18731: [Usage]:  GPU/CPU communication sanity check failed on K8S env

| 字段 | 值 |
| --- | --- |
| Issue | [#18731](https://github.com/vllm-project/vllm/issues/18731) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]:  GPU/CPU communication sanity check failed on K8S env

### Issue 正文摘录

### Your current environment ```text INFO 05-27 08:54:12 [__init__.py:239] Automatically detected platform cuda. Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.4 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 4.0.0 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.6.0+cu124 Is debug build : False CUDA used to build PyTorch : 12.4 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.9 (main, Feb 5 2025, 08:49:00) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-5.15.0-122-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.4.131 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA H800 GPU 1: NVIDIA H800 GPU 2: NVIDIA H800 GPU 3: NVIDIA H800 GPU 4: NVIDIA H800 GPU 5: NVIDIA H800 GPU 6: NVIDIA H800 GPU 7: NVIDIA H800 Nvidia driver version :...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ========= OS : Ubuntu 22.04.4 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 4.0.0 Libc version : glibc-2.35 ==================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: xt INFO 05-27 08:54:12 [__init__.py:239] Automatically detected platform cuda. Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.4 LTS (x86...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: _.py:239] Automatically detected platform cuda. Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.4 LTS (x86_64) GCC version : (Ubuntu 11.4...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.2.1.post2+cu124torch2.6 [pip3] numpy==2.1.3 [pip3] nvidia-cublas-cu12==12.4.5.8 [pip3] nvidia-cuda-cupti-cu12==12.4.127 [pip3...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: oblem with my basic environment configuration. I'm seeking help from the experts in the community to resolve this issue. Thank you very much! ### Before submitting a new issue... - [x] Make sure you already searched for...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
