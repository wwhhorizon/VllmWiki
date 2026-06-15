# vllm-project/vllm#30383: [RFC]: Multi-Process Benchmark Architecture for Scaling Beyond Single-Core Limits

| 字段 | 值 |
| --- | --- |
| Issue | [#30383](https://github.com/vllm-project/vllm/issues/30383) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Multi-Process Benchmark Architecture for Scaling Beyond Single-Core Limits

### Issue 正文摘录

### Motivation. The current `vllm benchmark` tool relies on a **single-core, single-process** load generator. Under moderate or high request rates or high concurrency levels, the benchmark becomes limited by the CPU capacity of that single core. The overhead of coroutine scheduling prevents the client from: 1. **Sending requests at the configured request rate**, and 2. **Consuming server-side streaming chunks in real time**. As a result, the observed metrics deviate significantly from the actual behavior of the target service. This reduces benchmark reliability and makes it difficult to evaluate scenarios where models or serving systems are optimized for **high-concurrency** or **dense request** workloads. In these cases, the benchmark fails to reflect the true performance characteristics of the service. For example, I created a synthetic service using gunicorn with a fixed **TTFT = 100 ms** and **TPOT = 10 ms**. When running: ``` vllm bench serve --base-url http://127.0.0.1:8080 --model deepseek-ai/DeepSeek-R1 ``` (without specifying a `--request-rate`, i.e., effectively `inf`), both TTFT and TPOT became **significantly distorted**. When specifying `--request-rate 100`, the metri...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 7: [RFC]: Multi-Process Benchmark Architecture for Scaling Beyond Single-Core Limits RFC ### Motivation. The current `vllm benchmark` tool relies on a **single-core, single-process** load generator. Under moderate or high...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: or high concurrency levels, the benchmark becomes limited by the CPU capacity of that single core. The overhead of coroutine scheduling prevents the client from: 1. **Sending requests at the configured request rate**, a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [RFC]: Multi-Process Benchmark Architecture for Scaling Beyond Single-Core Limits RFC ### Motivation. The current `vllm benchmark` tool relies on a **single-core, single-process** load generator. Under moderate or high...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: rkDataset` output will be preloaded into shared memory. Only lightweight metadata (e.g., starting offset and length) will be passed to each worker. When generating a request, a worker retrieves the metadata and reconstr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: utine scheduling prevents the client from: 1. **Sending requests at the configured request rate**, and 2. **Consuming server-side streaming chunks in real time**. As a result, the observed metrics deviate significantly...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
