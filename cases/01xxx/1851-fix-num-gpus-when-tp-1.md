# vllm-project/vllm#1851: Fix num_gpus when TP > 1

| 字段 | 值 |
| --- | --- |
| Issue | [#1851](https://github.com/vllm-project/vllm/issues/1851) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Fix num_gpus when TP > 1

### Issue 正文摘录

For now we should do: ``` num_gpus=self.cache_config.gpu_memory_utilization if self.parallel_config.tensor_parallel_size < 2 else 1 ``` _Originally posted by @Yard1 in https://github.com/vllm-project/vllm/issues/1821#issuecomment-1833028091_

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: gpu_memory_utilization if self.parallel_config.tensor_parallel_size < 2 else 1 ``` _Originally posted by @Yard1 in https://github.com/vllm-project/vllm/issues/1821#issuecomment-1833028091_
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Fix num_gpus when TP > 1 For now we should do: ``` num_gpus=self.cache_config.gpu_memory_utilization if self.parallel_config.tensor_parallel_size < 2 else 1 ``` _Originally posted by @Yard1 in https://github.com/vllm-pr...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
