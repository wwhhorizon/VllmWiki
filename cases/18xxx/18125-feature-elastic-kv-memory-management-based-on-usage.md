# vllm-project/vllm#18125: [Feature]: Elastic KV memory management based on usage

| 字段 | 值 |
| --- | --- |
| Issue | [#18125](https://github.com/vllm-project/vllm/issues/18125) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Elastic KV memory management based on usage

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hello there, I'm considering whether it is possible to dynamically adjust runtime KV Cache memory usage based on the current system conditions and workload demand. For example, here are two scenarios: 1) When users do not need to perform inference for a while and GPU/CPU memory usage is low, current serving frameworks can free up memory for other tasks (e.g., other AI workloads.). 2) When users need to handle many concurrent requests during runtime, the serving framework increase GPU memory utilization without a restart. The problem is that I notice that mainstream serving frameworks, such as vLLM, SGLang and TGI typically pre-allocate a fixed percentage of GPU memory before server startup. (in vLLM it is `gpu_memory_utilization`). That means the pre-allocated GPU memory cannot be adjusted without a restart. I absolutely feel that this is a challenge for vLLM that depends on PagedAttention. As far as I understand, sequences are mapped into paged KV memory blocks. In a low-usage scenario (like case 1), if we want to free up memory, we would need to identify which KV memory blocks to evict and determine an appropriate eviction policy or ratio....

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ing a simple StaticCache (adapted to support continuous batching) mechanism, I implemented a rudimentary dynamic memory adjustment strategy. While it's far from production-ready, it suggests the potential for this appro...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: re, I'm considering whether it is possible to dynamically adjust runtime KV Cache memory usage based on the current system conditions and workload demand. For example, here are two scenarios: 1) When users do not need t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Elastic KV memory management based on usage feature request;stale ### 🚀 The feature, motivation and pitch Hello there, I'm considering whether it is possible to dynamically adjust runtime KV Cache memory usag...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ntion. As far as I understand, sequences are mapped into paged KV memory blocks. In a low-usage scenario (like case 1), if we want to free up memory, we would need to identify which KV memory blocks to evict and determi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
