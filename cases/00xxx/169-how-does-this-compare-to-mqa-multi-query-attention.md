# vllm-project/vllm#169: How does this compare to MQA (multi-query attention)?

| 字段 | 值 |
| --- | --- |
| Issue | [#169](https://github.com/vllm-project/vllm/issues/169) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How does this compare to MQA (multi-query attention)?

### Issue 正文摘录

https://arxiv.org/abs/1911.02150 For example, StarCoder uses MQA to speed up inference. How does PagedAttention compare to Multi-Query Attention? Are they compatible?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: How does this compare to MQA (multi-query attention)? new-model https://arxiv.org/abs/1911.02150 For example, StarCoder uses MQA to speed up inference. How does PagedAttention compare to Multi-Query Attention? Are they...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
