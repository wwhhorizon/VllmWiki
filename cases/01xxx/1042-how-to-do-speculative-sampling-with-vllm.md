# vllm-project/vllm#1042: How to do speculative sampling with vllm?

| 字段 | 值 |
| --- | --- |
| Issue | [#1042](https://github.com/vllm-project/vllm/issues/1042) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How to do speculative sampling with vllm?

### Issue 正文摘录

When I want to use speculative sampling in the vllm, in the generation step, the number of input tokens of each sequence is larger than one, and then error "an illegal memory access was encountered" is reported. Can you guys suggest a way to support speculative sampling with vllm? Thanks a lot

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: How to do speculative sampling with vllm? When I want to use speculative sampling in the vllm, in the generation step, the number of input tokens of each sequence is larger than one, and then error "an illegal memory ac...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
