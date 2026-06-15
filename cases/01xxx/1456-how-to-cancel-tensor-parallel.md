# vllm-project/vllm#1456: How to cancel tensor parallel.

| 字段 | 值 |
| --- | --- |
| Issue | [#1456](https://github.com/vllm-project/vllm/issues/1456) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How to cancel tensor parallel.

### Issue 正文摘录

Hi, I am making multi replica of the vllm instance with the fast-chat. But I found the `master-worker` is unstable which sometimes increase its output while sometimes not. After many experiments, I found that this is caused by the `Tensor Parallel`, the vllm's request in a period of time will be responsed all in one, which causes the sharpe decrease of the GPU utility. So I want to know how to cancel this feature to process the request one by one.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: iments, I found that this is caused by the `Tensor Parallel`, the vllm's request in a period of time will be responsed all in one, which causes the sharpe decrease of the GPU utility. So I want to know how to cancel thi...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
