# vllm-project/vllm#43736: [Bug]: Local prefix cache hit rate can be over-counted when scheduling retries after KV allocation failure

| 字段 | 值 |
| --- | --- |
| Issue | [#43736](https://github.com/vllm-project/vllm/issues/43736) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Local prefix cache hit rate can be over-counted when scheduling retries after KV allocation failure

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I observed that in some workloads the reported local prefix cache hit rate can become unexpectedly high. After checking the scheduler path, it looks like local prefix cache stats may be recorded before the request is actually scheduled. In `KVCacheManager.get_computed_blocks()`, prefix cache stats are updated immediately after a local prefix cache lookup. However, the scheduler may later fail to allocate KV slots for that request, leaving it in the waiting queue. If the same request is retried in a later scheduling step, it can perform the same local prefix cache lookup again and be counted again, even though it was not scheduled in the previous attempt. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: prefix cache hit rate can become unexpectedly high. After checking the scheduler path, it looks like local prefix cache stats may be recorded before the request is actually scheduled. In `KVCacheManager.get_computed_blo...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: efore the request is actually scheduled. In `KVCacheManager.get_computed_blocks()`, prefix cache stats are updated immediately after a local prefix cache lookup. However, the scheduler may later fail to allocate KV slot...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: Local prefix cache hit rate can be over-counted when scheduling retries after KV allocation failure bug ### Your current environment ### 🐛 Describe the bug I observed that in some workloads the reported local pre...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: pt. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug]: Local prefix cache hit rate can be over-counted when scheduling retries after KV allocation failure bug ### Your current environment ### 🐛 Describe the bug I observed that in some workloads the reported local pre...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
