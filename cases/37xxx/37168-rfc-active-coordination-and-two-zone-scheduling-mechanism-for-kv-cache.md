# vllm-project/vllm#37168: [RFC]:  Active Coordination and Two-Zone Scheduling Mechanism for KV Cache in Long-Running Agents

| 字段 | 值 |
| --- | --- |
| Issue | [#37168](https://github.com/vllm-project/vllm/issues/37168) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]:  Active Coordination and Two-Zone Scheduling Mechanism for KV Cache in Long-Running Agents

### Issue 正文摘录

### Motivation. ## 1. Problem Statement ### 1.1. Background: The Temporal Mismatch between Agent Context and KV Cache Modern LLM inference engines utilize **Prefix Caching** to store historical KV states in GPU memory, skipping redundant prefix computations to optimize Time-To-First-Token (TTFT). The fundamental assumption of this mechanism is that **the context is append-only**. However, in **Deep Agent** scenarios (e.g., OpenCLAW, Claude Code, AutoGen), the context engine performs continuous dynamic operations: * **Compression**: Merging multi-turn dialogues into concise summaries. * **Offloading**: Moving large text blocks or images to external storage. * **Refinement**: Replacing raw history with abstract summaries. * **Skill Switching**: Dynamically injecting or removing System Prompts and tool definitions. **The Core Contradiction**: The inference engine remains oblivious to these semantic changes. It retains KV cache blocks corresponding to context that the Agent has already discarded or modified. This leads to severe memory inefficiency and significant performance degradation of the inference service. ### 1.2. The Cascade of Performance Degradation In high-concurrency envi...

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 5: [RFC]: Active Coordination and Two-Zone Scheduling Mechanism for KV Cache in Long-Running Agents RFC ### Motivation. ## 1. Problem Statement ### 1.1. Background: The Temporal Mismatch between Agent Context and KV Cache...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: Prefill computations and incurs additional cache lookup overhead. 3. **Throughput Blockage**: Under multi-session concurrency, significant compute power is wasted on redundant Prefill operations and ineffective cache ma...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: dialogues into concise summaries. * **Offloading**: Moving large text blocks or images to external storage. * **Refinement**: Replacing raw history with abstract summaries. * **Skill Switching**: Dynamically injecting o...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: victed prematurely. The system is forced to repeatedly execute expensive Prefill computations and incurs additional cache lookup overhead. 3. **Throughput Blockage**: Under multi-session concurrency, significant compute...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: Motivation. ## 1. Problem Statement ### 1.1. Background: The Temporal Mismatch between Agent Context and KV Cache Modern LLM inference engines utilize **Prefix Caching** to store historical KV states in GPU memory, skip...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
