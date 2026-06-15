# vllm-project/vllm#1304: Could you support Attention Sink?

| 字段 | 值 |
| --- | --- |
| Issue | [#1304](https://github.com/vllm-project/vllm/issues/1304) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Could you support Attention Sink?

### Issue 正文摘录

Efficient Streaming Language Models with Attention Sinks [paper](https://arxiv.org/abs/2309.17453) These repo has already implemented it: [attention_sinks](https://github.com/tomaarsen/attention_sinks) [streaming-llm](https://github.com/mit-han-lab/streaming-llm)

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Could you support Attention Sink? feature request;stale Efficient Streaming Language Models with Attention Sinks [paper](https://arxiv.org/abs/2309.17453) These repo has already implemented it: [attention_sinks](https:/...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Could you support Attention Sink? feature request;stale Efficient Streaming Language Models with Attention Sinks [paper](https://arxiv.org/abs/2309.17453) These repo has already implemented it: [attention_sinks](https:/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: pport Attention Sink? feature request;stale Efficient Streaming Language Models with Attention Sinks [paper](https://arxiv.org/abs/2309.17453) These repo has already implemented it: [attention_sinks](https://github.com/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
