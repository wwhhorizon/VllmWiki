# vllm-project/vllm#22130: Feature: Lightweight Performance Regression Detection Script

| 字段 | 值 |
| --- | --- |
| Issue | [#22130](https://github.com/vllm-project/vllm/issues/22130) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Feature: Lightweight Performance Regression Detection Script

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hi all, opening this to explore whether a lightweight regression detection tool would be useful for the vLLM ecosystem. 🔍 Problem While .buildkite/scripts/run-benchmarks.sh runs key benchmarks (e.g., benchmark_throughput.py, benchmark_latency.py), it appears to operate on a single SHA without tracking historical trends or flagging regressions over time. 💡 Proposal Introduce a lightweight script that: • Runs benchmarks nightly on selected models • Compares FLOPs, QPS, latency against a previous SHA or rolling baseline • Flags potential performance regressions explicitly • Optionally logs metrics over time or emits perf hints (e.g., for dashboards) This could help surface regressions earlier in dev cycles, especially as scheduler/engine changes evolve rapidly. 📎 Related • [#20336](https://github.com/vllm-project/vllm/issues/20336): Debugging tool for perf profiling and numerics Happy to prototype if there's interest! cc @DarkLight1337 @Isotr0py

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: Feature: Lightweight Performance Regression Detection Script feature request;stale ### 🚀 The feature, motivation and pitch Hi all, opening this to explore whether a lightweight regression detection tool would be useful...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Feature: Lightweight Performance Regression Detection Script feature request;stale ### 🚀 The feature, motivation and pitch Hi all, opening this to explore whether a lightweight regression detection tool would be useful...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: etection tool would be useful for the vLLM ecosystem. 🔍 Problem While .buildkite/scripts/run-benchmarks.sh runs key benchmarks (e.g., benchmark_throughput.py, benchmark_latency.py), it appears to operate on a single SHA...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: m/vllm-project/vllm/issues/20336): Debugging tool for perf profiling and numerics Happy to prototype if there's interest! cc @DarkLight1337 @Isotr0py
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: roduce a lightweight script that: • Runs benchmarks nightly on selected models • Compares FLOPs, QPS, latency against a previous SHA or rolling baseline • Flags potential performance regressions explicitly • Optionally...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
