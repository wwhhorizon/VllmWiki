# vllm-project/vllm#5762: [Usage]: How to set --max-logprobs to the default length of LLM's vocab_size.

| 字段 | 值 |
| --- | --- |
| Issue | [#5762](https://github.com/vllm-project/vllm/issues/5762) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to set --max-logprobs to the default length of LLM's vocab_size.

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm When I use a different different LLM, I have to set --max-logprobs to it's vocab_size manually. Is there an easy way to set --max-logprobs to be vocab_size by default ?

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: w to set --max-logprobs to the default length of LLM's vocab_size. usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm When I use a different dif...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
