# vllm-project/vllm#46: Debug the optimal upper-bound performance for swapping (0-cost swapping).

| 字段 | 值 |
| --- | --- |
| Issue | [#46](https://github.com/vllm-project/vllm/issues/46) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Debug the optimal upper-bound performance for swapping (0-cost swapping).

### Issue 正文摘录

Rerun the experiment comparing 0-cost swapping and recomputation. Recomputation should not be faster in any case. If recomputation is consistently faster, we should debug into this.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: imal upper-bound performance for swapping (0-cost swapping). performance;stale Rerun the experiment comparing 0-cost swapping and recomputation. Recomputation should not be faster in any case. If recomputation is consis...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
