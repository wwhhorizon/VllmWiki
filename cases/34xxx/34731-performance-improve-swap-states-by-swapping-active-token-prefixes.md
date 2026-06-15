# vllm-project/vllm#34731: [Performance]: Improve swap_states by swapping active token prefixes

| 字段 | 值 |
| --- | --- |
| Issue | [#34731](https://github.com/vllm-project/vllm/issues/34731) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Improve swap_states by swapping active token prefixes

### Issue 正文摘录

### Proposal to improve performance `InputBatch.swap_states()` in `vllm/v1/worker/gpu_input_batch.py` currently does expensive full-row token buffer swapping on the request reordering path. This can be reduced by swapping only the active token prefix. cc @LucasWilkinson since the original TODO in #14253 calls out optimizing this copy path. ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: n #14253 calls out optimizing this copy path. ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: tch.py` currently does expensive full-row token buffer swapping on the request reordering path. This can be reduced by swapping only the active token prefix. cc @LucasWilkinson since the original TODO in #14253 calls ou...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
