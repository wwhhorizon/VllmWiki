# vllm-project/vllm#15600: [V1] [Performance Benchmark] Benchmark the performance of Speculative Decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#15600](https://github.com/vllm-project/vllm/issues/15600) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [V1] [Performance Benchmark] Benchmark the performance of Speculative Decoding

### Issue 正文摘录

1. Let's start with ngram, can you collect both latency and throughput numbers on ShareGPT dataset on H100 and one low end GPU? 2. If the numbers from 1 is not expected, could you run some profiling to understand the performance bottleneck. 3. Get more performance numbers on other datasets.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [V1] [Performance Benchmark] Benchmark the performance of Speculative Decoding stale 1. Let's start with ngram, can you collect both latency and throughput numbers on ShareGPT dataset on H100 and one low end GPU? 2. If...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [V1] [Performance Benchmark] Benchmark the performance of Speculative Decoding stale 1. Let's start with ngram, can you collect both latency and throughput numbers on ShareGPT dataset on H100 and one low end GPU? 2. If...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: n you collect both latency and throughput numbers on ShareGPT dataset on H100 and one low end GPU? 2. If the numbers from 1 is not expected, could you run some profiling to understand the performance bottleneck. 3. Get...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
