# vllm-project/vllm#24885: [RFC] Clarifying vLLM Shutdown Semantics

| 字段 | 值 |
| --- | --- |
| Issue | [#24885](https://github.com/vllm-project/vllm/issues/24885) |
| 状态 | open |
| 标签 | feature request;RFC |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC] Clarifying vLLM Shutdown Semantics

### Issue 正文摘录

### 🚀 The feature, motivation and pitch # RFC: Clarifying vLLM Shutdown Semantics ## Introduction This RFC defines the expected behavior of **vLLM during shutdown**, addressing two distinct use cases: 1. **Library API usage** (primarily offline inference). 2. **Online serving usage** (long-running HTTP server deployments). Documenting these expectations will reduce surprises for users and help us achieve a consistent implementation across all features. This RFC was motivated by #22295 and #22828. --- ## Library API Shutdown Library users expect deterministic, resource-safe cleanup when disposing of LLM instances. ### Expectations * Library users may create and destroy `vllm.LLM` instances. * Deleting an instance should: - Release all associated resources (memory, file descriptors, temporary files, etc.). - Shut down any child processes gracefully. * No library should define global signal handlers. - Signal handlers are global and may interfere with applications embedding vLLM. - Applications must configure their own signal-handling behavior. --- ## Online Serving Shutdown Online serving users expect graceful termination semantics, consistent with production environments like Kuber...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [RFC] Clarifying vLLM Shutdown Semantics feature request;RFC ### 🚀 The feature, motivation and pitch # RFC: Clarifying vLLM Shutdown Semantics ## Introduction This RFC defines the expected behavior of **vLLM during shut...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: tial restart scenario, for example a "reload model" or "restart workers" capability. ### Context * `vllm serve` launches an HTTP server for long-running online inference. * Each request is relatively expensive (100ms+)....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nd may interfere with applications embedding vLLM. - Applications must configure their own signal-handling behavior. --- ## Online Serving Shutdown Online serving users expect graceful termination semantics, consistent...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: y #22295 and #22828. --- ## Library API Shutdown Library users expect deterministic, resource-safe cleanup when disposing of LLM instances. ### Expectations * Library users may create and destroy `vllm.LLM` instances. *...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: y #22295 and #22828. --- ## Library API Shutdown Library users expect deterministic, resource-safe cleanup when disposing of LLM instances. ### Expectations * Library users may create and destroy `vllm.LLM` instances. *...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
