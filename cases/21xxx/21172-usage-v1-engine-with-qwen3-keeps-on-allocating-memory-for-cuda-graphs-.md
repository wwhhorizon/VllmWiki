# vllm-project/vllm#21172: [Usage]: V1 Engine with Qwen3 keeps on allocating memory for cuda graphs until OOM

| 字段 | 值 |
| --- | --- |
| Issue | [#21172](https://github.com/vllm-project/vllm/issues/21172) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: V1 Engine with Qwen3 keeps on allocating memory for cuda graphs until OOM

### Issue 正文摘录

### Your current environment ```text Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : 18.1.3 (1ubuntu1) CMake version : Could not collect Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.7.0+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (main, Jun 18 2025, 17:59:45) [GCC 13.3.0] (64-bit runtime) Python platform : Linux-6.6.72+-x86_64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.9.86 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA A100-SXM4-40GB Nvidia driver version : 535.230.02 cuDNN version : Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.9.10.2 /usr/lib/x86_64-linux-gnu/libcudnn_adv.so.9.10.2 /usr/lib/x86_64-linux-gnu/libcudnn_cnn.so.9.10.2 /usr...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : 18.1.3 (1ubuntu1) CMake version : Could not collect Libc version : glibc-2.39 ==============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Usage]: V1 Engine with Qwen3 keeps on allocating memory for cuda graphs until OOM usage;stale ### Your current environment ```text Collecting environment information... ============================== System Info ======...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Usage]: V1 Engine with Qwen3 keeps on allocating memory for cuda graphs until OOM usage;stale ### Your current environment ```text Collecting environment information... ============================== System Info ======...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ne with Qwen3 keeps on allocating memory for cuda graphs until OOM usage;stale ### Your current environment ```text Collecting environment information... ============================== System Info ======================...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ]: V1 Engine with Qwen3 keeps on allocating memory for cuda graphs until OOM usage;stale ### Your current environment ```text Collecting environment information... ============================== System Info ============...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
