# vllm-project/vllm#8279: [RFC]: More functionality for API control

| 字段 | 值 |
| --- | --- |
| Issue | [#8279](https://github.com/vllm-project/vllm/issues/8279) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: More functionality for API control

### Issue 正文摘录

### Motivation. In deploying to a production environment, we may need to consider certain controls over the API, such as: control over the number of API calls per second, security controls, among others. ### Proposed Change. For example, We can easily add constraints via code into the vllm endpoint. Where should the codes begin from a functional standpoint? Or, any thoughts related to the matter? ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things. _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [RFC]: More functionality for API control RFC;stale ### Motivation. In deploying to a production environment, we may need to consider certain controls over the API, such as: control over the number of API calls per seco...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
