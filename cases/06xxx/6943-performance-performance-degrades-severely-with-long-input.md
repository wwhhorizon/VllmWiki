# vllm-project/vllm#6943: [Performance]: Performance degrades severely with long input

| 字段 | 值 |
| --- | --- |
| Issue | [#6943](https://github.com/vllm-project/vllm/issues/6943) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Performance degrades severely with long input

### Issue 正文摘录

### Proposal to improve performance When I feed vllm with inputs of about 1000 tokens, its performance drops by about 20%-30% compared to very short inputs(like 'what is your name'). However, the same problem does not occur with lmdeploy and fastertransformer. With nv prof, I found that the difference is that the flashattention kernel takes longer time. the short input: ![image](https://github.com/user-attachments/assets/5c87f5ba-f0f4-4c6c-9a2b-7dc66a475dfc) long input ![image](https://github.com/user-attachments/assets/4fbf27b8-5769-401c-a30f-b36949eb33ea) So I want to know where the problem lies, please help me. ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ```

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: astertransformer. With nv prof, I found that the difference is that the flashattention kernel takes longer time. the short input: ![image](https://github.com/user-attachments/assets/5c87f5ba-f0f4-4c6c-9a2b-7dc66a475dfc)...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Performance]: Performance degrades severely with long input performance;stale ### Proposal to improve performance When I feed vllm with inputs of about 1000 tokens, its performance drops by about 20%-30% compared to ve...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: know where the problem lies, please help me. ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The ou...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
