# vllm-project/vllm#24513: [Bug]: vLLM fails to start with FLASHMLA with DeepSeek in DP=16 on B200 due to invalid shape.

| 字段 | 值 |
| --- | --- |
| Issue | [#24513](https://github.com/vllm-project/vllm/issues/24513) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM fails to start with FLASHMLA with DeepSeek in DP=16 on B200 due to invalid shape.

### Issue 正文摘录

### Your current environment ``` Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version : 14.0.0-1ubuntu1.1 CMake version : version 4.1.0 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11 (main, Jun 4 2025, 08:56:18) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-6.6.93+-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.8.93 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA B200 GPU 1: NVIDIA B200 GPU 2: NVIDIA B200 GPU 3: NVIDIA B200 GPU 4: NVIDIA B200 GPU 5: NVIDIA B200 GPU 6: NVIDIA B200 GPU 7: NVIDIA B200 Nvidia driver version : 575.57.08 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime ver...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version : 14.0.0-1ubuntu1.1 CMake version : version 4.1.0 Libc version : glibc-2.35 ================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: vLLM fails to start with FLASHMLA with DeepSeek in DP=16 on B200 due to invalid shape. bug ### Your current environment ``` Collecting environment information... ============================== System Info =======...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: u128 [pip3] torchvision==0.23.0+cu128 [pip3] transformers==4.56.1 [pip3] triton==3.4.0 [conda] Could not collect ============================== vLLM Info ============================== ROCM Version : Could not collect v...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: id shape. bug ### Your current environment ``` Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4....
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: :/usr/local/cuda/lib64 NCCL_CROSS_NIC=0 NCCL_DEBUG=INFO NCCL_IB_ADAPTIVE_ROUTING=1 NCCL_IB_FIFO_TC=84 NCCL_IB_QPS_PER_CONNECTION=4 NCCL_IB_TC=52 NCCL_NET=gIB NCCL_NET_GDR_LEVEL=PIX NCCL_NVLS_CHUNKSIZE=524288 NCCL_P2P_NE...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
