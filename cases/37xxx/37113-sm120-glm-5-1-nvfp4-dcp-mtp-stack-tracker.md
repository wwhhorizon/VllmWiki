# vllm-project/vllm#37113: [SM120][GLM-5.1] NVFP4 DCP/MTP stack tracker

| 字段 | 值 |
| --- | --- |
| Issue | [#37113](https://github.com/vllm-project/vllm/issues/37113) |
| 状态 | open |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;moe;sampling |
| 症状 | slowdown |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [SM120][GLM-5.1] NVFP4 DCP/MTP stack tracker

### Issue 正文摘录

This issue tracks the PR stack and launch contract for the GLM-5.1 NVFP4 SM120 vLLM configuration we are validating. The goal is that someone can rebuild the same runtime state from the PRs below, install the same external runtime dependencies, and launch vLLM with the same arguments. ## Runtime Target - Model: `lukealonso/GLM-5.1-NVFP4` - Runtime: vLLM with the PR stack listed below - GPUs: 8x SM120 - Tensor parallel: `8` - Decode context parallel: `4` - MTP draft tokens: `3` - Rejection sampling: `probabilistic` - KV cache dtype: `bfloat16` - Target MoE backend: `b12x` - Draft MoE backend: `flashinfer_cutlass` - External `b12x` package: `0.8.3` ## PR Stack - #39550: model-side loading for appended GLM NextN/MTP draft layers. - #39632: MTP runtime metadata reuse and DCP-aware draft execution plumbing. - #39633: PCIe custom-allreduce eligibility for the explicit PCIe opt-in path. - #39634: optional SM120 `b12x` NVFP4 MoE and dense FP4 backend integration. - #39635: FlashInfer MLA decode/runtime handling for DCP + MTP target validation. ## Current Launch The model config is used directly for context length; current logs show `max_seq_len=202752`. ```bash export HF_HUB_OFFLINE=1 exp...

## 现有链接修复摘要

#39634 [SM120][B12X] Add b12x NVFP4 MoE and dense backends | #39635 [SM120][MLA] Fix FlashInfer MLA DCP/MTP decode path | #40750 [Attention] Enable TRITON_MLA MTP full CUDA graphs for Kimi on Blackwell

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [SM120][GLM-5.1] NVFP4 DCP/MTP stack tracker This issue tracks the PR stack and launch contract for the GLM-5.1 NVFP4 SM120 vLLM configuration we are validating. The goal is that someone can rebuild the same runtime sta...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: with the PR stack listed below - GPUs: 8x SM120 - Tensor parallel: `8` - Decode context parallel: `4` - MTP draft tokens: `3` - Rejection sampling: `probabilistic` - KV cache dtype: `bfloat16` - Target MoE backend: `b12...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: tion sampling: `probabilistic` - KV cache dtype: `bfloat16` - Target MoE backend: `b12x` - Draft MoE backend: `flashinfer_cutlass` - External `b12x` package: `0.8.3` ## PR Stack - #39550: model-side loading for appended...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: 20 vLLM configuration we are validating. The goal is that someone can rebuild the same runtime state from the PRs below, install the same external runtime dependencies, and launch vLLM with the same arguments. ## Runtim...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [SM120][GLM-5.1] NVFP4 DCP/MTP stack tracker This issue tracks the PR stack and launch contract for the GLM-5.1 NVFP4 SM120 vLLM configuration we are validating. The goal is that someone can rebuild the same runtime stat

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39634](https://github.com/vllm-project/vllm/pull/39634) | mentioned | 0.6 | [SM120][B12X] Add b12x NVFP4 MoE and dense backends | [SM120][B12X] Add b12x NVFP4 MoE and dense backends Tracked in #37113. `b12x` is an external SM120-oriented kernel library for NVFP4 dense FP4 GEMM and MoE. On supported SM120 de |
| [#39635](https://github.com/vllm-project/vllm/pull/39635) | closes_keyword | 0.95 | [SM120][MLA] Fix FlashInfer MLA DCP/MTP decode path | Fix FlashInfer MLA DCP/MTP decode path Tracked in #37113. This PR fixes the FlashInfer MLA decode/runtime path used when GLM-5.1 runs with DCP and MTP enabled. ## Problem During |
| [#40750](https://github.com/vllm-project/vllm/pull/40750) | mentioned | 0.6 | [Attention] Enable TRITON_MLA MTP full CUDA graphs for Kimi on Blackwell | PCIe custom-allreduce prerequisite is tracked separately in #39633 / #37113 and is included here so this draft branch is runnable end-to-end. ## Validation Local validation: - `py… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
