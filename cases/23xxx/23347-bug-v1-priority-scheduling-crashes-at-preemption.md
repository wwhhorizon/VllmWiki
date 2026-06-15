# vllm-project/vllm#23347: [Bug]: V1 priority scheduling crashes at preemption

| 字段 | 值 |
| --- | --- |
| Issue | [#23347](https://github.com/vllm-project/vllm/issues/23347) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: V1 priority scheduling crashes at preemption

### Issue 正文摘录

### Your current environment N/A ### 🐛 Describe the bug While running a V1 server with `--scheduling-policy priority`, I sometimes run into this error, causing the server to crash: (I've edited the code to give a better assertion error message) ``` # Since some requests in the RUNNING queue may not be scheduled in # this step, the total number of scheduled requests can be smaller than # len(self.running). > assert (len(scheduled_new_reqs) + len(scheduled_resumed_reqs) + len(scheduled_running_reqs) " f"running: {len(self.running)}") E AssertionError: scheduled_new_reqs: 0 + scheduled_resumed_reqs: 0 + scheduled_running_reqs: 2 > running: 1 ../vllm-internal/vllm/v1/core/sched/scheduler.py:558: AssertionError ``` I've provided a repro here: https://github.com/vllm-project/vllm/pull/23346 The root cause seems to be that while scheduling running requests, requests are processed by the order of priority, so it's possible to schedule a request, then later be preempted by another request within the same scheduling cycle. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentati...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: code to give a better assertion error message) ``` # Since some requests in the RUNNING queue may not be scheduled in # this step, the total number of scheduled requests can be smaller than # len(self.running). > assert...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ed in # this step, the total number of scheduled requests can be smaller than # len(self.running). > assert (len(scheduled_new_reqs) + len(scheduled_resumed_reqs) + len(scheduled_running_reqs) " f"running: {len(self.run...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. cc @amitm02 @aarnphm @WoosukKwon

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
