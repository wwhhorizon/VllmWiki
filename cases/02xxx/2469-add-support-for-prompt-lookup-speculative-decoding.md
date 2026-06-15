# vllm-project/vllm#2469: Add support for prompt-lookup speculative decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#2469](https://github.com/vllm-project/vllm/issues/2469) |
| 状态 | closed |
| 标签 | performance;feature request |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Add support for prompt-lookup speculative decoding

### Issue 正文摘录

So transformers has introduced support for speculative decoding of ngrams. https://github.com/huggingface/transformers/pull/27979 It's as simple as passing `prompt_lookup_num_tokens=10` to `model.generate` in newer version of transformers. ## Why would this be useful? Most often it will speed up inference by up to 3x! I have not looked it up yet but I think it wouldn't be too complicated to add a parameter to vLLM so that we can use speculative decoding w/ vLLM. At least the speed up can make the trouble worthwhile. Let me know what you think.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: troduced support for speculative decoding of ngrams. https://github.com/huggingface/transformers/pull/27979 It's as simple as passing `prompt_lookup_num_tokens=10` to `model.generate` in newer version of transformers. #...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Add support for prompt-lookup speculative decoding performance;feature request So transformers has introduced support for speculative decoding of ngrams. https://github.com/huggingface/transformers/pull/27979 It's as si...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: le as passing `prompt_lookup_num_tokens=10` to `model.generate` in newer version of transformers. ## Why would this be useful? Most often it will speed up inference by up to 3x! I have not looked it up yet but I think i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
