# vllm-project/vllm#6362: [Misc]: Multimodal data and continuous batching

| 字段 | 值 |
| --- | --- |
| Issue | [#6362](https://github.com/vllm-project/vllm/issues/6362) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Multimodal data and continuous batching

### Issue 正文摘录

### Anything you want to discuss about vllm. I see multimodal data only send for first time. Will continuous batching put seq in prefill state and decode state together? If this happened, how to match the multimodal data to each seq? e.g. the current step batch_size=2, one is prefill and the other one is decode. the input_id_shape is [2,] the multimodal data shape is [1,], how can I tell the multimodal data belongs to which input?

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: modal data only send for first time. Will continuous batching put seq in prefill state and decode state together? If this happened, how to match the multimodal data to each seq? e.g. the current step batch_size=2, one i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Misc]: Multimodal data and continuous batching ### Anything you want to discuss about vllm. I see multimodal data only send for first time. Will continuous batching put seq in prefill state and decode state together? I...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
