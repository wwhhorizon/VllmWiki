# vllm-project/vllm#37162: [Feature] Fuse per-group FP8 dynamic quant onto Triton attention kernel

| 字段 | 值 |
| --- | --- |
| Issue | [#37162](https://github.com/vllm-project/vllm/issues/37162) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature] Fuse per-group FP8 dynamic quant onto Triton attention kernel

### Issue 正文摘录

### Motivation The "Attention+Quant | FP8 dynamic per-group" row in #36066 is currently ❌ across all platforms. Models using per-group FP8 quantization (e.g., with `group_size=128`) pay an unnecessary HBM round-trip between the attention output and the separate `per_token_group_fp8_quant` kernel. ### Proposal Fuse per-group FP8 dynamic output quantization into the in-tree Triton attention kernel epilogue. The kernel computes per-group dynamic scales and quantizes directly in registers, eliminating the intermediate BF16 write/read. Implementation in progress: #37110 ### Scope - `group_size=128` and `group_size=64` - All scale layouts (row-major, column-major, TMA-aligned, e8m0) - Both 2D kernel (prefill) and 3D+reduce_segments (decode) paths - Constraint: `head_size % group_size == 0`

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Feature] Fuse per-group FP8 dynamic quant onto Triton attention kernel ### Motivation The "Attention+Quant | FP8 dynamic per-group" row in #36066 is currently ❌ across all platforms. Models using per-group FP8 quantiza...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: e layouts (row-major, column-major, TMA-aligned, e8m0) - Both 2D kernel (prefill) and 3D+reduce_segments (decode) paths - Constraint: `head_size % group_size == 0`
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Feature] Fuse per-group FP8 dynamic quant onto Triton attention kernel ### Motivation The "Attention+Quant | FP8 dynamic per-group" row in #36066 is currently ❌ across all platforms. Models using per-group FP8 quantiza...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: s: #37110 ### Scope - `group_size=128` and `group_size=64` - All scale layouts (row-major, column-major, TMA-aligned, e8m0) - Both 2D kernel (prefill) and 3D+reduce_segments (decode) paths - Constraint: `head_size % gro...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: P8 dynamic per-group" row in #36066 is currently ❌ across all platforms. Models using per-group FP8 quantization (e.g., with `group_size=128`) pay an unnecessary HBM round-trip between the attention output and the separ...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
