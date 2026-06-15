# vllm-project/vllm#9603: [Usage]: How to add a plugin process to the vLLM process world?

| 字段 | 值 |
| --- | --- |
| Issue | [#9603](https://github.com/vllm-project/vllm/issues/9603) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to add a plugin process to the vLLM process world?

### Issue 正文摘录

### Your current environment xxx ### How would you like to use vllm My use case is as follows: there are `k+1` processes, they are in the same world, where processes `1` to `k` make up the same one LLM, and they will request data from process `k+1` sometimes. My question is: is there a mechanism for vLLM to help me implement such an application? To simplify, we can assume that the first k processes send messages to the `k+1` process at the same time. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: est data from process `k+1` sometimes. My question is: is there a mechanism for vLLM to help me implement such an application? To simplify, we can assume that the first k processes send messages to the `k+1` process at...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: How to add a plugin process to the vLLM process world? usage;stale ### Your current environment xxx ### How would you like to use vllm My use case is as follows: there are `k+1` processes, they are in the same...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
