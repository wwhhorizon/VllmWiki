# vllm-project/vllm#2713: BUG: TokenizerGroup doesn't behave like a PreTrainedTokenizer

| 字段 | 值 |
| --- | --- |
| Issue | [#2713](https://github.com/vllm-project/vllm/issues/2713) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> BUG: TokenizerGroup doesn't behave like a PreTrainedTokenizer

### Issue 正文摘录

The new [TokenizerGroup](https://github.com/vllm-project/vllm/blob/93b38bea5dd03e1b140ca997dfaadef86f8f1855/vllm/transformers_utils/tokenizer.py#L91) class that `LLM.llm_engine.tokenizer` has now become, doesn't behave like a tokenizer. For instance, the [LLM.set_tokenizer](https://github.com/vllm-project/vllm/blob/93b38bea5dd03e1b140ca997dfaadef86f8f1855/vllm/entrypoints/llm.py#L116) method sets the `tokenizer` attribute as a `PreTrainedTokenizer`, _not_ a `TokenizerGroup`. Also, tools like [lm-format-enforcer](https://github.com/noamgat/lm-format-enforcer/tree/main) [assumes that the `tokenizer` attribute is indeed a tokenizer](https://github.com/noamgat/lm-format-enforcer/blob/6a2784bf0b3ecc26b2e031af959cfd0f64f42020/lmformatenforcer/integrations/transformers.py#L58), causing it to now give `AttributeError`s. It seems like either the `LLM.llm_engine.tokenizer` should revert back to being a `PreTrainedTokenizer`, or otherwise at least have properties and methods which call the corresponding properties and methods of the underlying `PreTrainedTokenizer`.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: a `PreTrainedTokenizer`, _not_ a `TokenizerGroup`. Also, tools like [lm-format-enforcer](https://github.com/noamgat/lm-format-enforcer/tree/main) [assumes that the `tokenizer` attribute is indeed a tokenizer](https://gi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
