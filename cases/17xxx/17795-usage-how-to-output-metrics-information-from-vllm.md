# vllm-project/vllm#17795: [Usage]: How to output metrics information from vllm?

| 字段 | 值 |
| --- | --- |
| Issue | [#17795](https://github.com/vllm-project/vllm/issues/17795) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to output metrics information from vllm?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm When I run an LLM () object, I want to output the return metric value. How should I configure it? ![Image](https://github.com/user-attachments/assets/9404128c-cf32-4aa3-8244-64c70ab2f619) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: How to output metrics information from vllm? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm When I run an LLM () object, I want to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 19) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: How to output metrics information from vllm? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm When I run an LLM () object, I want to...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
