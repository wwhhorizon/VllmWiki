# vllm-project/vllm#6077: [RFC]: Priority Scheduling

| 字段 | 值 |
| --- | --- |
| Issue | [#6077](https://github.com/vllm-project/vllm/issues/6077) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 20; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Priority Scheduling

### Issue 正文摘录

### Motivation. vLLM supports first-come-first-served scheduling based on the arrival time of requests. A prioritization mechanism that enables certain requests to be given higher preference in scheduling is useful because it can enable: 1. Batch and interactive requests co-location: Batch and interactive requests can be served on the same vLLM instance. If interactive requests arrive while batch requests are executing, they preempt the batch requests for immediate execution. Once the interactive requests are completed, the batch request can resume. If the KV cache for batch requests is preserved, disruption to the overall throughput can be minimized. 2. Maintain fairness between multiple interactive requests: Recent papers (such as [Andes](https://arxiv.org/abs/2404.16283), [VTC](https://arxiv.org/abs/2401.00588), and [QLM](https://arxiv.org/abs/2407.00047)) have proposed mechanisms to maintain fairness between multiple executing requests (for e.g. by maintaining inter-token latency). Most of these mechanisms can be implemented by dynamically changing priority of requests in the waiting and running queue of vLLM. ### Proposed Change. vLLM already has a pluggable scheduling policy...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: supports first-come-first-served scheduling based on the arrival time of requests. A prioritization mechanism that enables certain requests to be given higher preference in scheduling is useful because it can enable: 1....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: e sequence group: This priority can be static or dynamic based on the specific scheduling policy. 2. Waiting queue sorting based on priority: Currently, only the running queue is sorted based on the scheduling policy, a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: the KV cache for batch requests is preserved, disruption to the overall throughput can be minimized. 2. Maintain fairness between multiple interactive requests: Recent papers (such as [Andes](https://arxiv.org/abs/2404....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: heduling based on the arrival time of requests. A prioritization mechanism that enables certain requests to be given higher preference in scheduling is useful because it can enable: 1. Batch and interactive requests co-...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: interactive requests are completed, the batch request can resume. If the KV cache for batch requests is preserved, disruption to the overall throughput can be minimized. 2. Maintain fairness between multiple interactive...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
