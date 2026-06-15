# vllm-project/vllm#41283: [Bug] Gemma 4 31B crashes on k_eq_v full-attention layers (QKV split shape mismatch)

| 字段 | 值 |
| --- | --- |
| Issue | [#41283](https://github.com/vllm-project/vllm/issues/41283) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug] Gemma 4 31B crashes on k_eq_v full-attention layers (QKV split shape mismatch)

### Issue 正文摘录

## Description Loading `google/gemma-4-31b-it` on vLLM 0.20.0 crashes immediately with a tensor shape mismatch during the QKV split. ## Error ``` RuntimeError: split_with_sizes expects split_sizes to sum exactly to the size of dimension -1 (18432), but got split_sizes=[16384, 2048, 2048] summing to 20480 ``` ## Root Cause Gemma 4 31B has two attention layer types: - **Sliding layers** — standard GQA with separate Q, K, V projections - **Full-attention (`k_eq_v`) layers** — K and V share the same projection; the checkpoint has `q_proj` and `k_proj` on disk but **no `v_proj`** `Gemma4Attention` routes all layers through `QKVParallelLinear`, then splits the output as `[q_size, kv_size, kv_size]`. For `k_eq_v` full-attention layers the actual packed tensor is only `[q_size + kv_size]` (no V column), so the split sums to `q_size + 2×kv_size` but the tensor is `q_size + kv_size` — causing the crash. The `_weight_iterator` attempted to paper over this by duplicating `k_proj` weights as `v_proj`, but `QKVParallelLinear` still expects both slots to be present in the packed layout. ## Affected models - `google/gemma-4-31b-it` (first Gemma 4 model with mixed sliding/full-attention layers) -...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: `k_proj` weights as `v_proj`, but `QKVParallelLinear` still expects both slots to be present in the packed layout. ## Affected models - `google/gemma-4-31b-it` (first Gemma 4 model with mixed sliding/full-attention laye...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug] Gemma 4 31B crashes on k_eq_v full-attention layers (QKV split shape mismatch) ## Description Loading `google/gemma-4-31b-it` on vLLM 0.20.0 crashes immediately with a tensor shape mismatch during the QKV split. #...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ug] Gemma 4 31B crashes on k_eq_v full-attention layers (QKV split shape mismatch) ## Description Loading `google/gemma-4-31b-it` on vLLM 0.20.0 crashes immediately with a tensor shape mismatch during the QKV split. ##...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ] Gemma 4 31B crashes on k_eq_v full-attention layers (QKV split shape mismatch) ## Description Loading `google/gemma-4-31b-it` on vLLM 0.20.0 crashes immediately with a tensor shape mismatch during the QKV split. ## Er...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug] Gemma 4 31B crashes on k_eq_v full-attention layers (QKV split shape mismatch) ## Description Loading `google/gemma-4-31b-it` on vLLM 0.20.0 crashes immediately with a tensor shape mismatch during the QKV split. #...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
