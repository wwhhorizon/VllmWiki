# vllm-project/vllm#6291: [Bug]: chatglm2 seems to have problems in vllm==0.5.0

| 字段 | 值 |
| --- | --- |
| Issue | [#6291](https://github.com/vllm-project/vllm/issues/6291) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;import_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: chatglm2 seems to have problems in vllm==0.5.0

### Issue 正文摘录

### Your current environment ```text Collecting environment information... WARNING 07-10 14:59:53 _custom_ops.py:14] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 24.04 LTS (x86_64) GCC version: (Ubuntu 11.4.0-9ubuntu1) 11.4.0 Clang version: Could not collect CMake version: version 3.29.2 Libc version: glibc-2.39 Python version: 3.10.0 (default, Mar 3 2022, 09:58:08) [GCC 7.5.0] (64-bit runtime) Python platform: Linux-6.8.0-36-generic-x86_64-with-glibc2.39 Is CUDA available: True CUDA runtime version: 12.0.140 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 4080 Nvidia driver version: 535.183.01 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 48 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 64 On-line CPU(s) list: 0-63 Vendor ID: AuthenticAMD Model name: AMD Ryzen Threadripper PRO 5975WX 32-Cores CPU family: 25 Model: 8 Threa...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: nment information... WARNING 07-10 14:59:53 _custom_ops.py:14] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build Py...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: ule named 'vllm._C'") PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 24.04 LTS (x86_64) GCC version: (Ubuntu 11.4.0-9ubuntu1) 11.4.0 Clang...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: bug;stale ### Your current environment ```text Collecting environment information... WARNING 07-10 14:59:53 _custom_ops.py:14] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") PyTorch...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: chatglm2 seems to have problems in vllm==0.5.0 bug;stale ### Your current environment ```text Collecting environment information... WARNING 07-10 14:59:53 _custom_ops.py:14] Failed to import from vllm._C with Mod...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: transformers==4.41.2 [pip3] transformers-stream-generator==0.0.5 [pip3] triton==2.3.0 [pip3] vllm-nccl-cu12==2.18.1.0.4.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-nccl-cu12 2.20.5 pypi_0 pypi [conda] torch

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
