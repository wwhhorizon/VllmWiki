# vllm-project/vllm#37995: [RFC]: Prefill Context Parallel for Qwen3.5 Hybrid Attention

| 字段 | 值 |
| --- | --- |
| Issue | [#37995](https://github.com/vllm-project/vllm/issues/37995) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Prefill Context Parallel for Qwen3.5 Hybrid Attention

### Issue 正文摘录

## Summary This RFC describes the implementation of Prefill Context Parallel (PCP) for Qwen3.5's hybrid attention architecture, which combines full attention and linear attention (GatedDeltaNet) layers. PCP reduces long-context prefill latency by: - **Full attention layers**: Distributing sequence tokens across ranks using zigzag ring attention (cp_size speedup per layer) - **Linear attention**: Splitting batch dimension instead of sequence, eliminating replicated computation and all_gather overhead - **MoE layers**: Spliting tokens dimension ## Motivation Long-context prefill is a major bottleneck for LLM inference: 1. **Quadratic attention complexity**: Full attention is O(N^2) in sequence length, making 256K+ contexts extremely slow 2. **Memory bandwidth** : Large KV caches stress memory subsystem Tensor Parallelism (TP) helps by distributing model weights, but each GPU still processes the full sequence. Context Parallel (CP) addresses this by distributing the sequence itself across GPUs. ### Challenge: Hybrid Attention Qwen3.5 uses a hybrid architecture: - **15 full attention layers**: Standard transformer attention - **45 linear attention layers**: GatedDeltaNet (GDN) with re...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [RFC]: Prefill Context Parallel for Qwen3.5 Hybrid Attention feature request ## Summary This RFC describes the implementation of Prefill Context Parallel (PCP) for Qwen3.5's hybrid attention architecture, which combines...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: quence, improving load balance for causal attention. For cp_size = 2 specifically: ``` Rank 0: [0, 3, 4, 7, 8, ...] (positions 0, 3, 4, 7, ...) Rank 1: [1, 2, 5, 6, 9, ...] (positions 1, 2, 5, 6, ...) ``` ### Layer-Type...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ntation of Prefill Context Parallel (PCP) for Qwen3.5's hybrid attention architecture, which combines full attention and linear attention (GatedDeltaNet) layers. PCP reduces long-context prefill latency by: - **Full att...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: th, making 256K+ contexts extremely slow 2. **Memory bandwidth** : Large KV caches stress memory subsystem Tensor Parallelism (TP) helps by distributing model weights, but each GPU still processes the full sequence. Con...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [RFC]: Prefill Context Parallel for Qwen3.5 Hybrid Attention feature request ## Summary This RFC describes the implementation of Prefill Context Parallel (PCP) for Qwen3.5's hybrid attention architecture, which combines...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
