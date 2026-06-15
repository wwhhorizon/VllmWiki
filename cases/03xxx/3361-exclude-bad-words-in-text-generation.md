# vllm-project/vllm#3361: Exclude bad words in text generation

| 字段 | 值 |
| --- | --- |
| Issue | [#3361](https://github.com/vllm-project/vllm/issues/3361) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Exclude bad words in text generation

### Issue 正文摘录

Is there a way to exclude bad tokens when generating? This is different from stop_words mentioned in the vLLM docs. Looking for something similar to this HF doc. https://huggingface.co/docs/transformers/v4.38.2/en/internal/generation_utils#transformers.NoBadWordsLogitsProcessor

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ords mentioned in the vLLM docs. Looking for something similar to this HF doc. https://huggingface.co/docs/transformers/v4.38.2/en/internal/generation_utils#transformers.NoBadWordsLogitsProcessor

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
