# vllm-project/vllm#43643: [RFC]: Streaming API for Real-Time Server State and Metrics

| 字段 | 值 |
| --- | --- |
| Issue | [#43643](https://github.com/vllm-project/vllm/issues/43643) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Streaming API for Real-Time Server State and Metrics

### Issue 正文摘录

### Motivation. Distributed inference routers (e.g., `llm-d-router`) require real-time visibility into engine capacity to balance load effectively. Current scraping/polling methods (like Prometheus `/metrics` pulling) introduce dual inefficiencies: 1. **Latency & Staleness:** A single large request can instantly saturate a server. Routing layers remain blind to this during the polling window, sending subsequent traffic that causes cascading queuing delays or OOMs. 2. **Resource Waste:** Continuous HTTP requests occur even when the server state is completely static. While routers try to mitigate this by estimating in-flight load locally, this state is fragile across router restarts and lacks accurate engine-level visibility into metrics like dynamic KV-cache occupancy. ### Proposed Change. Expose an optional **streaming API endpoint** (e.g., `grpc` streaming) from the engine allowing routers to establish a persistent connection. The model server will asynchronously push structured metrics the moment internal scheduling states change, reducing telemetry lag down to network transport latency. The detailed design will be updated later. ### Feedback Period. _No response_ ### CC List. _...

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ndow, sending subsequent traffic that causes cascading queuing delays or OOMs. 2. **Resource Waste:** Continuous HTTP requests occur even when the server state is completely static. While routers try to mitigate this by...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: Time Server State and Metrics RFC ### Motivation. Distributed inference routers (e.g., `llm-d-router`) require real-time visibility into engine capacity to balance load effectively. Current scraping/polling methods (lik...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: etheus `/metrics` pulling) introduce dual inefficiencies: 1. **Latency & Staleness:** A single large request can instantly saturate a server. Routing layers remain blind to this during the polling window, sending subseq...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: (like Prometheus `/metrics` pulling) introduce dual inefficiencies: 1. **Latency & Staleness:** A single large request can instantly saturate a server. Routing layers remain blind to this during the polling window, send...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: y & Staleness:** A single large request can instantly saturate a server. Routing layers remain blind to this during the polling window, sending subsequent traffic that causes cascading queuing delays or OOMs. 2. **Resou...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
