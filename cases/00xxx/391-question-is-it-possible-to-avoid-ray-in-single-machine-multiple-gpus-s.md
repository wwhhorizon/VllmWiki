# vllm-project/vllm#391: question: Is it possible to avoid ray in single machine multiple GPUs serving?

| 字段 | 值 |
| --- | --- |
| Issue | [#391](https://github.com/vllm-project/vllm/issues/391) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> question: Is it possible to avoid ray in single machine multiple GPUs serving?

### Issue 正文摘录

I'm uncertain whether it's feasible to bypass Ray when serving on a single machine with multiple GPUs. Ray introduces additional maintenance costs in this use case.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: t possible to avoid ray in single machine multiple GPUs serving? feature request I'm uncertain whether it's feasible to bypass Ray when serving on a single machine with multiple GPUs. Ray introduces additional maintenan...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
