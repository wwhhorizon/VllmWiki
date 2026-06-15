# vllm-project/vllm#23820: [Bug]: Incorrect output throughput calculation for concurrent requests in benchmark_serving.py

| 字段 | 值 |
| --- | --- |
| Issue | [#23820](https://github.com/vllm-project/vllm/issues/23820) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Incorrect output throughput calculation for concurrent requests in benchmark_serving.py

### Issue 正文摘录

## Problem The current output throughput calculation in `benchmarks/benchmark_serving.py` is incorrect: ```python # Current implementation (around line 197) output_throughput = sum(actual_output_lens) / dur_s ``` **Issue**: `dur_s` includes prompt processing time (TTFT), but we're only measuring output tokens. This gives incorrectly low throughput values. ## Fix Output throughput should only measure token generation time: ```python # Correct calculation output_throughput = sum(actual_output_lens) / (dur_s - max(ttfts)) ``` ## Additional Enhancement Add missing prompt processing throughput metric: ```python prompt_throughput = total_input / max(ttfts) ``` ## Impact - Current metrics are misleading for performance evaluation - Makes model/configuration comparisons unreliable - Missing key prefill performance metric ## Environment - File: `benchmarks/benchmark_serving.py` - Affects all models and backends vLLM version: main or latest

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Bug]: Incorrect output throughput calculation for concurrent requests in benchmark_serving.py bug;stale ## Problem The current output throughput calculation in `benchmarks/benchmark_serving.py` is incorrect: ```python...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Incorrect output throughput calculation for concurrent requests in benchmark_serving.py bug;stale ## Problem The current output throughput calculation in `benchmarks/benchmark_serving.py` is incorrect: ```python...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: act - Current metrics are misleading for performance evaluation - Makes model/configuration comparisons unreliable - Missing key prefill performance metric ## Environment - File: `benchmarks/benchmark_serving.py` - Affe...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nment - File: `benchmarks/benchmark_serving.py` - Affects all models and backends vLLM version: main or latest
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: benchmarks/benchmark_serving.py` - Affects all models and backends vLLM version: main or latest

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
