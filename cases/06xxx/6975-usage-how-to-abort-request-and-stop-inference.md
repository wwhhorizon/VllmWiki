# vllm-project/vllm#6975: [Usage]: how to abort request and stop inference?

| 字段 | 值 |
| --- | --- |
| Issue | [#6975](https://github.com/vllm-project/vllm/issues/6975) |
| 状态 | closed |
| 标签 | usage;unstale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: how to abort request and stop inference?

### Issue 正文摘录

### Your current environment vllm 0.5.0post1 ### How would you like to use vllm I want to abort a request and stop inference actively, considering the case: an inference of a request lasts too long time or generate token repeatly and cannot stop, I want to stop the inference in vllm (do not need to stop by user)

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: how to abort request and stop inference? usage;unstale ### Your current environment vllm 0.5.0post1 ### How would you like to use vllm I want to abort a request and stop inference actively, considering the case...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
