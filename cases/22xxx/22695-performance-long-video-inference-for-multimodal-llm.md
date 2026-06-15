# vllm-project/vllm#22695: [Performance]: Long-Video Inference for Multimodal LLM

| 字段 | 值 |
| --- | --- |
| Issue | [#22695](https://github.com/vllm-project/vllm/issues/22695) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Long-Video Inference for Multimodal LLM

### Issue 正文摘录

### Proposal to improve performance ## Motivation. vLLM currently schedules **the entire video** for vision encoding before any text tokens are produced. For long inputs of video this results in: * Very high peak GPU memory usage (all frame features resident simultaneously). * Long “dead time” during the pre-fill phase → poor latency & throughput. * Wasted opportunity: text generation already runs in a chunked fashion, so the LM seldom needs the full set of frame embeddings up-front. --- ## 🎯 Goal Introduce **streaming / chunk-level vision encoding** so that MMLM (e.g., LLaVa-MMLM) can handle arbitrarily long videos with: 1. Bounded memory (only a sliding window of frames kept on GPU). 2. Overlapped execution between the vision encoder, KV-cache computation, and token generation. --- ## 🛠️ Proposed Change ### 1. Frame-wise chunking * Slice the video along the temporal dimension into configurable chunks (e.g., 8–32 frames). * Encode each chunk independently to partial embedding tensors. ### 2. Lazy / on-demand encoding * During pre-fill, request only the chunks needed to emit the next text chunk. * Retain a small sliding window of recent chunk embeddings on GPU; spill older ones to...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: t simultaneously). * Long “dead time” during the pre-fill phase → poor latency & throughput. * Wasted opportunity: text generation already runs in a chunked fashion, so the LM seldom needs the full set of frame embeddin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Performance]: Long-Video Inference for Multimodal LLM performance;stale ### Proposal to improve performance ## Motivation. vLLM currently schedules **the entire video** for vision encoding before any text tokens are pr...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Performance]: Long-Video Inference for Multimodal LLM performance;stale ### Proposal to improve performance ## Motivation. vLLM currently schedules **the entire video** for vision encoding before any text tokens are pr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: request only the chunks needed to emit the next text chunk. * Retain a small sliding window of recent chunk embeddings on GPU; spill older ones to CPU/disk under pressure. ### 3. Scheduler updates * Extend `Scheduler` t...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: produced. For long inputs of video this results in: * Very high peak GPU memory usage (all frame features resident simultaneously). * Long “dead time” during the pre-fill phase → poor latency & throughput. * Wasted oppo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
