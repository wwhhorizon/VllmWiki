# vllm-project/vllm#1387: What is best preactice to serve to multiple user?

| 字段 | 值 |
| --- | --- |
| Issue | [#1387](https://github.com/vllm-project/vllm/issues/1387) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> What is best preactice to serve to multiple user?

### Issue 正文摘录

I think i can deal with Btach inference with queue, but is there any way to serve batch inference with streaming like chatGPT?

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: to serve to multiple user? I think i can deal with Btach inference with queue, but is there any way to serve batch inference with streaming like chatGPT?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
