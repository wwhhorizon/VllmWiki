# vllm-project/vllm#29928: [Bug]: Request Metrics Stale After Updating After Sudden Cancellation of All Running Reqs

| 字段 | 值 |
| --- | --- |
| Issue | [#29928](https://github.com/vllm-project/vllm/issues/29928) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Request Metrics Stale After Updating After Sudden Cancellation of All Running Reqs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug This is a bit of a contrived scenaro but occurs often in benchmarking. But it turns out that if all requests are simultaneously canceled, vllm does not refresh its prometheus stats until an engine core step runs again this is problematic because: - its common in cases like benchmarking to abruptly cut off requests - systems like llm-d rely on these prom metrics for scheduling decisions - pods with high load prior to the requests aborts can get "stuck" reporting 99% KV utilization, which will stop future scheduling to this pod - since requests never get sent to these pods, the metrics never reset and no load is scheduled to the pod we should actually ensure we flush the current scheduler state and avoid reporting these stale metrics Another idea: - we could trigger this with the health check, which should run a priority 0 forward pass ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Request Metrics Stale After Updating After Sudden Cancellation of All Running Reqs bug ### Your current environment ### 🐛 Describe the bug This is a bit of a contrived scenaro but occurs often in benchmarking. Bu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: scribe the bug This is a bit of a contrived scenaro but occurs often in benchmarking. But it turns out that if all requests are simultaneously canceled, vllm does not refresh its prometheus stats until an engine core st...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: equests - systems like llm-d rely on these prom metrics for scheduling decisions - pods with high load prior to the requests aborts can get "stuck" reporting 99% KV utilization, which will stop future scheduling to this...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ass ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
