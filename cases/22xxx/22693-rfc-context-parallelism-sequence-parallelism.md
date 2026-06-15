# vllm-project/vllm#22693: [RFC]: Context Parallelism && Sequence Parallelism

| 字段 | 值 |
| --- | --- |
| Issue | [#22693](https://github.com/vllm-project/vllm/issues/22693) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Context Parallelism && Sequence Parallelism

### Issue 正文摘录

### Motivation. As large language models (LLMs) support increasingly longer token contexts, vLLM currently employs the chunkprefill mechanism to handle long sequences: long sequences are split into individual chunks, and ring_attention is called to compute the attention results. However, the implementation of chunkprefill has two issues: （1）Each chunk is computed serially, so a single request fails to fully leverage the advantages of concurrency in a multi-GPU environment; （2）Each GPU within the tensor parallelism (TP) domain stores identical KV caches (kvcache), leading to resource waste. To address the above issues, we aim to resolve them by introducing the CP function and enhancing the SP capability. As mentioned in the paper, [https://arxiv.org/pdf/2411.01783](https://arxiv.org/pdf/2411.01783),The advantages of Context parallel lie in: （1）Compute parallelization: **CP distributes computation across multiple GPUs in order to reduce latency**, in contrast with pipeline parallelization (PP) that improves throughput but not latency. （2）Communication message size reduction: Compared to tensor parallelism (TP), **CP demands less communication bandwidth in multi-host environments, by...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [RFC]: Context Parallelism && Sequence Parallelism RFC;stale ### Motivation. As large language models (LLMs) support increasingly longer token contexts, vLLM currently employs the chunkprefill mechanism to handle long s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [RFC]: Context Parallelism && Sequence Parallelism RFC;stale ### Motivation. As large language models (LLMs) support increasingly longer token contexts, vLLM currently employs the chunkprefill mechanism to handle long s...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: on: **CP distributes computation across multiple GPUs in order to reduce latency**, in contrast with pipeline parallelization (PP) that improves throughput but not latency. （2）Communication message size reduction: Compa...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ; （2）Each GPU within the tensor parallelism (TP) domain stores identical KV caches (kvcache), leading to resource waste. To address the above issues, we aim to resolve them by introducing the CP function and enhancing t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ce waste. To address the above issues, we aim to resolve them by introducing the CP function and enhancing the SP capability. As mentioned in the paper, [https://arxiv.org/pdf/2411.01783](https://arxiv.org/pdf/2411.0178...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
