# vllm-project/vllm#7808: [Usage]: How to generate independent samples for a given input? 

| 字段 | 值 |
| --- | --- |
| Issue | [#7808](https://github.com/vllm-project/vllm/issues/7808) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to generate independent samples for a given input? 

### Issue 正文摘录

### Your current environment vllm==0.4.0 ### How would you like to use vllm For a given question, I want to independently sample N responses. I am not sure what is the best way to do it in vllm. I have several options: 1. In `SamplingParams`, I can set `n=20`. But I am not sure whether the generations in this way are independent. 2. I can feed the same 20 prompts in a list to `vllm.generate`. But in this case, the generate function seed is also fixed. 3. I can call `vllm.generate` 20 times can set different seed each time. But this takes very long to run. Anybody knows anything about this usage? Thanks!

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: How to generate independent samples for a given input? usage;stale ### Your current environment vllm==0.4.0 ### How would you like to use vllm For a given question, I want to independently sample N responses. I...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
