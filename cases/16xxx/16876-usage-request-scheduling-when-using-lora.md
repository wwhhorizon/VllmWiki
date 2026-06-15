# vllm-project/vllm#16876: [Usage]: Request scheduling when using LoRA

| 字段 | 值 |
| --- | --- |
| Issue | [#16876](https://github.com/vllm-project/vllm/issues/16876) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Request scheduling when using LoRA

### Issue 正文摘录

### Your current environment vllm0.7.4 ### How would you like to use vllm According to my understanding, the current request scheduling method of vllm (I am using v0.7.4) when LoRA is enabled is: FCFS, but later requests may be prioritized because its corresponding LoRA weights are already on the GPU buffer. For example, max num for buffered LoRA is 1, and request1 with LoRA1 is being processed, request2 with LoRA2 is queueing, then request3 with LoRA1 comes. Request3 will be processed in preference to request 2. I wonder if my understanding is correct and if there is a way to ensure that request2 is handled strictly before request3(for example, give each request a decreasing priority based on the order in which it arrives). This is because the above scheduling methods increase the queuing time of request2. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Usage]: Request scheduling when using LoRA usage;stale ### Your current environment vllm0.7.4 ### How would you like to use vllm According to my understanding, the current request scheduling method of vllm (I am using...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: t2. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
