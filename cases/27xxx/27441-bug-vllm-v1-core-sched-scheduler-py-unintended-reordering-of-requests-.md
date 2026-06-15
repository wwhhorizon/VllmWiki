# vllm-project/vllm#27441: [Bug]: vllm/v1/core/sched/scheduler.py: Unintended reordering of requests during scheduling

| 字段 | 值 |
| --- | --- |
| Issue | [#27441](https://github.com/vllm-project/vllm/issues/27441) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm/v1/core/sched/scheduler.py: Unintended reordering of requests during scheduling

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Description The function `schedule()` in [vllm/v1/core/sched/scheduler.py](https://github.com/vllm-project/vllm/blob/main/vllm/v1/core/sched/scheduler.py) is responsible for scheduling inference requests. In certain cases — such as when a request is waiting for KV blocks from a remote prefill worker or when the token budget is exhausted — the request must be reinserted into the waiting queue `self.waiting`. Currently, the implementation pops such requests, prepends them to skipped_waiting_requests, and then prepends skipped_waiting_requests back to self.waiting. However, this behavior can shuffle the request order, potentially impacting the tail latency of request serving. ### How to Fix Replace all calls to `skipped_wating_requests.prepend_request(request)` with `skipped_wating_requests.add_request(request)` ### Result The figure compares the request-serving timelines of the original (left) and fixed (right) versions. * X-axis: Time * Y-axis: Request ID (submission order) * Green: Duration while the request is in `self.waiting` * Black: Time between GPU memory allocation and completion of the request’s prefill computation *...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: vllm/v1/core/sched/scheduler.py: Unintended reordering of requests during scheduling bug ### Your current environment ### 🐛 Describe the bug ### Description The function `schedule()` in [vllm/v1/core/sched/schedu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: s behavior can shuffle the request order, potentially impacting the tail latency of request serving. ### How to Fix Replace all calls to `skipped_wating_requests.prepend_request(request)` with `skipped_wating_requests.a...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: s the request-serving timelines of the original (left) and fixed (right) versions. * X-axis: Time * Y-axis: Request ID (submission order) * Green: Duration while the request is in `self.waiting` * Black: Time between GP...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: n: Duration while the request is in `self.waiting` * Black: Time between GPU memory allocation and completion of the request’s prefill computation * Red: Time between the end of prefill computation and GPU memory releas...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
