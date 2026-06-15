# vllm-project/vllm#37842: _update_request_as_session does not update max_tokens from StreamingUpdate

| 字段 | 值 |
| --- | --- |
| Issue | [#37842](https://github.com/vllm-project/vllm/issues/37842) |
| 状态 | open |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> _update_request_as_session does not update max_tokens from StreamingUpdate

### Issue 正文摘录

## Bug Description In `_update_request_as_session` (`vllm/v1/core/sched/scheduler.py`), the method updates `sampling_params` and `arrival_time` from the `StreamingUpdate`, but does not update `session.max_tokens`. The `StreamingUpdate` dataclass carries a `max_tokens` field (`vllm/v1/request.py`, line 41), but this value is silently discarded. ## Affected Code ```python # scheduler.py, _update_request_as_session session.arrival_time = update.arrival_time session.sampling_params = update.sampling_params # max_tokens is not updated from update.max_tokens ``` ## Impact In streaming sessions where subsequent chunks specify a different `max_tokens`, the request always uses the initial chunk's value. The stop condition in `check_stop()` (`request.num_output_tokens >= request.max_tokens`) uses a stale value, causing: - Too few tokens generated if the user increases `max_tokens` in a subsequent chunk - Too many tokens generated if the user decreases it ## Fix Add `session.max_tokens = update.max_tokens` after the `sampling_params` update.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: _update_request_as_session does not update max_tokens from StreamingUpdate ## Bug Description In `_update_request_as_session` (`vllm/v1/core/sched/scheduler.py`), the method updates `sampling_params` and `arrival_time`...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: _tokens ``` ## Impact In streaming sessions where subsequent chunks specify a different `max_tokens`, the request always uses the initial chunk's value. The stop condition in `check_stop()` (`request.num_output_tokens >...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
