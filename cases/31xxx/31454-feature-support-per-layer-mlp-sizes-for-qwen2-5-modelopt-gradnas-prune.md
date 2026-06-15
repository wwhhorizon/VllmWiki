# vllm-project/vllm#31454: [Feature]: Support per-layer MLP sizes for Qwen2.5 ModelOpt/GradNAS pruned checkpoints

| 字段 | 值 |
| --- | --- |
| Issue | [#31454](https://github.com/vllm-project/vllm/issues/31454) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support per-layer MLP sizes for Qwen2.5 ModelOpt/GradNAS pruned checkpoints

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ## Background When using Qwen2.5 pruned checkpoints exported by ModelOpt/GradNAS, the MLP `intermediate_size` varies per layer. However, the HF `config.json` still exposes only a global `intermediate_size`. ## Problem vLLM currently builds MLP layers from the global `intermediate_size`, which causes shape mismatches when loading pruned weights where each layer has a different MLP width. ## Motivation We want vLLM to load pruned checkpoints correctly without manual config edits or patching model code. ## Proposed Plan 1. Add an opt-in flag `enable_modelopt_pruning` (default: False) to avoid impacting existing models. 2. When enabled, infer per-layer intermediate sizes by reading local/cached safetensors: - Use `model.layers.{i}.mlp.gate_proj.weight` and take `shape[0]` as the layer’s intermediate size. - Build `layer_intermediate_sizes` and inject into config at runtime. - Validate completeness, consistency, and divisibility by TP size. 3. In Qwen2/Qwen3 MLP construction, use per-layer sizes when `layer_intermediate_sizes` is present; otherwise fall back to the global `intermediate_size`. 4. Provide an offline helper script to persist sizes i...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Feature]: Support per-layer MLP sizes for Qwen2.5 ModelOpt/GradNAS pruned checkpoints feature request;stale ### 🚀 The feature, motivation and pitch ## Background When using Qwen2.5 pruned checkpoints exported by ModelO...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: s MLP layers from the global `intermediate_size`, which causes shape mismatches when loading pruned weights where each layer has a different MLP width. ## Motivation We want vLLM to load pruned checkpoints correctly wit...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: -layer MLP sizes for Qwen2.5 ModelOpt/GradNAS pruned checkpoints feature request;stale ### 🚀 The feature, motivation and pitch ## Background When using Qwen2.5 pruned checkpoints exported by ModelOpt/GradNAS, the MLP `i...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: lds MLP layers from the global `intermediate_size`, which causes shape mismatches when loading pruned weights where each layer has a different MLP width. ## Motivation We want vLLM to load pruned checkpoints correctly w...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: exposes only a global `intermediate_size`. ## Problem vLLM currently builds MLP layers from the global `intermediate_size`, which causes shape mismatches when loading pruned weights where each layer has a different MLP...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
