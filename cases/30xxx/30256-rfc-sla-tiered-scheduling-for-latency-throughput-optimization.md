# vllm-project/vllm#30256: [RFC]: SLA-Tiered Scheduling for Latency/Throughput Optimization

| 字段 | 值 |
| --- | --- |
| Issue | [#30256](https://github.com/vllm-project/vllm/issues/30256) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: SLA-Tiered Scheduling for Latency/Throughput Optimization

### Issue 正文摘录

### Motivation. #### **Summary** This RFC proposes adding a Service Level Agreement (SLA) tier parameter to requests, enabling the scheduler to optimize for mixed workloads. The scheduler will use this tier to influence queue ordering, batch formation, and preemption order, guaranteeing lower latency for interactive requests while maintaining high throughput for batch processing. The current scheduler excels at aggregate throughput but treats all requests equally within a policy (FCFS or priority integer). In production, clusters often serve mixed workloads: * **Interactive** (e.g., chat, API): Requires low, predictable latency (P99). * **Batch** (e.g., summarization, embeddings): Maximizes throughput, tolerant to higher latency. * **Background** (e.g., research): Lowest priority, can be preempted. Without differentiation, interactive requests can be queued behind large batch jobs, hurting quality of service. While separate engine instances guarantee isolation, they underutilize hardware. A tiered scheduler allows efficient co-location on the same hardware with predictable performance. ### Proposed Change. Introduce a request-level `sla_tier` parameter with three values: `"interac...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [RFC]: SLA-Tiered Scheduling for Latency/Throughput Optimization RFC;stale ### Motivation. #### **Summary** This RFC proposes adding a Service Level Agreement (SLA) tier parameter to requests, enabling the scheduler to...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: tch"` to `SamplingParams`. * Propagate this value to `Request`/`RequestMetadata` in the engine. * Support setting via the OpenAI-compatible API `extra_body` field. **2. Scheduler Modifications (`vllm/v1/core/sched/sched...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ads. The scheduler will use this tier to influence queue ordering, batch formation, and preemption order, guaranteeing lower latency for interactive requests while maintaining high throughput for batch processing. The c...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [RFC]: SLA-Tiered Scheduling for Latency/Throughput Optimization RFC;stale ### Motivation. #### **Summary** This RFC proposes adding a Service Level Agreement (SLA) tier parameter to requests, enabling the scheduler to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: es throughput, tolerant to higher latency. * **Background** (e.g., research): Lowest priority, can be preempted. Without differentiation, interactive requests can be queued behind large batch jobs, hurting quality of se...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
