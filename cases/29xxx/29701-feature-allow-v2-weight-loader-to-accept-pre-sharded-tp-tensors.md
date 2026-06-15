# vllm-project/vllm#29701: [Feature]: Allow v2 weight loader to accept pre-sharded TP tensors

| 字段 | 值 |
| --- | --- |
| Issue | [#29701](https://github.com/vllm-project/vllm/issues/29701) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Allow v2 weight loader to accept pre-sharded TP tensors

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hi vLLM team, I’d like to raise a feature request around the v2 weight-loading path. Today, the v2 weight loader appears to assume that the caller provides the full logical tensor for a given weight, and vLLM then handles tensor-parallel (TP) slicing/sharding internally. This works well in the standard “load from checkpoint” flow, but can be limiting in integrations where weights are already TP-sharded upstream. In some scenarios (e.g., coupling vLLM to an external training system), each rank already holds its own TP-local shard of a weight. To use vLLM’s v2 loader, we currently need to materialize a full logical tensor, only for vLLM to slice it back down by TP rank. That adds unnecessary work and memory pressure, especially for large models. As a workaround today, we monkey-patch the relevant layers to force them to use the v1 loader instead of the v2 loader, so that we can pass in per-rank shards directly. This works but is brittle and diverges from the default code path. It would be very helpful to have an *opt-in* way for advanced users to tell vLLM "this tensor is already the TP-local shard for the current rank; please treat it as such...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: eature]: Allow v2 weight loader to accept pre-sharded TP tensors feature request;stale ### 🚀 The feature, motivation and pitch Hi vLLM team, I’d like to raise a feature request around the v2 weight-loading path. Today,...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: tensor for a given weight, and vLLM then handles tensor-parallel (TP) slicing/sharding internally. This works well in the standard “load from checkpoint” flow, but can be limiting in integrations where weights are alrea...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ring the shard layout matches what vLLM expects for that weight type and quantization scheme. Related but distinct existing issue: #19020 discusses extending `load_weights(...)` for online quantization in GRPO-style wor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: d" mode, and that the caller would be responsible for ensuring the shard layout matches what vLLM expects for that weight type and quantization scheme. Related but distinct existing issue: #19020 discusses extending `lo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
