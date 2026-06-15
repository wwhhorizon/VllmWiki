# vllm-project/vllm#22545: [Bug]: Stats don't update to zero when all requests are aborted

| 字段 | 值 |
| --- | --- |
| Issue | [#22545](https://github.com/vllm-project/vllm/issues/22545) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Stats don't update to zero when all requests are aborted

### Issue 正文摘录

### 🐛 Describe the bug After a load test where all requests are aborted, metrics/stats don't update back to zero: ``` DEBUG 08-07 15:35:23 [loggers.py:122] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 106 reqs, Waiting: 15 reqs, GPU KV cache usage: 90.4%, Prefix cache hit rate: 30.5% DEBUG 08-07 15:35:33 [loggers.py:122] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 106 reqs, Waiting: 15 reqs, GPU KV cache usage: 90.4%, Prefix cache hit rate: 30.5% DEBUG 08-07 15:35:43 [loggers.py:122] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 106 reqs, Waiting: 15 reqs, GPU KV cache usage: 90.4%, Prefix cache hit rate: 30.5% ```` Need to repro / confirm vLLM version. Reported by @dagrayvid.

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ation throughput: 0.0 tokens/s, Running: 106 reqs, Waiting: 15 reqs, GPU KV cache usage: 90.4%, Prefix cache hit rate: 30.5% DEBUG 08-07 15:35:33 [loggers.py:122] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg gen...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Stats don't update to zero when all requests are aborted bug ### 🐛 Describe the bug After a load test where all requests are aborted, metrics/stats don't update back to zero: ``` DEBUG 08-07 15:35:23 [loggers.py:...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: o when all requests are aborted bug ### 🐛 Describe the bug After a load test where all requests are aborted, metrics/stats don't update back to zero: ``` DEBUG 08-07 15:35:23 [loggers.py:122] Engine 000: Avg prompt thro...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: , Running: 106 reqs, Waiting: 15 reqs, GPU KV cache usage: 90.4%, Prefix cache hit rate: 30.5% DEBUG 08-07 15:35:33 [loggers.py:122] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 90.4%, Prefix cache hit rate: 30.5% ```` Need to repro / confirm vLLM version. Reported by @dagrayvid.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
