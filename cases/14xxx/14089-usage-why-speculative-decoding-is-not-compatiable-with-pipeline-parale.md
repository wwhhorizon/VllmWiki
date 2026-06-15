# vllm-project/vllm#14089: [Usage]: Why Speculative decoding is not compatiable with Pipeline Paralelism?

| 字段 | 值 |
| --- | --- |
| Issue | [#14089](https://github.com/vllm-project/vllm/issues/14089) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Why Speculative decoding is not compatiable with Pipeline Paralelism?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Why Speculative decoding is not compatiable with Pipeline Paralelism? Any docs or design ? I want to run R1 with both PP and MTP. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: sage]: Why Speculative decoding is not compatiable with Pipeline Paralelism? usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Why Speculative decodi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Why Speculative decoding is not compatiable with Pipeline Paralelism? usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Why Speculative deco...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
