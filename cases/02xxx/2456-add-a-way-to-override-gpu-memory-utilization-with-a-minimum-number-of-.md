# vllm-project/vllm#2456: Add a way to override gpu_memory_utilization with a minimum number of cache blocks

| 字段 | 值 |
| --- | --- |
| Issue | [#2456](https://github.com/vllm-project/vllm/issues/2456) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Add a way to override gpu_memory_utilization with a minimum number of cache blocks

### Issue 正文摘录

Sometimes we want to load multiple models at once on the same GPU for testing purposes. Performance isn't a major concern in these cases, and we'd like to be able to specify something like gpu_memory_utilization=0, and have that result in just the model loaded and a very small number of cache blocks. Is this currently possible? If not, would be hard to add this functionality, perhaps via a separate min_cache_blocks parameter?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: nce isn't a major concern in these cases, and we'd like to be able to specify something like gpu_memory_utilization=0, and have that result in just the model loaded and a very small number of cache blocks. Is this curre...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: _utilization=0, and have that result in just the model loaded and a very small number of cache blocks. Is this currently possible? If not, would be hard to add this functionality, perhaps via a separate min_cache_blocks...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: Add a way to override gpu_memory_utilization with a minimum number of cache blocks Sometimes we want to load multiple models at once on the same GPU for testing purposes. Performance isn't a major concern in these cases...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: a way to override gpu_memory_utilization with a minimum number of cache blocks Sometimes we want to load multiple models at once on the same GPU for testing purposes. Performance isn't a major concern in these cases, an...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: with a minimum number of cache blocks Sometimes we want to load multiple models at once on the same GPU for testing purposes. Performance isn't a major concern in these cases, and we'd like to be able to specify somethi...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
