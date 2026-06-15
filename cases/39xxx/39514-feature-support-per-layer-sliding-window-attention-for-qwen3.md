# vllm-project/vllm#39514: [Feature]: Support per-layer sliding window attention for Qwen3

| 字段 | 值 |
| --- | --- |
| Issue | [#39514](https://github.com/vllm-project/vllm/issues/39514) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support per-layer sliding window attention for Qwen3

### Issue 正文摘录

### Motivation Qwen3's HuggingFace config (`Qwen3Config`) already supports per-layer sliding window attention via the `layer_types` attribute (with `"sliding_attention"` and `"full_attention"` entries) and `sliding_window` size. This is used when `use_sliding_window=True` — either through explicit `layer_types` in `config.json` or auto-generated from `max_window_layers`. However, vLLM's Qwen3 model implementation does not read `layer_types` or pass `per_layer_sliding_window` to the `Attention` layer, so all layers always use full attention regardless of the config. This feature is needed because: - We are training a new model based on the Qwen3 architecture with interleaved sliding window attention (e.g., 3:1 sliding:full pattern), and it will be released when training is done. - Transformers already supports this natively — vLLM should be consistent. - Other models in vLLM (Gemma2, Llama, CommandR, etc.) already implement this exact pattern. ### Proposed Change Wire up `config.layer_types` in `Qwen3Attention` and `Qwen3MoeAttention` to pass `per_layer_sliding_window` to the `Attention` constructor, following the same pattern as Gemma2. ### Additional Context - The `is_interleaved...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Feature]: Support per-layer sliding window attention for Qwen3 ### Motivation Qwen3's HuggingFace config (`Qwen3Config`) already supports per-layer sliding window attention via the `layer_types` attribute (with `"slidi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: ers from inheriting the global sliding window). - All standard attention backends (FlashAttention, FlashInfer, Triton, FlexAttention) support sliding window. - No changes are needed outside the model files — the existin...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: ports this natively — vLLM should be consistent. - Other models in vLLM (Gemma2, Llama, CommandR, etc.) already implement this exact pattern. ### Proposed Change Wire up `config.layer_types` in `Qwen3Attention` and `Qwe...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: size. This is used when `use_sliding_window=True` — either through explicit `layer_types` in `config.json` or auto-generated from `max_window_layers`. However, vLLM's Qwen3 model implementation does not read `layer_type...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ture is needed because: - We are training a new model based on the Qwen3 architecture with interleaved sliding window attention (e.g., 3:1 sliding:full pattern), and it will be released when training is done. - Transfor...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
