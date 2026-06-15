# vllm-project/vllm#766: Serving a .tar.gz model file

| 字段 | 值 |
| --- | --- |
| Issue | [#766](https://github.com/vllm-project/vllm/issues/766) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Serving a .tar.gz model file

### Issue 正文摘录

I have a 13GB llama 2 fine tuned model called "llama2-finetuned.tar.zst". How would I go about deploying this using vllm? I have only tried the hugging face models.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Serving a .tar.gz model file I have a 13GB llama 2 fine tuned model called "llama2-finetuned.tar.zst". How would I go about deploying this using vllm? I have only tried the hugging face models.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
