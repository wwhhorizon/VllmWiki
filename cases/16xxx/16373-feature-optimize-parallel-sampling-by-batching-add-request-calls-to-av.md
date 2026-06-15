# vllm-project/vllm#16373: [Feature]: Optimize parallel sampling by batching add_request calls to avoid split scheduling latency

| 字段 | 值 |
| --- | --- |
| Issue | [#16373](https://github.com/vllm-project/vllm/issues/16373) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Optimize parallel sampling by batching add_request calls to avoid split scheduling latency

### Issue 正文摘录

## Issue Currently, when using n > 1 for parallel sampling in AsyncLLM, each of the child requests is sent individually to the EngineCore via add_request_async. This results in the first request being processed immediately (if the engine is idle), while subsequent requests get scheduled in the next step. This introduces a consistent latency of one scheduling cycle due to split scheduling between the first and second scheduling steps. ## Proposal: Introduce a new method such as batched_add_request that sends all n requests in a single ZMQ message to the EngineCore. This would allow the engine to prefill and schedule all parallel samples simultaneously, eliminating the extra latency caused by staggered request insertion. ## Additional context This behavior stems from the design where each sample is added sequentially rather than as a batch. As a result, the first token of the first request is typically scheduled and runs immediately, while the rest lag by a full scheduling cycle. External [slack convo](https://vllm-dev.slack.com/archives/C07QP347J4D/p1744244221904719) with additional context. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issu...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Optimize parallel sampling by batching add_request calls to avoid split scheduling latency feature request;stale ## Issue Currently, when using n > 1 for parallel sampling in AsyncLLM, each of the child reque...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: arallel sampling by batching add_request calls to avoid split scheduling latency feature request;stale ## Issue Currently, when using n > 1 for parallel sampling in AsyncLLM, each of the child requests is sent individua...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ull scheduling cycle. External [slack convo](https://vllm-dev.slack.com/archives/C07QP347J4D/p1744244221904719) with additional context. ### Before submitting a new issue... - [x] Make sure you already searched for rele...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
