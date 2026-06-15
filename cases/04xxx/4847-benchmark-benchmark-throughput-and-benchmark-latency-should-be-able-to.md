# vllm-project/vllm#4847: Benchmark: benchmark_throughput and benchmark_latency should be able to write output to JSON file. 

| 字段 | 值 |
| --- | --- |
| Issue | [#4847](https://github.com/vllm-project/vllm/issues/4847) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Benchmark: benchmark_throughput and benchmark_latency should be able to write output to JSON file. 

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Similar to `benchmarks/benchmark_serving.py`, the throughput and latency benchmark should be able to write their metrics to JSON file for result aggregated so we don't need to parse the log data. ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: Benchmark: benchmark_throughput and benchmark_latency should be able to write output to JSON file. feature request ### 🚀 The feature, motivation and pitch Similar to `benchmarks/benchmark_serving.py`, the throughput an
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: benchmark_latency should be able to write output to JSON file. feature request ### 🚀 The feature, motivation and pitch Similar to `benchmarks/benchmark_serving.py`, the throughput and latency benchmark should be able to...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
