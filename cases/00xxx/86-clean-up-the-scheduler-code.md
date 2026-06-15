# vllm-project/vllm#86: Clean up the scheduler code

| 字段 | 值 |
| --- | --- |
| Issue | [#86](https://github.com/vllm-project/vllm/issues/86) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Clean up the scheduler code

### Issue 正文摘录

Currently, the scheduler code includes the code for experimental purposes (e.g., collecting various system stats). The code should be removed or minimized.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Clean up the scheduler code Currently, the scheduler code includes the code for experimental purposes (e.g., collecting various system stats). The code should be removed or minimized.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
