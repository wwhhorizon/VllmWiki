# vllm-project/vllm#21505: [Feature]: Full cudagraph support for MLA attention backend with DeepSeek MTP(Speculative decode)

| 字段 | 值 |
| --- | --- |
| Issue | [#21505](https://github.com/vllm-project/vllm/issues/21505) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;frontend_api;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | attention;cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Full cudagraph support for MLA attention backend with DeepSeek MTP(Speculative decode)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch On cudagraph capture stage, the `MLACommonMetadataBuilder` build metadata with `max_query_len =1`, [with this PR](https://github.com/vllm-project/vllm/pull/18581) ```python def build_for_cudagraph_capture( self, common_attn_metadata: CommonAttentionMetadata) -> M: """ This method builds the metadata for full cudagraph capture. Currently, only decode is supported for full cudagraphs with MLA. """ m = common_attn_metadata assert m.num_reqs == m.num_actual_tokens, \ "MLA only supports decode-only full CUDAGraph capture. " \ "Make sure all cudagraph capture sizes torch.Tensor: ... if has_prefill: output[num_decode_tokens:] = self._forward_prefill( prefill_q, prefill_k_c_normed, prefill_k_pe, kv_cache, attn_metadata) if has_decode: # Run DeepSeek R1 with MTP, has_decode is always False ... output[:num_decode_tokens] = self._forward_decode( decode_ql_nope, decode_q_pe, kv_cache, attn_metadata) ``` So, Is there any way to support DeepSeek MTP with full cudagraph？ @ProExpertProg @LucasWilkinson @zixi-qi @YaoJiayi Looking forward to your reply. Other Refs: https://github.com/vllm-project/vllm/pull/17211 https://github.com/vllm-project/vllm/pull/18435...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ure]: Full cudagraph support for MLA attention backend with DeepSeek MTP(Speculative decode) feature request;stale ### 🚀 The feature, motivation and pitch On cudagraph capture stage, the `MLACommonMetadataBuilder` build...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: motivation and pitch On cudagraph capture stage, the `MLACommonMetadataBuilder` build metadata with `max_query_len =1`, [with this PR](https://github.com/vllm-project/vllm/pull/18581) ```python def build_for_cudagraph_c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: Full cudagraph support for MLA attention backend with DeepSeek MTP(Speculative decode) feature request;stale ### 🚀 The feature, motivation and pitch On cudagraph capture stage, the `MLACommonMetadataBuilder`...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: feature, motivation and pitch On cudagraph capture stage, the `MLACommonMetadataBuilder` build metadata with `max_query_len =1`, [with this PR](https://github.com/vllm-project/vllm/pull/18581) ```python def build_for_cu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Feature]: Full cudagraph support for MLA attention backend with DeepSeek MTP(Speculative decode) feature request;stale ### 🚀 The feature, motivation and pitch On cudagraph capture stage, the `MLACommonMetadataBuilder`...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
