# vllm-project/vllm#379: [Feature] Add support for `logit_bias`

| 字段 | 值 |
| --- | --- |
| Issue | [#379](https://github.com/vllm-project/vllm/issues/379) |
| 状态 | closed |
| 标签 | good first issue;feature request |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature] Add support for `logit_bias`

### Issue 正文摘录

Support just landed in `transformers` lib for this. See: - [`SequenceBiasLogitsProcessor`](https://huggingface.co/docs/transformers/main/en/internal/generation_utils#transformers.SequenceBiasLogitsProcessor) - [Corresponding `GenerationConfig`](https://huggingface.co/docs/transformers/main/en/main_classes/text_generation#transformers.GenerationConfig.sequence_bias) - [discussion](https://github.com/huggingface/transformers/issues/22168#issuecomment-1477998997)

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ansformers` lib for this. See: - [`SequenceBiasLogitsProcessor`](https://huggingface.co/docs/transformers/main/en/internal/generation_utils#transformers.SequenceBiasLogitsProcessor) - [Corresponding `GenerationConfig`](...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature] Add support for `logit_bias` good first issue;feature request Support just landed in `transformers` lib for this. See: - [`SequenceBiasLogitsProcessor`](https://huggingface.co/docs/transformers/main/en/interna...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
