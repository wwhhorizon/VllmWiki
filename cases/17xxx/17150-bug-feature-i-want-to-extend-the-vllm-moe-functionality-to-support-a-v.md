# vllm-project/vllm#17150: [Bug]: [Feature]: I want to extend the vLLM MoE functionality to support a variable number of experts.

| 字段 | 值 |
| --- | --- |
| Issue | [#17150](https://github.com/vllm-project/vllm/issues/17150) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | frontend_api;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;moe;sampling;triton |
| 症状 | nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [Feature]: I want to extend the vLLM MoE functionality to support a variable number of experts.

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Issue Report: Dynamic Expert Allocation in MoE Causes Numerical Instability Description: In my use case, I want the MoE (Mixture of Experts) model to dynamically allocate a variable number of experts per token based on a threshold. Here, topk represents the maximum number of experts a token can be assigned. Example Implementation: ```python def router( hidden_states: torch.Tensor, gating_output: torch.Tensor, topk: int, renormalize: bool, ): assert hidden_states.shape[0] == gating_output.shape[0] M, E = gating_output.shape # Adjust logits and select top-k experts router_logits = torch.softmax(gating_output, dim=-1) - 0.131 topk_weights, topk_ids = torch.topk(router_logits, topk, dim=1) # Mask out invalid experts (weights ≤ 0) and pad with `E` valid_mask = topk_weights > 0 topk_ids = torch.where(valid_mask, topk_ids, E) return topk_weights.to(torch.float32), topk_ids.to(torch.int32) If a token is assigned fewer than topk experts, the remaining slots in topk_ids are filled with E (total number of experts). ``` CUDA Kernel Modifications: I modified moe_align_sum_kernels.cu (v0.7.3) to ensure sorted_token_ids excludes tokens where topk_ids == E:...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 5: [Bug]: [Feature]: I want to extend the vLLM MoE functionality to support a variable number of experts. feature request ### 🚀 The feature, motivation and pitch Issue Report: Dynamic Expert Allocation in MoE Causes Numeri...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ivation and pitch Issue Report: Dynamic Expert Allocation in MoE Causes Numerical Instability Description: In my use case, I want the MoE (Mixture of Experts) model to dynamically allocate a variable number of experts p...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: torch.where(valid_mask, topk_ids, E) return topk_weights.to(torch.float32), topk_ids.to(torch.int32) If a token is assigned fewer than topk experts, the remaining slots in topk_ids are filled with E (total number of exp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ning slots in topk_ids are filled with E (total number of experts). ``` CUDA Kernel Modifications: I modified moe_align_sum_kernels.cu (v0.7.3) to ensure sorted_token_ids excludes tokens where topk_ids == E: ```cpp // I...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: h.int32) If a token is assigned fewer than topk experts, the remaining slots in topk_ids are filled with E (total number of experts). ``` CUDA Kernel Modifications: I modified moe_align_sum_kernels.cu (v0.7.3) to ensure...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
