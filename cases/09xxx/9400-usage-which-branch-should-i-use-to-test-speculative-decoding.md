# vllm-project/vllm#9400: [Usage]: Which branch should I use to test speculative decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#9400](https://github.com/vllm-project/vllm/issues/9400) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Which branch should I use to test speculative decoding

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Which branch should I use to test speculative decoding, and which branch currently has the best optimizations for speculative decoding? Is it the main branch? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Which branch should I use to test speculative decoding usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Which branch should I use to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ch? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Usage]: Which branch should I use to test speculative decoding usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Which branch should I use to...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
