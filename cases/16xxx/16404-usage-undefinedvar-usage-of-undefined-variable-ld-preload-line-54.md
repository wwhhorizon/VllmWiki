# vllm-project/vllm#16404: [Usage]: UndefinedVar: Usage of undefined variable '$LD_PRELOAD' (line 54)

| 字段 | 值 |
| --- | --- |
| Issue | [#16404](https://github.com/vllm-project/vllm/issues/16404) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: UndefinedVar: Usage of undefined variable '$LD_PRELOAD' (line 54)

### Issue 正文摘录

### Your current environment Collecting environment information... PyTorch version: 2.6.0+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 24.04.2 LTS (x86_64) GCC version: (Ubuntu 12.3.0-17ubuntu1) 12.3.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.39 Python version: 3.12.3 (main, Feb 4 2025, 14:48:35) [GCC 13.3.0] (64-bit runtime) Python platform: Linux-6.8.0-55-generic-x86_64-with-glibc2.39 Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 52 bits physical, 57 bits virtual Byte Order: Little Endian CPU(s): 344 On-line CPU(s) list: 0-343 Vendor ID: GenuineIntel Model name: Intel(R) Xeon(R) 6787P CPU family: 6 Model: 173 Thread(s) per core: 2 Core(s) per socket: 86 Socket(s): 2 Stepping: 1 CPU(s) scaling MHz: 84% CPU max MHz: 3800.0000 CPU min MHz: 800.0000 BogoMIPS: 4000.00 Flags: fpu vme de pse tsc msr pae...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: Your current environment Collecting environment information... PyTorch version: 2.6.0+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 24.04.2 LTS (x86_64) GCC versio...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ironment information... PyTorch version: 2.6.0+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 24.04.2 LTS (x86_64) GCC version: (Ubuntu 12.3.0-17ubuntu1) 12.3.0 Cla...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ' (line 54) usage ### Your current environment Collecting environment information... PyTorch version: 2.6.0+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 24.04.2 L...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ed Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Reg file data sampling: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Not affecte...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: cqm_mbm_total cqm_mbm_local split_lock_detect user_shstk avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts hwp hwp_act_window hwp_epp hwp_pkg_req vnmi avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmul...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
