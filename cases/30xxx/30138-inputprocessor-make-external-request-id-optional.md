# vllm-project/vllm#30138: [InputProcessor] Make external request_id optional

| 字段 | 值 |
| --- | --- |
| Issue | [#30138](https://github.com/vllm-project/vllm/issues/30138) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [InputProcessor] Make external request_id optional

### Issue 正文摘录

Perhaps we can do this as a follow-on, but it might be good to make the external req id optional so in the default case we can then have a more compact internal id. We could then also avoid generating multiple uuids per request in the api server case. _Originally posted by @njhill in https://github.com/vllm-project/vllm/pull/27987#discussion_r2578690704_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [InputProcessor] Make external request_id optional stale Perhaps we can do this as a follow-on, but it might be good to make the external req id optional so in the default case we can then have a more compact internal i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
