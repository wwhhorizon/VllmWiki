# vllm-project/vllm#42393: [Installation]: RuntimeError: FlashInfer requires GPUs with sm75 or higher when running vllm server

| 字段 | 值 |
| --- | --- |
| Issue | [#42393](https://github.com/vllm-project/vllm/issues/42393) |
| 状态 | open |
| 标签 | installation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: RuntimeError: FlashInfer requires GPUs with sm75 or higher when running vllm server

### Issue 正文摘录

### Your current environment Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.1 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 3.28.3 Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.9.1+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A XPU used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (main, Jan 8 2026, 11:30:50) [GCC 13.3.0] (64-bit runtime) Python platform : Linux-6.19.12-arch1-1-x86_64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : Could not collect CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA GeForce RTX 5090 Nvidia driver version : 595.58.03 cuDNN version : Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.9.7.1 /usr/lib/x86_64-linux-gnu/libcudnn_adv.so.9.7.1 /usr/lib/x86_64-linux...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Installation]: RuntimeError: FlashInfer requires GPUs with sm75 or higher when running vllm server installation ### Your current environment Collecting environment information... ============================== S
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Installation]: RuntimeError: FlashInfer requires GPUs with sm75 or higher when running vllm server installation ### Your current environment Collecting environment information... ============================== System I...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: aves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local user_shstk avx512_bf16 clzero irperf xsaveerptr rdpru wbnoinvd amd_ppin cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: rver installation ### Your current environment Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.1 LTS (x86_64) GCC version : (Ubuntu 13.3....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Installation]: RuntimeError: FlashInfer requires GPUs with sm75 or higher when running vllm server installation ### Your current environment Collecting environment information... ============================== System I...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
