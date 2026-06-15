# vllm-project/vllm#4814: Remove EOS token before passing the tokenized input to model

| 字段 | 值 |
| --- | --- |
| Issue | [#4814](https://github.com/vllm-project/vllm/issues/4814) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Remove EOS token before passing the tokenized input to model

### Issue 正文摘录

How to remove eos token id before passing the input tokens to model. I'm trying for fine-tuned mistral model. Just because there is an eos token id at the end of sentence, model generates the results for a different input which is similar to original input

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Remove EOS token before passing the tokenized input to model How to remove eos token id before passing the input tokens to model. I'm trying for fine-tuned mistral model. Just because there is an eos token id at the end...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
