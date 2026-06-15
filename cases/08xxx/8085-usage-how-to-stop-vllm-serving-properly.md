# vllm-project/vllm#8085: [Usage]: How to stop vllm serving properly?

| 字段 | 值 |
| --- | --- |
| Issue | [#8085](https://github.com/vllm-project/vllm/issues/8085) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to stop vllm serving properly?

### Issue 正文摘录

### Your current environment The output of `python collect_env.py` ``` PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Red Hat Enterprise Linux 9.4 (Plow) (x86_64) GCC version: (GCC) 11.4.1 20231218 (Red Hat 11.4.1-3) Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.34 Python version: 3.10.14 (main, May 6 2024, 19:42:50) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.14.0-427.31.1.el9_4.x86_64-x86_64-with-glibc2.34 Is CUDA available: True CUDA runtime version: 12.6.20 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L40S GPU 1: NVIDIA L40S GPU 2: NVIDIA L40S GPU 3: NVIDIA L40S Nvidia driver version: 560.28.03 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 52 bits physical, 57 bits virtual Byte Order: Little Endian CPU(s): 256 On-line CPU(s) list: 0-255 Vendor ID: AuthenticAMD BIOS Vendor ID: Advanced Micro Devices, Inc. Model name: AMD EPYC 9554 64-Core Processor BIOS Model name: AMD EPYC 9554 64-Core...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: n cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif x2avic v_spec_ctrl vnmi avx512vbmi umip pku ospke avx512_vbmi2 gfni vaes vpclmulqd...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: r current environment The output of `python collect_env.py` ``` PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Red Hat Enterprise Linux 9.4 (Plow)...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local avx512_bf16 clzero irperf xsaveerptr rdpru wbnoinvd amd_ppin cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefil...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: n collect_env.py` ``` PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Red Hat Enterprise Linux 9.4 (Plow) (x86_64) GCC version: (GCC) 11.4.1 202312...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: True CUDA runtime version: 12.6.20 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L40S GPU 1: NVIDIA L40S GPU 2: NVIDIA L40S GPU 3: NVIDIA L40S Nvidia driver version: 560.28.03 cuDNN versio...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
