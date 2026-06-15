# vllm-project/vllm#5557: [RFC]: Implement disaggregated prefilling via KV cache transfer

| 字段 | 值 |
| --- | --- |
| Issue | [#5557](https://github.com/vllm-project/vllm/issues/5557) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Implement disaggregated prefilling via KV cache transfer

### Issue 正文摘录

### Motivation. There are more and more use cases, where we need to transfer KV caches between vLLM instances, or store KV caches for future use. Some concrete use cases: - Disaggregated prefilling. In this case, the KV cache needs to be transferred from the prefilling instances to the decoding instances - The user want to query a fixed set of long documents (examples: software manual, internal documents, etc). In this case, the GPU memory + CPU memory may not be enough to store the KV cache of all documents, and we may want to storage the KV cache of these documents and move them to GPU on-demand. ### Proposed Change. My current thought is to introduce two new abstractions: communicator and KV database. The workflow will be ``` vllm communicator KV database ``` where - The communicator transfer the data from `src` to `dst`, where both `src` and `dst` can be a KV block in vllm, or an entry in database - The KV database is a database using the hash (generated in automatic prefix caching) as the key, the corresponding KV cache tensor as the value. This will be a huge framework, with a wide range of challenging (but fun!) questions inside, including but not limited to: - How to lever...

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [RFC]: Implement disaggregated prefilling via KV cache transfer RFC;stale ### Motivation. There are more and more use cases, where we need to transfer KV caches between vLLM instances, or store KV caches for future use....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [RFC]: Implement disaggregated prefilling via KV cache transfer RFC;stale ### Motivation. There are more and more use cases, where we need to transfer KV caches between vLLM instances, or store KV caches for future use....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: , including but not limited to: - How to leverage infrastructures like NVLink to transfer KV cache faster? - How to properly pipeline the KV cache transfer? - How to make sure the blocks are not swapped out when the com...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: fer the data from `src` to `dst`, where both `src` and `dst` can be a KV block in vllm, or an entry in database - The KV database is a database using the hash (generated in automatic prefix caching) as the key, the corr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
