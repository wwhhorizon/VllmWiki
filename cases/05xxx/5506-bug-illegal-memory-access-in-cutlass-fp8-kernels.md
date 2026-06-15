# vllm-project/vllm#5506: [Bug]: Illegal memory access in CUTLASS FP8 kernels

| 字段 | 值 |
| --- | --- |
| Issue | [#5506](https://github.com/vllm-project/vllm/issues/5506) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;fp8;gemm;kernel;operator;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Illegal memory access in CUTLASS FP8 kernels

### Issue 正文摘录

For now, I've filed to use torch._scaled_mm in https://github.com/vllm-project/vllm/pull/5505 ### Your current environment ``` Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.29.3 Libc version: glibc-2.35 Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.19.0-1010-nvidia-lowlatency-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.5.40 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA H100 NVL GPU 1: NVIDIA H100 NVL GPU 2: NVIDIA H100 NVL GPU 3: NVIDIA H100 NVL GPU 4: NVIDIA H100 NVL GPU 5: NVIDIA H100 NVL GPU 6: NVIDIA H100 NVL GPU 7: NVIDIA H100 NVL Nvidia driver version: 555.42.02 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 57 bits virtual Byte Order: Little Endian CPU(s): 1...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: r current environment ``` Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: Illegal memory access in CUTLASS FP8 kernels bug For now, I've filed to use torch._scaled_mm in https://github.com/vllm-project/vllm/pull/5505 ### Your current environment ``` Collecting environment information.....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: lm/pull/5505 ### Your current environment ``` Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: Illegal memory access in CUTLASS FP8 kernels bug For now, I've filed to use torch._scaled_mm in https://github.com/vllm-project/vllm/pull/5505 ### Your current environment ``` Collecting environment information.....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
