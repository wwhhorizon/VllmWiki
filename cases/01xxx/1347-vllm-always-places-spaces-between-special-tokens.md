# vllm-project/vllm#1347: vLLM always places spaces between special tokens

| 字段 | 值 |
| --- | --- |
| Issue | [#1347](https://github.com/vllm-project/vllm/issues/1347) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> vLLM always places spaces between special tokens

### Issue 正文摘录

I have a model that in certain cases is expected to generate sequences of special tokens. When I call in to vLLM the expected special tokens in the `text` of the response have spaces between them. This is caused by an incomplete (when compared with the adapted huggingface version) API for `_convert_tokens_to_string_with_added_encoders`. The referenced implementation (see below) allows for the caller to pass a `spaces_between_special_tokens: bool` but this option is absent from the vLLM implementation. ``` # Adapted from # https://github.com/huggingface/transformers/blob/v4.28.0/src/transformers/tokenization_utils.py#L921 # NOTE(woosuk): The following code is slow because it runs a for loop over # the output_tokens. In Python, running a for loop over a list can be slow # even when the loop body is very simple.```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: vLLM always places spaces between special tokens I have a model that in certain cases is expected to generate sequences of special tokens. When I call in to vLLM the expected special tokens in the `text` of the response...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: vLLM always places spaces between special tokens I have a model that in certain cases is expected to generate sequences of special tokens. When I call in to vLLM the expected special tokens in the `text` of the response...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
