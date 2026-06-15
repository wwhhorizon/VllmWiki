# vllm-project/vllm#1870: Add latency metrics

| 字段 | 值 |
| --- | --- |
| Issue | [#1870](https://github.com/vllm-project/vllm/issues/1870) |
| 状态 | closed |
| 标签 | help wanted;good first issue |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Add latency metrics

### Issue 正文摘录

After #1662 (initial metrics support) and #1756 (refactoring chat endpoint), it will become practical to include latency metrics that's important to production (courtesy of @Yard1): * histogram of time to first token, and gauge of the mean, in ms * histogram of inter-token latency, and gauge of the mean, in ms * histogram of e2e time per request, and gauge of the mean, in ms * gauge of mean tokens per s per request. we currently only track the prefill and generation throughput, no request level. A natural place to do it would be in the LLM engine or chat completion API, which ever one is less intrusive.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: -token latency, and gauge of the mean, in ms * histogram of e2e time per request, and gauge of the mean, in ms * gauge of mean tokens per s per request. we currently only track the prefill and generation throughput, no...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: Add latency metrics help wanted;good first issue After #1662 (initial metrics support) and #1756 (refactoring chat endpoint), it will become practical to include latency metrics that's important to production (courtesy...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: at endpoint), it will become practical to include latency metrics that's important to production (courtesy of @Yard1): * histogram of time to first token, and gauge of the mean, in ms * histogram of inter-token latency,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
