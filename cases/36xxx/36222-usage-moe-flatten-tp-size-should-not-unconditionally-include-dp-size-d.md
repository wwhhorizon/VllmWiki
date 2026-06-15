# vllm-project/vllm#36222: [Usage]: MoE flatten_tp_size should not unconditionally include dp_size — DP loses its original semantics for MoE layers

| 字段 | 值 |
| --- | --- |
| Issue | [#36222](https://github.com/vllm-project/vllm/issues/36222) |
| 状态 | open |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: MoE flatten_tp_size should not unconditionally include dp_size — DP loses its original semantics for MoE layers

### Issue 正文摘录

## Summary In FusedMoEParallelConfig.flatten_tp_across_dp_and_pcp (vllm/model_executor/layers/fused_moe/config.py:979-988), when EP is not enabled, dp_size is unconditionally folded into the flattened TP size: ``` flatten_tp_size = dp_size * pcp_size * tp_size flatten_tp_rank = dp_rank * pcp_size * tp_size + pcp_rank * tp_size + tp_rank ``` This means that for MoE layers, DP no longer behaves as "data parallelism" (independent replicas processing different data). Instead, it becomes an additional weight-sharding dimension — effectively turning DP ranks into extra TP ranks for MoE weights only. I believe this conflates two distinct parallelism concepts and leads to practical deployment issues. Concrete failure case When deploying Qwen3.5-35B-A3B-FP8 (which has intermediate_size=512 for MoE experts): TP=8, DP=1: intermediate_size_per_partition = 512 / 8 = 64, which is smaller than the FP8 block quantization size (128). This causes a quantization alignment error. TP=4, DP=2 (hoping to avoid the above issue): The MoE layer computes flatten_tp_size = 2 * 1 * 4 = 8, so intermediate_size_per_partition = 512 / 8 = 64 — the exact same problem. DP=2 does not help at all because DP is silent...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: s original semantics for MoE layers usage ## Summary In FusedMoEParallelConfig.flatten_tp_across_dp_and_pcp (vllm/model_executor/layers/fused_moe/config.py:979-988), when EP is not enabled, dp_size is unconditionally fo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: sers cannot independently control the MoE sharding strategy — it is implicitly determined by dp_size, which was chosen for throughput/batch scheduling reasons, not for MoE weight distribution. - The tight coupling preve...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: deployment issues. Concrete failure case When deploying Qwen3.5-35B-A3B-FP8 (which has intermediate_size=512 for MoE experts): TP=8, DP=1: intermediate_size_per_partition = 512 / 8 = 64, which is smaller than the FP8 bl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ` This means that for MoE layers, DP no longer behaves as "data parallelism" (independent replicas processing different data). Instead, it becomes an additional weight-sharding dimension — effectively turning DP ranks i...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Usage]: MoE flatten_tp_size should not unconditionally include dp_size — DP loses its original semantics for MoE layers usage ## Summary In FusedMoEParallelConfig.flatten_tp_across_dp_and_pcp (vllm/model_executor/layer...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
