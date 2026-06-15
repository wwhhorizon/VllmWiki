# vllm-project/vllm#3119: Should one use tokenizer templates during offline inference?

| 字段 | 值 |
| --- | --- |
| Issue | [#3119](https://github.com/vllm-project/vllm/issues/3119) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Should one use tokenizer templates during offline inference?

### Issue 正文摘录

Hi, I've found that vllm uses [the default tokenizer templates](https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/openai/serving_chat.py#L50) when querying a model via API. However, it is unclear if one should apply the tokenizer templates before generating outputs when using vllm in the offline inference, which happens [here](https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/llm.py). I've found some examples of using the templates during the offline inference (e.g., [here](https://modal.com/docs/examples/vllm_inference)), but I just wanted to clarify this. Thank you.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: m/blob/main/vllm/entrypoints/openai/serving_chat.py#L50) when querying a model via API. However, it is unclear if one should apply the tokenizer templates before generating outputs when using vllm in the offline inferen...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
