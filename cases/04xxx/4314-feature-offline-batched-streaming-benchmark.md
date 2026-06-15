# vllm-project/vllm#4314: [Feature]: Offline Batched Streaming Benchmark

| 字段 | 值 |
| --- | --- |
| Issue | [#4314](https://github.com/vllm-project/vllm/issues/4314) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Offline Batched Streaming Benchmark

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hi, I want to benchmark some models' performance using vllm. I want to use the offline Engine to do batch(given a fixed batch size input) and streaming inference so that i can get time to first token and total generation time. Seems the current AsyncEngine doesn't support this? ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Offline Batched Streaming Benchmark feature request;stale ### 🚀 The feature, motivation and pitch Hi, I want to benchmark some models' performance using vllm. I want to use the offline Engine to do batch(give...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: le ### 🚀 The feature, motivation and pitch Hi, I want to benchmark some models' performance using vllm. I want to use the offline Engine to do batch(given a fixed batch size input) and streaming inference so that i can...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Feature]: Offline Batched Streaming Benchmark feature request;stale ### 🚀 The feature, motivation and pitch Hi, I want to benchmark some models' performance using vllm. I want to use the offline Engine to do batch(give...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
