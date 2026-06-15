# vllm-project/vllm#1742: Lookahead decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#1742](https://github.com/vllm-project/vllm/issues/1742) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 23; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Lookahead decoding

### Issue 正文摘录

They claim lookahead decoding provides a 1.5~2x decoding speedup without a speculative model. Blog post: https://lmsys.org/blog/2023-11-21-lookahead-decoding/ Twitter thread: https://twitter.com/lmsysorg/status/1727056892671950887 Reference implementation: https://github.com/hao-ai-lab/LookaheadDecoding/tree/main Not sure if this would be possible to integrate into vllm?

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Lookahead decoding stale They claim lookahead decoding provides a 1.5~2x decoding speedup without a speculative model. Blog post: https://lmsys.org/blog/2023-11-21-lookahead-decoding/ Twitter thread: https://twitter.com...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: kahead decoding provides a 1.5~2x decoding speedup without a speculative model. Blog post: https://lmsys.org/blog/2023-11-21-lookahead-decoding/ Twitter thread: https://twitter.com/lmsysorg/status/1727056892671950887 Re...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
