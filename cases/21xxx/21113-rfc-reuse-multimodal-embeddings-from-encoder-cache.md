# vllm-project/vllm#21113: [RFC]: Reuse multimodal embeddings from encoder cache

| 字段 | 值 |
| --- | --- |
| Issue | [#21113](https://github.com/vllm-project/vllm/issues/21113) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Reuse multimodal embeddings from encoder cache

### Issue 正文摘录

### 🚀 The feature, motivation and pitch --- #### Motivation In real-world multimodal workflows (vision chat, RAG-with-images, agent loops) the *same* image or audio clip is often reused across many prompts. Today, vLLM re-encodes identical media on different request, wasting: * Encoder + projector compute * GPU memory bandwidth * Scheduler slots Re-using cached embeddings will cut end-to-end latency and boost throughput. --- #### High-Level Plan 1. **Stable key per media asset** Compute a deterministic `mm_hash` (e.g., SHA-256 of raw bytes or deterministic pre-processor output) for every image / audio / video frame. 2. **LRU Multimodal Embedding Cache** GPU-resident key → tensor store with configurable capacity and LRU eviction. 3. **Scheduler & EncoderCacheManager changes** • On request arrival, Scheduler queries EncoderCacheManager with each `mm_hash`. • Cache hit ⇒ skip Encoder + Projector, fetch embeddings. • Cache miss ⇒ run Encoder + Projector and write back. 4. **Memory control & eviction** EncoderCacheManager owns allocation, frees memory, and evicts least-recently-used entries under pressure. 5. **Backward compatibility** Cache is opt-in (`multimodal_cache.enabled=false`...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: dwidth * Scheduler slots Re-using cached embeddings will cut end-to-end latency and boost throughput. --- #### High-Level Plan 1. **Stable key per media asset** Compute a deterministic `mm_hash` (e.g., SHA-256 of raw by...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: - #### High-Level Plan 1. **Stable key per media asset** Compute a deterministic `mm_hash` (e.g., SHA-256 of raw bytes or deterministic pre-processor output) for every image / audio / video frame. 2. **LRU Multimodal Em...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ross many prompts. Today, vLLM re-encodes identical media on different request, wasting: * Encoder + projector compute * GPU memory bandwidth * Scheduler slots Re-using cached embeddings will cut end-to-end latency and...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ting: * Encoder + projector compute * GPU memory bandwidth * Scheduler slots Re-using cached embeddings will cut end-to-end latency and boost throughput. --- #### High-Level Plan 1. **Stable key per media asset** Comput...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [RFC]: Reuse multimodal embeddings from encoder cache RFC ### 🚀 The feature, motivation and pitch --- #### Motivation In real-world multimodal workflows (vision chat, RAG-with-images, agent loops) the *same* image or au...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
