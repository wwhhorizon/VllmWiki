# vllm-project/vllm#16982: [Bug]: Is the logic order correct during the scheduler procedure?

| 字段 | 值 |
| --- | --- |
| Issue | [#16982](https://github.com/vllm-project/vllm/issues/16982) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Is the logic order correct during the scheduler procedure?

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi @WoosukKwon, is the order of these two lines of code correct? Why is `self.append(request)` called before updating the request attribute in the update section during the scheduling? ``` def schedule(self) -> SchedulerOutput: ...... self.running.append(request) ..... ..... request.num_computed_tokens = num_computed_tokens ``` [https://github.com/vllm-project/vllm/blame/0e237f00357c968a4f7ae25accd533e924baceff/vllm/v1/core/sched/scheduler.py#L384](url) [https://github.com/vllm-project/vllm/blame/0e237f00357c968a4f7ae25accd533e924baceff/vllm/v1/core/sched/scheduler.py#L405C3-L405C3](url) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Is the logic order correct during the scheduler procedure? bug;stale ### Your current environment ### 🐛 Describe the bug Hi @WoosukKwon, is the order of these two lines of code correct? Why is `self.append(reques...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rl) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
