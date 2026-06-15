# vllm-project/vllm#2614: [RFC] Automatic Prefix Caching

| 字段 | 值 |
| --- | --- |
| Issue | [#2614](https://github.com/vllm-project/vllm/issues/2614) |
| 状态 | closed |
| 标签 | feature request;RFC |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC] Automatic Prefix Caching

### Issue 正文摘录

This RFC discusses our plan for implementing automatic prefix caching in vLLM. ## High-level idea We observe that every block in the KV cache can be uniquely identified by ``` hash(prefix tokens, tokens in this block) ``` With this, we can add another indirection in vLLM's KV cache management: ``` Logical block table --> hash table --> physical block table. ``` Then, all the sharing in vLLM, including sharing prefixes, can be achieved by logical blocks pointing to the block with the same hash value. Automatic prefix caching can be achieved by not freeing blocks with reference one in the KV cache. Specifically, this design enables us to manage the KV blocks as ordinary caches in operating systems. We can maintain the following information in every block: - Block's hash - Reference count - Last accessed time - Total access count - The prefix length of this block Then, for example, the following cache eviction policy will give the same policy as in [RadixAttetion](https://arxiv.org/pdf/2312.07104.pdf): 1. Check the reference count first. Only evict the blocks with `ref count == 0`. 2. Then check the last accessed time. Prefer to free older blocks following LRU. 3. If the last accesse...

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: caching in vLLM. ## High-level idea We observe that every block in the KV cache can be uniquely identified by ``` hash(prefix tokens, tokens in this block) ``` With this, we can add another indirection in vLLM's KV cach...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: be achieved by not freeing blocks with reference one in the KV cache. Specifically, this design enables us to manage the KV blocks as ordinary caches in operating systems. We can maintain the following information in ev...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: omatic prefix caching in vLLM. ## High-level idea We observe that every block in the KV cache can be uniquely identified by ``` hash(prefix tokens, tokens in this block) ``` With this, we can add another indirection in...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: s ordinary caches in operating systems. We can maintain the following information in every block: - Block's hash - Reference count - Last accessed time - Total access count - The prefix length of this block Then, for ex...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [RFC] Automatic Prefix Caching feature request;RFC This RFC discusses our plan for implementing automatic prefix caching in vLLM. ## High-level idea We observe that every block in the KV cache can be uniquely identified...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
