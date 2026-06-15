# vllm-project/vllm#30167: [Bug][ROCm]: `vision_embeddings` in transformers inaccurate without math SDP

| 字段 | 值 |
| --- | --- |
| Issue | [#30167](https://github.com/vllm-project/vllm/issues/30167) |
| 状态 | open |
| 标签 | bug;rocm;unstale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf;oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][ROCm]: `vision_embeddings` in transformers inaccurate without math SDP

### Issue 正文摘录

``` ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version : 20.0.0git (https://github.com/RadeonOpenCompute/llvm-project roc-7.1.0 25425 1b0eada6b0ee93e2e694c8c146d23fca90bc11c5) CMake version : version 3.31.10 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.9.0a0+git1c57644 Is debug build : False CUDA used to build PyTorch : N/A ROCM used to build PyTorch : 7.1.25424-4179531dcd ============================== Python Environment ============================== Python version : 3.12.12 (main, Oct 10 2025, 08:52:57) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-5.15.0-161-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : Could not collect CUDA_MODULE_LOADING set to : GPU models and configuration : (gfx942:sramecc+:xnack-) Nvidia driver version : Could not collect cuDNN version : Could not collect HIP runtime version : 7.1.25424 MIOpen runtime version : 3.5.1 Is XNNPACK available : T...

## 现有链接修复摘要

#30270 [ROCm][CI][Bugfix] Multi-Modal Model Support Fixes and Attention Backend Improvements | #31612 [ROCm][CI] Fix ModernBERT token classification test

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version : 20.0.0git (https://github.com/RadeonOpenCompute/llvm-project roc-7.1.0 25425 1b0eada6b0ee93e2e694c8c146d23...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: e version : Could not collect CUDA_MODULE_LOADING set to : GPU models and configuration : (gfx942:sramecc+:xnack-) Nvidia driver version : Could not collect cuDNN version : Could not collect HIP runtime version : 7.1.25...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug][ROCm]: `vision_embeddings` in transformers inaccurate without math SDP bug;rocm;unstale ``` ============================== System Info ============================== OS : Ubuntu 22.04.5
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: g the vLLM Transformers backend produce incorrect/garbage outputs due to accuracy issues with the `flash_sdp` and `mem_efficient_sdp` backends in PyTorch's `scaled_dot_product_attention` when used in vision encoders. **...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: saves cqm_llc cqm_occup_llc cqm_mbm_total cqm_m bm_local avx_vnni avx512_bf16 clzero irperf xsaveerptr rdpru wbnoinvd amd_ppin cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefi...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#30270](https://github.com/vllm-project/vllm/pull/30270) | mentioned | 0.6 | [ROCm][CI][Bugfix] Multi-Modal Model Support Fixes and Attention Backend Improvements | racy issues with `flash_sdp` and `mem_efficient_sdp` - Patches issue [#30167](https://github.com/vllm-project/vllm/issues/30167) **SigLIP2 NaViT (`vllm/model_executor/models/sigli… |
| [#31612](https://github.com/vllm-project/vllm/pull/31612) | mentioned | 0.6 | [ROCm][CI] Fix ModernBERT token classification test | =1e-2`. This is a known HF Transformers accuracy issue on ROCm (see [#30167](https://github.com/vllm-project/vllm/issues/30167)), not a vLLM issue. ## Solution Force HuggingFace t… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
