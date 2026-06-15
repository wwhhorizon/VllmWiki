# vllm-project/vllm#34817: [Bug]: Trying to run gpt-oss-120b on rtx pro 6000

| 字段 | 值 |
| --- | --- |
| Issue | [#34817](https://github.com/vllm-project/vllm/issues/34817) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;gemm;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Trying to run gpt-oss-120b on rtx pro 6000

### Issue 正文摘录

### Your current environment ============================== System Info ============================== OS : Ubuntu 24.04.4 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.10.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (main, Jan 22 2026, 20:57:42) [GCC 13.3.0] (64-bit runtime) Python platform : Linux-6.8.0-100-generic-x86_64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 13.0.88 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA RTX PRO 6000 Blackwell Server Edition Nvidia driver version : 580.126.09 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ============================== CPU Info ============================== Architecture: x86_64 CP...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 24.04.4 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.39 ==============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: [Bug]: Trying to run gpt-oss-120b on rtx pro 6000 bug;stale ### Your current environment ============================== System Info ============================== OS : Ubuntu 24.04.4 LTS (x86_64) GCC version
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.6.3 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cupti-cu12==12.8.90 [pip3] nvidia-cuda-nvrtc-c...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: -120b', 'api_server_count': 1, 'model': 'openai/gpt-oss-120b', 'kv_cache_dtype': 'fp8', 'enable_prefix_caching': False, 'max_num_batched_tokens': 8192, 'async_scheduling': True, 'stream_interval': 20, 'max_cudagraph_cap...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Trying to run gpt-oss-120b on rtx pro 6000 bug;stale ### Your current environment ============================== System Info ============================== OS : Ubuntu 24.04.4 LTS (x86_64) GCC versio

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
