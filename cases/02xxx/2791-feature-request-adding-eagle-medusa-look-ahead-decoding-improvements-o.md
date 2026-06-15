# vllm-project/vllm#2791: [Feature Request] Adding Eagle, Medusa, Look Ahead decoding ( improvements of Speculative decoding)

| 字段 | 值 |
| --- | --- |
| Issue | [#2791](https://github.com/vllm-project/vllm/issues/2791) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature Request] Adding Eagle, Medusa, Look Ahead decoding ( improvements of Speculative decoding)

### Issue 正文摘录

Thanks for the great work team. I wonder if there is any plan to add new improvements to speculative decoding such as [Eagle](https://sites.google.com/view/eagle-llm), [Medusa](https://sites.google.com/view/medusa-llm), [look ahead decoding](https://github.com/hao-ai-lab/LookaheadDecoding). These could result in accumulative speed ups for VLLM. cc: @WoosukKwon

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature Request] Adding Eagle, Medusa, Look Ahead decoding ( improvements of Speculative decoding) stale Thanks for the great work team. I wonder if there is any plan to add new improvements to speculative decoding suc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
