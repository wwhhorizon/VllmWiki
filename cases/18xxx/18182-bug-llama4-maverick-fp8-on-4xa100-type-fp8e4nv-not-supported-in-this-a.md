# vllm-project/vllm#18182: [Bug]: Llama4 Maverick FP8 on 4xA100: type fp8e4nv not supported in this architecture. The supported fp8 dtypes are ('fp8e4b15', 'fp8e5')")

| 字段 | 值 |
| --- | --- |
| Issue | [#18182](https://github.com/vllm-project/vllm/issues/18182) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;fp8;operator |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Llama4 Maverick FP8 on 4xA100: type fp8e4nv not supported in this architecture. The supported fp8 dtypes are ('fp8e4b15', 'fp8e5')")

### Issue 正文摘录

### Your current environment PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: version 3.31.5 Libc version: glibc-2.31 Python version: 3.12.9 | packaged by Anaconda, Inc. | (main, Feb 6 2025, 18:56:27) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.4.0-215-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 12.4.131 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB GPU 2: NVIDIA A100-SXM4-80GB GPU 3: NVIDIA A100-SXM4-80GB Nvidia driver version: 570.124.06 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 48 bits physical, 48 bits virtual CPU(s): 128 On-line CPU(s) list: 0-127 Thread(s) per core: 2 Core(s) per socket: 32 Socket(s): 2 NUMA node(s): 2 Vendor ID: AuthenticAMD CPU family: 25 Model: 1 Model name: AMD EPYC 7543 32-Core...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: es are ('fp8e4b15', 'fp8e5')") bug ### Your current environment PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: Llama4 Maverick FP8 on 4xA100: type fp8e4nv not supported in this architecture. The supported fp8 dtypes are ('fp8e4b15', 'fp8e5')") bug ### Your current environment PyTorch version: 2.6.0+cu124 Is debug build: F...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Llama4 Maverick FP8 on 4xA100: type fp8e4nv not supported in this architecture. The supported fp8 dtypes are ('fp8e4b15', 'fp8e5')") bug ### Your current environment PyTorch version: 2.6.0+cu124 Is debug build: F...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Llama4 Maverick FP8 on 4xA100: type fp8e4nv not supported in this architecture. The supported fp8 dtypes are ('fp8e4b15', 'fp8e5')") bug ### Your current environment PyTorch version: 2.6.0+cu124 Is debug build: F...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: llel-size 4 --gpu-memory-utilization 0.95 --enable-chunked-prefill --cpu-offload-gb 350 --max-model-len 32000` Seems like a similar issue to this one on A100? https://github.com/deepseek-ai/DeepSeek-V3/issues/4#issuecom...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
