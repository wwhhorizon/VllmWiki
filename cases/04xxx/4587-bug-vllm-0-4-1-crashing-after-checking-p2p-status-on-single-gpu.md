# vllm-project/vllm#4587: [Bug]: vllm 0.4.1 crashing after checking P2P status on single GPU 

| 字段 | 值 |
| --- | --- |
| Issue | [#4587](https://github.com/vllm-project/vllm/issues/4587) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm 0.4.1 crashing after checking P2P status on single GPU 

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.29.2 Libc version: glibc-2.35 Python version: 3.10.13 (main, Sep 11 2023, 13:44:35) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.3.52 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: GRID A100X-40C Nvidia driver version: 535.129.03 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 40 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 32 On-line CPU(s) list: 0-31 Vendor ID: AuthenticAMD Model name: AMD EPYC-Milan Processor CPU family: 25 Model: 1 Thread(s) per core: 1 Core(s) per socket: 1 Socket(s): 32 Stepping: 1 BogoMIPS: 3992.50 Flags: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge m...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: rrent environment ```text Collecting environment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: bug;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ec xgetbv1 xsaves clzero xsaveerptr wbnoinvd arat npt lbrv nrip_save tsc_scale vmcb_clean pausefilter pfthreshold umip pku ospke vaes vpclmulqdq rdpid arch_capabilities Virtualization: AMD-V Hypervisor vendor: KVM Virtu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: torch==2.2.1 [pip3] torchaudio==2.2.1 [pip3] torchvision==0.17.1 [pip3] triton==2.2.0 [pip3] vllm-nccl-cu12==2.18.1.0.4.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-nccl-cu12 2.19.3 pypi_0 pypi [conda] torch

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
