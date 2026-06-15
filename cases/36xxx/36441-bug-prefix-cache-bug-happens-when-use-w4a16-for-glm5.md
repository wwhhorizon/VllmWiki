# vllm-project/vllm#36441: [Bug]: prefix cache bug happens when use w4a16 for GLM5

| 字段 | 值 |
| --- | --- |
| Issue | [#36441](https://github.com/vllm-project/vllm/issues/36441) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: prefix cache bug happens when use w4a16 for GLM5

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug (APIServer pid=1) INFO 03-09 02:05:27 [v1/metrics/loggers.py:259] Engine 000: Avg prompt throughput: 2356.1 tokens/s, Avg generation throughput: 11.5 tokens/s, Running: 8 reqs, Waiting: 0 reqs, GPU KV cache usage: 45.7%, Prefix cache hit rate: 0.0% ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: prefix cache bug happens when use w4a16 for GLM5 bug ### Your current environment ### 🐛 Describe the bug (APIServer pid=1) INFO 03-09 02:05:27 [v1/metrics/loggers.py:259] Engine 000: Avg prompt throughput: 2356.1...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ) INFO 03-09 02:05:27 [v1/metrics/loggers.py:259] Engine 000: Avg prompt throughput: 2356.1 tokens/s, Avg generation throughput: 11.5 tokens/s, Running: 8 reqs, Waiting: 0 reqs, GPU KV cache usage: 45.7%, Prefix cache h...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: s/s, Running: 8 reqs, Waiting: 0 reqs, GPU KV cache usage: 45.7%, Prefix cache hit rate: 0.0% ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: .0% ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: 6.1 tokens/s, Avg generation throughput: 11.5 tokens/s, Running: 8 reqs, Waiting: 0 reqs, GPU KV cache usage: 45.7%, Prefix cache hit rate: 0.0% ### Before submitting a new issue... - [x] Make sure you already searched...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
