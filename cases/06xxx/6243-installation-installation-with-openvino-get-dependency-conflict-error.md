# vllm-project/vllm#6243: [Installation]: Installation with OpenVINO get dependency conflict Error !!!

| 字段 | 值 |
| --- | --- |
| Issue | [#6243](https://github.com/vllm-project/vllm/issues/6243) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | build_error;import_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Installation with OpenVINO get dependency conflict Error !!!

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` Collecting environment information... The cache for model files in Transformers v4.22.0 has been updated. Migrating your old cache. This is a one-time only operation. You can interrupt this and resume the migration later on by calling `transformers.utils.move_cache()`. 0it [00:00, ?it/s] WARNING 07-09 11:48:31 _custom_ops.py:14] Failed to import from vllm._C with ImportError('libcuda.so.1: cannot open shared object file: No such file or directory') PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.30.0 Libc version: glibc-2.35 Python version: 3.10.14 (main, May 6 2024, 19:42:50) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-6.5.0-41-generic-x86_64-with-glibc2.35 Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNP...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: [Installation]: Installation with OpenVINO get dependency conflict Error !!! installation ### Your current environment ```text The output of `python collect_env.py` Collecting environment information... The cache for mod
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: 31 _custom_ops.py:14] Failed to import from vllm._C with ImportError('libcuda.so.1: cannot open shared object file: No such file or directory') PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTor...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ```text The output of `python collect_env.py` Collecting environment information... The cache for model files in Transformers v4.22.0 has been updated. Migrating your old cache. This is a one-time only operation. You ca...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: rch==2.3.0 [pip3] torchvision==0.18.0 [pip3] transformers==4.42.3 [pip3] triton==2.3.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-nccl-cu12 2.20.5 pypi_0 pypi [conda] torch 2.3.0
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: such file or directory') PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
