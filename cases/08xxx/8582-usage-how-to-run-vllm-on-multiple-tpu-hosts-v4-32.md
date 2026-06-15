# vllm-project/vllm#8582: [Usage]: How to run VLLM on multiple tpu hosts  V4-32

| 字段 | 值 |
| --- | --- |
| Issue | [#8582](https://github.com/vllm-project/vllm/issues/8582) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to run VLLM on multiple tpu hosts  V4-32

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm As there is an example for offline inference on TPUs, but it is not utilizing all 4 hosts in v4-32, if I run the code on all hosts , ray detects each hosts TPU resource only, Environment is correct it works for single host but maybe I dont know how to let VLLM detect and use all 4 hosts , I would like to do that for bigger models. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ls. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: let VLLM detect and use all 4 hosts , I would like to do that for bigger models. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: How to run VLLM on multiple tpu hosts V4-32 usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm As there is an example for offline infer...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
