# vllm-project/vllm#32843: [Feature]: `kv_cache_dtype="auto"` should resolve to the actual `kv_cache_dtype` picked by vllm, and be displayed to users

| 字段 | 值 |
| --- | --- |
| Issue | [#32843](https://github.com/vllm-project/vllm/issues/32843) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | attention;cache;fp8;operator;quantization |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: `kv_cache_dtype="auto"` should resolve to the actual `kv_cache_dtype` picked by vllm, and be displayed to users

### Issue 正文摘录

### 🚀 The feature, motivation and pitch As per title. At the moment, even in [`TritonAttentionImpl.forward`](https://github.com/vllm-project/vllm/blob/8ebf271bb6d1e7e9b1a55be73d755ef1a57dbbe5/vllm/v1/attention/backends/triton_attn.py#L469), if the argument `--kv-cache-dtype` is not specified, it remains `kv_cache_dtype="auto"` even at the forward level. Although [the documentation](https://docs.vllm.ai/en/latest/features/quantization/quantized_kvcache/#performance-impact) specifies `"auto": Uses the model's default "unquantized" data type`, one might at first expect that a model as https://huggingface.co/amd/Qwen3-8B-WMXFP4FP8-AMXFP4FP8-AMP-KVFP8 that contains `k_proj.output_scale`, `v_proj.output_scale` effectively loads these, and **by default uses FP8 KV cache**. Should this not be the case? It is currently not the case as we currently do not go through https://github.com/vllm-project/vllm/blob/8ebf271bb6d1e7e9b1a55be73d755ef1a57dbbe5/vllm/model_executor/layers/quantization/kv_cache.py#L59 and the default `1.0` `Attention._k_scale` and `Attention._v_scale` remain: https://github.com/vllm-project/vllm/blob/8ebf271bb6d1e7e9b1a55be73d755ef1a57dbbe5/vllm/attention/layer.py#L60-L61...

## 现有链接修复摘要

#33021 fix: Resolve kv_cache_dtype='auto' to actual dtype and log it (#32843)

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Feature]: `kv_cache_dtype="auto"` should resolve to the actual `kv_cache_dtype` picked by vllm, and be displayed to users feature request;stale ### 🚀 The feature, motivation and pitch As per title. At the moment, even...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ation/quantized_kvcache/#performance-impact) specifies `"auto": Uses the model's default "unquantized" data type`, one might at first expect that a model as https://huggingface.co/amd/Qwen3-8B-WMXFP4FP8-AMXFP4FP8-AMP-KV...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: e feature, motivation and pitch As per title. At the moment, even in [`TritonAttentionImpl.forward`](https://github.com/vllm-project/vllm/blob/8ebf271bb6d1e7e9b1a55be73d755ef1a57dbbe5/vllm/v1/attention/backends/triton_a...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: bbe5/vllm/v1/attention/backends/triton_attn.py#L469), if the argument `--kv-cache-dtype` is not specified, it remains `kv_cache_dtype="auto"` even at the forward level. Although [the documentation](https://docs.vllm.ai/...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ctual `kv_cache_dtype` picked by vllm, and be displayed to users feature request;stale ### 🚀 The feature, motivation and pitch As per title. At the moment, even in [`TritonAttentionImpl.forward`](https://github.com/vllm...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#33021](https://github.com/vllm-project/vllm/pull/33021) | closes_keyword | 0.95 | fix: Resolve kv_cache_dtype='auto' to actual dtype and log it (#32843) | Fixes #32843 When `--kv-cache-dtype` is not specified, it defaults to `"auto"`. However, this `"auto"` string remains unresolved throughout the codebase, causing: 1. **Users don' |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
