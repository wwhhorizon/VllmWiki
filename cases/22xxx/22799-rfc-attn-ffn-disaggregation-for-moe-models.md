# vllm-project/vllm#22799: [RFC]: ATTN-FFN Disaggregation for MoE Models

| 字段 | 值 |
| --- | --- |
| Issue | [#22799](https://github.com/vllm-project/vllm/issues/22799) |
| 状态 | open |
| 标签 | RFC;stale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: ATTN-FFN Disaggregation for MoE Models

### Issue 正文摘录

### Motivation. In large-scale MoE inference, the benefits of sparsity in the decoding phase drive continuous expansion of expert parallelism (EP). Prior designs (e.g., DeepEP[1]) improve throughput at scale but have limited scalability because they place EP shards across data-parallel (DP) ranks. Recently, Attention–FFN disaggregation (AFD) has been proposed by ByteDance[2], StepFun[3], and Huawei[4]. The motivation is straightforward: the attention phase is memory-bound, whereas the FFN/expert phase is compute-bound, so a single homogeneous deployment cannot optimize both simultaneously. Module-wise heterogeneous placement is beneficial as EP continues to scale. Based on these production insights, we propose introducing AFD in vLLM: decouple Attention and FFN/experts at resource levels so they can scale independently, and overlap communication in a “perfectly balanced” pipeline to improve throughput. The initial revision targets an eager-mode MVP without custom kernels: it runs multiple DP replicas on the Attention side and EP replicas on the MoE side, enabling cross-node M2N routing with correctness guarantees. Subsequently, we will provide stable AFD interfaces for communicati...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: sion of expert parallelism (EP). Prior designs (e.g., DeepEP[1]) improve throughput at scale but have limited scalability because they place EP shards across data-parallel (DP) ranks. Recently, Attention–FFN disaggregat...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: [RFC]: ATTN-FFN Disaggregation for MoE Models RFC;stale ### Motivation. In large-scale MoE inference, the benefits of sparsity in the decoding phase drive continuous expansion of expert parallelism (EP). Prior designs (...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: sity in the decoding phase drive continuous expansion of expert parallelism (EP). Prior designs (e.g., DeepEP[1]) improve throughput at scale but have limited scalability because they place EP shards across data-paralle...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: Attention side and EP replicas on the MoE side, enabling cross-node M2N routing with correctness guarantees. Subsequently, we will provide stable AFD interfaces for communication, load balancing, and elasticity. [1] htt...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [RFC]: ATTN-FFN Disaggregation for MoE Models RFC;stale ### Motivation. In large-scale MoE inference, the benefits of sparsity in the decoding phase drive continuous expansion of expert parallelism (EP). Prior designs (...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
