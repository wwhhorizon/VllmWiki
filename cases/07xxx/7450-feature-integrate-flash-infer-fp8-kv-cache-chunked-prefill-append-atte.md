# vllm-project/vllm#7450: [Feature]: Integrate `flash-infer` FP8 KV Cache Chunked-Prefill (Append Attention)

| 字段 | 值 |
| --- | --- |
| Issue | [#7450](https://github.com/vllm-project/vllm/issues/7450) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Integrate `flash-infer` FP8 KV Cache Chunked-Prefill (Append Attention)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch From new Flash Infer Release https://github.com/flashinfer-ai/flashinfer/releases/tag/v0.1.4 cc @comaniac ### Additional context Follow up to: https://github.com/vllm-project/vllm/pull/7208, https://github.com/vllm-project/vllm/pull/7185

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Integrate `flash-infer` FP8 KV Cache Chunked-Prefill (Append Attention) feature request;stale ### 🚀 The feature, motivation and pitch From new Flash Infer Release https://github.com/flashinfer-ai/flashinfer/r...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: e, motivation and pitch From new Flash Infer Release https://github.com/flashinfer-ai/flashinfer/releases/tag/v0.1.4 cc @comaniac ### Additional context Follow up to: https://github.com/vllm-project/vllm/pull/7208, http...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Feature]: Integrate `flash-infer` FP8 KV Cache Chunked-Prefill (Append Attention) feature request;stale ### 🚀 The feature, motivation and pitch From new Flash Infer Release https://github.com/flashinfer-ai/flashinfer/r...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Feature]: Integrate `flash-infer` FP8 KV Cache Chunked-Prefill (Append Attention) feature request;stale ### 🚀 The feature, motivation and pitch From new Flash Infer Release https://github.com/flashinfer-ai/flashinfer/r...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
