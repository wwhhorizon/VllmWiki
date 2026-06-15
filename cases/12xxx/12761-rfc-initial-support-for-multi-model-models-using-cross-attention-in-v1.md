# vllm-project/vllm#12761: [RFC]: Initial support for multi-model models using cross attention in V1

| 字段 | 值 |
| --- | --- |
| Issue | [#12761](https://github.com/vllm-project/vllm/issues/12761) |
| 状态 | closed |
| 标签 | RFC;keep-open |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Initial support for multi-model models using cross attention in V1

### Issue 正文摘录

### Motivation. The goal of this RFC is to propose a simple initial design to support multi-modal models that use cross attention for the V1 architecture. Whisper is a prime example of such a model. The design aims to be as simple as possible and easily replaceable without disrupting other ongoing V1 work. Currently in V1, the only encoder/decoder models that are supported are ones that do not use cross attention. These models use the `EncoderCacheManager` to communicate the outputs of the encode to the decoder. Multi-modal models that use cross attention need a separate KV cache for the encoder portion of the model. This cross attention KV cache has to be populated by the encoder and is used by the decoder's cross attention layers (as read only). The cross attention KV cache is separate from the existing decoder KV cache and has to be managed separately. ### Non-goals Since we are focusing on Whisper for the initial design, there are certain features/optimizations that can be deferred. For now, the following optimizations will be disabled for cross attention models since they probably won't provide much benefit: - Chunked prefill for the encoder - Prefix caching Supporting attent...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: out disrupting other ongoing V1 work. Currently in V1, the only encoder/decoder models that are supported are ones that do not use cross attention. These models use the `EncoderCacheManager` to communicate the outputs o...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: - Chunked prefill for the encoder - Prefix caching Supporting attention backends other than flash attention. Abstracting the `GPUModelRunner` For additional background see: [](https://github.com/vllm-project/vllm/issues...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [RFC]: Initial support for multi-model models using cross attention in V1 RFC;keep-open ### Motivation. The goal of this RFC is to propose a simple initial design to support multi-modal models that use cross attention f...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ather_cross_metadata`, analogous to `_gather_encoder_outputs`. 3. The `profile_run`/`_dummy_run` functions also need to be updated to follow the same general steps as execute_model. ### `FlashAttentionImpl` Add support...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: design to support multi-modal models that use cross attention for the V1 architecture. Whisper is a prime example of such a model. The design aims to be as simple as possible and easily replaceable without disrupting ot...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
