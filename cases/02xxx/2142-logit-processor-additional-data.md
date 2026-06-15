# vllm-project/vllm#2142: Logit Processor additional data

| 字段 | 值 |
| --- | --- |
| Issue | [#2142](https://github.com/vllm-project/vllm/issues/2142) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Logit Processor additional data

### Issue 正文摘录

Hi, Currently, logit processors are only aware of the previous generated tokens and the logits: https://github.com/vllm-project/vllm/blob/2acd76f346efcdff4f6ca1d92fe1575c448e4b70/vllm/model_executor/layers/sampler.py#L210 For some applications (like watermarking), additional context can be useful, such as the index of the generation in the original batch. It would be nice if these could be passed as optional parameters to logit processors. Passing the `seq_id` variable would be neat for instance. Additionally, having a higher level interface (such as a LogitProcessor similar to the one in HuggingFace that handles batches instead of individual generations) could be useful (see the changes in https://github.com/vllm-project/vllm/compare/main...julien-piet:vllm:main). Happy to help out with this! Julien

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: com/vllm-project/vllm/blob/2acd76f346efcdff4f6ca1d92fe1575c448e4b70/vllm/model_executor/layers/sampler.py#L210 For some applications (like watermarking), additional context can be useful, such as the index of the genera...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Logit Processor additional data feature request Hi, Currently, logit processors are only aware of the previous generated tokens and the logits: https://github.com/vllm-project/vllm/blob/2acd76f346efcdff4f6ca1d92fe1575c4...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
