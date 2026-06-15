# vllm-project/vllm#1342: what is the recommended way to call function of model like transformers do?

| 字段 | 值 |
| --- | --- |
| Issue | [#1342](https://github.com/vllm-project/vllm/issues/1342) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> what is the recommended way to call function of model like transformers do?

### Issue 正文摘录

for example baichuan2-13b has a function `chat` in huggingface's example page using transformers ``` response = model.chat(tokenizer, messages) ``` how could I call this function using vllm like that?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: what is the recommended way to call function of model like transformers do? for example baichuan2-13b has a function `chat` in huggingface's example page using transformers ``` response = model.chat(tokenizer, messages)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
