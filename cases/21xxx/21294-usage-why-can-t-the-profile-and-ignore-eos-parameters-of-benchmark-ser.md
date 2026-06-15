# vllm-project/vllm#21294: [Usage]: Why can't the --profile and --ignore-eos parameters of benchmark_serving take effect at the same time?

| 字段 | 值 |
| --- | --- |
| Issue | [#21294](https://github.com/vllm-project/vllm/issues/21294) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Why can't the --profile and --ignore-eos parameters of benchmark_serving take effect at the same time?

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.4.1 Is debug build: False CUDA used to build PyTorch: N/A ROCM used to build PyTorch: 6.3.25211 OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: 15.0.0 CMake version: version 3.29.0 Libc version: glibc-2.35 Python version: 3.10.12 (main, May 27 2025, 17:12:29) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-4.18.0-348.el8.x86_64-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: K100_AI (gfx928:sramecc+:xnack-) Nvidia driver version: Could not collect cuDNN version: Could not collect HIP runtime version: 6.3.25211 MIOpen runtime version: 2.17.0 Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 52 bits physical, 57 bits virtual Byte Order: Little Endian CPU(s): 128 On-line CPU(s) list: 0-127 Vendor ID: GenuineIntel Model name: Intel(R) Xeon(R) Gold 6430 CPU family: 6 Model: 143 Thread(s) per core: 2 Core(s) per socket: 32 Socket(s): 2 Stepping: 8 Frequency boost: enabled CPU max MHz: 2101.0000 CPU min MHz: 800.0000 BogoMIPS: 4200...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ct at the same time? usage ### Your current environment ```text PyTorch version: 2.4.1 Is debug build: False CUDA used to build PyTorch: N/A ROCM used to build PyTorch: 6.3.25211 OS: Ubuntu 22.04.5 LTS (x86_64) GCC vers...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: urrent environment ```text PyTorch version: 2.4.1 Is debug build: False CUDA used to build PyTorch: N/A ROCM used to build PyTorch: 6.3.25211 OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: K100_AI (gfx928:sramecc+:xnack-) Nvidia driver version: Could not collect cuDNN version: Could not collect HIP runtime ve...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Usage]: Why can't the --profile and --ignore-eos parameters of benchmark_serving take effect at the same time? usage ### Your current environment ```text PyTorch version: 2.4.1 Is debug build: False CUDA used to build...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: _occup_llc cqm_mbm_total cqm_mbm_local split_lock_detect avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg tme avx512_vpo...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
