# vllm-project/vllm#41886: [Feature]: NIXL P/D Disaggregation: GDN support (Qwen3.5)

| 字段 | 值 |
| --- | --- |
| Issue | [#41886](https://github.com/vllm-project/vllm/issues/41886) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: NIXL P/D Disaggregation: GDN support (Qwen3.5)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Add GDN (Gated Delta Net) model support for NIXL-based Prefill/Decode disaggregation. GDN models (e.g. Qwen3.5) have a different SSM layout than Mamba2 — conv state is `[K, K, V]` instead of `[x, B, C]`, and temporal state shape is `(num_v_heads, v_dim, k_dim)` instead of `(num_heads, head_dim)`. **PR:** #41869 ### Verified Configs **Model:** `Qwen/Qwen3.5-0.8B` | GSM8K 5-shot (baseline ~0.323) - **Homogeneous TP** (1p1d, 2p2d, 4p4d): all pass across all backends (FLASHINFER, FLASH_ATTN, TRITON_ATTN) and block sizes (16, 32, 64, 128). - **Heterogeneous TP** (1p2d, 2p1d): all pass across all backends and block sizes. - **Heterogeneous TP with TP=4 (FA replication)** (1p4d, 4p1d, 2p4d, 4p2d): pass on FLASHINFER/FLASH_ATTN with block sizes 32, 64, 128. ### Known Issues / TODOs - [ ] Heterogeneous TP not supported when P and D have mismatched **kernel** block sizes — e.g. TP=4 configs with `block_size=16` on FLASHINFER/FLASH_ATTN, or all TP=4 configs on TRITON_ATTN. - [ ] Async scheduling not supported (#37285) - [ ] Prefix caching not supported (WIP) ### Alternatives N/A - extends the existing NIXL Mamba2 transfer path. ### Additional context T...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ne ~0.323) - **Homogeneous TP** (1p1d, 2p2d, 4p4d): all pass across all backends (FLASHINFER, FLASH_ATTN, TRITON_ATTN) and block sizes (16, 32, 64, 128). - **Heterogeneous TP** (1p2d, 2p1d): all pass across all backends...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: NIXL P/D Disaggregation: GDN support (Qwen3.5) ### 🚀 The feature, motivation and pitch Add GDN (Gated Delta Net) model support for NIXL-based Prefill/Decode disaggregation. GDN models (e.g. Qwen3.5) have a di...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: efill/Decode disaggregation. GDN models (e.g. Qwen3.5) have a different SSM layout than Mamba2 — conv state is `[K, K, V]` instead of `[x, B, C]`, and temporal state shape is `(num_v_heads, v_dim, k_dim)` instead of `(n...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ll/Decode disaggregation. GDN models (e.g. Qwen3.5) have a different SSM layout than Mamba2 — conv state is `[K, K, V]` instead of `[x, B, C]`, and temporal state shape is `(num_v_heads, v_dim, k_dim)` instead of `(num_...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: vation and pitch Add GDN (Gated Delta Net) model support for NIXL-based Prefill/Decode disaggregation. GDN models (e.g. Qwen3.5) have a different SSM layout than Mamba2 — conv state is `[K, K, V]` instead of `[x, B, C]`...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
