# vllm-project/vllm#11747: [Misc]: why there two multi_gpu_barrier in cross_device_reduce_1stage?

| 字段 | 值 |
| --- | --- |
| Issue | [#11747](https://github.com/vllm-project/vllm/issues/11747) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: why there two multi_gpu_barrier in cross_device_reduce_1stage?

### Issue 正文摘录

### Anything you want to discuss about vllm. i think only one multi_gpu_barrier is need for cross_device_reduce_1stage. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ge. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Misc]: why there two multi_gpu_barrier in cross_device_reduce_1stage? stale ### Anything you want to discuss about vllm. i think only one multi_gpu_barrier is need for cross_device_reduce_1stage. ### Before submitting...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
