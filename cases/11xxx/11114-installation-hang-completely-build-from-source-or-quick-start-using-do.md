# vllm-project/vllm#11114: [Installation]: Hang completely Build from source or Quick start using Dockerfile 

| 字段 | 值 |
| --- | --- |
| Issue | [#11114](https://github.com/vllm-project/vllm/issues/11114) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;import_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Hang completely Build from source or Quick start using Dockerfile 

### Issue 正文摘录

### Your current environment ```text WARNING 12-11 22:38:53 _custom_ops.py:20] Failed to import from vllm._C with ImportError('libcudart.so.12: cannot open shared object file: No such file or directory') INFO 12-11 22:38:53 importing.py:15] Triton not installed or not compatible; certain GPU-related functions will not be available. Collecting environment information... PyTorch version: 2.5.1+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Linux Mint 22 (x86_64) GCC version: (Ubuntu 12.3.0-17ubuntu1) 12.3.0 Clang version: Could not collect CMake version: version 3.31.1 Libc version: glibc-2.39 Python version: 3.12.3 (main, Nov 6 2024, 18:32:19) [GCC 13.2.0] (64-bit runtime) Python platform: Linux-6.8.0-50-generic-x86_64-with-glibc2.39 Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 39 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 8 On-line...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Installation]: Hang completely Build from source or Quick start using Dockerfile installation;stale ### Your current environment ```text WARNING 12-11 22:38:53 _custom_ops.py:20] Failed to import from vllm._C with Impo
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: 53 _custom_ops.py:20] Failed to import from vllm._C with ImportError('libcudart.so.12: cannot open shared object file: No such file or directory') INFO 12-11 22:38:53 importing.py:15] Triton not installed or not compati...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: in GPU-related functions will not be available. Collecting environment information... PyTorch version: 2.5.1+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Linux Mint 22 (...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: mpletely Build from source or Quick start using Dockerfile installation;stale ### Your current environment ```text WARNING 12-11 22:38:53 _custom_ops.py:20] Failed to import from vllm._C with ImportError('libcudart.so.1...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: t file: No such file or directory') INFO 12-11 22:38:53 importing.py:15] Triton not installed or not compatible; certain GPU-related functions will not be available. Collecting environment information... PyTorch version...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
