# vllm-project/vllm#35169: [Bug]: Memory Access Fault during Step-3.5-Flash inference (ROCM)

| 字段 | 值 |
| --- | --- |
| Issue | [#35169](https://github.com/vllm-project/vllm/issues/35169) |
| 状态 | open |
| 标签 | bug;rocm |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Memory Access Fault during Step-3.5-Flash inference (ROCM)

### Issue 正文摘录

### Your current environment The output of python collect_env.py ```text ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version : 20.0.0git (https://github.com/RadeonOpenCompute/llvm-project roc-7.0.0 25314 f4087f6b428f0e6f575ebac8a8a724dab123d06e) CMake version : version 3.31.10 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.9.1+git8907517 Is debug build : False CUDA used to build PyTorch : N/A ROCM used to build PyTorch : 7.0.51831-a3e329ad8 ============================== Python Environment ============================== Python version : 3.12.12 (main, Oct 10 2025, 08:52:57) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-5.15.0-144-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : Could not collect CUDA_MODULE_LOADING set to : GPU models and configuration : (gfx950:sramecc+:xnack-) Nvidia driver version : Could not collect cuDNN version : Could not collect HIP runtime version :...

## 现有链接修复摘要

#36374 [Bugfix][ROCm] full graph capture on triton-attn fix - Option1

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version : 20.0.0git (https://github.com/RadeonOpenCompute/llvm-project roc-7.0.0 25314 f4087f6b428f0e6f575ebac8a8a72...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: Memory Access Fault during Step-3.5-Flash inference (ROCM) bug;rocm ### Your current environment The output of python collect_env.py ```text ============================== System Info ============================...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: n cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl avx512vbmi umip pku ospke avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnn...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local avx_vnni avx512_bf16 clzero irperf xsaveerptr rdpru wbnoinvd amd_ppin cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: version : 2.9.1+git8907517 Is debug build : False CUDA used to build PyTorch : N/A ROCM used to build PyTorch : 7.0.51831-a3e329ad8 ============================== Python Environment ============================== Python...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36374](https://github.com/vllm-project/vllm/pull/36374) | closes_keyword | 0.95 | [Bugfix][ROCm] full graph capture on triton-attn fix - Option1 | Fix ROCm full CUDA graph capture fault with Triton attention (#35169) and (#34154). On ROCm, full graph capture triggered “Write access to read-only page” because the Triton 3D a |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
