# vllm-project/vllm#33526: [RFC]: Progressive KV Cache CPU Onloading

| 字段 | 值 |
| --- | --- |
| Issue | [#33526](https://github.com/vllm-project/vllm/issues/33526) |
| 状态 | open |
| 标签 | RFC;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Progressive KV Cache CPU Onloading

### Issue 正文摘录

### Motivation. KV Cache CPU offloading is a new native vLLM feature introduced with RFC #19854. It enables offloading of KV cache blocks to CPU memory from GPU memory which is especially useful when not enough GPU memory is available for storage. The current design onloads KV cache blocks for entire requests at once and prevents concurrent onloading operations for the same KV cache blocks. This can introduce a head of line blocking bottleneck where a larger request sharing the same prefix as a smaller request prevents the smaller request from being scheduled due to the larger request’s blocks being onloaded. The smaller request needs to wait for all of the blocks relevant to the larger request to be onloaded before it can be scheduled, even if it only requires a small portion of the blocks for itself. Already discussed as a desired feature, this RFC outlines support for more progressive onloading of KV cache blocks such that the head of line blocking issue is reduced. ### Proposed Change. ### A quick recap of the existing design The following diagram taken from RFC #19854 illustrates the current design of CPU offloading. ### Batched Progressive Loading Instead of a single block t...

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: [RFC]: Progressive KV Cache CPU Onloading RFC;stale ### Motivation. KV Cache CPU offloading is a new native vLLM feature introduced with RFC #19854. It enables offloading of KV cache blocks to CPU memory from GPU memory...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: offloading of KV cache blocks to CPU memory from GPU memory which is especially useful when not enough GPU memory is available for storage. The current design onloads KV cache blocks for entire requests at once and prev...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: LM feature introduced with RFC #19854. It enables offloading of KV cache blocks to CPU memory from GPU memory which is especially useful when not enough GPU memory is available for storage. The current design onloads KV...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [RFC]: Progressive KV Cache CPU Onloading RFC;stale ### Motivation. KV Cache CPU offloading is a new native vLLM feature introduced with RFC #19854. It enables offloading of KV cache blocks to CPU memory from GPU memory...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: blocking bottleneck where a larger request sharing the same prefix as a smaller request prevents the smaller request from being scheduled due to the larger request’s blocks being onloaded. The smaller request needs to w...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
