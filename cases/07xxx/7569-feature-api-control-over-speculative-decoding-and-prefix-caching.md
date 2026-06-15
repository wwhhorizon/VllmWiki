# vllm-project/vllm#7569: [Feature]: API control over speculative decoding and prefix caching

| 字段 | 值 |
| --- | --- |
| Issue | [#7569](https://github.com/vllm-project/vllm/issues/7569) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: API control over speculative decoding and prefix caching

### Issue 正文摘录

### 🚀 The feature, motivation and pitch speculative decoding can only be enabled at startup, but incurs a loss compared to normal decoding. So it would be useful if can control at runtime. ### Alternatives Restart vllm for each mode and test for each case. Very challenging for 405B etc. and leads to downtimes. ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: API control over speculative decoding and prefix caching feature request;stale ### 🚀 The feature, motivation and pitch speculative decoding can only be enabled at startup, but incurs a loss compared to normal...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: an control at runtime. ### Alternatives Restart vllm for each mode and test for each case. Very challenging for 405B etc. and leads to downtimes. ### Additional context _No response_

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
