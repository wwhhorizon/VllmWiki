# vllm-project/vllm#21027: [Performance]: The GPU memory usage of vllm v0.9.2 is significantly higher than that of v0.9.1. Why is this? How can it be improved?

| 字段 | 值 |
| --- | --- |
| Issue | [#21027](https://github.com/vllm-project/vllm/issues/21027) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: The GPU memory usage of vllm v0.9.2 is significantly higher than that of v0.9.1. Why is this? How can it be improved?

### Issue 正文摘录

### Proposal to improve performance The GPU memory usage of vllm v0.9.2 is significantly higher than that of v0.9.1. Why is this? How can it be improved? ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: v0.9.1. Why is this? How can it be improved? ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The ou...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Performance]: The GPU memory usage of vllm v0.9.2 is significantly higher than that of v0.9.1. Why is this? How can it be improved? performance;stale ### Proposal to improve performance The GPU memory usage of vllm v0....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: er than that of v0.9.1. Why is this? How can it be improved? performance;stale ### Proposal to improve performance The GPU memory usage of vllm v0.9.2 is significantly higher than that of v0.9.1. Why is this? How can it...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
