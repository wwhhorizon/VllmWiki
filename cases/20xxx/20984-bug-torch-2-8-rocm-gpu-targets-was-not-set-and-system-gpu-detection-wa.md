# vllm-project/vllm#20984: [Bug][torch 2.8][rocm] GPU_TARGETS was not set, and system GPU detection was unsuccsesful

| 字段 | 值 |
| --- | --- |
| Issue | [#20984](https://github.com/vllm-project/vllm/issues/20984) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug][torch 2.8][rocm] GPU_TARGETS was not set, and system GPU detection was unsuccsesful

### Issue 正文摘录

### Your current environment ``` ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 3.31.6 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.8.0+rocm6.4 Is debug build : False CUDA used to build PyTorch : N/A ROCM used to build PyTorch : 6.4.43482-0f2d60242 ============================== Python Environment ============================== Python version : 3.12.10 | packaged by conda-forge | (main, Apr 10 2025, 22:21:13) [GCC 13.3.0] (64-bit runtime) Python platform : Linux-6.8.0-60-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : Could not collect CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : AMD Instinct MI300X (gfx942:sramecc+:xnack-) Nvidia driver version : Could not collect cuDNN version : Could not collect HIP runtime version : 6.4.43482 MIOpen runtime version : 3.4.0 Is XNNPACK available : True ==========================...

## 现有链接修复摘要

#21 Add ninja to dependency

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 3.31.6 Libc version : glibc-2.35 =================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: [Bug][torch 2.8][rocm] GPU_TARGETS was not set, and system GPU detection was unsuccsesful bug;stale ### Your current environment ``` ============================== System Info ============================== OS
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: sion : Could not collect CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : AMD Instinct MI300X (gfx942:sramecc+:xnack-) Nvidia driver version : Could not collect cuDNN version : Could not collect HIP runt...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ] GPU_TARGETS was not set, and system GPU detection was unsuccsesful bug;stale ### Your current environment ``` ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64)...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: aves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local user_shstk avx512_bf16 clzero irperf xsaveerptr rdpru wbnoinvd amd_ppin cppc amd_ibpb_ret arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeas...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#21](https://github.com/vllm-project/vllm/pull/21) | mentioned | 0.45 | Add ninja to dependency | for subsuqent #21 5.251 compilations, and the default architecture #21 5.251 (gfx906 for dynamic build / gfx942 for static build) will be used ``` this may or may not be relate |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
