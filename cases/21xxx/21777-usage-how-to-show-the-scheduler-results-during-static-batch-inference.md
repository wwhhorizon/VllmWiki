# vllm-project/vllm#21777: [Usage]: how to show the scheduler results during static batch inference

| 字段 | 值 |
| --- | --- |
| Issue | [#21777](https://github.com/vllm-project/vllm/issues/21777) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: how to show the scheduler results during static batch inference

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I'm trying to run experiments with static-batch inference and wanted to inspect the scheduler’s result on every step by print or logging. However, any log statements I added inside the corresponding methods of the LLM-Engine class never appear. After digging around, it seems the LLMEngine is executed in a multiprocessing method, but I haven’t found a clean way to work around this yet. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: how to show the scheduler results during static batch inference usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I'm trying to run ex...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: et. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
