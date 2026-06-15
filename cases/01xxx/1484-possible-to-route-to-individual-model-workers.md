# vllm-project/vllm#1484: possible to route to individual model workers?

| 字段 | 值 |
| --- | --- |
| Issue | [#1484](https://github.com/vllm-project/vllm/issues/1484) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> possible to route to individual model workers?

### Issue 正文摘录

Is it possible to route requests to different model workers depending on some criteria? Thanks!

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: possible to route to individual model workers? Is it possible to route requests to different model workers depending on some criteria? Thanks!
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: possible to route to individual model workers? Is it possible to route requests to different model workers depending on some criteria? Thanks!

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
