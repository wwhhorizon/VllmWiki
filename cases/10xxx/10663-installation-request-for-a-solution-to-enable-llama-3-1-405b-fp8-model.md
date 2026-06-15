# vllm-project/vllm#10663: [Installation]: Request for a Solution to Enable Llama 3.1 405B-FP8 Model Compatibility with AMD Mi250

| 字段 | 值 |
| --- | --- |
| Issue | [#10663](https://github.com/vllm-project/vllm/issues/10663) |
| 状态 | closed |
| 标签 | installation;rocm;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Request for a Solution to Enable Llama 3.1 405B-FP8 Model Compatibility with AMD Mi250

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` Collecting environment information... PyTorch version: 2.6.0.dev20240918+rocm6.2 Is debug build: False CUDA used to build PyTorch: N/A ROCM used to build PyTorch: 6.2.41133-dd7f95766 OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: 18.0.0git (https://github.com/RadeonOpenCompute/llvm-project roc-6.2.0 24292 26466ce804ac523b398608f17388eb6d605a3f09) CMake version: version 3.26.4 Libc version: glibc-2.31 Python version: 3.9.19 (main, May 6 2024, 19:43:03) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-4.18.0-553.22.1.el8_10.x86_64-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: AMD Instinct MI250X/MI250 (gfx90a:sramecc+:xnack-) Nvidia driver version: Could not collect cuDNN version: Could not collect HIP runtime version: 6.2.41133 MIOpen runtime version: 3.2.0 Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 48 bits physical, 48 bits virtual CPU(s): 128 On-line CPU(s) list: 0-127 T...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Installation]: Request for a Solution to Enable Llama 3.1 405B-FP8 Model Compatibility with AMD Mi250 installation;rocm;stale ### Your current environment ```text The output of `python collect_env.py` Collecting environ
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: nable Llama 3.1 405B-FP8 Model Compatibility with AMD Mi250 installation;rocm;stale ### Your current environment ```text The output of `python collect_env.py` Collecting environment information... PyTorch version: 2.6.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Installation]: Request for a Solution to Enable Llama 3.1 405B-FP8 Model Compatibility with AMD Mi250 installation;rocm;stale ### Your current environment ```text The output of `python collect_env.py` Collecting enviro...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Installation]: Request for a Solution to Enable Llama 3.1 405B-FP8 Model Compatibility with AMD Mi250 installation;rocm;stale ### Your current environment ```text The output of `python collect_env.py` Collecting enviro...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Installation]: Request for a Solution to Enable Llama 3.1 405B-FP8 Model Compatibility with AMD Mi250 installation;rocm;stale ### Your current environment ```text The output of `python collect_env.py` Collecting enviro...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
