# vllm-project/vllm#3159: Request for fine-tuning using api endpoint

| 字段 | 值 |
| --- | --- |
| Issue | [#3159](https://github.com/vllm-project/vllm/issues/3159) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Request for fine-tuning using api endpoint

### Issue 正文摘录

Similar to https://platform.openai.com/docs/guides/fine-tuning/example-format, could this feature be added? This would make fine-tuning much easier.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: t Similar to https://platform.openai.com/docs/guides/fine-tuning/example-format, could this feature be added? This would make fine-tuning much easier.
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Request for fine-tuning using api endpoint Similar to https://platform.openai.com/docs/guides/fine-tuning/example-format, could this feature be added? This would make fine-tuning much easier.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
