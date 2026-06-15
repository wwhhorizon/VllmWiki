# vllm-project/vllm#5535: [Bug]: Performance : very slow inference for Mixtral 8x7B Instruct FP8 on H100 with 0.5.0 and 0.5.0.post1

| 字段 | 值 |
| --- | --- |
| Issue | [#5535](https://github.com/vllm-project/vllm/issues/5535) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;moe;operator;quantization;sampling |
| 症状 | build_error;nan_inf;oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Performance : very slow inference for Mixtral 8x7B Instruct FP8 on H100 with 0.5.0 and 0.5.0.post1

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.35 Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.15.0-107-generic-x86_64-with-glibc2.35 Is CUDA available: N/A CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: N/A GPU models and configuration: GPU 0: NVIDIA H100 80GB HBM3 GPU 1: NVIDIA H100 80GB HBM3 Nvidia driver version: 555.42.02 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: N/A CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 45 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 16 On-line CPU(s) list: 0-15 Vendor ID: GenuineIntel Model name: Intel(R) Xeon(R) Gold 5418Y CPU family: 6 Model: 143 Thread(s) per core: 1 Core(s) per socket: 1 Socket(s): 16 Stepping: 8 BogoMIPS: 3999.99 Flags: fpu vme de pse t...

## 现有链接修复摘要

#5327 [MISC] Upgrade dependency to PyTorch 2.3.1

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: rrent environment ```text Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubun...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Bug]: Performance : very slow inference for Mixtral 8x7B Instruct FP8 on H100 with 0.5.0 and 0.5.0.post1 bug ### Your current environment ```text Collecting environment information... PyTorch version: N/A Is debug buil...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: Bug]: Performance : very slow inference for Mixtral 8x7B Instruct FP8 on H100 with 0.5.0 and 0.5.0.post1 bug ### Your current environment ```text Collecting environment information... PyTorch version: N/A Is debug build...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Unknown: No mitigations Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Not affected Vulnerability Spec store bypass: Mit...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: post1 bug ### Your current environment ```text Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_6...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#5327](https://github.com/vllm-project/vllm/pull/5327) | closes_keyword | 0.95 | [MISC] Upgrade dependency to PyTorch 2.3.1 | FIX #5535 FIX #5579 FIX #5705 **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <details> <!-- inside this <details> section, m |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
