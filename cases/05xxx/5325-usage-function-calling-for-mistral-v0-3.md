# vllm-project/vllm#5325: [Usage]: Function calling for mistral v0.3

| 字段 | 值 |
| --- | --- |
| Issue | [#5325](https://github.com/vllm-project/vllm/issues/5325) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Function calling for mistral v0.3

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of a mistral instruct 0.3 for function calling. Is function calling supported with vllm for mistral ?

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Function calling for mistral v0.3 usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of a mistral instruct 0.3...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
