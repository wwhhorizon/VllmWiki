# vllm-project/vllm#9554: [Installation]: vLLM does not support torch 2.5

| 字段 | 值 |
| --- | --- |
| Issue | [#9554](https://github.com/vllm-project/vllm/issues/9554) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;import_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: vLLM does not support torch 2.5

### Issue 正文摘录

### Your current environment ```text WARNING 10-21 14:21:00 _custom_ops.py:19] Failed to import from vllm._C with ImportError('libcuda.so.1: cannot open shared object file: No such file or directory') PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 24.04.1 LTS (x86_64) GCC version: (Ubuntu 13.2.0-23ubuntu4) 13.2.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.39 Python version: 3.12.6 (main, Oct 21 2024, 14:12:25) [GCC 13.2.0] (64-bit runtime) Python platform: Linux-6.8.0-1015-gcp-x86_64-with-glibc2.39 Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 8 On-line CPU(s) list: 0-7 Vendor ID: GenuineIntel Model name: Intel(R) Xeon(R) CPU @ 2.20GHz CPU family: 6 Model: 79 Thread(s) per core: 2 Core(s) per socket: 4 Socket(s)...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Installation]: vLLM does not support torch 2.5 installation ### Your current environment ```text WARNING 10-21 14:21:00 _custom_ops.py:19] Failed to import from vllm._C with ImportError('libcuda.so.1: cannot open shared
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: 00 _custom_ops.py:19] Failed to import from vllm._C with ImportError('libcuda.so.1: cannot open shared object file: No such file or directory') PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTor...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNN...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Vulnerability Meltdown: Mitigation; PTI Vulnerability Mmio stale data: Vulnerable: Clear CPU buffers attempted, no microcode; SMT Host state unknown Vulnerability Reg file data sampling: Not affected Vulnerability Retbl...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rch==2.4.0 [pip3] torchvision==0.19.0 [pip3] transformers==4.45.2 [pip3] triton==3.0.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.6.3.post1 vLLM Build Flags: CUDA A...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
