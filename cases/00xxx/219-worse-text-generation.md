# vllm-project/vllm#219: worse text generation

| 字段 | 值 |
| --- | --- |
| Issue | [#219](https://github.com/vllm-project/vllm/issues/219) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> worse text generation

### Issue 正文摘录

first of all thanks for releasing the awesome library. The output texts seem significantly worse compared to huggingface transformers. Could this be an issue with the tokenizer? Any other ideas? I dont know if it is relevant, but the prompts I am trying are in german and not english.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: awesome library. The output texts seem significantly worse compared to huggingface transformers. Could this be an issue with the tokenizer? Any other ideas? I dont know if it is relevant, but the prompts I am trying are...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
