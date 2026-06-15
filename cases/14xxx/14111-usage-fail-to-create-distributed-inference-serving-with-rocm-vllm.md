# vllm-project/vllm#14111: [Usage]: Fail to create distributed inference serving with rocm/vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#14111](https://github.com/vllm-project/vllm/issues/14111) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Fail to create distributed inference serving with rocm/vllm

### Issue 正文摘录

### Your current environment ```text root@tw033:~# python collect_env.py INFO 03-03 03:18:21 __init__.py:179] Automatically detected platform rocm. WARNING 03-03 03:18:21 rocm.py:34] `fork` method is not supported by ROCm. VLLM_WORKER_MULTIPROC_METHOD is overridden to `spawn` instead. Collecting environment information... PyTorch version: 2.7.0a0+git3a58512 Is debug build: False CUDA used to build PyTorch: N/A ROCM used to build PyTorch: 6.3.42133-1b9c17779 OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: 18.0.0git (https://github.com/RadeonOpenCompute/llvm-project roc-6.3.1 24491 1e0fda770a2079fbd71e4b70974d74f62fd3af10) CMake version: version 3.31.4 Libc version: glibc-2.35 Python version: 3.12.8 (main, Dec 4 2024, 08:54:12) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.15.0-116-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: AMD Instinct MI300X (gfx942:sramecc+:xnack-) Nvidia driver version: Could not collect cuDNN version: Could not collect HIP runtime version: 6.3.42133 MIOpen runtime version: 3.3.0 Is XNNPACK a...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ridden to `spawn` instead. Collecting environment information... PyTorch version: 2.7.0a0+git3a58512 Is debug build: False CUDA used to build PyTorch: N/A ROCM used to build PyTorch: 6.3.42133-1b9c17779 OS: Ubuntu 22.04...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: n cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl avx512vbmi umip pku ospke avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnn...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: [Usage]: Fail to create distributed inference serving with rocm/vllm usage ### Your current environment ```text root@tw033:~# python collect_env.py INFO 03-03 03:18:21 __init__.py:179] Automatically detected platform ro...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local avx512_bf16 clzero irperf xsaveerptr rdpru wbnoinvd amd_ppin cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefil...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: TIPROC_METHOD is overridden to `spawn` instead. Collecting environment information... PyTorch version: 2.7.0a0+git3a58512 Is debug build: False CUDA used to build PyTorch: N/A ROCM used to build PyTorch: 6.3.42133-1b9c1...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
