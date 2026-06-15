# vllm-project/vllm#28086: [Feature][Kernel][DSR1]: Make`fused_grouped_topk` more fused (integrate TRT-LLM kernel)

| 字段 | 值 |
| --- | --- |
| Issue | [#28086](https://github.com/vllm-project/vllm/issues/28086) |
| 状态 | closed |
| 标签 | good first issue;feature request |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][Kernel][DSR1]: Make`fused_grouped_topk` more fused (integrate TRT-LLM kernel)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Right now, this operation kernel has multiple steps (https://github.com/vllm-project/vllm/blob/4ea62b77f5c009515f50d14cda24665101a5d910/vllm/model_executor/layers/fused_moe/fused_moe.py#L1320-L1350) ```python def fused_grouped_topk( hidden_states: torch.Tensor, gating_output: torch.Tensor, topk: int, renormalize: bool, e_score_correction_bias: torch.Tensor, num_expert_group: int = 0, topk_group: int = 0, scoring_func: str = "softmax", routed_scaling_factor: float = 1.0, ) -> tuple[torch.Tensor, torch.Tensor]: assert hidden_states.size(0) == gating_output.size(0), "Number of tokens mismatch" if scoring_func == "softmax": scores = torch.softmax(gating_output, dim=-1) elif scoring_func == "sigmoid": scores = gating_output.sigmoid() else: raise ValueError(f"Unsupported scoring function: {scoring_func}") scores_with_bias = scores + e_score_correction_bias.unsqueeze(0) topk_values, topk_indices = ops.grouped_topk( scores, scores_with_bias.to(scores.dtype), num_expert_group, topk_group, topk, renormalize, routed_scaling_factor, ) return topk_values.to(torch.float32), topk_indices.to(torch.int32) ``` We should make this one single kernel to do the:...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Feature][Kernel][DSR1]: Make`fused_grouped_topk` more fused (integrate TRT-LLM kernel) good first issue;feature request ### 🚀 The feature, motivation and pitch Right now, this operation kernel has multiple steps (https...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: s = ops.grouped_topk( scores, scores_with_bias.to(scores.dtype), num_expert_group, topk_group, topk, renormalize, routed_scaling_factor, ) return topk_values.to(torch.float32), topk_indices.to(torch.int32) ``` We should...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: sert hidden_states.size(0) == gating_output.size(0), "Number of tokens mismatch" if scoring_func == "softmax": scores = torch.softmax(gating_output, dim=-1) elif scoring_func == "sigmoid": scores = gating_output.sigmoid...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: assert hidden_states.size(0) == gating_output.size(0), "Number of tokens mismatch" if scoring_func == "softmax": scores = torch.softmax(gating_output, dim=-1) elif scoring_func == "sigmoid": scores = gating_output.sigmo...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: scoring_func == "sigmoid": scores = gating_output.sigmoid() else: raise ValueError(f"Unsupported scoring function: {scoring_func}") scores_with_bias = scores + e_score_correction_bias.unsqueeze(0) topk_values, topk_indi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
