# vllm-project/vllm#3401: [BUG] dist.broadcast miss group argument

| 字段 | 值 |
| --- | --- |
| Issue | [#3401](https://github.com/vllm-project/vllm/issues/3401) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [BUG] dist.broadcast miss group argument

### Issue 正文摘录

https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/parallel_utils/communication_op.py#L180 if group is not none, this call will hang all workers.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: miss group argument https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/parallel_utils/communication_op.py#L180 if group is not none, this call will hang all workers.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
