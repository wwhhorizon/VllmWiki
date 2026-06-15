# vllm-project/vllm#19329: [RFC]: Graceful Error Handling for KV Connector Load Failures

| 字段 | 值 |
| --- | --- |
| Issue | [#19329](https://github.com/vllm-project/vllm/issues/19329) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Graceful Error Handling for KV Connector Load Failures

### Issue 正文摘录

### Motivation. ### 🧩 Summary This RFC proposes adding fault recovery support to the KV connector infrastructure introduced in #15960. The goal is to make vLLM resilient to KV block load failures (e.g., due to eviction or network disconnections) by detecting failures and rescheduling only affected requests for recomputation. ### 🧠 Background vLLM recently introduced the KV connector abstraction, providing a pluggable interface for integrating external solutions for KV cache offload and transfer. This enables supporting use cases like KV cache sharing and prefill-decode (P-D) disaggregation. Notable examples include the LMCache connector (PR #16625) and NIXL connector (PR #17751). The KV loading protocol involves: - start_load_kv() → invoked before the forward pass to initiate (asynchronous) loading of all required KV blocks. - wait_for_layer_load() → invoked before each layer’s attention kernel to ensure the relevant blocks are available. ### ⚠️ Problem Currently, vLLM lacks a mechanism to detect or recover from KV load failures. If one or more KV blocks fail to load, it may lead to system instability (crash or hang) or incorrect outputs (silent corruption of the KV cache). This u...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [RFC]: Graceful Error Handling for KV Connector Load Failures RFC;stale ### Motivation. ### 🧩 Summary This RFC proposes adding fault recovery support to the KV connector infrastructure introduced in #15960. The goal is...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: t blocks are available. ### ⚠️ Problem Currently, vLLM lacks a mechanism to detect or recover from KV load failures. If one or more KV blocks fail to load, it may lead to system instability (crash or hang) or incorrect...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: , providing a pluggable interface for integrating external solutions for KV cache offload and transfer. This enables supporting use cases like KV cache sharing and prefill-decode (P-D) disaggregation. Notable examples i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: connectors to report failed block IDs. 2. Executor Reporting - `GPUModelRunner` retrieves the failed block IDs and includes them in `ModelRunnerOutput` (should be aggregated across all workers in TP setups). 3. Schedule...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ts (silent corruption of the KV cache). This undermines reliability, especially in large-scale or disaggregated deployments. --- ### Proposed Change. Even if KV load failures occur, the forward pass should complete. Pos...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
