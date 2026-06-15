# vllm-project/vllm#5787: [Usage]: About the use of benchmark_latency.py

| 字段 | 值 |
| --- | --- |
| Issue | [#5787](https://github.com/vllm-project/vllm/issues/5787) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: About the use of benchmark_latency.py

### Issue 正文摘录

### How would you like to use vllm I tried to run benchmark_latency.py for profiling and collected a large JSON file (about GiB). After changing the iteration times from the default value (30) to a small number, I still found the JSON had a larger size. Such a large file is not convenient for analysis in chrome://tracing or similar tools. Could I get some suggestions from you to decrease the size of the JSON file? Or a tool recommended for analysis is welcomed as well. Thanks.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Usage]: About the use of benchmark_latency.py usage;stale ### How would you like to use vllm I tried to run benchmark_latency.py for profiling and collected a large JSON file (about GiB). After changing the iteration t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: er size. Such a large file is not convenient for analysis in chrome://tracing or similar tools. Could I get some suggestions from you to decrease the size of the JSON file? Or a tool recommended for analysis is welcomed...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: iB). After changing the iteration times from the default value (30) to a small number, I still found the JSON had a larger size. Such a large file is not convenient for analysis in chrome://tracing or similar tools. Cou...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: About the use of benchmark_latency.py usage;stale ### How would you like to use vllm I tried to run benchmark_latency.py for profiling and collected a large JSON file (about GiB). After changing the iteration t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
