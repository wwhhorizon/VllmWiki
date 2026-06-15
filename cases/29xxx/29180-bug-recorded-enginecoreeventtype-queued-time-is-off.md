# vllm-project/vllm#29180: [Bug]: Recorded `EngineCoreEventType.QUEUED` time is off

| 字段 | 值 |
| --- | --- |
| Issue | [#29180](https://github.com/vllm-project/vllm/issues/29180) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Recorded `EngineCoreEventType.QUEUED` time is off

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running benchmarking with the CLI: - on one side the serving point `vllm serve ...` - on the other side the benchmarking client : `vllm bench serve...` (note that the two are running on the same machine, there is no networking delay) I noticed that the `EngineCoreEventType.QUEUED` event recorder on the server side didn't match the time of posting the request. In my understanding these two should events should be approximately equivalent. These values aren't off by a few milliseconds, but here the mismatch can be pretty big, up to a few seconds. I think the reason might be because adding [request to the scheduler](https://github.com/vllm-project/vllm/blob/fcb1d570bb8f95f5b7ded716a52fec902c535f0e/vllm/v1/core/sched/scheduler.py#L1166) cannot be done when the engine is running a decoding or a prefill, see the [`_process_input_queue` function](https://github.com/vllm-project/vllm/blob/fcb1d570bb8f95f5b7ded716a52fec902c535f0e/vllm/v1/engine/core.py#L801), where `add_request()` ultimately gets called. This can introduce delays before the queued event gets recorded, having "floating" requests that are not tracked in the logs. ### B...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Recorded `EngineCoreEventType.QUEUED` time is off bug ### Your current environment ### 🐛 Describe the bug When running benchmarking with the CLI: - on one side the serving point `vllm serve ...` - on the other si...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: quivalent. These values aren't off by a few milliseconds, but here the mismatch can be pretty big, up to a few seconds. I think the reason might be because adding [request to the scheduler](https://github.com/vllm-proje...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ug ### Your current environment ### 🐛 Describe the bug When running benchmarking with the CLI: - on one side the serving point `vllm serve ...` - on the other side the benchmarking client : `vllm bench serve...` (note t...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: equivalent. These values aren't off by a few milliseconds, but here the mismatch can be pretty big, up to a few seconds. I think the reason might be because adding [request to the scheduler](https://github.com/vllm-proj...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
