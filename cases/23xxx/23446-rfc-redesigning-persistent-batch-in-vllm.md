# vllm-project/vllm#23446: [RFC]: Redesigning Persistent Batch in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#23446](https://github.com/vllm-project/vllm/issues/23446) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Redesigning Persistent Batch in vLLM

### Issue 正文摘录

### Motivation. To reduce the overhead of input data construction, vLLM v1 introduced the **persistent batch** technique, inspired by [LMDeploy](https://github.com/InternLM/lmdeploy). ## How vLLM's Persistent Batch Works At a high level, the mechanism operates as follows: 1. Each request’s state is stored in an `InputBatch`, which consists of CPU tensors shaped either as `[num_reqs]` (e.g., sampling temperature) or `[num_reqs, L]` (e.g., block tables). 2. When `N` requests are scheduled, we reorder `InputBatch` so that the first `N` entries correspond to the scheduled requests. 3. Finally, these `N` entries are then copied from CPU to GPU (using regular `cudaMemcpyAsync`). The key insight is that the set of scheduled requests typically changes only slightly between steps. Thus, the `InputBatch` from the previous step can be reused with only incremental updates (e.g., appending `new_block_ids` to the block table and reordering a few rows when some requests finish). ## Limitations of Current Implementation While effective in many cases, vLLM's persistent batch has several drawbacks: 1. **Efficiency depends on minimal changes between steps**—a condition that doesn’t always hold: * (w...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: r as `[num_reqs]` (e.g., sampling temperature) or `[num_reqs, L]` (e.g., block tables). 2. When `N` requests are scheduled, we reorder `InputBatch` so that the first `N` entries correspond to the scheduled requests. 3....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: atch Works At a high level, the mechanism operates as follows: 1. Each request’s state is stored in an `InputBatch`, which consists of CPU tensors shaped either as `[num_reqs]` (e.g., sampling temperature) or `[num_reqs...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: loy). ## How vLLM's Persistent Batch Works At a high level, the mechanism operates as follows: 1. Each request’s state is stored in an `InputBatch`, which consists of CPU tensors shaped either as `[num_reqs]` (e.g., sam...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: it happens on GPU**. Given `index_mapping` (determined by the attention backend), we write a custom Triton kernel that gathers entries from `RequestStates` into dense GPU tensors. The kernel can access the CPU tensors i...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: in many cases, vLLM's persistent batch has several drawbacks: 1. **Efficiency depends on minimal changes between steps**—a condition that doesn’t always hold: * (while it's not the default case in vLLM) A scheduler may...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
