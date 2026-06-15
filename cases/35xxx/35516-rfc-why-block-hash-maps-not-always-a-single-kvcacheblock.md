# vllm-project/vllm#35516: [RFC]: why block_hash maps not always a single KVCacheBlock.

| 字段 | 值 |
| --- | --- |
| Issue | [#35516](https://github.com/vllm-project/vllm/issues/35516) |
| 状态 | open |
| 标签 | RFC;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: why block_hash maps not always a single KVCacheBlock.

### Issue 正文摘录

### Motivation. I understand that mapping block_hash to a dictionary like {block_id: KVCacheBlock} is due to Note #1. However, I think that even if we only map each block_hash to a single KVCacheBlock, we still would not need to modify the block table — it could remain append-only. In my view, updating the hash map would not affect the block table mapping, because previously allocated block_ids have already been assigned and would not change. So why don’t we enforce that each block_hash maps to a single KVCacheBlock? Wouldn’t that make the design simpler? ### Proposed Change. ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [RFC]: why block_hash maps not always a single KVCacheBlock. RFC;stale ### Motivation. I understand that mapping block_hash to a dictionary like {block_id: KVCacheBlock} is due to Note #1. However, I think that even if...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ock_hash to a single KVCacheBlock, we still would not need to modify the block table — it could remain append-only. In my view, updating the hash map would not affect the block table mapping, because previously allocate...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [RFC]: why block_hash maps not always a single KVCacheBlock. RFC;stale ### Motivation. I understand that mapping block_hash to a dictionary like {block_id: KVCacheBlock} is due to Note #1. However, I think that even if...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
