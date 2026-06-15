# vllm-project/vllm#6899: [Feature]: Add Sliding Window support to FlashInfer backend?

| 字段 | 值 |
| --- | --- |
| Issue | [#6899](https://github.com/vllm-project/vllm/issues/6899) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add Sliding Window support to FlashInfer backend?

### Issue 正文摘录

### 🚀 The feature, motivation and pitch FlashInfer v0.1.2 was just released with sliding window support: https://github.com/flashinfer-ai/flashinfer/releases/tag/v0.1.2 This should allow vLLM to add it, and achieve 8k context length with gemma2. However, in FlashAttention's code I see the following block: ``` if sliding_window is not None: # NOTE(woosuk): flash-attn's sliding window does not work with # paged KV cache. raise ValueError( "Sliding window is not supported in FlashAttention.") ``` Despite FlashAttention supporting sliding window, vLLM's wrapper of flash attention does not. What is the conflict between sliding window and paged KV cache? Does this limitation mean that using it with FlashInfer is also not possible? ### Alternatives FlashAttention was recently updated with logits capping, so if vLLM's wrapper was updated to use it and enabled sliding window support as well, Gemma2 8k context would also be achievable in that route. ### Additional context _No response_

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Feature]: Add Sliding Window support to FlashInfer backend? feature request;stale ### 🚀 The feature, motivation and pitch FlashInfer v0.1.2 was just released with sliding window support: https://github.com/flashinfer-a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Add Sliding Window support to FlashInfer backend? feature request;stale ### 🚀 The feature, motivation and pitch FlashInfer v0.1.2 was just released with sliding window support: https://github.com/flashinfer-a...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: suk): flash-attn's sliding window does not work with # paged KV cache. raise ValueError( "Sliding window is not supported in FlashAttention.") ``` Despite FlashAttention supporting sliding window, vLLM's wrapper of flas...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ngth with gemma2. However, in FlashAttention's code I see the following block: ``` if sliding_window is not None: # NOTE(woosuk): flash-attn's sliding window does not work with # paged KV cache. raise ValueError( "Slidi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: .2 This should allow vLLM to add it, and achieve 8k context length with gemma2. However, in FlashAttention's code I see the following block: ``` if sliding_window is not None: # NOTE(woosuk): flash-attn's sliding window...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
