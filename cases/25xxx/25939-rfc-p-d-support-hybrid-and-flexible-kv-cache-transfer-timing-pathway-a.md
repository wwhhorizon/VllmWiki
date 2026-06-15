# vllm-project/vllm#25939: [RFC][P/D]: Support hybrid and flexible KV Cache transfer timing & pathway at request-level

| 字段 | 值 |
| --- | --- |
| Issue | [#25939](https://github.com/vllm-project/vllm/issues/25939) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC][P/D]: Support hybrid and flexible KV Cache transfer timing & pathway at request-level

### Issue 正文摘录

### Motivation. In current prefill-decode (PD) disaggregated architectures, a static strategy determining KV Cache transfer timing and method is adopted, which is uniformly applied to all requests. This inflexible approach fails to account for key trade-offs: between latency and throughput when choosing ***when*** to start KV Cache transfer(during versus after prefill), and between latency and scalability when choosing ***how*** to transfer it (via P2P communication or through a centralized store). As a result, the system cannot dynamically adapt to diverse workload requirements—such as low-latency interactive chats, high-throughput multi-round AI agent tasks, or research queries with variable-depth—hindering its capability to meet fine-grained Service Level Objective (SLO) targets across different types of tasks. | Decode Scheduling Time | Extra Data Copy | Time Latency | Compute/Transfer Overlap | | :----: | :----: | :----: | :----: | |Before prefill | No | Low | Yes | |After prefill | Yes | High | No | Table 1. P/D Binding Timing (KV Cache Transfer Timing) Trade-offs ### Proposed Change. In this RFC, we propose several changes to support hybrid and flexible KV Cache transfer ti...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [P/D]: Support hybrid and flexible KV Cache transfer timing & pathway at request-level RFC;stale ### Motivation. In current prefill-decode (PD) disaggregated architectures, a static strategy determining KV Cache transfe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: RFC;stale ### Motivation. In current prefill-decode (PD) disaggregated architectures, a static strategy determining KV Cache transfer timing and method is adopted, which is uniformly applied to all requests. This inflex...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: s. This inflexible approach fails to account for key trade-offs: between latency and throughput when choosing ***when*** to start KV Cache transfer(during versus after prefill), and between latency and scalability when...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ector`, which already enables concurrent management of multiple transfer backends. However, the current implementation lacks per-request customization. Here, we propose to extend this component to enable fine-grained, d...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ing deployment to address the previously mentioned problem. Our approach builds upon the existing `MultiConnector`, which already enables concurrent management of multiple transfer backends. However, the current impleme...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
