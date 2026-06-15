# vllm-project/vllm#23130: [Bug]: Async KVConnectors can break shared prefix check

| 字段 | 值 |
| --- | --- |
| Issue | [#23130](https://github.com/vllm-project/vllm/issues/23130) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Async KVConnectors can break shared prefix check

### Issue 正文摘录

### 🐛 Describe the bug `KVCacheManager.get_num_common_prefix_blocks` is used to identify the longest common prefix of requests in the current batch (actually all `RUNNING` requests), which in turn is used to determine whether to use cascade attention. The logic currently assumes each ref count on a block corresponds to a running request, however with async kv offloading, ref counts can be held after a request has completed and is no longer in running state. This means the logic could incorrectly identify a common prefix that isn't actually shared by all batch constituents. With forthcoming changes to the KVConnector API there may be other situations that connectors hold their own reference to blocks.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Async KVConnectors can break shared prefix check bug;stale ### 🐛 Describe the bug `KVCacheManager.get_num_common_prefix_blocks` is used to identify the longest common prefix of requests in the current batch (actu...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: count on a block corresponds to a running request, however with async kv offloading, ref counts can be held after a request has completed and is no longer in running state. This means the logic could incorrectly identif...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: bug;stale ### 🐛 Describe the bug `KVCacheManager.get_num_common_prefix_blocks` is used to identify the longest common prefix of requests in the current batch (actually all `RUNNING` requests), which in turn is used to d...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
