# vllm-project/vllm#40429: [RFC]: Expose per-parameter sharding as DTensor metadata

| 字段 | 值 |
| --- | --- |
| Issue | [#40429](https://github.com/vllm-project/vllm/issues/40429) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Expose per-parameter sharding as DTensor metadata

### Issue 正文摘录

### Motivation. A growing class of deployments treats vLLM as an inference backend that receives weight updates from an external process — RL rollouts (GRPO/PPO), online fine-tuning, reward-model swap-in, disaggregated prefill/decode refresh. The sender must move each global tensor from its training-side layout (FSDP / HSDP / 3D parallelism / FP8) to vLLM's inference-side layout (TP + optional EP + PP + attention-DP). **To do this without duplicating data on the wire, the sender must know, for every vLLM parameter, which slice of the global tensor lives on which vLLM rank — i.e. a sharding spec.** vLLM has this knowledge; the parallel primitives (`ColumnParallelLinear`, `QKVParallelLinear`, `FusedMoE`, ...) embed it in their constructors and `weight_loader` methods. But there is no queryable API. Consumers are forced into one of: 1. **Send full tensors and slice on vLLM side** — wastes ~TP× bandwidth, dominates weight-sync time at scale. 2. **Hard-code vLLM's sharding rules externally** — a growing `isinstance(module, X) → Placement` table, brittle across versions, silently broken when a new primitive lands, duplicated across every downstream (RL framework, checkpoint tool, debugg...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: [RFC]: Expose per-parameter sharding as DTensor metadata ### Motivation. A growing class of deployments treats vLLM as an inference backend that receives weight updates from an external process — RL rollouts (GRPO/PPO),...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: an external process — RL rollouts (GRPO/PPO), online fine-tuning, reward-model swap-in, disaggregated prefill/decode refresh. The sender must move each global tensor from its training-side layout (FSDP / HSDP / 3D paral...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ** — a growing `isinstance(module, X) → Placement` table, brittle across versions, silently broken when a new primitive lands, duplicated across every downstream (RL framework, checkpoint tool, debugger). 3. **Reverse-e...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: bal tensor from its training-side layout (FSDP / HSDP / 3D parallelism / FP8) to vLLM's inference-side layout (TP + optional EP + PP + attention-DP). **To do this without duplicating data on the wire, the sender must kn...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: outs (GRPO/PPO), online fine-tuning, reward-model swap-in, disaggregated prefill/decode refresh. The sender must move each global tensor from its training-side layout (FSDP / HSDP / 3D parallelism / FP8) to vLLM's infer...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
