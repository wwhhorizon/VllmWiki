# vllm-project/vllm#33666: [Bug]: `RotaryEmbedding+KVCache` ops unable to pattern match for `ROCmAiterTritonRopeReshapeKVCacheFusionPass`

| 字段 | 值 |
| --- | --- |
| Issue | [#33666](https://github.com/vllm-project/vllm/issues/33666) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: `RotaryEmbedding+KVCache` ops unable to pattern match for `ROCmAiterTritonRopeReshapeKVCacheFusionPass`

### Issue 正文摘录

### Your current environment ``` Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version : 20.0.0git (https://github.com/RadeonOpenCompute/llvm-project roc-7.0.0 25314 f4087f6b428f0e6f575ebac8a8a724dab123d06e) CMake version : version 3.31.10 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.9.1+git8907517 Is debug build : False CUDA used to build PyTorch : N/A ROCM used to build PyTorch : 7.0.51831-a3e329ad8 ============================== Python Environment ============================== Python version : 3.12.12 (main, Oct 10 2025, 08:52:57) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-6.8.2-amdsos-build58-ubuntu-22.04+-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : Could not collect CUDA_MODULE_LOADING set to : GPU models and configuration : (gfx950:sramecc+:xnack-) Nvidia driver version : Could not collect cuDNN version : Could not collect HIP run...

## 现有链接修复摘要

#27165 [Kernel][Perf] fuse QK Norm and RoPE into one cuda kernel for Qwen Model | #33443 [ROCm] AITER fused RoPE+KVCache | #34037 [ROCm][AITER] Add fused RoPE+KVCache pass with MultiOutputPattern fix

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version : 20.0.0git (https://github.com/RadeonOpenCompute/llvm-project roc-7.0.0 25314 f4087f6b428f0e6f575ebac8a8a72...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: `RotaryEmbedding+KVCache` ops unable to pattern match for `ROCmAiterTritonRopeReshapeKVCacheFusionPass` bug;rocm ### Your current environment ``` Collecting environment information... ============================...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ass` bug;rocm ### Your current environment ``` Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local avx_vnni avx512_bf16 clzero irperf xsaveerptr rdpru wbnoinvd amd_ppin cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: n cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif x2avic v_spec_ctrl vnmi avx512vbmi umip pku ospke avx512_vbmi2 gfni vaes vpclmulqd...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#27165](https://github.com/vllm-project/vllm/pull/27165) | mentioned | 0.45 | [Kernel][Perf] fuse QK Norm and RoPE into one cuda kernel for Qwen Model | sponding graph. i've reused the rotaryembedding customop matcher from #27165, which partially helped, but there's still a bug (described below). please see the relevant definition… |
| [#33443](https://github.com/vllm-project/vllm/pull/33443) | mentioned | 0.45 | [ROCm] AITER fused RoPE+KVCache | test_rope_kvcache_fusion.py` i'm working on the pattern matching for #33443, but i can't seem to get the inductor pattern to match with the corresponding graph. i've reused the ro… |
| [#34037](https://github.com/vllm-project/vllm/pull/34037) | closes_keyword | 0.95 | [ROCm][AITER] Add fused RoPE+KVCache pass with MultiOutputPattern fix | Fix for #33666:** PyTorch's `MultiOutputPattern` only traces the first output's subgraph for anchor node discovery. By returning `(dummy, q, k, v)` instead of `(q, k, v, dummy)`, t |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
