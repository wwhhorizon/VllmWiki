# vllm-project/vllm#11945: [RFC]: Pipeline-Parallelism for vLLM V1

| 字段 | 值 |
| --- | --- |
| Issue | [#11945](https://github.com/vllm-project/vllm/issues/11945) |
| 状态 | closed |
| 标签 | RFC;stale;v1 |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Pipeline-Parallelism for vLLM V1

### Issue 正文摘录

### Motivation. This RFC describes the approach for supporting pipeline parallelism in [vLLM V1 architecture](https://github.com/vllm-project/vllm/issues/8779). Pipeline parallelism was [supported in V0 with the virtual-engine approach](https://github.com/vllm-project/vllm/issues/4461). In short, we create multiple virtual engines to match the number of pipeline stages, and each virtual engine has its own scheduler, block manager and cache engine, so that they can schedule multiple batches simultaneously to the same executor with pipeline parallelism, saturating all pipeline stages to improve the efficiency. However, virtual engine introduces the following drawbacks: 1. The lack of a centralized scheduler prevents global optimization from being applied. 2. It introduces complexity to the engine architecture and implementation. In this RFC, we aim to support pipeline parallelism in the V1 LLMEngineCore, with the following properties: - Good performance: throughput and TTFT - The design should minimize pipeline bubbles - KV-cache efficiency - The design should minimize KV-cache fragmentation - The design should facilitate KV-cache block reuse across different requests - The design s...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [RFC]: Pipeline-Parallelism for vLLM V1 RFC;stale;v1 ### Motivation. This RFC describes the approach for supporting pipeline parallelism in [vLLM V1 architecture](https://github.com/vllm-project/vllm/issues/8779). Pipel...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [RFC]: Pipeline-Parallelism for vLLM V1 RFC;stale;v1 ### Motivation. This RFC describes the approach for supporting pipeline parallelism in [vLLM V1 architecture](https://github.com/vllm-project/vllm/issues/8779). Pipel...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: e: throughput and TTFT - The design should minimize pipeline bubbles - KV-cache efficiency - The design should minimize KV-cache fragmentation - The design should facilitate KV-cache block reuse across different request...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: e V1 LLMEngineCore, with the following properties: - Good performance: throughput and TTFT - The design should minimize pipeline bubbles - KV-cache efficiency - The design should minimize KV-cache fragmentation - The de...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: pipeline parallelism, saturating all pipeline stages to improve the efficiency. However, virtual engine introduces the following drawbacks: 1. The lack of a centralized scheduler prevents global optimization from being...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
