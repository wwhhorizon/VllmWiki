# vllm-project/vllm#12498: [Bug]: triton.runtime.errors.OutOfResources: out of resource: shared memory, Required: 66560, Hardware limit: 65536. Reducing block sizes or `num_stages` may help.

| 字段 | 值 |
| --- | --- |
| Issue | [#12498](https://github.com/vllm-project/vllm/issues/12498) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: triton.runtime.errors.OutOfResources: out of resource: shared memory, Required: 66560, Hardware limit: 65536. Reducing block sizes or `num_stages` may help.

### Issue 正文摘录

### Your current environment Ignore name "vllm_python12" it's really python 3.10. ``` (vllm_python12) root@6e2c9e6215c7:/go# python collect_env.py INFO 01-28 03:22:03 __init__.py:183] Automatically detected platform rocm. WARNING 01-28 03:22:03 rocm.py:31] `fork` method is not supported by ROCm. VLLM_WORKER_MULTIPROC_METHOD is overridden to `spawn` instead. Collecting environment information... PyTorch version: 2.5.1+rocm6.2 Is debug build: False CUDA used to build PyTorch: N/A ROCM used to build PyTorch: 6.2.41133-dd7f95766 OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: 17.0.0 (https://github.com/RadeonOpenCompute/llvm-project roc-6.1.0 24103 7db7f5e49612030319346f900c08f474b1f9023a) CMake version: version 3.31.4 Libc version: glibc-2.35 Python version: 3.10.16 (main, Dec 11 2024, 16:24:50) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-6.5.0-28-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: AMD Instinct MI300X (gfx942:sramecc+:xnack-) Nvidia driver version: Could not collect cuDNN version: Could not collect HIP run...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: of resource: shared memory, Required: 66560, Hardware limit: 65536. Reducing block sizes or `num_stages` may help. bug;stale ### Your current environment Ignore name "vllm_python12" it's really python 3.10. ``` (vllm_py...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 9: ardware limit: 65536. Reducing block sizes or `num_stages` may help. bug;stale ### Your current environment Ignore name "vllm_python12" it's really python 3.10. ``` (vllm_python12) root@6e2c9e6215c7:/go# python collect_...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local avx512_bf16 clzero irperf xsaveerptr rdpru wbnoinvd amd_ppin cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefil...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: .py INFO 01-28 03:22:03 __init__.py:183] Automatically detected platform rocm. WARNING 01-28 03:22:03 rocm.py:31] `fork` method is not supported by ROCm. VLLM_WORKER_MULTIPROC_METHOD is overridden to `spawn` instead. Co...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: esource: shared memory, Required: 66560, Hardware limit: 65536. Reducing block sizes or `num_stages` may help. bug;stale ### Your current environment Ignore name "vllm_python12" it's really python 3.10. ``` (vllm_python...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
