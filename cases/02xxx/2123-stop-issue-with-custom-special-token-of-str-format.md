# vllm-project/vllm#2123: Stop issue with custom special token of str format

| 字段 | 值 |
| --- | --- |
| Issue | [#2123](https://github.com/vllm-project/vllm/issues/2123) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Stop issue with custom special token of str format

### Issue 正文摘录

version: 0.2.4 SamplingParams provides two stop types, str and token id, but there is a problem with using str if a stop words is a special word. Parameters where this problem occurs: ``` stop = " " # is a special word in tokenizer skip_special_tokens = True ``` Code position: vllm/engine/llm_engine.py Reason: The engine will initially use `detokenize_incrementally` to generate `new_text`, followed by `_check_stop` to filter out stop words and raise stop. However, if `skip_special_tokens` is set to `true` and the stop word is deemed special, it will be excluded from the `new_text`, meaning `_check_stop` will not process it. In this case, if the `skip_special_tokens` must remain `true`, we must use the related token ids to handle the stop words.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Stop issue with custom special token of str format version: 0.2.4 SamplingParams provides two stop types, str and token id, but there is a problem with using str if a stop words is a special word. Parameters where this...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Stop issue with custom special token of str format version: 0.2.4 SamplingParams provides two stop types, str and token id, but there is a problem with using str if a stop words is a special word. Parameters where this...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
