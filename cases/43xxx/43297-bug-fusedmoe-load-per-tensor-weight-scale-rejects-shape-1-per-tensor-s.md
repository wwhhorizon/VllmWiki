# vllm-project/vllm#43297: [Bug] FusedMoE `_load_per_tensor_weight_scale` rejects shape `(1,)` per-tensor scales

| 字段 | 值 |
| --- | --- |
| Issue | [#43297](https://github.com/vllm-project/vllm/issues/43297) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug] FusedMoE `_load_per_tensor_weight_scale` rejects shape `(1,)` per-tensor scales

### Issue 正文摘录

## Summary `FusedMoE._load_per_tensor_weight_scale` at `vllm/model_executor/layers/fused_moe/layer.py:573` does `param_data[expert_id][idx] = loaded_weight` to install per-expert, per-(w1|w3)-shard scalar scales. When the on-disk per-tensor scale is stored as a length-1 tensor (shape `(1,)`) rather than a 0-D scalar (shape `()`), the assignment fails: ``` RuntimeError: output with shape [] doesn't match the broadcast shape [1] ``` This trips during weight load before the engine reaches forward — server init fails. ## Trigger `compressed-tensors` quantization schemes that produce per-tensor `weight_global_scale` / `input_global_scale` tensors emit them as shape `(1,)` by default (the `torch.tensor([x])` form rather than `torch.tensor(x)`). On NVFP4 MoE artifacts produced by `llm-compressor` with the standard `NVFP4` preset, every routed expert has shape-`(1,)` `*_global_scale` entries — for our DeepSeek-V4-Flash artifact with 256 routed experts × 43 main layers × 4 scale tensors each (`w1`/`w2`/`w3` × `weight_global_scale` + `input_global_scale`), that's ~66,000 affected tensors. ## Reproducer Load any compressed-tensors NVFP4 MoE artifact whose `*_global_scale` tensors are saved a...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Bug] FusedMoE `_load_per_tensor_weight_scale` rejects shape `(1,)` per-tensor scales ## Summary `FusedMoE._load_per_tensor_weight_scale` at `vllm/model_executor/layers/fused_moe/layer.py:573` does `param_data[expert_id...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: d_moe/layer.py:573` does `param_data[expert_id][idx] = loaded_weight` to install per-expert, per-(w1|w3)-shard scalar scales. When the on-disk per-tensor scale is stored as a length-1 tensor (shape `(1,)`) rather than a...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: empty(num_experts, num_shards, dtype=torch.float32), requires_grad=False, ).data loaded_weight = torch.tensor([0.5]) # shape (1,), llm-compressor default expert_id, idx = 0, 0 param_data[expert_id][idx] = loaded_weight...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug] FusedMoE `_load_per_tensor_weight_scale` rejects shape `(1,)` per-tensor scales ## Summary `FusedMoE._load_per_tensor_weight_scale` at `vllm/model_executor/layers/fused_moe/layer.py:573` does `param_data[expert_id...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: bal_scale` + `input_global_scale`), that's ~66,000 affected tensors. ## Reproducer Load any compressed-tensors NVFP4 MoE artifact whose `*_global_scale` tensors are saved as shape `(1,)`: ```python import torch import t...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
