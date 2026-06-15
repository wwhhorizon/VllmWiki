# vllm-project/vllm#7586: [Feature]: Benchmark script with speculative decode metrics

| 字段 | 值 |
| --- | --- |
| Issue | [#7586](https://github.com/vllm-project/vllm/issues/7586) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Benchmark script with speculative decode metrics

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I am looking to assess the performance of vllm for speculative decode, but I have been unable to find an offline benchmark script similar to [benchmark_latency.py](https://github.com/vllm-project/vllm/blob/main/benchmarks/benchmark_latency.py) that would allow me to test speculative decode performance. While I can use [benchmark_latency.py](https://github.com/vllm-project/vllm/blob/main/benchmarks/benchmark_latency.py) to obtain e2e latency, it does not provide all of the spec-decode metrics such as the time spent on scoring, verifying, and proposing, as well as the acceptance rate. Thanks to @cadedaniel's excellent contributions such as https://github.com/vllm-project/vllm/pull/6963 and https://github.com/vllm-project/vllm/pull/3103, we are now able to display spec-decode metrics, including scoring time, verification time, proposal time, and acceptance rate, in the server logging. However, these metrics can only be viewed in online server logs and are implemented through an asynchronous collector, which could result in inaccuracies. I am considering adding a script called 'benchmark_spec_decode.py' for spec-decode benchmarking in order to c...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Feature]: Benchmark script with speculative decode metrics feature request;stale ### 🚀 The feature, motivation and pitch I am looking to assess the performance of vllm for speculative decode, but I have been unable to...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Feature]: Benchmark script with speculative decode metrics feature request;stale ### 🚀 The feature, motivation and pitch I am looking to assess the performance of vllm for speculative decode, but I have been unable to...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: emented through an asynchronous collector, which could result in inaccuracies. I am considering adding a script called 'benchmark_spec_decode.py' for spec-decode benchmarking in order to capture more spec-decode-related...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
