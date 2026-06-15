# vllm-project/vllm#12889: [Bug]: vllm version 0.7.2 downloading and loading issues.

| 字段 | 值 |
| --- | --- |
| Issue | [#12889](https://github.com/vllm-project/vllm/issues/12889) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm version 0.7.2 downloading and loading issues.

### Issue 正文摘录

### Your current environment ``` NFO 02-07 11:03:45 __init__.py:190] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.35 Python version: 3.11.10 (main, Sep 7 2024, 18:35:41) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-6.8.0-49-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.4.131 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A40 GPU 1: NVIDIA A40 Nvidia driver version: 565.57.01 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 52 bits physical, 57 bits virtual Byte Order: Little Endian CPU(s): 96 On-line CPU(s) list: 0-95 Vendor ID: GenuineIntel Model name: Intel(R) Xeon(R) Gold 6342 CPU @ 2.80GHz CPU family: 6 Model: 106 Thread(s) per core: 2 Core(s) per socket: 24 Soc...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug]: vllm version 0.7.2 downloading and loading issues. bug;stale ### Your current environment ``` NFO 02-07 11:03:45 __init__.py:190] Automatically detected platform cuda. Collecting environment information... PyTorc...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: vllm version 0.7.2 downloading and loading issues. bug;stale ### Your current environment ``` NFO 02-07 11:03:45 __init__.py:190] Automatically detected platform cuda. Collecting environment information... PyTorc...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: th=None, download_dir=None, load_format='bitsandbytes', config_format= , dtype='bfloat16', kv_cache_dtype='auto', max_model_len=2000, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto',...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ``` NFO 02-07 11:03:45 __init__.py:190] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: _.py:190] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
