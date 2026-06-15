# vllm-project/vllm#5308: [Misc]: Question about adding more kv cache blocks

| 字段 | 值 |
| --- | --- |
| Issue | [#5308](https://github.com/vllm-project/vllm/issues/5308) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Question about adding more kv cache blocks

### Issue 正文摘录

### Anything you want to discuss about vllm. Is it theoretically possible to increase the total amount of kv cache blocks by adding new GPU resources, that only for kv cache allocation, without using tensor parallel or other parallel?

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Misc]: Question about adding more kv cache blocks ### Anything you want to discuss about vllm. Is it theoretically possible to increase the total amount of kv cache blocks by adding new GPU resources, that only for kv...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Misc]: Question about adding more kv cache blocks ### Anything you want to discuss about vllm. Is it theoretically possible to increase the total amount of kv cache blocks by adding new GPU resources, that only for kv...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
