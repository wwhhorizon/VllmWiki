# vllm-project/vllm#22177: [Usage]: Abnormal GPU usage for FP8 models on Ampere GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#22177](https://github.com/vllm-project/vllm/issues/22177) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Abnormal GPU usage for FP8 models on Ampere GPUs

### Issue 正文摘录

### Your current environment ```bash Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 3.22.1 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.7.1+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.9 | packaged by Anaconda, Inc. | (main, Feb 6 2025, 18:56:27) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-5.15.0-138-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.8.93 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA RTX A5000 GPU 1: NVIDIA RTX A5000 GPU 2: NVIDIA RTX A5000 GPU 3: NVIDIA RTX A5000 GPU 4: NVIDIA RTX A5000 GPU 5: NVIDIA RTX A5000 GPU 6: NVIDIA RTX A5000 GPU 7: NVIDIA RTX A5000 Nvidia driver version : 535....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 3.22.1 Libc version : glibc-2.35 =================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: [Usage]: Abnormal GPU usage for FP8 models on Ampere GPUs usage;stale ### Your current environment ```bash Collecting environment information... ============================== System Info ==============================...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: Abnormal GPU usage for FP8 models on Ampere GPUs usage;stale ### Your current environment ```bash Collecting environment information... ============================== System Info ==============================...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Usage]: Abnormal GPU usage for FP8 models on Ampere GPUs usage;stale ### Your current environment ```bash Collecting environment information... ============================== System Info ==============================...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: ory-utilization 0.85 \ --host 0.0.0.0 --port 21002 ``` and the initial gpu memory usage is about `22457MiB / 24564MiB` Available KV cache memory: 12.22 GiB GPU KV cache size: 534,064 tokens Maximum concurrency for 262,1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
