# vllm-project/vllm#8762: [Usage]: how to acquire logits in vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#8762](https://github.com/vllm-project/vllm/issues/8762) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: how to acquire logits in vllm

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to acquire logits when I run benchmark_throughput.py to do the softmax optimization, but the output in vllm doesn't have logits, how can I acquire it. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ### How would you like to use vllm I want to acquire logits when I run benchmark_throughput.py to do the softmax optimization, but the output in vllm doesn't have logits, how can I acquire it. ### Before submitting a ne...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: it. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: how to acquire logits in vllm usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to acquire logits when I run benchmark_throughp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
