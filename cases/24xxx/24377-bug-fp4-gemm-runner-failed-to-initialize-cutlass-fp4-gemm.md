# vllm-project/vllm#24377: [Bug]: [FP4 gemm Runner] Failed to initialize cutlass FP4 gemm.

| 字段 | 值 |
| --- | --- |
| Issue | [#24377](https://github.com/vllm-project/vllm/issues/24377) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [FP4 gemm Runner] Failed to initialize cutlass FP4 gemm.

### Issue 正文摘录

### Your current environment ``` Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.3 LTS (aarch64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.9.0 Is debug build : False CUDA used to build PyTorch : 13.0 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11 | packaged by Anaconda, Inc. | (main, Jun 5 2025, 12:59:05) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-6.8.12-tegra-aarch64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : Could not collect CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA Thor Nvidia driver version : 580.00 cuDNN version : Probably one of the following: /usr/lib/aarch64-linux-gnu/libcudnn.so.9.12.0 /usr/lib/aarch64-linux-gnu/libcudnn_adv.so.9.12.0 /usr/lib/aarch64-linux-gnu/libcu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ======== OS : Ubuntu 24.04.3 LTS (aarch64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.39 ==============
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: [Bug]: [FP4 gemm Runner] Failed to initialize cutlass FP4 gemm. bug;stale ### Your current environment ``` Collecting environment information... ============================== System Info ==============================...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ==================== OS : Ubuntu 24.04.3 LTS (aarch64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.39 ==
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: [FP4 gemm Runner] Failed to initialize cutlass FP4 gemm. bug;stale ### Your current environment ``` Collecting environment information... ============================== System Info ==============================
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: mm. bug;stale ### Your current environment ``` Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.3 LTS (aarch64) GCC version : (Ubuntu 13.3...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
