# vllm-project/vllm#26850: [Feature]: Add new stats metrics for available_kv_cache_memory

| 字段 | 值 |
| --- | --- |
| Issue | [#26850](https://github.com/vllm-project/vllm/issues/26850) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add new stats metrics for available_kv_cache_memory

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, vLLM logs the "Available KV cache memory" vllm log during engine initialization (as seen in logs like " Available KV cache memory: XX.XX GiB", but this information is not exposed as a Prometheus metric. The current logging approach only provides point-in-time visibility during startup, but doesn't enable continuous monitoring. This makes it difficult to: 1. Perform capacity planning by the user/customer when they want figure out the actual GPU mem utilization. 2. Track memory utilization trends over the time. We already capture "vllm:available_kv_cache_memory_bytes" but that shows how much of the already-allocated cache is being utilized. To calculate actual utilization we might need Available KV cache memory. Total GPU Memory: 80GB ├── Model Weights: 30GB ├── Other GPU Usage: 4GB └── Available for KV Cache: 46GB ← vllm:available_kv_cache_memory_bytes(new metrics) ├── Allocated KV Cache: 40GB │ ├── Used: 25GB (62.5%) ← vllm:kv_cache_usage_perc │ └── Free: 15GB (37.5%) └── Unallocated: 6GB ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [ ] Make sure you already searched fo...

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: 🚀 The feature, motivation and pitch Currently, vLLM logs the "Available KV cache memory" vllm log during engine initialization (as seen in logs like " Available KV cache memory: XX.XX GiB", but this information is not e...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: as seen in logs like " Available KV cache memory: XX.XX GiB", but this information is not exposed as a Prometheus metric. The current logging approach only provides point-in-time visibility during startup, but doesn't e...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Add new stats metrics for available_kv_cache_memory feature request;stale ### 🚀 The feature, motivation and pitch Currently, vLLM logs the "Available KV cache memory" vllm log during engine initialization (as...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: nable continuous monitoring. This makes it difficult to: 1. Perform capacity planning by the user/customer when they want figure out the actual GPU mem utilization. 2. Track memory utilization trends over the time. We a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [ ] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
