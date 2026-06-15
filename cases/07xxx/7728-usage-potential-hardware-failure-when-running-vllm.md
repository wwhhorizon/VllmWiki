# vllm-project/vllm#7728: [Usage]: Potential Hardware Failure when running vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#7728](https://github.com/vllm-project/vllm/issues/7728) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Potential Hardware Failure when running vllm

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: openSUSE Tumbleweed (x86_64) GCC version: (SUSE Linux) 13.2.1 20240206 [revision 67ac78caf31f7cb3202177e6428a46d829b70f23] Clang version: Could not collect CMake version: version 3.30.1 Libc version: glibc-2.39 Python version: 3.11.9 (main, Apr 08 2024, 06:18:15) [GCC] (64-bit runtime) Python platform: Linux-6.8.5-1-default-x86_64-with-glibc2.39 Is CUDA available: True CUDA runtime version: 12.4.131 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L40S GPU 1: NVIDIA L40S GPU 2: NVIDIA L40S GPU 3: NVIDIA L40S GPU 4: NVIDIA L40S GPU 5: NVIDIA L40S GPU 6: NVIDIA L40S GPU 7: NVIDIA L40S Nvidia driver version: 550.67 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 52 bits physical, 57 bits virtual Byte Order: Little Endian CPU(s): 48 On-line CPU(s) list: 0-47 Vendor ID: AuthenticAMD BIOS Vendor ID: Advanced Micro Devices, Inc. Model name: AMD EPYC 9254 24-Core Processor...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: re when running vllm usage ### Your current environment ```text PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: openSUSE Tumbleweed (x86_64) GCC ve...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local avx512_bf16 clzero irperf xsaveerptr rdpru wbnoinvd amd_ppin cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefil...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: environment ```text PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: openSUSE Tumbleweed (x86_64) GCC version: (SUSE Linux) 13.2.1 20240206 [revisio...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: True CUDA runtime version: 12.4.131 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L40S GPU 1: NVIDIA L40S GPU 2: NVIDIA L40S GPU 3: NVIDIA L40S GPU 4: NVIDIA L40S GPU 5: NVIDIA L40S GPU 6:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: n cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif x2avic v_spec_ctrl vnmi avx512vbmi umip pku ospke avx512_vbmi2 gfni vaes vpclmulqd...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
