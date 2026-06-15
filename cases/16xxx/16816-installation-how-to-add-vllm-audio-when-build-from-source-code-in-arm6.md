# vllm-project/vllm#16816: [Installation]: how to add vllm[audio] when build from source code in arm64 platform

| 字段 | 值 |
| --- | --- |
| Issue | [#16816](https://github.com/vllm-project/vllm/issues/16816) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: how to add vllm[audio] when build from source code in arm64 platform

### Issue 正文摘录

### Your current environment 2025-04-18 06:03:09 (182 KB/s) - ‘collect_env.py’ saved [26874/26874] INFO 04-18 06:03:19 [__init__.py:239] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.7.0a0+7c8ec84dab.nv25.03 Is debug build: False CUDA used to build PyTorch: 12.8 ROCM used to build PyTorch: N/A OS: Ubuntu 24.04.1 LTS (aarch64) GCC version: (Ubuntu 10.5.0-4ubuntu2) 10.5.0 Clang version: Could not collect CMake version: version 3.31.6 Libc version: glibc-2.39 Python version: 3.12.3 (main, Feb 4 2025, 14:48:35) [GCC 13.3.0] (64-bit runtime) Python platform: Linux-5.15.0-133-generic-aarch64-with-glibc2.39 Is CUDA available: True CUDA runtime version: 12.8.93 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L20 GPU 1: NVIDIA L20 GPU 2: NVIDIA L20 GPU 3: NVIDIA L20 GPU 4: NVIDIA L20 GPU 5: NVIDIA L20 GPU 6: NVIDIA L20 GPU 7: NVIDIA L20 Nvidia driver version: 560.35.05 cuDNN version: Probably one of the following: /usr/lib/aarch64-linux-gnu/libcudnn.so.9.8.0 /usr/lib/aarch64-linux-gnu/libcudnn_adv.so.9.8.0 /usr/lib/aarch64-linux-gnu/libcudnn_cnn.so.9.8.0 /usr/lib/aarch64-linux-gnu/libcudnn_engines_precompiled.so....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Installation]: how to add vllm[audio] when build from source code in arm64 platform installation;stale ### Your current environment 2025-04-18 06:03:09 (182 KB/s) - ‘collect_env.py’ saved [26874/26874] INFO 04-18 06:03
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ] INFO 04-18 06:03:19 [__init__.py:239] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.7.0a0+7c8ec84dab.nv25.03 Is debug build: False CUDA used to build PyTorch: 12.8 ROCM...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: _.py:239] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.7.0a0+7c8ec84dab.nv25.03 Is debug build: False CUDA used to build PyTorch: 12.8 ROCM used to build PyTorch: N/A OS...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: rmation... PyTorch version: 2.7.0a0+7c8ec84dab.nv25.03 Is debug build: False CUDA used to build PyTorch: 12.8 ROCM used to build PyTorch: N/A OS: Ubuntu 24.04.1 LTS (aarch64) GCC version: (Ubuntu 10.5.0-4ubuntu2) 10.5.0...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [pip3] torch-geometric==2.6.1 [pip3] torch_tensorrt==2.7.0a0 [pip3] torchprofile==0.0.4 [pip3] torchvision==0.22.0a0 [pip3] transformers==4.51.2 [pip3] triton==3.3.0 [conda] Could not collect ROCM Version: Could not col...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
