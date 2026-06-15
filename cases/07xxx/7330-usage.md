# vllm-project/vllm#7330: [Usage]:  流式输出前面几个字符为啥要设置成空字符？不能直接输出模型的生成吗

| 字段 | 值 |
| --- | --- |
| Issue | [#7330](https://github.com/vllm-project/vllm/issues/7330) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]:  流式输出前面几个字符为啥要设置成空字符？不能直接输出模型的生成吗

### Issue 正文摘录

### Your current environment 流式输出前面几个字符为啥要设置成空字符？不能直接输出模型的生成吗 ### How would you like to use vllm 流式输出前面几个字符为啥要设置成空字符？不能直接输出模型的生成吗

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: 流式输出前面几个字符为啥要设置成空字符？不能直接输出模型的生成吗 usage;stale ### Your current environment 流式输出前面几个字符为啥要设置成空字符？不能直接输出模型的生成吗 ### How would you like to use vllm 流式输出前面几个字符为啥要设置成空字符？不能直接输出模型的生成吗

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
