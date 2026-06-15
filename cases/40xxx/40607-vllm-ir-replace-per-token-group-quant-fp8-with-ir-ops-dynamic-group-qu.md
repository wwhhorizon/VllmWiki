# vllm-project/vllm#40607: [vllm IR]: Replace`per_token_group_quant_fp8` with `ir.ops.dynamic_group_quant_fp8`

| 字段 | 值 |
| --- | --- |
| Issue | [#40607](https://github.com/vllm-project/vllm/issues/40607) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [vllm IR]: Replace`per_token_group_quant_fp8` with `ir.ops.dynamic_group_quant_fp8`

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The `per_token_group_quant_fp8` function defined in `vllm/model_executor/layers/quantization/utils/fp8_utils.py` duplicates logic that will be expressed via `ir.ops.dynamic_group_quant_fp8` once #39481 is merged. This function should be removed in favour of the IR op. ### Blocker `deep_gemm_moe.py` passes a pre-allocated out_q tensor to `per_token_group_quant_fp8`. IR ops do not support output variants for now, making a direct substitution impossible at present. ### Two paths: - Remove `out_q`: if `deep_gemm_moe.py` can be refactored to allocate the output internally, the call site can be migrated to the IR op without further changes. - Extend the IR op: if `out_q` cannot be eliminated, IR ops have to be extended with an optional output-tensor argument (something similar to the `maybe_inplace` variant that has been proposed, see #36823) before migration proceeds. Once unblocked, `per_token_group_quant_fp8` should be removed from `fp8_utils.py` and replaced with the IR op. ### Alternatives _No response_ ### Additional context Keep per_token_group_quant_fp8 as-is, this leaves duplicate quantization logic in `fp8_utils.py`. ### Before submittin...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [vllm IR]: Replace`per_token_group_quant_fp8` with `ir.ops.dynamic_group_quant_fp8` feature request ### 🚀 The feature, motivation and pitch The `per_token_group_quant_fp8` function defined in `vllm/model_executor/layers...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: is function should be removed in favour of the IR op. ### Blocker `deep_gemm_moe.py` passes a pre-allocated out_q tensor to `per_token_group_quant_fp8`. IR ops do not support output variants for now, making a direct sub...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: . ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: is merged. This function should be removed in favour of the IR op. ### Blocker `deep_gemm_moe.py` passes a pre-allocated out_q tensor to `per_token_group_quant_fp8`. IR ops do not support output variants for now, making...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: on and pitch The `per_token_group_quant_fp8` function defined in `vllm/model_executor/layers/quantization/utils/fp8_utils.py` duplicates logic that will be expressed via `ir.ops.dynamic_group_quant_fp8` once #39481 is m...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
