# vllm-project/vllm#31912: MoE LoRA Kernel Correctness Verification Report

| 字段 | 值 |
| --- | --- |
| Issue | [#31912](https://github.com/vllm-project/vllm/issues/31912) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> MoE LoRA Kernel Correctness Verification Report

### Issue 正文摘录

## Summary This issue documents the comprehensive correctness verification of the fused MoE LoRA Triton kernel (`vllm/lora/ops/triton_ops/fused_moe_lora_op.py`). ## Test Methodology ### 1. Kernel-Level Testing Compared the fused MoE LoRA kernel output against a reference implementation that computes: ```python # For each token with lora_idx and expert_id: output[token, k] = hidden_states[token] @ lora_a[lora_idx, expert_id].T @ lora_b[lora_idx, expert_id].T ``` ### 2. End-to-End Testing (Merged Weights Reference) Compared full MoE+LoRA computation against HuggingFace-style merged weights: ```python # Reference: merge LoRA into base weights w_effective = w_base + lora_b @ lora_a output = activation(x @ w_effective.T) # vLLM approach: base + LoRA delta base_output = activation(x @ w_base.T) lora_delta = fused_moe_lora_kernel(x, lora_a, lora_b) output = base_output + lora_delta ``` ## Test Configurations | Configuration | Experts | Top-K | Tokens | LoRAs | Rank | Dtype | |--------------|---------|-------|--------|-------|------|-------| | Mixtral-like | 8 | 2 | 64 | 4 | 16 | fp16 | | Qwen-MoE-like | 60 | 4 | 32 | 4 | 16 | fp16 | | DeepSeek-MoE-like | 64 | 6 | 32 | 4 | 16 | fp16 | | L...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: figurations | Configuration | Experts | Top-K | Tokens | LoRAs | Rank | Dtype | |--------------|---------|-------|--------|-------|------|-------| | Mixtral-like | 8 | 2 | 64 | 4 | 16 | fp16 | | Qwen-MoE-like | 60 | 4 |...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: correct**: - `sorted_token_ids` correctly encodes (token_idx, expert_slot) as flattened indices - Stride calculations leverage `stride(2) * top_k_num == stride(1)` for correct memory access - Multi-slice operations (w13...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ng (Merged Weights Reference) Compared full MoE+LoRA computation against HuggingFace-style merged weights: ```python # Reference: merge LoRA into base weights w_effective = w_base + lora_b @ lora_a output = activation(x...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: MoE LoRA Kernel Correctness Verification Report ## Summary This issue documents the comprehensive correctness verification of the fused MoE LoRA Triton kernel (`vllm/lora/ops/triton_ops/fused_moe_lora_op.py`). ## Test
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: MoE), fp16 and bf16 produce exact matches (0.0 difference). 2. **Small numerical differences acceptable**: The observed differences (< 2e-3) are within expected floating-point tolerances for fused kernel operations. 3....

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
