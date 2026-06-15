# vllm-project/vllm#32235: [Bug]: Incorrect grid size in fused_moe_lora

| 字段 | 值 |
| --- | --- |
| Issue | [#32235](https://github.com/vllm-project/vllm/issues/32235) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Incorrect grid size in fused_moe_lora

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug In the `fused_moe_lora` kernel, the launch grid is currently derived from `max_loras = lora_a_stacked[0].shape[0]` https://github.com/vllm-project/vllm/blob/2a719e0865d68ef930c53f9b46f718c31ed39377/vllm/lora/ops/triton_ops/fused_moe_lora_op.py#L256 . This is off by one when the batch contains a mix of base-model tokens (represented by lora_id = -1) and LoRA tokens. Example: if max_loras = 4 and active_lora_ids = [-1, 0, 1, 2, 3], there are actually 5 distinct “LoRA slots” to iterate over (base + 4 adapters). Using max_loras to construct the grid only covers 4 slots, so the final slot (LoRA id 3) can be skipped because it is not included in the kernel grid. The grid size should therefore be `max_loras + 1`. This matches the behavior of regular LoRA shrink/expand kernels, where the grid is built from `lora_ids.size(0)` https://github.com/vllm-project/vllm/blob/2a719e0865d68ef930c53f9b46f718c31ed39377/vllm/lora/ops/triton_ops/lora_shrink_op.py#L190, which equals `max_loras + 1` (base-model slot + max_loras adapters). Consequently, fused_moe_lora kernels should also launch with max_loras + 1 to ensure all active LoRA IDs. ### Before...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: project/vllm/blob/2a719e0865d68ef930c53f9b46f718c31ed39377/vllm/lora/ops/triton_ops/fused_moe_lora_op.py#L256 . This is off by one when the batch contains a mix of base-model tokens (represented by lora_id = -1) and LoR...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Ds. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: active_lora_ids = [-1, 0, 1, 2, 3], there are actually 5 distinct “LoRA slots” to iterate over (base + 4 adapters). Using max_loras to construct the grid only covers 4 slots, so the final slot (LoRA id 3) can be skipped...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ra_op.py#L256 . This is off by one when the batch contains a mix of base-model tokens (represented by lora_id = -1) and LoRA tokens. Example: if max_loras = 4 and active_lora_ids = [-1, 0, 1, 2, 3], there are actually 5...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: Incorrect grid size in fused_moe_lora bug;stale ### Your current environment ### 🐛 Describe the bug In the `fused_moe_lora` kernel, the launch grid is currently derived from `max_loras = lora_a_stacked[0].shape[0...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
