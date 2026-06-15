# vllm-project/vllm#33991: [Installation]: building docker cpu image with VLLM_CPU_DISABLE_AVX512=true (or on any x86_64 CPU without AVX512) fails to compile mla_decode.cpp because BFloat16 has no AVX2 fallback

| 字段 | 值 |
| --- | --- |
| Issue | [#33991](https://github.com/vllm-project/vllm/issues/33991) |
| 状态 | closed |
| 标签 | installation;cpu |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;attention;cuda;kernel;moe;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: building docker cpu image with VLLM_CPU_DISABLE_AVX512=true (or on any x86_64 CPU without AVX512) fails to compile mla_decode.cpp because BFloat16 has no AVX2 fallback

### Issue 正文摘录

### Your current environment ```text Collecting environment information... uv is set ============================== System Info ============================== OS : Ubuntu 24.04.3 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : 18.1.3 (1ubuntu1) CMake version : version 3.30.2 Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.9.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.10 (main, Apr 9 2025, 04:03:51) [Clang 20.1.0 ] (64-bit runtime) Python platform : Linux-6.8.0-90-generic-x86_64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 13.1.115 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA TITAN RTX Nvidia driver version : 590.48.01 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ============================== CPU Info ============================...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 11: [Installation]: building docker cpu image with VLLM_CPU_DISABLE_AVX512=true (or on any x86_64 CPU without AVX512) fails to compile mla_decode.cpp because BFloat16 has no AVX2 fallback installation;cpu ### Your current e...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: out AVX512) fails to compile mla_decode.cpp because BFloat16 has no AVX2 fallback installation;cpu ### Your current environment ```text Collecting environment information... uv is set ============================== Syst...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.9.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.10 (...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ation;cpu ### Your current environment ```text Collecting environment information... uv is set ============================== System Info ============================== OS : Ubuntu 24.04.3 LTS (x86_64) GCC version : (Ub...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: n any x86_64 CPU without AVX512) fails to compile mla_decode.cpp because BFloat16 has no AVX2 fallback installation;cpu ### Your current environment ```text Collecting environment information... uv is set ==============...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
