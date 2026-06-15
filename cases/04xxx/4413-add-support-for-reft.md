# vllm-project/vllm#4413: Add support for ReFT

| 字段 | 值 |
| --- | --- |
| Issue | [#4413](https://github.com/vllm-project/vllm/issues/4413) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Add support for ReFT

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Motivation is to allow ReFT representations to be applied on the fly during inference, which can be done in a batchwise manner. this is much faster than applying LoRAs ### Alternatives LoRA is too slow as it requires adapter weights to be added, which increases the number of operations. ### Additional context See https://github.com/stanfordnlp/pyreft/issues/63

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Add support for ReFT feature request;stale ### 🚀 The feature, motivation and pitch Motivation is to allow ReFT representations to be applied on the fly during inference, which can be done in a batchwise manner. this is...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
