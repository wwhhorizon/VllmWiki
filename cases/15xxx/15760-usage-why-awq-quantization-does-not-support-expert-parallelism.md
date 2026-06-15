# vllm-project/vllm#15760: [Usage]: Why AWQ quantization does not support expert parallelism?

| 字段 | 值 |
| --- | --- |
| Issue | [#15760](https://github.com/vllm-project/vllm/issues/15760) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support;moe;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;moe;quantization |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Why AWQ quantization does not support expert parallelism?

### Issue 正文摘录

### Your current environment PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.26.0 Libc version: glibc-2.35 Python version: 3.12.9 | packaged by Anaconda, Inc. | (main, Feb 6 2025, 18:56:27) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-6.2.0-39-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.4.99 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A40 GPU 1: NVIDIA A40 Nvidia driver version: 560.35.03 ### How would you like to use vllm I want to run Deepseek-V3-AWQ with expert parallelism, but I get a error saying " Expert fused Parallelism is not supported for Marlin MoE method". I want to know whether awq can achieve expert parallelism under the current vllm architecture. " ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of freq...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: rt expert parallelism? usage;stale ### Your current environment PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Usage]: Why AWQ quantization does not support expert parallelism? usage;stale ### Your current environment PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: True CUDA runtime version: 12.4.99 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A40 GPU 1: NVIDIA A40 Nvidia driver version: 560.35.03 ### How would you like to use vllm I want to run Dee...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Usage]: Why AWQ quantization does not support expert parallelism? usage;stale ### Your current environment PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch:...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Usage]: Why AWQ quantization does not support expert parallelism? usage;stale ### Your current environment PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
