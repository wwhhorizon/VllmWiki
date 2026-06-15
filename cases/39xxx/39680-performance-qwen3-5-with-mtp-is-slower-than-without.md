# vllm-project/vllm#39680: [Performance]: Qwen3.5 with mtp is slower than without

| 字段 | 值 |
| --- | --- |
| Issue | [#39680](https://github.com/vllm-project/vllm/issues/39680) |
| 状态 | open |
| 标签 | performance |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Qwen3.5 with mtp is slower than without

### Issue 正文摘录

### Proposal to improve performance In Qwen3.5-0.8B, Whether under single-threaded or high-concurrency loads, enabling MTP results in degraded latency. without mtp (APIServer pid=1422509) INFO 04-09 11:27:10 [loggers.py:259] Engine 000: Avg prompt throughput: 967.2 tokens/s, Avg generation throughput: 342.2 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.1%, Prefix cache hit rate: 44.5%, MM cache hit rate: 16.7% with mtp (APIServer pid=1409788) INFO 04-09 11:17:53 [loggers.py:259] Engine 000: Avg prompt throughput: 1357.9 tokens/s, Avg generation throughput: 128.3 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.2%, Prefix cache hit rate: 22.3%, MM cache hit rate: 6.5% (APIServer pid=1409788) INFO 04-09 11:17:53 [metrics.py:101] SpecDecoding metrics: Mean acceptance length: 1.97, Accepted throughput: 63.00 tokens/s, Drafted throughput: 65.20 tokens/s, Accepted: 630 tokens, Drafted: 652 tokens, Per-position acceptance rate: 0.966, Avg Draft acceptance rate: 96.6% Please Help! ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The ou...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: gle-threaded or high-concurrency loads, enabling MTP results in degraded latency. without mtp (APIServer pid=1422509) INFO 04-09 11:27:10 [loggers.py:259] Engine 000: Avg prompt throughput: 967.2 tokens/s, Avg generatio...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ration throughput: 342.2 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.1%, Prefix cache hit rate: 44.5%, MM cache hit rate: 16.7% with mtp (APIServer pid=1409788) INFO 04-09 11:17:53 [loggers.py:259]...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: .2 tokens/s, Avg generation throughput: 342.2 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.1%, Prefix cache hit rate: 44.5%, MM cache hit rate: 16.7% with mtp (APIServer pid=1409788) INFO 04-09 11:1...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ns/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.1%, Prefix cache hit rate: 44.5%, MM cache hit rate: 16.7% with mtp (APIServer pid=1409788) INFO 04-09 11:17:53 [loggers.py:259] Engine 000: Avg prompt throu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
