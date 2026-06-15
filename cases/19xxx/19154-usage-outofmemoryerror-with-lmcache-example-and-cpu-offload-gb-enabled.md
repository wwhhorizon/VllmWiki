# vllm-project/vllm#19154: [Usage]: OutofMemoryError with LMCache example and cpu_offload_gb enabled

| 字段 | 值 |
| --- | --- |
| Issue | [#19154](https://github.com/vllm-project/vllm/issues/19154) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: OutofMemoryError with LMCache example and cpu_offload_gb enabled

### Issue 正文摘录

### Your current environment ```text INFO 06-04 13:31:21 [__init__.py:243] Automatically detected platform cuda. Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.2 LTS (aarch64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 4.0.2 Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.7.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.10 (main, May 30 2025, 05:26:00) [GCC 6.3.0 20170516] (64-bit runtime) Python platform : Linux-5.14.0-362.24.1.el9_3.aarch64+64k-aarch64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.8.93 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA GH200 120GB Nvidia driver version : 560.35.03 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ======== OS : Ubuntu 24.04.2 LTS (aarch64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 4.0.2 Libc version : glibc-2.39 ==================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: xt INFO 06-04 13:31:21 [__init__.py:243] Automatically detected platform cuda. Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.2 LTS (aar...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: p sve2 sveaes svepmull svebitperm svesha3 svesm4 flagm2 frint svei8mm svebf16 i8mm bf16 dgh L1d cache: 4.5 MiB (72 instances) L1i cache: 4.5 MiB (72 instances) L2 cache: 72 MiB (72 instances) L3 cache:
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: [Usage]: OutofMemoryError with LMCache example and cpu_offload_gb enabled usage;stale ### Your current environment ```text INFO 06-04 13:31:21 [__init__.py:243] Automatically detected platform cuda. Collecting environme...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: _.py:243] Automatically detected platform cuda. Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.2 LTS (aarch64) GCC version : (Ubuntu 13....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
