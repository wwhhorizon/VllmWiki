# vllm-project/vllm#12254: [RFC]: Sparse KV cache management framework

| 字段 | 值 |
| --- | --- |
| Issue | [#12254](https://github.com/vllm-project/vllm/issues/12254) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Sparse KV cache management framework

### Issue 正文摘录

### Motivation. Efficient use of KV cache not only saves scarce GPU memory but also accelerates speed. Evicting potentially many low-utilization tokens, especially in long context, is the way to do it. To this end, this RFC proposes a flexible and performant KV cache management framework. ### Proposed Change. The design is as the following figure shows: (1) CachePolicy is a general interface that manages KV cache allocations. It generalizes from basic cache behavior that always allocates new slots/blocks to append new tokens to the more sophisticated that dictates how cache space is used should there be new tokens, such as sliding window, H2O, FastGen, etc. (2) CachePolicy (modified from previous BlockTable) has two straightforward methods: add_tokens_prefill and add_tokens_decode to give slots/blocks to new tokens. The given slots/blocks may be new allocations, and if so they will be requested from allocator. Or they can be old ones, which are from the previous blocks at its disposal. It is the policy that selects victims, evicts them, and replaces them with the new ones. (3) To do so, two data structures are employed to keep track of blocks and tokens: a PhysicalBlockTable and a...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [RFC]: Sparse KV cache management framework RFC;stale ### Motivation. Efficient use of KV cache not only saves scarce GPU memory but also accelerates speed. Evicting potentially many low-utilization tokens, especially i...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ions. It generalizes from basic cache behavior that always allocates new slots/blocks to append new tokens to the more sophisticated that dictates how cache space is used should there be new tokens, such as sliding wind...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: should a window of blocks have been had. (5) Per layer cache management capability. (6) Attention weights from attention backend. This work has a draft PR https://github.com/vllm-project/vllm/pull/11928. It was worked o...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [RFC]: Sparse KV cache management framework RFC;stale ### Motivation. Efficient use of KV cache not only saves scarce GPU memory but also accelerates speed. Evicting potentially many low-utilization tokens, especially i...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: layer cache management capability. (6) Attention weights from attention backend. This work has a draft PR https://github.com/vllm-project/vllm/pull/11928. It was worked on V0 and will be revamped on V1 in the following...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
