# vllm-project/vllm#14887: [Bug]:0.74 dev ,the error occurred in the gptq_marlin_gemm function call

| 字段 | 值 |
| --- | --- |
| Issue | [#14887](https://github.com/vllm-project/vllm/issues/14887) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:0.74 dev ,the error occurred in the gptq_marlin_gemm function call

### Issue 正文摘录

### Your current environment PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 12.3.0-1ubuntu1~22.04) 12.3.0 Clang version: Could not collect CMake version: version 3.22.1 Libc version: glibc-2.35 Python version: 3.12.9 | packaged by Anaconda, Inc. | (main, Feb 6 2025, 18:56:27) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-6.8.0-52-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.6.85 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L40S GPU 1: NVIDIA L40S GPU 2: NVIDIA L40S GPU 3: NVIDIA L40S GPU 4: NVIDIA L40S GPU 5: NVIDIA L40S GPU 6: NVIDIA L40S GPU 7: NVIDIA L40S Nvidia driver version: 565.57.01 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: 架构： x86_64 CPU 运行模式： 32-bit, 64-bit Address sizes: 52 bits physical, 57 bits virtual 字节序： Little Endian CPU: 64 在线 CPU 列表： 0-63 厂商 ID： GenuineIntel 型号名称： INTEL(R) XEON(R) GOLD 6530 CPU 系列： 6 型号： 207 每个核的线程数： 1 每个座的核数： 32 座： 2 步进： 2 CPU 最大 MHz： 4000.0000 CPU 最小 MHz： 800.0000 BogoMIPS： 420...

## 现有链接修复摘要

#15374 [Bugfix] hotfix for gptq-marlin non-contiguous error

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: arlin_gemm function call bug;stale ### Your current environment PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC ver...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: ]:0.74 dev ,the error occurred in the gptq_marlin_gemm function call bug;stale ### Your current environment PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch:...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: cqm_mbm_total cqm_mbm_local split_lock_detect user_shstk avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts hwp hwp_act_window hwp_epp hwp_pkg_req vnmi avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmul...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 6: Your current environment PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 12.3.0-1ubuntu1~22.04) 12...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: current environment PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 12.3.0-1ubuntu1~22.04) 12.3.0...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#15374](https://github.com/vllm-project/vllm/pull/15374) | closes_keyword | 0.95 | [Bugfix] hotfix for gptq-marlin non-contiguous error | fix #14887 https://github.com/vllm-project/vllm/issues/15386 Hotfix for gptq-marlin non-contiguous error. Previous https://github.com/vllm-project/vllm/pull/15319 only fixed the G |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
