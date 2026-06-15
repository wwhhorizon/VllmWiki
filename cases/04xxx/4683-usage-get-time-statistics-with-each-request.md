# vllm-project/vllm#4683: [Usage]: Get time statistics with each request

| 字段 | 值 |
| --- | --- |
| Issue | [#4683](https://github.com/vllm-project/vllm/issues/4683) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Get time statistics with each request

### Issue 正文摘录

I would like to know if there is a way to get usage statistics with each request (maybe with a flag parameter): I would like to know queue wait time, num_prompt_tokens, num_generated_tokens, time for prefill stage, time for decoding stage etc returned with each request. If it doesnt already exist, please point me how i can add such a feature. Thanks

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Usage]: Get time statistics with each request usage;stale I would like to know if there is a way to get usage statistics with each request (maybe with a flag parameter): I would like to know queue wait time, num_prompt...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
