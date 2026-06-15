# vllm-project/vllm#38235: [Feature]: Quantization support (AWQ / GPTQ / FP8) for mistralai/Voxtral-Mini-4B-Realtime-2602

| 字段 | 值 |
| --- | --- |
| Issue | [#38235](https://github.com/vllm-project/vllm/issues/38235) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;model_support;multimodal_vlm;quantization |
| 子分类 | memory |
| Operator 关键词 | cache;fp8;quantization |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Quantization support (AWQ / GPTQ / FP8) for mistralai/Voxtral-Mini-4B-Realtime-2602

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I am currently deploying the new `mistralai/Voxtral-Mini-4B-Realtime-2602` model using the vLLM V1 Engine. Because it is a realtime multimodal audio model, the memory footprint is extremely high. On a standard mid-tier GPU like the RTX 5060 Ti (16GB VRAM), the `bf16` weights consume around 8.4GB. This leaves very little room for the `encoder_cache` and standard KV cache. As a result, the `max-model-len` has to be severely restricted (around ~4300 tokens), which is barely enough for a short audio session, and it completely prevents running multiple concurrent streams due to `encoder_cache_usage` hitting 100%. It would be incredibly helpful to have quantization support for the `VoxtralRealtimeGeneration` architecture. Specifically: 1. **Weight Quantization:** Support for loading AWQ, GPTQ, or bitsandbytes (int8/int4) formats for this specific model type. 2. **KV Cache Quantization:** Support for FP8 KV cache for Voxtral to further reduce the memory required for long audio streams. Reducing the weight footprint by half (e.g., to ~4GB using 8-bit) would drastically increase the viable audio context window and allow continuous batching of multipl...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Feature]: Quantization support (AWQ / GPTQ / FP8) for mistralai/Voxtral-Mini-4B-Realtime-2602 feature request ### 🚀 The feature, motivation and pitch I am currently deploying the new `mistralai/Voxtral-Mini-4B-Realtime...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: am currently deploying the new `mistralai/Voxtral-Mini-4B-Realtime-2602` model using the vLLM V1 Engine. Because it is a realtime multimodal audio model, the memory footprint is extremely high. On a standard mid-tier GP...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: emory footprint is extremely high. On a standard mid-tier GPU like the RTX 5060 Ti (16GB VRAM), the `bf16` weights consume around 8.4GB. This leaves very little room for the `encoder_cache` and standard KV cache. As a r...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: VRAM), the `bf16` weights consume around 8.4GB. This leaves very little room for the `encoder_cache` and standard KV cache. As a result, the `max-model-len` has to be severely restricted (around ~4300 tokens), which is...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: antization support for the `VoxtralRealtimeGeneration` architecture. Specifically: 1. **Weight Quantization:** Support for loading AWQ, GPTQ, or bitsandbytes (int8/int4) formats for this specific model type. 2. **KV Cac...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
