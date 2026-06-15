# vllm-project/vllm#3646: [Bug]: No output on WSL (Debian, Windows 11)

| 字段 | 值 |
| --- | --- |
| Issue | [#3646](https://github.com/vllm-project/vllm/issues/3646) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: No output on WSL (Debian, Windows 11)

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 12 (bookworm) (x86_64) GCC version: (Debian 12.2.0-14) 12.2.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.36 Python version: 3.11.2 (main, Mar 13 2023, 12:18:29) [GCC 12.2.0] (64-bit runtime) Python platform: Linux-5.15.146.1-microsoft-standard-WSL2-x86_64-with-glibc2.36 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce GTX 1660 SUPER Nvidia driver version: 546.65 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 48 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 12 On-line CPU(s) list: 0-11 Vendor ID: AuthenticAMD Model name: AMD Ryzen 5 4600G with Radeon Graphics CPU family: 23 Model: 96 Thread(s) per core: 2 Core(s) per socket: 6 Socket(s): 1 Stepping: 1 BogoMIPS: 7385.89 Flags: fpu vme de pse tsc msr pae mce cx8 apic...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: L (Debian, Windows 11) bug ### Your current environment ```text PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 12 (bookworm) (x86...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: sha_ni xsaveopt xsavec xgetbv1 clzero xsaveerptr arat npt nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold v_vmsave_vmload umip rdpid Virtualization: AMD-V Hypervisor vendor: Microsoft Vi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: environment ```text PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 12 (bookworm) (x86_64) GCC version: (Debian 12.2.0-14) 12.2.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce GTX 1660 SUPER Nvidia driver version: 546.65 cuDNN version: Could not collect HIP runtime version:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: v1 clzero xsaveerptr arat npt nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold v_vmsave_vmload umip rdpid Virtualization: AMD-V Hypervisor vendor: Microsoft Virtualization type: full L1d...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
