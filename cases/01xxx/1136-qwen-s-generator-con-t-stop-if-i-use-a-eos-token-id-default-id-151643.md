# vllm-project/vllm#1136: QWen's generator con't stop if I use a eos_token_id != default id (151643)

| 字段 | 值 |
| --- | --- |
| Issue | [#1136](https://github.com/vllm-project/vllm/issues/1136) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> QWen's generator con't stop if I use a eos_token_id != default id (151643)

### Issue 正文摘录

I add a eos_token to the tokenizer's config files, it wokered

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: QWen's generator con't stop if I use a eos_token_id != default id (151643) I add a eos_token to the tokenizer's config files, it wokered

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
