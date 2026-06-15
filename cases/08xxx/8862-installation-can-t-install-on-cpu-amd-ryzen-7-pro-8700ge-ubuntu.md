# vllm-project/vllm#8862: [Installation]: can't install on cpu AMD Ryzen 7 PRO 8700GE ubuntu 

| 字段 | 值 |
| --- | --- |
| Issue | [#8862](https://github.com/vllm-project/vllm/issues/8862) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;kernel;operator;sampling;triton |
| 症状 | build_error;import_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: can't install on cpu AMD Ryzen 7 PRO 8700GE ubuntu 

### Issue 正文摘录

### Your current environment ```text Collecting environment information... WARNING 09-26 18:43:17 _custom_ops.py:18] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") INFO 09-26 18:43:17 importing.py:10] Triton not installed; certain GPU-related functions will not be available. PyTorch version: 2.4.0+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 24.04.1 LTS (x86_64) GCC version: (Ubuntu 12.3.0-17ubuntu1) 12.3.0 Clang version: Could not collect CMake version: version 3.30.3 Libc version: glibc-2.39 Python version: 3.12.3 (main, Sep 11 2024, 14:17:37) [GCC 13.2.0] (64-bit runtime) Python platform: Linux-6.8.0-45-generic-x86_64-with-glibc2.39 Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 48 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 16 On-line CPU(s) list: 0-15 Vendor ID: AuthenticAMD Model nam...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Installation]: can't install on cpu AMD Ryzen 7 PRO 8700GE ubuntu installation ### Your current environment ```text Collecting environment information... WARNING 09-26 18:43:17 _custom_ops.py:18] Failed to import from
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: will not be available. PyTorch version: 2.4.0+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 24.04.1 LTS (x86_64) GCC version: (Ubuntu 12.3.0-17ubuntu1) 12.3.0 Clan...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: tallation ### Your current environment ```text Collecting environment information... WARNING 09-26 18:43:17 _custom_ops.py:18] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") INFO 09-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: d cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif x2avic v_spec_ctrl vnmi avx512vbmi umip pku ospke avx512_vbmi2 gfni vaes vpclmulqd...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: aves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local user_shstk avx512_bf16 clzero irperf xsaveerptr rdpru wbnoinvd cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfth...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
