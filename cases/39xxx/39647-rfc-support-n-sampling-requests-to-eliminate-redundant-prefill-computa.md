# vllm-project/vllm#39647: [RFC]: support n sampling requests to eliminate redundant prefill computation and memory

| 字段 | 值 |
| --- | --- |
| Issue | [#39647](https://github.com/vllm-project/vllm/issues/39647) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: support n sampling requests to eliminate redundant prefill computation and memory

### Issue 正文摘录

### Motivation. Background: the `n` sampling parameter allows generating multiple different responses for a single prompt. The original implementation immediately splits an `n>1` request into `n` separate child requests at the entry point. It causes severe resource waste especialy in **PD Disaggregation** scenarios. The problems with immediate splitting in PD disaggregation: 1. **Redundant Prefill Computation**: The same prompt is computed `n` times on the Prefill instance 2. **Memory Waste**: Each child request independently allocates KV cache, storing `n` copies of identical prefill KV 3. **Network Transfer Overhead**: The same KV cache is transferred `n` times from P-side to D-side Even with Prefix Caching enabled, the original approach still has significant limitations: - Prefix caching operates at the Block level; only complete blocks can be cached and reused - Network transfer remains `n` copies of complete KV cache in PD disaggregation Goals: - Eliminate redundant prefill computation for `n>1` requests in both PD disaggregation and PD colocated scenarios - Reduce memory footprint by sharing prefill KV cache among child requests - Minimize network transfer overhead in PD dis...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [RFC]: support n sampling requests to eliminate redundant prefill computation and memory RFC ### Motivation. Background: the `n` sampling parameter allows generating multiple different responses for a single prompt. The...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: letion, allowing all child requests to share the prefill KV cache. #### Architecture Overview **Entry Point Decision** (`vllm/v1/engine/async_llm.py`): - D-side (KV consumer): Immediate split at entry, each child loads...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: oach still has significant limitations: - Prefix caching operates at the Block level; only complete blocks can be cached and reused - Network transfer remains `n` copies of complete KV cache in PD disaggregation Goals:...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: tart sampling from prompt independently │ ▼ Phase 4: Testing and Validation ├─ Step 4.1: Unit tests for n>1 scenarios ├─ Step 4.2: PD disaggregation integration tests ├─ Step 4.3: PD colocated integration tests └─ Step...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: once - n child requests decode independently - Each child generates different output - Final output contains n independent results - **n=1**: Split logic not triggered, backward compatible - **Streaming Output**: Correc...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
