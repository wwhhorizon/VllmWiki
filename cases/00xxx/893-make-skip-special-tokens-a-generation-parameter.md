# vllm-project/vllm#893: Make `skip_special_tokens` a generation parameter.

| 字段 | 值 |
| --- | --- |
| Issue | [#893](https://github.com/vllm-project/vllm/issues/893) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Make `skip_special_tokens` a generation parameter.

### Issue 正文摘录

Hi, I have a few models that return structured output by utilizing special tokens as delimiters. As of now, vLLM always skips special tokens during decoding. Would it be possible to add `skip_special_tokens` as a generation parameter? TGI sort of supports this by giving you the option to return individual tokens with their IDs and a boolean indicating whether they are special or not.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Make `skip_special_tokens` a generation parameter. Hi, I have a few models that return structured output by utilizing special tokens as delimiters. As of now, vLLM always skips special tokens during decoding. Would it b...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Make `skip_special_tokens` a generation parameter. Hi, I have a few models that return structured output by utilizing special tokens as delimiters. As of now, vLLM always skips special tokens during decoding. Would it b...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
