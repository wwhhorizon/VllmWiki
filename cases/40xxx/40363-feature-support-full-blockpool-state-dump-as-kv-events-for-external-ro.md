# vllm-project/vllm#40363: [Feature]: Support full BlockPool state dump as KV events for external router

| 字段 | 值 |
| --- | --- |
| Issue | [#40363](https://github.com/vllm-project/vllm/issues/40363) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support full BlockPool state dump as KV events for external router

### Issue 正文摘录

### 🚀 The feature, motivation and pitch # Problem When deploying vLLM with an external KV-cache-aware router that builds a radix tree from KV events, the router needs to reconstruct the full KV cache state of each worker on startup or after a crash. vLLM's ZmqEventPublisher provides a replay buffer to recover from transient KV event gaps. However, due to its limited capacity, the router cannot reconstruct the full index once the replay buffer has been exhausted, leaving it with an incomplete view of the worker's cache and no recovery path. # Proposal Add a tree dump capability to vLLM's EventPublisher that serializes the current BlockPool state as a sequence of BlockStored events, enabling external consumers to reconstruct the full index on demand. This capability could be exposed via the existing replay socket or a dedicated HTTP endpoint such as /dump_kv_cache_state ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently a...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Problem When deploying vLLM with an external KV-cache-aware router that builds a radix tree from KV events, the router needs to reconstruct the full KV cache state of each worker on startup or after a crash. vLLM's ZmqE...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: of the worker's cache and no recovery path. # Proposal Add a tree dump capability to vLLM's EventPublisher that serializes the current BlockPool state as a sequence of BlockStored events, enabling external consumers to...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: re, motivation and pitch # Problem When deploying vLLM with an external KV-cache-aware router that builds a radix tree from KV events, the router needs to reconstruct the full KV cache state of each worker on startup or...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Feature]: Support full BlockPool state dump as KV events for external router feature request ### 🚀 The feature, motivation and pitch # Problem When deploying vLLM with an external KV-cache-aware router that builds a ra...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Feature]: Support full BlockPool state dump as KV events for external router feature request ### 🚀 The feature, motivation and pitch # Problem When deploying vLLM with an external KV-cache-aware router that builds a ra...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
