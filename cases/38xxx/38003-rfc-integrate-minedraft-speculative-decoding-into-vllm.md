# vllm-project/vllm#38003: [RFC]: Integrate MineDraft speculative decoding into vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#38003](https://github.com/vllm-project/vllm/issues/38003) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Integrate MineDraft speculative decoding into vLLM

### Issue 正文摘录

### Motivation. Current speculative decoding in vLLM executes drafting and verification sequentially, which places drafting on the critical path and limits achievable speedup. MineDraft introduces a batch-parallel speculative decoding paradigm that overlaps drafting and verification across different batches, effectively hiding drafting latency. This RFC aims to explore integrating this paradigm into vLLM to further improve throughput and latency without requiring model retraining. ### Proposed Change. This RFC proposes integrating MineDraft, a batch-parallel speculative decoding framework, into vLLM. Full design and details: [MineDraft.md](https://github.com/user-attachments/files/26212782/MineDraft.md) ### Summary - Introduce a two-batch scheduling mechanism - Overlap drafting and verification: - Batch A → verification - Batch B → drafting - Alternate roles per decoding step ### Key Integration Points - Scheduler: batch-level coordination - LLMEngine: overlapping execution flow - KV cache: avoid over-allocation for draft-only requests ### Compatibility - Continuous batching - PagedAttention - Existing speculative decoding methods ### Feedback Period. 1–2 weeks for initial feedbac...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [RFC]: Integrate MineDraft speculative decoding into vLLM RFC ### Motivation. Current speculative decoding in vLLM executes drafting and verification sequentially, which places drafting on the critical path and limits a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: g and verification across different batches, effectively hiding drafting latency. This RFC aims to explore integrating this paradigm into vLLM to further improve throughput and latency without requiring model retraining...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 82/MineDraft.md) ### Summary - Introduce a two-batch scheduling mechanism - Overlap drafting and verification: - Batch A → verification - Batch B → drafting - Alternate roles per decoding step ### Key Integration Points...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: r Things. - I am not the author of MineDraft, but implemented a working version and validated its behavior. - This feature can be implemented as an optional decoding mode and does not affect existing workflows. - I plan...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: uler: batch-level coordination - LLMEngine: overlapping execution flow - KV cache: avoid over-allocation for draft-only requests ### Compatibility - Continuous batching - PagedAttention - Existing speculative decoding m...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
