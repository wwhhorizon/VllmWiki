# vllm-project/vllm#39701: [RFC] Replace routing replay with CUDA-graph-compatible device cache approach

| 字段 | 值 |
| --- | --- |
| Issue | [#39701](https://github.com/vllm-project/vllm/issues/39701) |
| 状态 | open |
| 标签 | performance;RFC;rl |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;kernel;moe;quantization;sampling;triton |
| 症状 | build_error;mismatch;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC] Replace routing replay with CUDA-graph-compatible device cache approach

### Issue 正文摘录

# [RFC] Replace routing replay with CUDA-graph-compatible device cache approach ## Motivation Routing replay (`--enable-return-routed-experts`) captures which MoE experts process each token during inference. This is needed by RL training pipelines (GRPO, RLHF) where the training step reconstructs expert routing decisions from the inference pass. We've been running a fork with a production-grade routing replay replacement on our internal GPU clusters for large MoE models (120B and 400B+ parameter). The current upstream implementation has fundamental issues that prevent real-world use - it breaks under CUDA graphs, doesn't work multi-node, misses the monolithic kernel path entirely, and has no MTP or prefix caching support. We'd like to upstream our replacement. The implementation is code complete and validated across 9 configurations with Ray DAG -> scheduler, replacing the SharedMemory path entirely. ## FlashInfer dependency This depends on a companion [FlashInfer PR](https://github.com/flashinfer-ai/flashinfer/compare/main...TomerBN-Nvidia:flashinfer:upstream-routing-replay) that adds `routing_replay_out` as an optional parameter to all MoE kernel launchers (FP8 block, FP8 per-te...

## 现有链接修复摘要

#39917 [Core] Replace routing replay with device cache and async D2H pipeline | #44115 [Bugfix] routed_experts: fall back to Triton MoE backend (FlashInfer kernels bypass capture)

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: outing_replay_out` as an optional parameter to all MoE kernel launchers (FP8 block, FP8 per-tensor, BF16, FP4, MXINT4) and routing kernels (Custom, DeepSeek, Llama4). When `None` (the default), there is zero overhead -...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [RFC] Replace routing replay with CUDA-graph-compatible device cache approach performance;RFC;rl # [RFC] Replace routing replay with CUDA-graph-compatible device cache approach ## Motivation Routing replay (`--enable-re...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: lines (GRPO, RLHF) where the training step reconstructs expert routing decisions from the inference pass. We've been running a fork with a production-grade routing replay replacement on our internal GPU clusters for lar...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: ng_replay_out` as an optional parameter to all MoE kernel launchers (FP8 block, FP8 per-tensor, BF16, FP4, MXINT4) and routing kernels (Custom, DeepSeek, Llama4). When `None` (the default), there is zero overhead - the...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: token during inference. This is needed by RL training pipelines (GRPO, RLHF) where the training step reconstructs expert routing decisions from the inference pass. We've been running a fork with a production-grade routi...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39917](https://github.com/vllm-project/vllm/pull/39917) | mentioned | 0.6 | [Core] Replace routing replay with device cache and async D2H pipeline | lithic kernel support and prefix caching are in a follow-up PR. RFC: #39701 ## What this PR does Replaces the SharedMemory-based routing replay with: - Pre-allocated `(L, N, K)` i… |
| [#44115](https://github.com/vllm-project/vllm/pull/44115) | mentioned | 0.6 | [Bugfix] routed_experts: fall back to Triton MoE backend (FlashInfer kernels bypass capture) | resses the internal-router/capture mismatch. - Complementary to **RFC #39701** (which proposes a CUDA-graph-compatible device-cache capture that would let the FlashInfer path capt… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
