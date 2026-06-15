# vllm-project/vllm#7560: [Feature]: Automatic Prefix Caching and Truncating. Possibilty for Context Shifting.

| 字段 | 值 |
| --- | --- |
| Issue | [#7560](https://github.com/vllm-project/vllm/issues/7560) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Automatic Prefix Caching and Truncating. Possibilty for Context Shifting.

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently when using the Automatic Prefix Caching when you truncate the input (for chat related generation) because of the context limit. The Automatic Prefix Caching will invalidate the cache because the first block will not correlate to the first block of the truncated input. If it would be possible to Context Shift like [llama.cpp](https://github.com/ggerganov/llama.cpp/blob/master/examples/server/server.cpp#L1949) It would eliminate long TTFT times in my case using 24k context length. Would this be possible to implement? Thank you for your time! ### Alternatives _No response_ ### Additional context The hash is calculated based on the token IDs in the block and the hash of the previous block. When the input gets truncated due to the context length, the token IDs in the block change, which in turn changes the content hash. This causes the cache to be invalidated.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Prefix Caching and Truncating. Possibilty for Context Shifting. feature request;stale ### 🚀 The feature, motivation and pitch Currently when using the Automatic Prefix Caching when you truncate the input (for chat relat...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: The Automatic Prefix Caching will invalidate the cache because the first block will not correlate to the first block of the truncated input. If it would be possible to Context Shift like [llama.cpp](https://github.com/g...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: k of the truncated input. If it would be possible to Context Shift like [llama.cpp](https://github.com/ggerganov/llama.cpp/blob/master/examples/server/server.cpp#L1949) It would eliminate long TTFT times in my case usin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
