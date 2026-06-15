# vllm-project/vllm#1556: ValueError: Double free!

| 字段 | 值 |
| --- | --- |
| Issue | [#1556](https://github.com/vllm-project/vllm/issues/1556) |
| 状态 | closed |
| 标签 |  |
| 评论 | 23; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> ValueError: Double free!

### Issue 正文摘录

Getting this error really frequently when querying a Mistral-based model: ValueError: Double free! PhysicalTokenBlock(device=Device.GPU, block_number=9180, ref_count=0) is already freed. Interestingly, it ~primarily~ happens when I'm hitting the endpoint from pure python/request, not when I'm using Postman. But, it has happened when using Postman and when just querying the model locally, though less frequently.

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: en querying a Mistral-based model: ValueError: Double free! PhysicalTokenBlock(device=Device.GPU, block_number=9180, ref_count=0) is already freed. Interestingly, it ~primarily~ happens when I'm hitting the endpoint fro...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: free! Getting this error really frequently when querying a Mistral-based model: ValueError: Double free! PhysicalTokenBlock(device=Device.GPU, block_number=9180, ref_count=0) is already freed. Interestingly, it ~primari...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: y, it ~primarily~ happens when I'm hitting the endpoint from pure python/request, not when I'm using Postman. But, it has happened when using Postman and when just querying the model locally, though less frequently.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
