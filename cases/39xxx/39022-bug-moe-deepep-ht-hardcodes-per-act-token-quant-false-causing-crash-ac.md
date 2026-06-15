# vllm-project/vllm#39022: [Bug][MoE] DeepEP HT hardcodes per_act_token_quant=False, causing crash/accuracy loss

| 字段 | 值 |
| --- | --- |
| Issue | [#39022](https://github.com/vllm-project/vllm/issues/39022) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug][MoE] DeepEP HT hardcodes per_act_token_quant=False, causing crash/accuracy loss

### Issue 正文摘录

## Bug Description In `vllm/model_executor/layers/fused_moe/prepare_finalize/deepep_ht.py:242`, `per_act_token_quant` is hardcoded to `False`: ```python # TODO: support per_act_token_quant, expert_x, expert_x_scale = moe_kernel_quantize_input( expert_x, a1_scale, quant_dtype=quant_config.quant_dtype, per_act_token_quant=False, # <-- should be quant_config.per_act_token_quant block_shape=quant_config.block_shape, ) ``` This causes two issues depending on the quantization method: ### 1. Crash (INT8 models) `CompressedTensorsW8A8Int8MoEMethod` always sets `per_act_token_quant=True`. When using DeepEP HT, the hardcoded `False` is passed to `_int8_quantize()`, which hits: ```python assert per_act_token, "int8 quantization only supports block or channel-wise" ``` ### 2. Silent accuracy degradation (FP8 per-token models) For FP8 models with per-token activation quantization (e.g., `CompressedTensorsW8A8Fp8MoEMethod` with TOKEN strategy, `CompressedTensorsW4A8Fp8MoEMethod`, `QuarkFp8MoEMethod` with per-channel input), the hardcoded `False` causes `scaled_fp8_quant(use_per_token_if_dynamic=False)`, computing a single per-tensor scale instead of per-token scales. This can cause significant...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug][MoE] DeepEP HT hardcodes per_act_token_quant=False, causing crash/accuracy loss ## Bug Description In `vllm/model_executor/layers/fused_moe/prepare_finalize/deepep_ht.py:242`, `per_act_token_quant` is hardcoded to...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Bug][MoE] DeepEP HT hardcodes per_act_token_quant=False, causing crash/accuracy loss ## Bug Description In `vllm/model_executor/layers/fused_moe/prepare_finalize/deepep_ht.py:242`, `per_act_token_quant` is hardcoded to...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: en_quant=False, causing crash/accuracy loss ## Bug Description In `vllm/model_executor/layers/fused_moe/prepare_finalize/deepep_ht.py:242`, `per_act_token_quant` is hardcoded to `False`: ```python # TODO: support per_ac...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug][MoE] DeepEP HT hardcodes per_act_token_quant=False, causing crash/accuracy loss ## Bug Description In `vllm/model_executor/layers/fused_moe/prepare_finalize/deepep_ht.py:242`, `per_act_token_quant` is hardcoded to...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug][MoE] DeepEP HT hardcodes per_act_token_quant=False, causing crash/accuracy loss ## Bug Description In `vllm/model_executor/layers/fused_moe/prepare_finalize/deepep_ht.py:242`, `per_act_token_quant` is hardcoded to...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
