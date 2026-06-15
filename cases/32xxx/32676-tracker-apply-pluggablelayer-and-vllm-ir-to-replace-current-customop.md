# vllm-project/vllm#32676: [Tracker]: Apply PluggableLayer and vLLM IR to replace current CustomOp

| 字段 | 值 |
| --- | --- |
| Issue | [#32676](https://github.com/vllm-project/vllm/issues/32676) |
| 状态 | open |
| 标签 | feature request;vllm-ir |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Tracker]: Apply PluggableLayer and vLLM IR to replace current CustomOp

### Issue 正文摘录

### Tracking the replacement of CustomOp Proposes: After `PluggableLayer` and `vLLM IR` getting ready, we need to replace original CustomOp with these two new mechanisms. Here we track the list of all custom ops: list of `CustomOp` that need to be replaced by `PluggableLayer`: - [x] `multi_head_latent_attention`, replaced in https://github.com/vllm-project/vllm/pull/32331 - [x] `replicated_linear, column_parallel_linear, row_parallel_linear`, replaced in https://github.com/vllm-project/vllm/pull/33152 - [x] `mamba_mixer, mamba_mixer2, plamo2_mamba_mixer`, replaced in https://github.com/vllm-project/vllm/pull/33660 - [x] `rel_pos_attention`, replaced in https://github.com/vllm-project/vllm/pull/33753 by @shen-shanshan - [x] `logits_processor, vocab_parallel_embedding, parallel_lm_head` replaced in https://github.com/vllm-project/vllm/pull/33465 - [x] `fused_moe, modular_fused_moe, transformers_fused_moe` replaced in https://github.com/vllm-project/vllm/pull/33556 - [ ] `static_sink_attention` `short_conv` `dual_chunk_rotary_embedding` WIP in https://github.com/vllm-project/vllm/pull/36080 list of `CustomOp` that need to be replaced by `vLLM IR`: - [ ] `fatrelu_and_mul, silu_and_mul...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: eplaced in https://github.com/vllm-project/vllm/pull/33465 - [x] `fused_moe, modular_fused_moe, transformers_fused_moe` replaced in https://github.com/vllm-project/vllm/pull/33556 - [ ] `static_sink_attention` `short_co...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [ ] `conv2d, conv3d` @R3hankhan123 - [ ] `mm_encoder_attn` - [ ] `unquantized_fused_moe, grouped_topk` - [ ] `rms_norm, gemma_rms_norm, rms_norm_gated, mixer2_gated_rms_norm` @wxsIcey - [ ] `quant_fp8` - [ ] `rotary_emb...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ng ready, we need to replace original CustomOp with these two new mechanisms. Here we track the list of all custom ops: list of `CustomOp` that need to be replaced by `PluggableLayer`: - [x] `multi_head_latent_attention...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: der_attn` - [ ] `unquantized_fused_moe, grouped_topk` - [ ] `rms_norm, gemma_rms_norm, rms_norm_gated, mixer2_gated_rms_norm` @wxsIcey - [ ] `quant_fp8` - [ ] `rotary_embedding, apply_rotary_emb` @wxsIcey ### Before sub...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: r]: Apply PluggableLayer and vLLM IR to replace current CustomOp feature request;vllm-ir ### Tracking the replacement of CustomOp Proposes: After `PluggableLayer` and `vLLM IR` getting ready, we need to replace original...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
