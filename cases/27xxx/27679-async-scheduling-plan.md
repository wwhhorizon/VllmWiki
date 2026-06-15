# vllm-project/vllm#27679: Async Scheduling Plan

| 字段 | 值 |
| --- | --- |
| Issue | [#27679](https://github.com/vllm-project/vllm/issues/27679) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Async Scheduling Plan

### Issue 正文摘录

- [x] https://github.com/vllm-project/vllm/pull/27615 - [x] https://github.com/vllm-project/vllm/pull/27756 - [x] https://github.com/vllm-project/vllm/pull/26866 - [x] https://github.com/vllm-project/vllm/pull/27910 - [x] https://github.com/vllm-project/vllm/pull/27922 - [x] https://github.com/vllm-project/vllm/pull/27648 - [x] https://github.com/vllm-project/vllm/pull/28012 - perf fix for regression in `#26866` - [x] https://github.com/vllm-project/vllm/pull/28250 - [x] https://github.com/vllm-project/vllm/pull/28706 - [x] https://github.com/vllm-project/vllm/pull/28744 - [x] https://github.com/vllm-project/vllm/pull/28787 - [x] https://github.com/vllm-project/vllm/pull/24799 - [x] https://github.com/vllm-project/vllm/pull/29355 - [x] https://github.com/vllm-project/vllm/pull/29372 - [x] Address general duplicate request ids issue: - https://github.com/vllm-project/vllm/pull/27987 - [x] https://github.com/vllm-project/vllm/pull/31332 - [x] https://github.com/vllm-project/vllm/pull/31373 - [x] https://github.com/vllm-project/vllm/pull/27614 - [ ] Follow-on async scheduling + spec decode hardening/compatibility issues (in parallel) - [x] https://github.com/vllm-project/vllm/pull/29...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Async Scheduling Plan feature request - [x] https://github.com/vllm-project/vllm/pull/27615 - [x] https://github.com/vllm-project/vllm/pull/27756 - [x] https://github.com/vllm-project/vllm/pull/26866 - [x] https://githu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: 648 - [x] https://github.com/vllm-project/vllm/pull/28012 - perf fix for regression in `#26866` - [x] https://github.com/vllm-project/vllm/pull/28250 - [x] https://github.com/vllm-project/vllm/pull/28706 - [x] https://g...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
