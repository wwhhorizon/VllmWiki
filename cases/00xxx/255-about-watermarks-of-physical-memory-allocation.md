# vllm-project/vllm#255: About watermarks of physical memory allocation

| 字段 | 值 |
| --- | --- |
| Issue | [#255](https://github.com/vllm-project/vllm/issues/255) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> About watermarks of physical memory allocation

### Issue 正文摘录

In current verison of codes(0.1.1), I noticed that both the [can_allocate()](https://github.com/vllm-project/vllm/blob/main/vllm/core/block_manager.py#L80) method and [can_swap_in()](https://github.com/vllm-project/vllm/blob/main/vllm/core/block_manager.py#L158) method of the BlockSpaceManager class deal with watermarks while [can_append_slot()](https://github.com/vllm-project/vllm/blob/main/vllm/core/block_manager.py#L105) doesn't. It seems that they should have the same mechanism on GPU memory management.

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: can_allocate()](https://github.com/vllm-project/vllm/blob/main/vllm/core/block_manager.py#L80) method and [can_swap_in()](https://github.com/vllm-project/vllm/blob/main/vllm/core/block_manager.py#L158) method of the Blo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: manager.py#L105) doesn't. It seems that they should have the same mechanism on GPU memory management.
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: r.py#L105) doesn't. It seems that they should have the same mechanism on GPU memory management.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
