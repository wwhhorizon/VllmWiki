# vllm-project/vllm#2265: Q: Support for session-aware cache eviction?

| 字段 | 值 |
| --- | --- |
| Issue | [#2265](https://github.com/vllm-project/vllm/issues/2265) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Q: Support for session-aware cache eviction?

### Issue 正文摘录

Some inference engines (like [lmdeploy](https://github.com/InternLM/lmdeploy/blob/c95863cbd8ec9a8f1863a23cd83bf4ccc4afd13d/docs/en/restful_api.md?plain=1#L24)) support passing `session_id`s at inference time to hint the engine to manage cache for that request accordingly for persistent sessions where the previous messages of the context are going to remain fixed within that session. I think this would be a growing need over time and it'd be very useful to have built-in support for this in vllm. That said, the interface is going to be tricky and needs a lot of thought. What do you think @WoosukKwon ? If it aligns with the project goals, we could start an RFC for this.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ssion_id`s at inference time to hint the engine to manage cache for that request accordingly for persistent sessions where the previous messages of the context are going to remain fixed within that session. I think this...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
