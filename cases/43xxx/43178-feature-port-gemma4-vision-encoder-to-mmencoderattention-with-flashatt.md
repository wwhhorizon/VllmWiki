# vllm-project/vllm#43178: [Feature]: Port Gemma4 vision encoder to MMEncoderAttention with FlashAttention support

| 字段 | 值 |
| --- | --- |
| Issue | [#43178](https://github.com/vllm-project/vllm/issues/43178) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;frontend_api;model_support;multimodal_vlm |
| 子分类 | shape_align |
| Operator 关键词 | attention;cuda;kernel |
| 症状 | slowdown |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Port Gemma4 vision encoder to MMEncoderAttention with FlashAttention support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Gemma4's vision encoder currently runs via HuggingFace `AutoModel.from_config` in eager mode, using SDPA (scaled dot-product attention) for the encoder's self-attention layers. SDPA is quadratic in sequence length, which drives high peak VRAM for large patch counts and limits how many images/frames can be batched in a single encoder call. Porting the Gemma4 vision encoder to vLLM-native layers using `MMEncoderAttention` with FlashAttention support would: - **Reduce peak VRAM** per encoder call (FA is O(N) memory vs O(N^2) for SDPA), allowing larger encoder batch sizes under the same memory budget - **Improve throughput** by leveraging FA's fused kernels instead of PyTorch's generic SDPA path - **Enable CUDA graph capture** for the encoder path (`compile_mm_encoder=True`), which is currently not practical with the HF eager model - **Align with vLLM's direction** for other vision models that already use `MMEncoderAttention` (e.g., Qwen2-VL, Pixtral) **Context**: The recently merged batched encoder PR groups encoder calls across images/frames, improving video throughput 1.7-3.8x. However, the encoder itself still uses HF's SDPA attention. The d...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: [Feature]: Port Gemma4 vision encoder to MMEncoderAttention with FlashAttention support feature request ### 🚀 The feature, motivation and pitch Gemma4's vision encoder currently runs via HuggingFace `AutoModel.from_conf...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: generic SDPA path - **Enable CUDA graph capture** for the encoder path (`compile_mm_encoder=True`), which is currently not practical with the HF eager model - **Align with vLLM's direction** for other vision models that...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: with `MMEncoderAttention`, adapting the 2D RoPE computation, validating numerical parity, and enabling `compile_mm_encoder` / `cudagraph_mm_encoder` support. ### Alternatives - **Keep SDPA with larger batch budget**: No...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ing FA's fused kernels instead of PyTorch's generic SDPA path - **Enable CUDA graph capture** for the encoder path (`compile_mm_encoder=True`), which is currently not practical with the HF eager model - **Align with vLL...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: flash=True`**: Only works on CUDA with compatible head dims and requires contiguous QKV layout. Not portable across vLLM's supported platforms. - **xFormers memory-efficient attention**: Similar benefits to FA but not i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
