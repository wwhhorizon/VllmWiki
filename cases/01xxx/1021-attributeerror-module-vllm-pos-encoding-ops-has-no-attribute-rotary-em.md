# vllm-project/vllm#1021: AttributeError: module 'vllm.pos_encoding_ops' has no attribute 'rotary_embedding'. Did you mean: 'rotary_embedding_neox'?

| 字段 | 值 |
| --- | --- |
| Issue | [#1021](https://github.com/vllm-project/vllm/issues/1021) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> AttributeError: module 'vllm.pos_encoding_ops' has no attribute 'rotary_embedding'. Did you mean: 'rotary_embedding_neox'?

### Issue 正文摘录

llama2-7b 微调后的模型

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: no attribute 'rotary_embedding'. Did you mean: 'rotary_embedding_neox'? llama2-7b 微调后的模型

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
