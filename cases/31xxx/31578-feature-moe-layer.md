# vllm-project/vllm#31578: [Feature]: MoE Layer

| 字段 | 值 |
| --- | --- |
| Issue | [#31578](https://github.com/vllm-project/vllm/issues/31578) |
| 状态 | open |
| 标签 | feature request;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: MoE Layer

### Issue 正文摘录

This is a tracking doc where I will add notes as I go ### 🚀 The feature, motivation and pitch We currently have the following features in FusedMoE - shared expert overlap (multi-steam for tp-case) - shared expert overlap (with deepep for dp-case) - naive dispatch/combine - sequence parallelism - dcp + pcp - chunking - eplb - shared expert fusion (aiter) The logic for this is very complicated logic in the forward method - https://github.com/vllm-project/vllm/blob/cf16342d435f5d6cbbeaf076ed4546bda0f89a20/vllm/model_executor/layers/fused_moe/layer.py#L1732-L2059 ### Shared Expert Overlap The issue with shared experts is that we break the abstraction of the layer, since the shared expert is sometimes added as an attr of the FusedMoE layer. To make matters more complicated, there are actually two modes - TP Case: SharedFusedMoE -> FusedMoE -> FP8 ---- fused moe is responsible for running the shared expert - DP Case: SharedFusedMoE -> FusedMoE -> mk(Fp8) --- mk is responsible for running the shared expert Also, in this case, the gate is run by the FusedMoE layer. We need a class to manage the full MoE layer with clear view of which "mode" we are in ``` class MoELayer: gate: Router selec...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: m for tp-case) - shared expert overlap (with deepep for dp-case) - naive dispatch/combine - sequence parallelism - dcp + pcp - chunking - eplb - shared expert fusion (aiter) The logic for this is very complicated logic...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Feature]: MoE Layer feature request;stale This is a tracking doc where I will add notes as I go ### 🚀 The feature, motivation and pitch We currently have the following features in FusedMoE - shared expert overlap (mult...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: p (with deepep for dp-case) - naive dispatch/combine - sequence parallelism - dcp + pcp - chunking - eplb - shared expert fusion (aiter) The logic for this is very complicated logic in the forward method - https://githu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: MoE Layer feature request;stale This is a tracking doc where I will add notes as I go ### 🚀 The feature, motivation and pitch We currently have the following features in FusedMoE - shared expert overlap (mult...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: d, there are actually two modes - TP Case: SharedFusedMoE -> FusedMoE -> FP8 ---- fused moe is responsible for running the shared expert - DP Case: SharedFusedMoE -> FusedMoE -> mk(Fp8) --- mk is responsible for running...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
