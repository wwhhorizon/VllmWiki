# vllm-project/vllm#42419: [RFC]: [V1][Attention] Add an experimental training-free sparse prefill attention backend for long-context workloads (vLLM 0.19.1)

| 字段 | 值 |
| --- | --- |
| Issue | [#42419](https://github.com/vllm-project/vllm/issues/42419) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: [V1][Attention] Add an experimental training-free sparse prefill attention backend for long-context workloads (vLLM 0.19.1)

### Issue 正文摘录

### Motivation. ### Motivation Long-context prefill is often dominated by attention computation. As context lengths grow to 64K, 128K, and beyond, dense prefill attention becomes a major deployment bottleneck even when decoding is already optimized. We have been experimenting with a training-free sparse prefill attention mechanism called **BFLA (Block-Filtered Long-Context Attention)** for vLLM-style paged-attention workloads. BFLA is designed as an opt-in runtime attention backend: it does not modify model weights, does not require training or calibration, and falls back to dense attention for unsupported cases. Reference implementation: https://github.com/Alicewithrabbit/BFLA I would like to ask whether the vLLM maintainers would be open to upstreaming this as an experimental V1 Triton attention feature, possibly in several small PRs. ### Proposed Change. ### Proposal Add an experimental sparse prefill path to the V1 Triton attention backend. At a high level, the method works in two stages: 1. **Runtime block-level importance estimation** During prefill, BFLA partitions the query and KV sequences into coarse blocks. It builds lightweight pooled Q/K representations and estimates...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: a high level, the method works in two stages: 1. **Runtime block-level importance estimation** During prefill, BFLA partitions the query and KV sequences into coarse blocks. It builds lightweight pooled Q/K representati...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 1][Attention] Add an experimental training-free sparse prefill attention backend for long-context workloads (vLLM 0.19.1) RFC ### Motivation. ### Motivation Long-context prefill is often dominated by attention computati...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: been experimenting with a training-free sparse prefill attention mechanism called **BFLA (Block-Filtered Long-Context Attention)** for vLLM-style paged-attention workloads. BFLA is designed as an opt-in runtime attentio...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: g with a training-free sparse prefill attention mechanism called **BFLA (Block-Filtered Long-Context Attention)** for vLLM-style paged-attention workloads. BFLA is designed as an opt-in runtime attention backend: it doe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: A is designed as an opt-in runtime attention backend: it does not modify model weights, does not require training or calibration, and falls back to dense attention for unsupported cases. Reference implementation: https:...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
