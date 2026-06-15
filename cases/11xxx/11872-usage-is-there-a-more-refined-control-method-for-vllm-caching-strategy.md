# vllm-project/vllm#11872: [Usage]: Is there a more refined control method for VLLM caching strategy?

| 字段 | 值 |
| --- | --- |
| Issue | [#11872](https://github.com/vllm-project/vllm/issues/11872) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Is there a more refined control method for VLLM caching strategy?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I have a scenario: some requests have frequent and important content, and I want them to go through the cache every time, while others are only called occasionally (with a lot of content). I don't want them to go through the cache. Is there any way to control whether a certain request goes through the cache or not through certain parameters? Or is there a development plan in this area ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Is there a more refined control method for VLLM caching strategy? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I have a scenario: some req...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: you like to use vllm I have a scenario: some requests have frequent and important content, and I want them to go through the cache every time, while others are only called occasionally (with a lot of content). I don't w...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rea ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
