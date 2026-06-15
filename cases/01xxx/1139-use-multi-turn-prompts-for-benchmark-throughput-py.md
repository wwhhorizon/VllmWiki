# vllm-project/vllm#1139: Use multi-turn prompts for benchmark_throughput.py

| 字段 | 值 |
| --- | --- |
| Issue | [#1139](https://github.com/vllm-project/vllm/issues/1139) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Use multi-turn prompts for benchmark_throughput.py

### Issue 正文摘录

Do we consider using multi-turn prompts instead of the first turn for throughput benchmarking? It would be more realistic.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: Use multi-turn prompts for benchmark_throughput.py stale Do we consider using multi-turn prompts instead of the first turn for throughput benchmarking? It would be more realistic.
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Use multi-turn prompts for benchmark_throughput.py stale Do we consider using multi-turn prompts instead of the first turn for throughput benchmarking? It would be more realistic.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
