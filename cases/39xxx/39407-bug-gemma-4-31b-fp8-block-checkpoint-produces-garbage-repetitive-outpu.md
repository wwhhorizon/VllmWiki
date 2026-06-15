# vllm-project/vllm#39407: [Bug]: Gemma 4 31B FP8_BLOCK checkpoint produces garbage repetitive output — logit saturation at softcap wall due to absorbed activation scales being double-applied

| 字段 | 值 |
| --- | --- |
| Issue | [#39407](https://github.com/vllm-project/vllm/issues/39407) |
| 状态 | open |
| 标签 |  |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;distributed_parallel;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | activation;attention;cuda;fp8;gemm;kernel;moe;quantization;sampling;triton |
| 症状 | nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma 4 31B FP8_BLOCK checkpoint produces garbage repetitive output — logit saturation at softcap wall due to absorbed activation scales being double-applied

### Issue 正文摘录

# [Bug]: Gemma 4 31B FP8_BLOCK checkpoint produces garbage repetitive output (" a a a a") — logit saturation at softcap wall due to absorbed activation scales being double-applied ## Describe the bug When running **Gemma 4 31B** (dense, not MoE) with an **FP8_BLOCK checkpoint** produced by `llm-compressor`, vLLM produces garbage repetitive output consisting of a single token repeated indefinitely (e.g., `" a a a a a a a a"`). The model loads without errors and tokenizes correctly, but generation is completely broken. **Root cause identified via instrumented diagnostics:** The FP8_BLOCK checkpoint has activation scales **already absorbed into the weights** at quantization time (llm-compressor's default behavior for `FP8_BLOCK`). However, `compressed_tensors_w8a8_fp8.py` → `process_weights_after_loading()` still applies dynamic per-token activation quantization at inference time. This double-scales activations, causing hidden state norms to blow up across layers until all logits saturate at the softcap ceiling: `30 * tanh(x/30) ≈ 23.625` (BF16 representation of the softcap wall). With every token's logit at ~23.625, the distribution collapses and the model greedily repeats a single...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Bug]: Gemma 4 31B FP8_BLOCK checkpoint produces garbage repetitive output — logit saturation at softcap wall due to absorbed activation scales being double-applied # [Bug]: Gemma 4 31B FP8_BLOCK checkpoint produces gar...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ondary contributing factor: **CUTLASS block FP8 GEMM is not supported on SM 12.0 (RTX 5060 Ti / Blackwell) with CUDA = 12.9 (×8, one per worker) WARNING: Using default W8A8 Block FP8 kernel config. Performance might be...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Gemma 4 31B FP8_BLOCK checkpoint produces garbage repetitive output — logit saturation at softcap wall due to absorbed activation scales being double-applied # [Bug]: Gemma 4 31B FP8_BLOCK checkpoint produces gar...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: del greedily repeats a single token. A secondary contributing factor: **CUTLASS block FP8 GEMM is not supported on SM 12.0 (RTX 5060 Ti / Blackwell) with CUDA = 12.9 (×8, one per worker) WARNING: Using default W8A8 Bloc...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: on for block FP8 GEMMs on SM 12.0 with CUDA 12.8. The Triton fallback is numerically correct but untuned. This is a separate issue from the saturation bug. ## Suspected fix location `vllm/model_executor/layers/quantizat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
