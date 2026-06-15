# vllm-project/vllm#4131: [Bug]: Invalid Device Ordinal on ROCm

| 字段 | 值 |
| --- | --- |
| Issue | [#4131](https://github.com/vllm-project/vllm/issues/4131) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Invalid Device Ordinal on ROCm

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.4.0.dev20240415+rocm6.0 Is debug build: False CUDA used to build PyTorch: N/A ROCM used to build PyTorch: 6.0.32830-d62f6a171 OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.29.2 Libc version: glibc-2.35 Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.15.0-102-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: AMD Instinct MI300X (gfx942:sramecc+:xnack-) Nvidia driver version: Could not collect cuDNN version: Could not collect HIP runtime version: 6.0.32830 MIOpen runtime version: 3.0.0 Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 52 bits physical, 57 bits virtual Byte Order: Little Endian CPU(s): 384 On-line CPU(s) list: 0-383 Vendor ID: AuthenticAMD Model name: AMD EPYC 9654 96-Core Processor CPU family: 25 Model: 17 Thread(s) per core: 2 Core(s) per socket: 96 Socket(s): 2 Stepping: 1 Frequency boost: enabled CPU m...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: e Ordinal on ROCm bug;rocm ### Your current environment ```text PyTorch version: 2.4.0.dev20240415+rocm6.0 Is debug build: False CUDA used to build PyTorch: N/A ROCM used to build PyTorch: 6.0.32830-d62f6a171 OS: Ubuntu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: [Bug]: Invalid Device Ordinal on ROCm bug;rocm ### Your current environment ```text PyTorch version: 2.4.0.dev20240415+rocm6.0 Is debug build: False CUDA used to build PyTorch: N/A ROCM used to build PyTorch: 6.0.32830-...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local avx512_bf16 clzero irperf xsaveerptr rdpru wbnoinvd amd_ppin cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefil...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: n cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl avx512vbmi umip pku ospke avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnn...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: AMD Instinct MI300X (gfx942:sramecc+:xnack-) Nvidia driver version: Could not collect cuDNN version: Could not collect HI...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
