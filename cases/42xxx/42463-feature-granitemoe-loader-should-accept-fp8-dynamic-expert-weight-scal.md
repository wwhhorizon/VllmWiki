# vllm-project/vllm#42463: [Feature]: granitemoe loader should accept FP8_DYNAMIC expert weight_scale tensors

| 字段 | 值 |
| --- | --- |
| Issue | [#42463](https://github.com/vllm-project/vllm/issues/42463) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: granitemoe loader should accept FP8_DYNAMIC expert weight_scale tensors

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### Summary The `GraniteMoeForCausalLM` weight loader in `vllm/model_executor/models/granitemoe.py` does not route `.block_sparse_moe.input_linear.weight_scale` or `.block_sparse_moe.output_linear.weight_scale` tensors into FusedMoE expert slots. Its expert branches in `load_weights` only match on `.weight`; tensors ending in `.weight_scale` fall through to a generic pass-through that has no mapping for them, so loading raises `KeyError` on `params_dict[name]` in `_load_weights` once it tries to look up the unrecognized name. As a result, FP8-quantized Granite MoE (non-hybrid) checkpoints cannot be served. This issue is scoped to the **`FP8_DYNAMIC`** scheme (compressed-tensors `weights.strategy="channel"`, per-output-row weight scales; dynamic per-token activation scales computed at runtime; no `input_scale` tensor on disk). Producer-side tooling (e.g. `llm-compressor`'s `GraniteMoeHybridParallelExpertsLinear` helper, adapted for the plain `GraniteMoeParallelExperts` module) emits fused expert weight scales with shape `[num_experts, 2*intermediate_size, 1]` on `input_linear` and `[num_experts, hidden_size, 1]` on `output_linear`, which matc...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Feature]: granitemoe loader should accept FP8_DYNAMIC expert weight_scale tensors feature request ### 🚀 The feature, motivation and pitch ### Summary The `GraniteMoeForCausalLM` weight loader in `vllm/model_executor/mo...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: ht loader in `vllm/model_executor/models/granitemoe.py` does not route `.block_sparse_moe.input_linear.weight_scale` or `.block_sparse_moe.output_linear.weight_scale` tensors into FusedMoE expert slots. Its expert branc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: nd pitch ### Summary The `GraniteMoeForCausalLM` weight loader in `vllm/model_executor/models/granitemoe.py` does not route `.block_sparse_moe.input_linear.weight_scale` or `.block_sparse_moe.output_linear.weight_scale`...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Feature]: granitemoe loader should accept FP8_DYNAMIC expert weight_scale tensors feature request ### 🚀 The feature, motivation and pitch ### Summary The `GraniteMoeForCausalLM` weight loader in `vllm/model_executor/mo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: Downstream, `_load_weights`'s existing `expert_params_mapping` dispatcher matches on `.w1.` / `.w2.` / `.w3.` substrings and routes the rewritten names into `w13_weight_scale` / `w2_weight_scale` FusedMoE slots via the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
