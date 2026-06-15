# vllm-project/vllm#4201: [Installation]: Failed to build form source code. Python=3.9 CUDA=12.1

| 字段 | 值 |
| --- | --- |
| Issue | [#4201](https://github.com/vllm-project/vllm/issues/4201) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Failed to build form source code. Python=3.9 CUDA=12.1

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` Collecting environment information... PyTorch version: 2.1.0 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 12.3.0-1ubuntu1~22.04) 12.3.0 Clang version: Could not collect CMake version: version 3.22.1 Libc version: glibc-2.35 Python version: 3.9.19 (main, Mar 21 2024, 17:11:28) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-102-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.1.66 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 3090 GPU 1: NVIDIA GeForce RTX 3090 GPU 2: NVIDIA GeForce RTX 3090 GPU 3: NVIDIA GeForce RTX 3090 GPU 4: NVIDIA GeForce RTX 3090 GPU 5: NVIDIA GeForce RTX 3090 GPU 6: NVIDIA GeForce RTX 3090 GPU 7: NVIDIA GeForce RTX 3090 Nvidia driver version: 530.41.03 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 56 On-l...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: [Installation]: Failed to build form source code. Python=3.9 CUDA=12.1 installation;stale ### Your current environment ```text The output of `python collect_env.py` Collecting environment information... PyTorch version:
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Installation]: Failed to build form source code. Python=3.9 CUDA=12.1 installation;stale ### Your current environment ```text The output of `python collect_env.py` Collecting environment information... PyTorch version:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ```text The output of `python collect_env.py` Collecting environment information... PyTorch version: 2.1.0 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ting environment information... PyTorch version: 2.1.0 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 12.3.0-1ubuntu1~22.04) 1...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: target arches: 86-real -- Enabling C extension. -- Enabling moe extension. -- Configuring done (10.5s) -- Generating done (0.0s) -- Build files have been written to: /tmp/tmp3bv_up2q.build-temp Using MAX_JOBS=6 as the n...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
