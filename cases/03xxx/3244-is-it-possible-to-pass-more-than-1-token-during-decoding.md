# vllm-project/vllm#3244: Is it possible to pass more than 1 token during decoding?

| 字段 | 值 |
| --- | --- |
| Issue | [#3244](https://github.com/vllm-project/vllm/issues/3244) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Is it possible to pass more than 1 token during decoding?

### Issue 正文摘录

I'm tring to implement fast json decoding, but I found that when I pass 2 or more tokens in one iteration, there comes an illegal memroy access error. The idea is inspired by this blog: https://lmsys.org/blog/2024-02-05-compressed-fsm/

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: is inspired by this blog: https://lmsys.org/blog/2024-02-05-compressed-fsm/
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Is it possible to pass more than 1 token during decoding? stale I'm tring to implement fast json decoding, but I found that when I pass 2 or more tokens in one iteration, there comes an illegal memroy access error. The...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
