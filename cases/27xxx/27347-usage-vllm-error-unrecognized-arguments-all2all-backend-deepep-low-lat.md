# vllm-project/vllm#27347: [Usage]: vllm: error: unrecognized arguments: --all2all-backend deepep_low_latency

| 字段 | 值 |
| --- | --- |
| Issue | [#27347](https://github.com/vllm-project/vllm/issues/27347) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: vllm: error: unrecognized arguments: --all2all-backend deepep_low_latency

### Issue 正文摘录

### Your current environment ```text Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 3.31.6 Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.0 (default, Mar 3 2022, 09:58:08) [GCC 7.5.0] (64-bit runtime) Python platform : Linux-5.15.0-89-generic-x86_64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.8.93 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA H200 GPU 1: NVIDIA H200 GPU 2: NVIDIA H200 GPU 3: NVIDIA H200 GPU 4: NVIDIA H200 GPU 5: NVIDIA H200 GPU 6: NVIDIA H200 GPU 7: NVIDIA H200 Nvidia driver version : 570.133.20 cuDNN version : Probably one of the following: /usr/lib/x86_64-...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 3.31.6 Libc version : glibc-2.39 =================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.0 (d...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ncy usage ### Your current environment ```text Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (Ubuntu 13.3....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Usage]: vllm: error: unrecognized arguments: --all2all-backend deepep_low_latency usage ### Your current environment ```text Collecting environment information... ============================== System Info ============...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: i--DeepSeek-V3/ --tensor-parallel-size 1 --data-parallel-size 8 --enable-expert-parallel --all2all-backend deepep_low_latency ``` get error: ``` vllm: error: unrecognized arguments: --all2all-backend deepep_low_latency...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
