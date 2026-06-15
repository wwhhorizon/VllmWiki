# vllm-project/vllm#21017: [Performance]: current slide window kv manager can lead to more cache miss in certain cases.

| 字段 | 值 |
| --- | --- |
| Issue | [#21017](https://github.com/vllm-project/vllm/issues/21017) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: current slide window kv manager can lead to more cache miss in certain cases.

### Issue 正文摘录

### Proposal to improve performance https://github.com/vllm-project/vllm/blob/10be20949350153651c86cdecb862a9ec324965a/vllm/v1/core/single_type_kv_cache_manager.py#L338-L352 In the current implementation of slide window manager, we do early exit as shown above. This makes sense but one side effect is that the earlier blocks beyond the local horizon are not touched hence would slowly "sink" into the tail of LRU and will eventually get evicted. While in the full attention layer, all blocks are kept "alive". This becomes problematic when we ever "rewind" a sequence where earlier tokens (e.g. system prompt) come back into the slide window again. In this case, those tokens would be cache hit in the full attention layers but cache miss in the SWA layers, and hence cache miss overall. This is counter intuitive since one would expect SWA layers would have equal or fewer cache misses than full layers. A solution would be to recursively "touch" (without increasing the ref count) the blocks beyond the local horizon in SWA layer to prevent them from sinking in LRU.

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: [Performance]: current slide window kv manager can lead to more cache miss in certain cases. performance;stale ### Proposal to improve performance https://github.com/vllm-project/vllm/blob/10be20949350153651c86cdecb862a...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: as shown above. This makes sense but one side effect is that the earlier blocks beyond the local horizon are not touched hence would slowly "sink" into the tail of LRU and will eventually get evicted. While in the full...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: dow kv manager can lead to more cache miss in certain cases. performance;stale ### Proposal to improve performance https://github.com/vllm-project/vllm/blob/10be20949350153651c86cdecb862a9ec324965a/vllm/v1/core/single_t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
