# vllm-project/vllm#1892: feature request：skip some tokens when use presence_penalty or frequency_penalty

| 字段 | 值 |
| --- | --- |
| Issue | [#1892](https://github.com/vllm-project/vllm/issues/1892) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> feature request：skip some tokens when use presence_penalty or frequency_penalty

### Issue 正文摘录

i find that, when use those two hyper parameters, punctions will be dissappeared in the text when it goes long and long. i think the basic reason is those two hyper parameters. it's obviously that puntions will occured multiple times in an answer and so will be peanltified bigger then other punctions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: feature request：skip some tokens when use presence_penalty or frequency_penalty i find that, when use those two hyper parameters, punctions will be dissappeared in the text when it goes long and long. i think the basic...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
