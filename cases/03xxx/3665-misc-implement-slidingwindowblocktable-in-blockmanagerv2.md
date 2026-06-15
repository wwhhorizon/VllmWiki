# vllm-project/vllm#3665: [Misc]: Implement SlidingWindowBlockTable in BlockManagerV2

| 字段 | 值 |
| --- | --- |
| Issue | [#3665](https://github.com/vllm-project/vllm/issues/3665) |
| 状态 | closed |
| 标签 | good first issue |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Implement SlidingWindowBlockTable in BlockManagerV2

### Issue 正文摘录

Recently, we refactored the block manager subsystem to improve testability by separating concerns of each layer. See https://github.com/vllm-project/vllm/pull/3492 for more information. The V2 implementation does not yet have sliding window support. This issue tracks adding sliding window to the V2 block table so that we can support models that use this feature. My initial take on the design is to implement a `SlidingWindowBlockTable` that composes within it a `BlockTable`. The `SlidingWindowBlockTable` will then drop blocks that are outside of the context window (potentially mapping them to a devnull block). This will preserve the semantics of the v1 block manager sliding window while fitting into the new design.

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Misc]: Implement SlidingWindowBlockTable in BlockManagerV2 good first issue Recently, we refactored the block manager subsystem to improve testability by separating concerns of each layer. See https://github.com/vllm-p...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ach layer. See https://github.com/vllm-project/vllm/pull/3492 for more information. The V2 implementation does not yet have sliding window support. This issue tracks adding sliding window to the V2 block table so that w...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: liding window support. This issue tracks adding sliding window to the V2 block table so that we can support models that use this feature. My initial take on the design is to implement a `SlidingWindowBlockTable` that co...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: rst issue Recently, we refactored the block manager subsystem to improve testability by separating concerns of each layer. See https://github.com/vllm-project/vllm/pull/3492 for more information. The V2 implementation d...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
