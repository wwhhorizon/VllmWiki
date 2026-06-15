# vllm-project/vllm#6197: [Usage]: Is there a way to make the results of two different calls to VLLM with temperature > 0 consistent?

| 字段 | 值 |
| --- | --- |
| Issue | [#6197](https://github.com/vllm-project/vllm/issues/6197) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Is there a way to make the results of two different calls to VLLM with temperature > 0 consistent?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I know that setting the temperature to 0 ensures that the results of two different calls with the same input will be identical. Is there a way to ensure consistent results when the input is different, perhaps by using a seed?

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ts of two different calls to VLLM with temperature > 0 consistent? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I know that setting the te...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
