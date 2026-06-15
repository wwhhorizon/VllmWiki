# vllm-project/vllm#30055: [RFC]: Sharded Context Parallelism for Deepseek DSA

| 字段 | 值 |
| --- | --- |
| Issue | [#30055](https://github.com/vllm-project/vllm/issues/30055) |
| 状态 | open |
| 标签 | RFC;unstale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Sharded Context Parallelism for Deepseek DSA

### Issue 正文摘录

### Motivation. Context Parallelism (CP) is a promising approach for scaling inference of long-context and sparse-attention models. Recent work (e.g., [arXiv:2411.01783](https://arxiv.org/abs/2411.01783)) highlights its key advantages: latency reduction via sequence-level compute parallelization, lower inter-node communication than Tensor Parallelism (TP), and distributed KV cache storage that scales with more devices. However, current CP implementations (e.g., RFC #22693) adopt a CP+TP hybrid design, which imposes critical limitations: 1. **Redundant weight storage across CP ranks** Although the sequence is partitioned across CP ranks, each rank still holds a full copy (or TP-sharded copy) of all weights. This prevents CP from scaling to many devices—especially at fine granularity (e.g., one rank per GPU)—as total memory usage grows linearly with the number of CP ranks. 2. **Redundant computation within CP rank** Despite sequence partitioning, each CP rank still performs standard Tensor Parallelism (TP) internally. Even when combined with Sequence Parallelism (SP), this setup leads to redundant computation within each rank. This issue is especially pronounced in sparse attention...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: copy) of all weights. This prevents CP from scaling to many devices—especially at fine granularity (e.g., one rank per GPU)—as total memory usage grows linearly with the number of CP ranks. 2. **Redundant computation wi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [RFC]: Sharded Context Parallelism for Deepseek DSA RFC;unstale ### Motivation. Context Parallelism (CP) is a promising approach for scaling inference of long-context and sparse-attention models. Recent work (e.g., [arX...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: sing approach for scaling inference of long-context and sparse-attention models. Recent work (e.g., [arXiv:2411.01783](https://arxiv.org/abs/2411.01783)) highlights its key advantages: latency reduction via sequence-lev...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: 01783](https://arxiv.org/abs/2411.01783)) highlights its key advantages: latency reduction via sequence-level compute parallelization, lower inter-node communication than Tensor Parallelism (TP), and distributed KV cach...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ation of the indexer module but also reduced the access volume of sparse flash attention， which brought in huge performance benefits. ## Parallel size and Communication domain We still maintain the original TP size beca...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
