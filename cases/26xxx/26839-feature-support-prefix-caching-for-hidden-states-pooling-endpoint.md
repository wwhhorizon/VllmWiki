# vllm-project/vllm#26839: [Feature]: Support Prefix Caching for Hidden States (Pooling Endpoint)

| 字段 | 值 |
| --- | --- |
| Issue | [#26839](https://github.com/vllm-project/vllm/issues/26839) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support Prefix Caching for Hidden States (Pooling Endpoint)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I would like the `/pooling` endpoint to support prefix caching for hidden states. ### Background The `/pooling` endpoint is designed to extract hidden states/embeddings by performing a full prefill pass over all input tokens. However, it currently doesn't support prefix caching - every request recomputes all tokens from scratch, even for repeated prefixes. ### Feature Request: Enable prefix caching for the `/pooling` endpoint, so that: - Hidden states for cache-hit tokens are retrieved from cache (not recomputed) - Only new/uncached tokens need computation - The complete hidden states (cached + newly computed) are returned ### Why This Matters: Many applications process the same prefixes repeatedly (system prompts, instruction templates, etc.): - Without hidden state caching: every `/pooling` request recomputes the entire sequence - With hidden state caching: reuse cached hidden states -> only compute new tokens -> much better throughput ### Alternatives Currently, the only option is to use `/pooling` without prefix caching, which results in high latency for repeated prefixes. ### Additional context Related issues: - #12249 - #11905 This fea...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: re]: Support Prefix Caching for Hidden States (Pooling Endpoint) feature request;stale ### 🚀 The feature, motivation and pitch I would like the `/pooling` endpoint to support prefix caching for hidden states. ### Backgr...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ng: reuse cached hidden states -> only compute new tokens -> much better throughput ### Alternatives Currently, the only option is to use `/pooling` without prefix caching, which results in high latency for repeated pre...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: prefix caching for the `/pooling` endpoint, so that: - Hidden states for cache-hit tokens are retrieved from cache (not recomputed) - Only new/uncached tokens need computation - The complete hidden states (cached + newl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: icy. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [[documentation page](https://docs.vllm.ai/en/latest/)](...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: 249 - #11905 This feature would require caching hidden states alongside KV cache, sharing the same prefix matching logic and eviction policy. ### Before submitting a new issue... - [x] Make sure you already searched for...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
