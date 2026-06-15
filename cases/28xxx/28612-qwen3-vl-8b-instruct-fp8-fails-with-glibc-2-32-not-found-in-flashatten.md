# vllm-project/vllm#28612: Qwen3-VL-8B-Instruct-FP8 fails with GLIBC_2.32 not found in FlashAttention (works fine with Qwen3-VL-4B-Instruct)

| 字段 | 值 |
| --- | --- |
| Issue | [#28612](https://github.com/vllm-project/vllm/issues/28612) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | attention;cache;cuda;fp8;gemm;operator;quantization;sampling;triton |
| 症状 | build_error;crash;import_error |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Qwen3-VL-8B-Instruct-FP8 fails with GLIBC_2.32 not found in FlashAttention (works fine with Qwen3-VL-4B-Instruct)

### Issue 正文摘录

### Your current environment ``` Collecting environment information... ============================== System Info ============================== OS : TencentOS Server 3.1 (Final) (x86_64) GCC version : (GCC) 11.2.1 20210728 (Red Hat 11.2.1-1) Clang version : Could not collect CMake version : version 4.1.2 Libc version : glibc-2.28 ============================== PyTorch Info ============================== PyTorch version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.11.14 | packaged by conda-forge | (main, Oct 22 2025, 22:46:25) [GCC 14.3.0] (64-bit runtime) Python platform : Linux-5.4.119-19.0009.56-x86_64-with-glibc2.28 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.4.99 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA GeForce RTX 4090 D GPU 1: NVIDIA GeForce RTX 4090 D GPU 2: NVIDIA GeForce RTX 4090 D GPU 3: NVIDIA GeForce RTX 4090 D GPU 4: NVIDIA GeForce RTX 4090 D GPU 5: NVIDIA GeForce RTX 4090 D GPU 6: NVIDIA G...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: Qwen3-VL-8B-Instruct-FP8 fails with GLIBC_2.32 not found in FlashAttention (works fine with Qwen3-VL-4B-Instruct) bug;stale ### Your current environment ``` Collecting environment information... ========================...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 8: Qwen3-VL-8B-Instruct-FP8 fails with GLIBC_2.32 not found in FlashAttention (works fine with Qwen3-VL-4B-Instruct) bug;stale ### Your current environment ``` Collecting environment information... ========================...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: Qwen3-VL-8B-Instruct-FP8 fails with GLIBC_2.32 not found in FlashAttention (works fine with Qwen3-VL-4B-Instruct) bug;stale ### Your current environment ``` Collecting environment information... ========================...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.11.14 |...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: Qwen3-VL-8B-Instruct-FP8 fails with GLIBC_2.32 not found in FlashAttention (works fine with Qwen3-VL-4B-Instruct) bug;stale ### Your current environment ``` Collecting environment information... =========================

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
