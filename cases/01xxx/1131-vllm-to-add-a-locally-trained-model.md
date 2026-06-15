# vllm-project/vllm#1131: vLLM to add a locally trained model

| 字段 | 值 |
| --- | --- |
| Issue | [#1131](https://github.com/vllm-project/vllm/issues/1131) |
| 状态 | closed |
| 标签 |  |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> vLLM to add a locally trained model

### Issue 正文摘录

I see a prerequisite of uploading a trained transformer model on Hugging Face, can we instead serve our pre-trained transformer models saved locally in a directory

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: vLLM to add a locally trained model I see a prerequisite of uploading a trained transformer model on Hugging Face, can we instead serve our pre-trained transformer models saved locally in a directory

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
