# vllm-project/vllm#4514: [Bug]: For RDNA3 (navi31; gfx1100) VLLM_USE_TRITON_FLASH_ATTN=0 currently must be forced

| 字段 | 值 |
| --- | --- |
| Issue | [#4514](https://github.com/vllm-project/vllm/issues/4514) |
| 状态 | closed |
| 标签 | bug;rocm;stale |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: For RDNA3 (navi31; gfx1100) VLLM_USE_TRITON_FLASH_ATTN=0 currently must be forced

### Issue 正文摘录

### Your current environment ```text Collecting environment information... /opt/conda/envs/py_3.9/lib/python3.9/site-packages/torch/cuda/__init__.py:611: UserWarning: Can't initialize NVML warnings.warn("Can't initialize NVML") PyTorch version: 2.1.1+git011de5c Is debug build: False CUDA used to build PyTorch: N/A ROCM used to build PyTorch: 6.0.32830-d62f6a171 OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: 17.0.0 (https://github.com/RadeonOpenCompute/llvm-project roc-6.0.0 23483 7208e8d15fbf218deb74483ea8c549c67ca4985e) CMake version: version 3.29.2 Libc version: glibc-2.31 Python version: 3.9.18 (main, Sep 11 2023, 13:41:44) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-6.5.0-28-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 10.1.243 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: AMD Radeon PRO W7900NoGCNArchNameOnOldPyTorch Nvidia driver version: Could not collect cuDNN version: Could not collect HIP runtime version: 6.0.32830 MIOpen runtime version: 3.0.0 Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address size...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: : Can't initialize NVML warnings.warn("Can't initialize NVML") PyTorch version: 2.1.1+git011de5c Is debug build: False CUDA used to build PyTorch: N/A ROCM used to build PyTorch: 6.0.32830-d62f6a171 OS: Ubuntu 20.04.6 L...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: vi31; gfx1100) VLLM_USE_TRITON_FLASH_ATTN=0 currently must be forced bug;rocm;stale ### Your current environment ```text Collecting environment information... /opt/conda/envs/py_3.9/lib/python3.9/site-packages/torch/cud...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Bug]: For RDNA3 (navi31; gfx1100) VLLM_USE_TRITON_FLASH_ATTN=0 currently must be forced bug;rocm;stale ### Your current environment ```text Collecting environment information... /opt/conda/envs/py_3.9/lib/python3.9/sit...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ocm;stale ### Your current environment ```text Collecting environment information... /opt/conda/envs/py_3.9/lib/python3.9/site-packages/torch/cuda/__init__.py:611: UserWarning: Can't initialize NVML warnings.warn("Can't...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: gfx1100) VLLM_USE_TRITON_FLASH_ATTN=0 currently must be forced bug;rocm;stale ### Your current environment ```text Collecting environment information... /opt/conda/envs/py_3.9/lib/python3.9/site-packages/torch/cuda/__in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
