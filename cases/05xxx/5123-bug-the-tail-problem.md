# vllm-project/vllm#5123: [Bug]: The tail problem

| 字段 | 值 |
| --- | --- |
| Issue | [#5123](https://github.com/vllm-project/vllm/issues/5123) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: The tail problem

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug I wonder if I'm the only one to meet the problem that each time the generation process is closing up, it just sticks there for a long time. So the main cost of time is at the very beginning and the closing procedure. I wonder why and how can i fix it.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: The tail problem bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug I wonder if I'm the only one to meet the problem that each time the generation proc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
