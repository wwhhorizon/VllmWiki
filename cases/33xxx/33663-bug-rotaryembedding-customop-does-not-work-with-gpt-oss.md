# vllm-project/vllm#33663: [Bug]: `RotaryEmbedding` CustomOp does not work with gpt-oss

| 字段 | 值 |
| --- | --- |
| Issue | [#33663](https://github.com/vllm-project/vllm/issues/33663) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: `RotaryEmbedding` CustomOp does not work with gpt-oss

### Issue 正文摘录

### Your current environment ``` Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version : 20.0.0git (https://github.com/RadeonOpenCompute/llvm-project roc-7.0.0 25314 f4087f6b428f0e6f575ebac8a8a724dab123d06e) CMake version : version 3.31.10 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.9.1+git8907517 Is debug build : False CUDA used to build PyTorch : N/A ROCM used to build PyTorch : 7.0.51831-a3e329ad8 ============================== Python Environment ============================== Python version : 3.12.12 (main, Oct 10 2025, 08:52:57) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-6.8.2-amdsos-build58-ubuntu-22.04+-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : Could not collect CUDA_MODULE_LOADING set to : GPU models and configuration : (gfx950:sramecc+:xnack-) Nvidia driver version : Could not collect cuDNN version : Could not collect HIP run...

## 现有链接修复摘要

#33443 [ROCm] AITER fused RoPE+KVCache | #33800 [Bugfix] Support `RotaryEmbedding` CustomOp for gpt-oss

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version : 20.0.0git (https://github.com/RadeonOpenCompute/llvm-project roc-7.0.0 25314 f4087f6b428f0e6f575ebac8a8a72...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: `RotaryEmbedding` CustomOp does not work with gpt-oss bug;rocm ### Your current environment ``` Collecting environment information... ============================== System Info ============================== OS :...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local avx_vnni avx512_bf16 clzero irperf xsaveerptr rdpru wbnoinvd amd_ppin cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: `RotaryEmbedding` CustomOp does not work with gpt-oss bug;rocm ### Your current environment ``` Collecting environment information... ============================== System Info ============================== OS :...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: n cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif x2avic v_spec_ctrl vnmi avx512vbmi umip pku ospke avx512_vbmi2 gfni vaes vpclmulqd...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#33443](https://github.com/vllm-project/vllm/pull/33443) | mentioned | 0.45 | [ROCm] AITER fused RoPE+KVCache | uctor_compile_threads=1 ``` ### 🐛 describe the bug while working on #33443, i'm hitting the following error for gpt-oss (works on llama, mixtral, qwen, etc): `vllm serve openai/gp… |
| [#33800](https://github.com/vllm-project/vllm/pull/33800) | closes_keyword | 0.95 | [Bugfix] Support `RotaryEmbedding` CustomOp for gpt-oss | Fixes #33663. ## Purpose Prevent RoPE’s `cos_sin_cache` buffer from being mutated during `torch.compile` with cudagraphs, which caused gpt-oss with `+rotary_embedding` to fail at |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
