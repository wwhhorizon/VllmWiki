# vllm-project/vllm#31985: [Feature]: Unwrap FusedMoE custom op

| 字段 | 值 |
| --- | --- |
| Issue | [#31985](https://github.com/vllm-project/vllm/issues/31985) |
| 状态 | open |
| 标签 | feature request;torch.compile |
| 评论 | 26; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Unwrap FusedMoE custom op

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, the whole `FusedMoE` layer is wrapped in the `fused_moe`/`fused_moe_shared` custom ops. This is due to chunking and multi-streaming but prevents torch.compile-based optimizations, increases CPU overhead, and makes it more likely for inefficiencies (copies, sequences of torch ops, etc.) to pop up unexpectedly - for example, we currently use `SiluMul` custom op in some cases, resulting in bad performance as `forward_native` gets used (but not compiled). It also increases complexity in many cases as we have to write custom kernels for code that could otherwise be implemented in native torch and be efficiently compiled to triton kernels automatically with torch.compile. Finally, MoE models currently suffer from longer cold-start compile times because the layer name interferes with layerwise/piecewise caching. There are two kinds of chunking in the fused_moe layer: - DP chunking (outer), which happens in the DPEP low-latency scenario where we use a batched layout for activations (`E x max_m_per_expert x K`). To make sure we avoid a scenario where one expert receives more tokens than `max_m_per_expert`, we chunk `M`. This chunking canno...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Feature]: Unwrap FusedMoE custom op feature request;torch.compile ### 🚀 The feature, motivation and pitch Currently, the whole `FusedMoE` layer is wrapped in the `fused_moe`/`fused_moe_shared` custom ops. This is due t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: cross graphs if possible~~ In theory, this work should not run afoul of cudagraphs, DBO or SP or other MoE optimizations, and we can resolve any issues as they come up. ### CC list @bnellnm @robertgshaw2-redhat @zou3519...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ), which happens in the DPEP low-latency scenario where we use a batched layout for activations (`E x max_m_per_expert x K`). To make sure we avoid a scenario where one expert receives more tokens than `max_m_per_expert...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Feature]: Unwrap FusedMoE custom op feature request;torch.compile ### 🚀 The feature, motivation and pitch Currently, the whole `FusedMoE` layer is wrapped in the `fused_moe`/`fused_moe_shared` custom ops. This is due t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: he fused_moe layer: - DP chunking (outer), which happens in the DPEP low-latency scenario where we use a batched layout for activations (`E x max_m_per_expert x K`). To make sure we avoid a scenario where one expert rec...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
