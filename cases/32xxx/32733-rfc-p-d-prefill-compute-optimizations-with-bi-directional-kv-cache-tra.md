# vllm-project/vllm#32733: [RFC]: [P/D] Prefill compute optimizations with bi-directional KV cache transfers between P and D nodes

| 字段 | 值 |
| --- | --- |
| Issue | [#32733](https://github.com/vllm-project/vllm/issues/32733) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: [P/D] Prefill compute optimizations with bi-directional KV cache transfers between P and D nodes

### Issue 正文摘录

### Motivation. Today, vLLM P-D disaggregation architecture utilizing Nixl KV connector has a distinct role for prefill (P) and decode (D) nodes for KV cache handling; the KV transfers are uni-directional with P node as a producer and D node as a consumer. This constraint introduces inefficiencies in two critical scenarios: multi-turn conversation and cache-evicted prefill nodes, requiring redundant recomputation of previously generated KV blocks during incremental prefill requests on P nodes. **1. Multi-turn conversations** Multi-turn conversational inference refers to sequential dialogue exchanges between end-users and LLM systems that maintain contextual coherence across interaction cycles. Implementation requires persistent conversation history management, wherein each subsequent user query is concatenated with relevant historical context: system prompts, prior user queries, and model-generated responses. Optimal performance in non-disaggregated deployments is achieved through session persistence on LLM inference servers, enabling KV cache reuse across turns. However, P-D disaggregated architectures present a fundamental challenge: the KV cache corresponding to model-generated...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [RFC]: [P/D] Prefill compute optimizations with bi-directional KV cache transfers between P and D nodes RFC ### Motivation. Today, vLLM P-D disaggregation architecture utilizing Nixl KV connector has a distinct role for...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: etween P and D nodes RFC ### Motivation. Today, vLLM P-D disaggregation architecture utilizing Nixl KV connector has a distinct role for prefill (P) and decode (D) nodes for KV cache handling; the KV transfers are uni-d...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: fill nodes, requiring redundant recomputation of previously generated KV blocks during incremental prefill requests on P nodes. **1. Multi-turn conversations** Multi-turn conversational inference refers to sequential di...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: o query D node for its KV params that can be passed to P node but buring benchmarking I identified that the additional round-trip to the Decode node to query KV block metadata introduces latency overhead. To address thi...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: system prompts, historical user queries, and prior model responses) upon cache misses. Both computational redundancy scenarios can be mitigated through implementation of bidirectional KV cache transfer capabilities betw...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
