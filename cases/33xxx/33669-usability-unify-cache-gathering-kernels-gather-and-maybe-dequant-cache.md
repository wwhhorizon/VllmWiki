# vllm-project/vllm#33669: [Usability]:  Unify cache gathering kernels (gather_and_maybe_dequant_cache, cp_gather_cache, cp_gather_and_upconvert_fp8_kv_cache)

| 字段 | 值 |
| --- | --- |
| Issue | [#33669](https://github.com/vllm-project/vllm/issues/33669) |
| 状态 | open |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usability]:  Unify cache gathering kernels (gather_and_maybe_dequant_cache, cp_gather_cache, cp_gather_and_upconvert_fp8_kv_cache)

### Issue 正文摘录

Currently, MLA attention uses multiple separate kernel calls for gathering cache data based on the datatype of ouput kv buffers and stored kv cache: - `ops.gather_and_maybe_dequant_cache` - gathers cache with optional dequantization - `ops.cp_gather_cache` - gathers cache without dequantization (FP8 path) - `ops.cp_gather_and_upconvert_fp8_kv_cache` - gathers and upconverts FP8 cache Example from `_compute_prefill_context`: ``` if not use_fp8_prefill: ops.gather_and_maybe_dequant_cache( src_cache=kv_c_and_k_pe_cache, dst=workspace, block_table=prefill_metadata.block_table, cu_seq_lens=prefill_metadata.chunked_context.cu_seq_lens[i], token_to_seq=prefill_metadata.chunked_context.token_to_seq[i], num_tokens=prefill_metadata.chunked_context.chunk_total_token[i], kv_cache_dtype=self.kv_cache_dtype, scale=k_scale, seq_starts=prefill_metadata.chunked_context.starts[i], ) else: # FP8 path: gather cache without dequantization ops.cp_gather_cache( src_cache=kv_c_and_k_pe_cache, dst=workspace, block_table=prefill_metadata.block_table, cu_seq_lens=prefill_metadata.chunked_context.cu_seq_lens[i], batch_size=attn_metadata.num_prefills, seq_starts=prefill_metadata.chunked_context.starts[i], ) `...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Usability]: Unify cache gathering kernels (gather_and_maybe_dequant_cache, cp_gather_cache, cp_gather_and_upconvert_fp8_kv_cache) feature request;stale Currently, MLA attention uses multiple separate kernel calls for g...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: e( src_cache=kv_c_and_k_pe_cache, dst=workspace, block_table=prefill_metadata.block_table, cu_seq_lens=prefill_metadata.chunked_context.cu_seq_lens[i], token_to_seq=prefill_metadata.chunked_context.token_to_seq[i], num_...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: nt_cache, cp_gather_cache, cp_gather_and_upconvert_fp8_kv_cache) feature request;stale Currently, MLA attention uses multiple separate kernel calls for gathering cache data based on the datatype of ouput kv buffers and...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nto a single Python wrapper (even if they remain separate kernels on the backend) to simplify the API and reduce code duplication The refactored wrapper can be used in more places outside of MLAAttention too and provide...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: rts[i], ) ``` Proposed Changes: - Unify into a single kernel that decides whether to dequantize based on the destination dtype, eliminating the need for conditional branching in Python - Bundle all cache gathering ops i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
