# vllm-project/vllm#9587: [Bug]: llama-3.1-8b-instruct running v0.6.3.post1 crash on h20

| 字段 | 值 |
| --- | --- |
| Issue | [#9587](https://github.com/vllm-project/vllm/issues/9587) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: llama-3.1-8b-instruct running v0.6.3.post1 crash on h20

### Issue 正文摘录

### Your current environment Collecting environment information... /usr/local/lib/python3.12/dist-packages/torch/cuda/__init__.py:654: UserWarning: Can't initialize NVML warnings.warn("Can't initialize NVML") PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.35 Python version: 3.12.7 (main, Oct 1 2024, 08:52:12) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.15.0-124-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: Could not collect Nvidia driver version: Could not collect cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 52 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 128 On-line CPU(s) list: 0-127 Vendor ID: AuthenticAMD Model name: AMD EPYC 9K84 96-Core Processor CPU family: 25 M...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: : Can't initialize NVML warnings.warn("Can't initialize NVML") PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC vers...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: ed Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Reg file data sampling: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Mitigation;...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: pt clwb avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 avx512_bf16 clzero xsaveerptr wbnoinvd arat avx512vbmi umip avx512_vbmi2 vaes vpclmulqdq avx512_vnni avx512_bitalg avx512_vpopcntdq rdpid fsrm Hypervisor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: environment information... /usr/local/lib/python3.12/dist-packages/torch/cuda/__init__.py:654: UserWarning: Can't initialize NVML warnings.warn("Can't initialize NVML") PyTorch version: 2.4.0+cu121 Is debug build: False...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: llama-3.1-8b-instruct running v0.6.3.post1 crash on h20 bug ### Your current environment Collecting environment information... /usr/local/lib/python3.12/dist-packages/torch/cuda/__init__.py:654: UserWarning: Can'...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
