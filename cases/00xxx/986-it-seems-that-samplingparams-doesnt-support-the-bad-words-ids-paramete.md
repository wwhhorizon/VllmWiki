# vllm-project/vllm#986: It seems that SamplingParams doesnt support the bad_words_ids parameter when generating

| 字段 | 值 |
| --- | --- |
| Issue | [#986](https://github.com/vllm-project/vllm/issues/986) |
| 状态 | closed |
| 标签 | good first issue;feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> It seems that SamplingParams doesnt support the bad_words_ids parameter when generating

### Issue 正文摘录

`bad_words_ids` described [here](https://github.com/huggingface/transformers/blob/main/src/transformers/generation/configuration_utils.py#L145C11-L145C11) is useful for production applications. However It seems that vlllm doesnt support the bad_words_ids parameter when generating. Is there a plan to support it? ``` bad_words_ids(`List[List[int]]`, *optional*): List of list of token ids that are not allowed to be generated. Check [`~generation.NoBadWordsLogitsProcessor`] for further documentation and examples. ```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ssue;feature request `bad_words_ids` described [here](https://github.com/huggingface/transformers/blob/main/src/transformers/generation/configuration_utils.py#L145C11-L145C11) is useful for production applications. Howe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ort the bad_words_ids parameter when generating good first issue;feature request `bad_words_ids` described [here](https://github.com/huggingface/transformers/blob/main/src/transformers/generation/configuration_utils.py#...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
