# vllm-project/vllm#39308: [Performance] DSV3.2 Indexer: Overlap indexer op || q_b_proj + MLA RoPE on separate CUDA streams

| 字段 | 值 |
| --- | --- |
| Issue | [#39308](https://github.com/vllm-project/vllm/issues/39308) |
| 状态 | open |
| 标签 | performance |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;frontend_api;moe;quantization;sampling_logits |
| 子分类 |  |
| Operator 关键词 | activation;attention;cuda;fp8;moe;operator;quantization;sampling |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Performance] DSV3.2 Indexer: Overlap indexer op \|\| q_b_proj + MLA RoPE on separate CUDA streams

### Issue 正文摘录

## Motivation In the DeepSeek-V3.2 attention layer, `q_b_proj` + `MLA RoPE` and the full indexer (projections + op) execute sequentially on the same CUDA stream despite having no data dependency. This is complementary to the multi-stream overlap of the indexer k+w path || q path (separate issue): see https://github.com/vllm-project/vllm/issues/39309 ## Current Execution ``` #4 QKV A Proj (fused_a_gemm) 7.7us #8 q_a_rmsnorm + split qkv_lora 2.3us #9 kv_a_rmsnorm + split kv_lora 2.5us ↓ #14 Q B Proj (q_b_proj) 15.1us → reads q_c #15 MLA RoPE (Q RoPE + KV RoPE) 2.0us → reads q + k_pe ↓ Full indexer (self.indexer(hidden_states, q_c, ...)): #5 wk_weights_proj (splitK) 4.8us #6 splitKreduce 2.8us #7 k_norm (LayerNorm) 2.2us #10 wq_b 7.2us #11 Indexer RoPE (q+k) 2.0us #12 FP8 quant 2.3us #13 W scale 1.4us #16 Indexer Cache (k_quant_and_cache) 2.5us #17 fill 1.1us #18 Indexer MQA (paged_mqa_logits) 4.5us #19 Logits Top K (topk_kernel) 1.4us ↓ #20 concat_and_cache_mla 2.0us ← start of mla_attn ... MLA attention continues ... ``` ## Proposed Standalone Execution Run the full indexer on the default stream and `q_b_proj + MLA RoPE` on an aux stream in parallel. In the current code, `q_b_proj`...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #12 Implement preemption via recomputation & Refactor scheduling logic | #16 Add custom kernel for RMS normalization | #20 Optimize data movement | #21 Add ninja to dependency

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: Indexer RoPE (q+k) 2.0us #12 FP8 quant 2.3us #13 W scale 1.4us #16 Indexer Cache (k_quant_and_cache) 2.5us #17 fill
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: ct/vllm/issues/39309 ## Current Execution ``` #4 QKV A Proj (fused_a_gemm) 7.7us #8 q_a_rmsnorm + split qkv_lora 2.3us #9 kv_a_rmsnorm + split kv_lora 2.5us ↓ #14 Q B Proj (q_b_proj
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e] DSV3.2 Indexer: Overlap indexer op || q_b_proj + MLA RoPE on separate CUDA streams performance ## Motivation In the DeepSeek-V3.2 attention layer, `q_b_proj` + `MLA RoPE` and the full indexer (projections + op) execu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ation;attention;cuda;fp8;moe;operator;quantization;sampling dtype #4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #12 Impl...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: op) execute sequentially on the same CUDA stream despite having no data dependency. This is complementary to the multi-stream overlap of the indexer k+w path || q path (separate issue): see https://github.com/vllm-proje...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | `mla q` (from q_b_proj) and `topk_indices` (from the indexer): ``` #4 qkv a proj 7.7us #8 q_a_rmsnorm + split |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | ghts_proj 4.8us #14 q b proj (q_b_proj) 15.1us #6 splitkreduce 2.8us #15 mla rope (q+kv) 2.0us #7 k_norm 2.2u |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | reduce 2.8us #15 mla rope (q+kv) 2.0us #7 k_norm 2.2us → mla q ready #10 wq_b 7.2us ( |
| [#12](https://github.com/vllm-project/vllm/pull/12) | mentioned | 0.45 | Implement preemption via recomputation & Refactor scheduling logic | 7.2us (17.1us total) #11 indexer rope 2.0us #12 fp8 quant 2.3us #13 w scale 1.4us #16 indexer cache 2.5us #17 fi |
| [#16](https://github.com/vllm-project/vllm/pull/16) | mentioned | 0.45 | Add custom kernel for RMS normalization | #12 fp8 quant 2.3us #13 w scale 1.4us #16 indexer cache 2.5us #17 fill 1.1us #18 indexer mqa 4.5us #19 lo |
| [#20](https://github.com/vllm-project/vllm/pull/20) | mentioned | 0.45 | Optimize data movement | ↓ #20 concat_and_cache_mla 2.0us #21 kv_b_proj (w_uv) |
| [#21](https://github.com/vllm-project/vllm/pull/21) | mentioned | 0.45 | Add ninja to dependency | concat_and_cache_mla 2.0us #21 kv_b_proj (w_uv) 5.9us ... sparse flashmla ... ``` ## co |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
