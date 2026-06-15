# vllm-project/vllm#2668: Mixtral AWQ result cut short

| 字段 | 值 |
| --- | --- |
| Issue | [#2668](https://github.com/vllm-project/vllm/issues/2668) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Mixtral AWQ result cut short

### Issue 正文摘录

Whenever I use vLLM with Mixtral AWQ I am finding that the response gets cut short with **'finish_reason': 'length'** Even though I have set high values for **--max_tokens** and **--max-model-len** Does anyone know why this might be?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ** Even though I have set high values for **--max_tokens** and **--max-model-len** Does anyone know why this might be?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
