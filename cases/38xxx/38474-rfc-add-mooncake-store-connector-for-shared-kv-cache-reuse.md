# vllm-project/vllm#38474: [RFC]: Add Mooncake Store Connector for Shared KV Cache Reuse

| 字段 | 值 |
| --- | --- |
| Issue | [#38474](https://github.com/vllm-project/vllm/issues/38474) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Add Mooncake Store Connector for Shared KV Cache Reuse

### Issue 正文摘录

## Motivation In production LLM serving, many requests share common prompt prefixes — system prompts, few-shot examples, RAG context, multi-turn conversation history, etc. vLLM's local prefix caching effectively reuses KV cache within a single instance, but it cannot help in the following scenarios: - **Cross-instance reuse**: Multiple vLLM instances serving similar traffic recompute the same KV blocks independently. - **Post-eviction recomputation**: After KV cache eviction due to memory pressure, the same blocks must be recomputed from scratch. - **Cold-start warm-up**: A newly launched instance has an empty KV cache and must compute all blocks, even those that have been computed elsewhere. A **Mooncake Store Connector** addresses these gaps by using [Mooncake](https://github.com/kvcache-ai/Mooncake)'s distributed store as a shared KV cache pool. Computed KV cache blocks are stored with content-addressable keys (block hashes). Before computing a prefill, the engine queries the store — if the blocks already exist, they are loaded directly, **skipping redundant prefill computation**. This capability is orthogonal to PD disaggregation and benefits any vLLM deployment topology. ## C...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: *: Multiple vLLM instances serving similar traffic recompute the same KV blocks independently. - **Post-eviction recomputation**: After KV cache eviction due to memory pressure, the same blocks must be recomputed from s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: Shared KV Cache Reuse RFC ## Motivation In production LLM serving, many requests share common prompt prefixes — system prompts, few-shot examples, RAG context, multi-turn conversation history, etc. vLLM's local prefix c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: y are loaded directly, **skipping redundant prefill computation**. This capability is orthogonal to PD disaggregation and benefits any vLLM deployment topology. ## Current Implementation in vllm-ascend We have implement...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: REP server that handles cache existence queries from the scheduler. Key configuration options: - `use_layerwise`: Enable per-layer transfer (pipelined with forward pass) vs. whole-request transfer. - `consumer_is_to_put...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Lookup cache hit│ │ - Register KV caches │ │ │ │ - Build metadata │ │ - LookupKeyServer │ │ │ │ - Track requests │ │ (rank 0 only) │ │ │ └────────────────────┘ │ - Transfer threads │ │ │

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
