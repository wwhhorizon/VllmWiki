# vllm-project/vllm#5222: [Usage]: RuntimeError: CUDA error: uncorrectable ECC error encountered

| 字段 | 值 |
| --- | --- |
| Issue | [#5222](https://github.com/vllm-project/vllm/issues/5222) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: RuntimeError: CUDA error: uncorrectable ECC error encountered

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: version 3.29.3 Libc version: glibc-2.31 Python version: 3.8.10 (default, Nov 22 2023, 10:22:35) [GCC 9.4.0] (64-bit runtime) Python platform: Linux-5.4.0-182-generic-x86_64-with-glibc2.29 Is CUDA available: True CUDA runtime version: 12.4.131 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-40GB Nvidia driver version: 550.54.14 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 44 bits physical, 48 bits virtual CPU(s): 4 On-line CPU(s) list: 0-3 Thread(s) per core: 2 Core(s) per socket: 2 Socket(s): 1 NUMA node(s): 1 Vendor ID: AuthenticAMD CPU family: 25 Model: 17 Model name: AMD EPYC 9354 32-Core Processor Stepping: 1 CPU MHz: 3245.141 BogoMIPS: 6490.28 Hypervisor vendor: Microsoft Virtualization type: ful...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: CC error encountered usage ### Your current environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Usage]: RuntimeError: CUDA error: uncorrectable ECC error encountered usage ### Your current environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build Py...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: True CUDA runtime version: 12.4.131 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-40GB Nvidia driver version: 550.54.14 cuDNN version: Could not collect HIP runtime version: N/A...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: he following error: WARNING 06-03 17:32:17 config.py:1155] Casting torch.bfloat16 to torch.float16. WARNING 06-03 17:32:17 config.py:427] Possibly too large swap space. 4.00 GiB out of the 7.70 GiB total CPU memory is a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec store bypass: Vulnerable Vulnerability Spectre v1: Mitigation; usercopy/swapg...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
