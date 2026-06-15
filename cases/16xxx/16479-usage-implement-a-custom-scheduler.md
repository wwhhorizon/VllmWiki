# vllm-project/vllm#16479: [Usage]: Implement a custom scheduler

| 字段 | 值 |
| --- | --- |
| Issue | [#16479](https://github.com/vllm-project/vllm/issues/16479) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Implement a custom scheduler

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I am new with scheduling and vLLM. Since, vLLM already implements a default FCFS strategy for vLLM, I would like to know how to implement a custom scheduler. I want to prioritize decodes in my custom scheduling approach and I was wondering do I need to change only the `_scheduler_default` function in vllm/vllm/core/scheduling.py or do I need to make changes in the engine and worker too? I changed the above mentioned function but I am getting the same results as the default FCFS strategy ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Implement a custom scheduler usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I am new with scheduling and vLLM. Since, vLLM already implem...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: gy ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
