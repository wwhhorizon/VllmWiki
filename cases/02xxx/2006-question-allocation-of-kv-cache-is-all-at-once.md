# vllm-project/vllm#2006: Question: Allocation of KV cache is all at once?

| 字段 | 值 |
| --- | --- |
| Issue | [#2006](https://github.com/vllm-project/vllm/issues/2006) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Question: Allocation of KV cache is all at once?

### Issue 正文摘录

I have a question regarding the KV cache allocation: where in the source code does the allocation happen? I have looked through to find it, but can only find the following function, which generates a list of tensors that seem to be the KV cache. > https://github.com/vllm-project/vllm/blob/2e8fc0d4c3bf8374f1f55569069e59ef45d4bc98/vllm/worker/cache_engine.py#L70-L86 It seems like this is *the* allocation of the KV cache? In the paper, it states that "Instead, it reserves only the necessary KV blocks to accommodate the KV cache generated during prompt computation". Does the `gpu_cache` act like an allocation arena for the KV blocks?

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: Question: Allocation of KV cache is all at once? I have a question regarding the KV cache allocation: where in the source code does the allocation happen? I have looked through to find it, but can only find the followin...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: In the paper, it states that "Instead, it reserves only the necessary KV blocks to accommodate the KV cache generated during prompt computation". Does the `gpu_cache` act like an allocation arena for the KV blocks?

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
