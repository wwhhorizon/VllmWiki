# vllm-project/vllm#1253: StreamingLLM support?

| 字段 | 值 |
| --- | --- |
| Issue | [#1253](https://github.com/vllm-project/vllm/issues/1253) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> StreamingLLM support?

### Issue 正文摘录

Hey, This was a really interesting solution to the KV cache for long context. https://github.com/mit-han-lab/streaming-llm I was wondering it could be implemented here. From the looks of things it doesn't change anything about the model itself, its more about how the KV cache is implemented. They show that they can have coherent inference over millions of tokens Thanks!

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: StreamingLLM support? feature request;stale Hey, This was a really interesting solution to the KV cache for long context. https://github.com/mit-han-lab/streaming-llm I was wondering it could be implemented here. From t...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: eature request;stale Hey, This was a really interesting solution to the KV cache for long context. https://github.com/mit-han-lab/streaming-llm I was wondering it could be implemented here. From the looks of things it d...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: nted here. From the looks of things it doesn't change anything about the model itself, its more about how the KV cache is implemented. They show that they can have coherent inference over millions of tokens Thanks!

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
