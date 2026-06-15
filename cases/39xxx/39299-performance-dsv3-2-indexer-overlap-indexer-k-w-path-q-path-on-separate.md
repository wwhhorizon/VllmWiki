# vllm-project/vllm#39299: [Performance] DSV3.2 Indexer: Overlap indexer k+w path || q path on separate CUDA streams

| 字段 | 值 |
| --- | --- |
| Issue | [#39299](https://github.com/vllm-project/vllm/issues/39299) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;frontend_api;gemm_linear;quantization |
| 子分类 |  |
| Operator 关键词 | activation;attention;cuda;fp8;gemm;kernel;operator;quantization |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Performance] DSV3.2 Indexer: Overlap indexer k+w path \|\| q path on separate CUDA streams

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ## Motivation In the DeepSeek-V3.2 attention layer, the indexer's k+w path (`wk_weights_proj` → `k_norm`) and the q path (`QKV A Proj` → `q_a_rmsnorm` → `wq_b`) both read `hidden_states` as input but have no data dependency between them. Currently they execute sequentially on the same CUDA stream. Overlapping them on separate streams hides the k+w path entirely behind the longer q path. `wk_weights_proj(hidden_states)` reads the original layer input directly — it does NOT depend on `QKV A Proj` output. Only the q path depends on `QKV A Proj` (via `q_c = q_a_layernorm(split(fused_qkv_a_proj(hidden_states)))`). So the fork can happen as soon as `hidden_states` is available (after `AR + Add + RMS`), with `wk_weights_proj` running in parallel with `QKV A Proj` itself. PR #38684 already fused `wk` + `weights_proj` into a single `wk_weights_proj` GEMM. This proposal is the natural next step: overlap the fused GEMM and its downstream ops with the q path on a secondary stream. ## Current Execution All operations run sequentially on the default CUDA stream: ``` Stream 19 (default) — all sequential: #4 QKV A Proj (fused_a_gemm) → produces qr + hidden_...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #12 Implement preemption via recomputation & Refactor scheduling logic | #39695 Introduce De-dup/Similarity-Check in CI Workflow for PR/Issue

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: its + cats 2.0us → rotary_emb(q_pe, k_pe) combined #12 Indexer Q FP8 quant 2.3us → q → q_fp8, q_scale #13 Indexer W scale 1.4us → weights * q_scale * scale ↓ continues to q_b_proj → indexer op → MLA attention... ``` ## P
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: a_rmsnorm` → `wq_b`) both read `hidden_states` as input but have no data dependency between them. Currently they execute sequentially on the same CUDA stream. Overlapping them on separate streams hides the k+w path enti...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: formance] DSV3.2 Indexer: Overlap indexer k+w path || q path on separate CUDA streams feature request ### 🚀 The feature, motivation and pitch ## Motivation In the DeepSeek-V3.2 attention layer, the indexer's k+w path (`...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: vation;attention;cuda;fp8;gemm;kernel;operator;quantization dtype #4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #12 Impl...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #12 Implement preemption via recomputation & Refactor scheduling logic | #39695 Int...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | : ──────────────────────── ────────────────────── #4 qkv a proj 7.7us #5 wk_weights_proj 4.8us split → q_c, kv_lora |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | eights_proj 4.8us split → q_c, kv_lora #6 splitkreduce 2.8us #8 q_a_rmsnorm + split 2.3us #7 k_norm + split kw 2.2us |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | tkreduce 2.8us #8 q_a_rmsnorm + split 2.3us #7 k_norm + split kw 2.2us #9 kv_a_rmsnorm + split 2.5us → k_pe, k_nope, weights ready |
| [#12](https://github.com/vllm-project/vllm/pull/12) | mentioned | 0.45 | Implement preemption via recomputation & Refactor scheduling logic | rope(q_pe, k_pe) combined 2.0us #12 fp8 quant(q) 2.3us #13 w scale (weights * q_scale) |
| [#39695](https://github.com/vllm-project/vllm/pull/39695) | mentioned | 0.6 | Introduce De-dup/Similarity-Check in  CI Workflow for PR/Issue | r Affine Score Calibration (Platt Scaling) \| \| 100% \| 100% \| 100% \| [#39299](https://github.com/vllm-project/vllm/issues/39299) [Performance] DSV3.2 Indexer: Overlap indexer k+w p… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
