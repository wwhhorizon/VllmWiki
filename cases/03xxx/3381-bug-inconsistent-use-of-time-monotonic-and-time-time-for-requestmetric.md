# vllm-project/vllm#3381: [Bug] Inconsistent use of `time.monotonic()` and `time.time()` for `RequestMetrics`

| 字段 | 值 |
| --- | --- |
| Issue | [#3381](https://github.com/vllm-project/vllm/issues/3381) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug] Inconsistent use of `time.monotonic()` and `time.time()` for `RequestMetrics`

### Issue 正文摘录

It seems that some of the timestamps in `RequestMetrics` are populated using `time.monotonic()` and others are populated using `time.time()`, leading to inconsistent metrics. Here's an example of a real `RequestMetrics` object returned in a response with nonsensical results: ```python RequestMetrics( arrival_time=16092.64213226, last_token_time=16092.64213226, first_scheduled_time=1710345206.088379, first_token_time=1710345206.378028, time_in_queue=1710329113.4462466, finished_time=1710345213.7548933, ) ``` I would suggest picking one of `time.monotonic()` or `time.time()` and using that everywhere for consistency.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug] Inconsistent use of `time.monotonic()` and `time.time()` for `RequestMetrics` It seems that some of the timestamps in `RequestMetrics` are populated using `time.monotonic()` and others are populated using `time.ti...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
