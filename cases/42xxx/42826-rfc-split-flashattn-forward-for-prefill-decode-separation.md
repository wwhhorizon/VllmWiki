# vllm-project/vllm#42826: [RFC]: Split Flashattn Forward for Prefill/Decode Separation

| 字段 | 值 |
| --- | --- |
| Issue | [#42826](https://github.com/vllm-project/vllm/issues/42826) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Split Flashattn Forward for Prefill/Decode Separation

### Issue 正文摘录

### Motivation. ## Summary Separate the attention forward computation into prefill and decode paths, using `flash_attn_varlen_func` for prefill and `flash_attn_with_kvcache` for decode tokens. ## Motivation 1. **Different access patterns**: Prefill accesses full KV sequences while decode accesses sparse KV cache entries. 2. **API optimization**: `flash_attn_with_kvcache` is optimized for block-based KV cache lookups during decode. 3. **Prefix caching**: Support explicit `cu_prefix_kv_lens` for better prefix caching strategy. ### Proposed Change. ## Detailed Design ### Data Flow ### Implementation Refer to vllm-metax: https://github.com/MetaX-MACA/vLLM-metax/blob/v0.19.0-dev/vllm_metax/v1/attention/backends/flash_attn.py#L1085 ### Backward Compatibility - Default behavior unchanged - New behavior enabled by `VLLM_ENABLE_FA_SPLIT_FORWARD` ## Questions for Upstream 1. Would upstream accept this split if it doesn't change behavior for existing use cases? 2. Is there interest in making this configurable? ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [RFC]: Split Flashattn Forward for Prefill/Decode Separation RFC ### Motivation. ## Summary Separate the attention forward computation into prefill and decode paths, using `flash_attn_varlen_func` for prefill and `flash...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ithub.com/MetaX-MACA/vLLM-metax/blob/v0.19.0-dev/vllm_metax/v1/attention/backends/flash_attn.py#L1085 ### Backward Compatibility - Default behavior unchanged - New behavior enabled by `VLLM_ENABLE_FA_SPLIT_FORWARD` ## Q...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: KV cache lookups during decode. 3. **Prefix caching**: Support explicit `cu_prefix_kv_lens` for better prefix caching strategy. ### Proposed Change. ## Detailed Design ### Data Flow ### Implementation Refer to vllm-meta...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: s**: Prefill accesses full KV sequences while decode accesses sparse KV cache entries. 2. **API optimization**: `flash_attn_with_kvcache` is optimized for block-based KV cache lookups during decode. 3. **Prefix caching*...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
