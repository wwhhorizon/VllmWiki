# vllm-project/vllm#15640: [Usage]: profiling.py broken on v0.8.1

| 字段 | 值 |
| --- | --- |
| Issue | [#15640](https://github.com/vllm-project/vllm/issues/15640) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: profiling.py broken on v0.8.1

### Issue 正文摘录

### Your current environment ```text INFO 03-27 15:09:21 [__init__.py:256] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.6.0+cu126 Is debug build: False CUDA used to build PyTorch: 12.6 ROCM used to build PyTorch: N/A OS: Ubuntu 24.04.2 LTS (aarch64) GCC version: (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.39 Python version: 3.12.9 (main, Mar 17 2025, 20:48:41) [GCC 6.3.0 20170516] (64-bit runtime) Python platform: Linux-5.14.0-362.24.1.el9_3.aarch64+64k-aarch64-with-glibc2.39 Is CUDA available: True CUDA runtime version: 12.6.85 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GH200 120GB Nvidia driver version: 560.35.03 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: aarch64 CPU op-mode(s): 64-bit Byte Order: Little Endian CPU(s): 72 On-line CPU(s) list: 0-71 Vendor ID: ARM Model name: Neoverse-V2 Model: 0 Thread(s) per core: 1 Core(s) per socket: 72 Socket(s): 1 Stepping: r0p0 Frequency boost: disabled CPU(s) scaling MHz: 100% CPU max MHz:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ly detected platform cuda. Collecting environment information... PyTorch version: 2.6.0+cu126 Is debug build: False CUDA used to build PyTorch: 12.6 ROCM used to build PyTorch: N/A OS: Ubuntu 24.04.2 LTS (aarch64) GCC v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: xt INFO 03-27 15:09:21 [__init__.py:256] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.6.0+cu126 Is debug build: False CUDA used to build PyTorch: 12.6 ROCM used to build...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: p sve2 sveaes svepmull svebitperm svesha3 svesm4 flagm2 frint svei8mm svebf16 i8mm bf16 dgh L1d cache: 4.5 MiB (72 instances) L1i cache: 4.5 MiB (72 instances) L2 cache: 72 MiB (72 instances) L3 cache:
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: _.py:256] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.6.0+cu126 Is debug build: False CUDA used to build PyTorch: 12.6 ROCM used to build PyTorch: N/A OS: Ubuntu 24.04....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Usage]: profiling.py broken on v0.8.1 usage;stale ### Your current environment ```text INFO 03-27 15:09:21 [__init__.py:256] Automatically detected platform cuda. Collecting environment information... PyTorch version:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
