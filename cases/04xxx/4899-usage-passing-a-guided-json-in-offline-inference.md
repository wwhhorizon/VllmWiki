# vllm-project/vllm#4899: [Usage]: Passing a guided_json in offline inference

| 字段 | 值 |
| --- | --- |
| Issue | [#4899](https://github.com/vllm-project/vllm/issues/4899) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Passing a guided_json in offline inference

### Issue 正文摘录

### Your current environment ```text vllm 0.4.2 ``` ### How would you like to use vllm I'm trying to force a json generation using outlines in offline inference. I don't see anything related in the documentation. I haven't found an example of chat completion for offline inference, but I've managed to mimic it using chat templates, this is why I need to force a json generation.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Passing a guided_json in offline inference usage;stale ### Your current environment ```text vllm 0.4.2 ``` ### How would you like to use vllm I'm trying to force a json generation using outlines in offline infe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
