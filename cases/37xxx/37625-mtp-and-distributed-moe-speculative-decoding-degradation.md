# vllm-project/vllm#37625: MTP and Distributed MoE Speculative Decoding Degradation

| 字段 | 值 |
| --- | --- |
| Issue | [#37625](https://github.com/vllm-project/vllm/issues/37625) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> MTP and Distributed MoE Speculative Decoding Degradation

### Issue 正文摘录

### Problem Description The integration of MTP into Sparse MoEs under EP topologies presents a hardware interconnect bottleneck. A common assumption is that speculative decoding is meant strictly for low-concurrency, memory-bound environments. However, on distributed MoEs, speculative verification reduces performance even at low concurrency due to unamortized All-to-All communication latency. ### Reproduction / Context When verifying $K$ speculative tokens in a standard dense model, standard tensor parallelism applies efficiently. In an MoE, verifying $K$ disparate tokens requires the router to dispatch to entirely different physical GPUs simultaneously. This transforms a normally compute-light verification step into an All-to-All network scatter-gather operation across the NVLink/PCIe fabric.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: okens in a standard dense model, standard tensor parallelism applies efficiently. In an MoE, verifying $K$ disparate tokens requires the router to dispatch to entirely different physical GPUs simultaneously. This transf...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: MTP and Distributed MoE Speculative Decoding Degradation ### Problem Description The integration of MTP into Sparse MoEs under EP topologies presents a hardware interconnect bottleneck. A common assumption is that specu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: iently. In an MoE, verifying $K$ disparate tokens requires the router to dispatch to entirely different physical GPUs simultaneously. This transforms a normally compute-light verification step into an All-to-All network...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: $ speculative tokens in a standard dense model, standard tensor parallelism applies efficiently. In an MoE, verifying $K$ disparate tokens requires the router to dispatch to entirely different physical GPUs simultaneous...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ion / Context When verifying $K$ speculative tokens in a standard dense model, standard tensor parallelism applies efficiently. In an MoE, verifying $K$ disparate tokens requires the router to dispatch to entirely diffe...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
