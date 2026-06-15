# vllm-project/vllm#15091: [Misc]: Why not sort the waiting queue before popleft waiting queue?

| 字段 | 值 |
| --- | --- |
| Issue | [#15091](https://github.com/vllm-project/vllm/issues/15091) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Why not sort the waiting queue before popleft waiting queue?

### Issue 正文摘录

### Anything you want to discuss about vllm. The current logic is to popleft the seq in the waiting queue first, then compare it with the lowest priority seq in the running queue. https://github.com/vllm-project/vllm/blob/437f9162d0eacf5b3f179c864c9664dfc8a020ff/vllm/core/scheduler.py#L988-L997 However, the step of sorting the waiting queue is placed later. https://github.com/vllm-project/vllm/blob/437f9162d0eacf5b3f179c864c9664dfc8a020ff/vllm/core/scheduler.py#L1026 Shouldn't the waiting queue be sorted first then popleft? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Misc]: Why not sort the waiting queue before popleft waiting queue? stale ### Anything you want to discuss about vllm. The current logic is to popleft the seq in the waiting queue first, then compare it with the lowest...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ft? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
