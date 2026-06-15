# vllm-project/vllm#28632: [Bug]: Qwen3-Next，fused_recurrent_gated_delta_rule_fwd do not support ( inplace_final_state: bool = False)

| 字段 | 值 |
| --- | --- |
| Issue | [#28632](https://github.com/vllm-project/vllm/issues/28632) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3-Next，fused_recurrent_gated_delta_rule_fwd do not support ( inplace_final_state: bool = False)

### Issue 正文摘录

### Your current environment def fused_recurrent_gated_delta_rule_fwd( q: torch.Tensor, k: torch.Tensor, v: torch.Tensor, g: torch.Tensor, beta: torch.Tensor, scale: float, initial_state: torch.Tensor, inplace_final_state: bool = True, cu_seqlens: torch.LongTensor | None = None, ssm_state_indices: torch.Tensor | None = None, num_accepted_tokens: torch.Tensor | None = None, use_qk_l2norm_in_kernel: bool = False, ) -> tuple[torch.Tensor, torch.Tensor]: B, T, H, K, V = *k.shape, v.shape[-1] HV = v.shape[2] N = B if cu_seqlens is None else len(cu_seqlens) - 1 BK, BV = triton.next_power_of_2(K), min(triton.next_power_of_2(V), 8) NK, NV = triton.cdiv(K, BK), triton.cdiv(V, BV) assert NK == 1, "NK > 1 is not supported yet" num_stages = 3 num_warps = 1 o = q.new_empty(NK, *v.shape) if inplace_final_state: final_state = initial_state else: final_state = q.new_empty(T, HV, K, V, dtype=initial_state.dtype) stride_init_state_token = initial_state.stride(0) stride_final_state_token = final_state.stride(0) ### 🐛 Describe the bug We are developing the kernel implementation for `fused_recurrent_gated_delta_rule_fwd` for the Baidu Kunlun backend. However, we noticed that the current code defaults...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 2] N = B if cu_seqlens is None else len(cu_seqlens) - 1 BK, BV = triton.next_power_of_2(K), min(triton.next_power_of_2(V), 8) NK, NV = triton.cdiv(K, BK), triton.cdiv(V, BV) assert NK == 1, "NK > 1 is not supported yet"...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: r, v: torch.Tensor, g: torch.Tensor, beta: torch.Tensor, scale: float, initial_state: torch.Tensor, inplace_final_state: bool = True, cu_seqlens: torch.LongTensor | None = None, ssm_state_indices: torch.Tensor | None =...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: state: bool = True, cu_seqlens: torch.LongTensor | None = None, ssm_state_indices: torch.Tensor | None = None, num_accepted_tokens: torch.Tensor | None = None, use_qk_l2norm_in_kernel: bool = False, ) -> tuple[torch.Ten...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: rent_gated_delta_rule_fwd do not support ( inplace_final_state: bool = False) bug;stale ### Your current environment def fused_recurrent_gated_delta_rule_fwd( q: torch.Tensor, k: torch.Tensor, v: torch.Tensor, g: torch....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: Qwen3-Next，fused_recurrent_gated_delta_rule_fwd do not support ( inplace_final_state: bool = False) bug;stale ### Your current environment def fused_recurrent_gated_delta_rule_fwd( q: torch.Tensor, k: torch.Te

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
