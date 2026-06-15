# vllm-project/vllm#24484: [RFC]: Enhancing the Pluggable Scheduler with a Workload-Aware Adaptive Policy

| 字段 | 值 |
| --- | --- |
| Issue | [#24484](https://github.com/vllm-project/vllm/issues/24484) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Enhancing the Pluggable Scheduler with a Workload-Aware Adaptive Policy

### Issue 正文摘录

### Motivation. Hi vLLm community and maintainers First, a huge thanks to the team for the excellent work on the pluggable interfaces in the vLLm engine. The ability to experiment with core components like the scheduler is a powerful feature that opens the door to significant performance optimizations for a wide range of use cases. To help explore and demonstrate the full potential of this interface, we have been developing a new, alternative scheduling policy internally. ### **The Challenge: Optimizing for Mixed Workloads** A common production scenario for LLM serving involves handling a mix of request types on the same infrastructure. For example, serving both low-latency, short-prompt "interactive" tasks (like chatbots) alongside high-throughput, long-prompt "batch" tasks (like document analysis). In this environment, a standard FCFS policy can create a trade-off: you can either have high latency for your interactive users or lower overall system throughput. It's like a supermarket checkout: when a "full cart" (long job) gets in line, all the "single item" (short job) customers behind it experience a long wait. ### **A Path Forward: Adaptive, Workload-Aware Scheduling** We beli...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [RFC]: Enhancing the Pluggable Scheduler with a Workload-Aware Adaptive Policy RFC;stale ### Motivation. Hi vLLm community and maintainers First, a huge thanks to the team for the excellent work on the pluggable interfa...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: request types on the same infrastructure. For example, serving both low-latency, short-prompt "interactive" tasks (like chatbots) alongside high-throughput, long-prompt "batch" tasks (like document analysis). In this en...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: the letter/emoji!) a) The current FCFS is fine, keep it simple. b) A smarter, adaptive scheduler like the one we're proposing. c) A fully pluggable interface so I can write my own custom scheduler. d) Something else? (L...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [RFC]: Enhancing the Pluggable Scheduler with a Workload-Aware Adaptive Policy RFC;stale ### Motivation. Hi vLLm community and maintainers First, a huge thanks to the team for the excellent work on the pluggable interfa...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ggable interface so I can write my own custom scheduler. d) Something else? (Let us know!) 3. Is anyone else actively researching LLM scheduling policies? We'd love to connect and compare notes. ### Feedback Period. 2-4...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
