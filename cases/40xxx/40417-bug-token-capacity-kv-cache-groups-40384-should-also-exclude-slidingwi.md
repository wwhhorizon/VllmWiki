# vllm-project/vllm#40417: [Bug]: `token_capacity_kv_cache_groups` (#40384) should also exclude `SlidingWindowSpec` / `ChunkedLocalAttentionSpec`

| 字段 | 值 |
| --- | --- |
| Issue | [#40417](https://github.com/vllm-project/vllm/issues/40417) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: `token_capacity_kv_cache_groups` (#40384) should also exclude `SlidingWindowSpec` / `ChunkedLocalAttentionSpec`

### Issue 正文摘录

Hi! Following up on #40384 — wanted to flag a related bug class in the same helper that I noticed while auditing #40384's reach for our hybrid-Mamba deployment. (Small disclaimer: I'm from Ukraine and my English is still a work in progress, so I'm using AI to help with translation. Hope it reads okay!) ## Description PR #40384 introduces `token_capacity_kv_cache_groups()` in [`vllm/v1/core/kv_cache_utils.py`](https://github.com/vllm-project/vllm/blob/main/vllm/v1/core/kv_cache_utils.py) that filters out `MambaSpec` groups when `mamba_cache_mode != 'all'`, fixing the per-token KV capacity divisor for hybrid Mamba+attention models. There are two more `KVCacheSpec` subtypes with the same property — bounded memory regardless of sequence length — but they're still counted in the divisor: 1. **`SlidingWindowSpec`** — `max_memory_usage_bytes` bounded by `min(sliding_window + max_num_batched_tokens, max_model_len)` ([`vllm/v1/kv_cache_interface.py:341-353`](https://github.com/vllm-project/vllm/blob/main/vllm/v1/kv_cache_interface.py)) 2. **`ChunkedLocalAttentionSpec`** — bounded by `attention_chunk_size + max_num_batched_tokens` (same file, lines 360-379) Both inherit from `AttentionSpec`...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: l'`, fixing the per-token KV capacity divisor for hybrid Mamba+attention models. There are two more `KVCacheSpec` subtypes with the same property — bounded memory regardless of sequence length — but they're still counte...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: tree today Anything with sliding-window layers in a hybrid config: - **Gemma 3** family (mixed local/global attention) - **Phi-3 / Phi-4** with sliding-window-only mode - **Mistral** variants with `sliding_window` enabl...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: um_blocks // 1 * min_block_size` → correct full-attention capacity Same regression direction as the Mamba bug — just less severe in the sense that bounded memory still scales with window/chunk size, not full sequence le...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: `token_capacity_kv_cache_groups` (#40384) should also exclude `SlidingWindowSpec` / `ChunkedLocalAttentionSpec` Hi! Following up on #40384 — wanted to flag a related bug class in the same helper that I noticed wh...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: roups()` includes them in the per-token divisor — even though they don't scale with full sequence length. ## Impact For a hybrid model with `1 sliding-window (e.g. 4k) + 1 full-attention` group running at `max_model_len...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
