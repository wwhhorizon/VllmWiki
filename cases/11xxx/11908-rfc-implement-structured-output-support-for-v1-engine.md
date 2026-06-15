# vllm-project/vllm#11908: [RFC]: Implement Structured Output support for V1 engine

| 字段 | 值 |
| --- | --- |
| Issue | [#11908](https://github.com/vllm-project/vllm/issues/11908) |
| 状态 | closed |
| 标签 | structured-output;RFC;v1 |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Implement Structured Output support for V1 engine

### Issue 正文摘录

### Motivation. Structured Output is supported in v0, but not yet in v1. One reason for the delay is there have been performance challenges with the integration in v0, and we'd like to rethink the integration approach. We would also like to account for supporting additional techniques, jump decoding in particular, in the future. The document below covers the proposed integration of the Structured Output functionality in V1 of the vLLM engine. ### Proposed Change. A draft proposal can be found in this google doc: https://docs.google.com/document/d/1H6m_Y3FLJ1FYGCmjXdZzoJv-JCDSxnKuSY2XiAj-c6c/edit?tab=t.0 This content will eventually be moved into a PR as an addition to the design docs section of the vllm docs. Related issue for closing xgrammar feature gaps: https://github.com/vllm-project/vllm/issues/12131 ### Feedback Period. _No response_ ### CC List. @mgoin @aarnphm @markmc @simon-mo @xuechendi @WoosukKwon ### Any Other Things. _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of fr...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Output functionality in V1 of the vLLM engine. ### Proposed Change. A draft proposal can be found in this google doc: https://docs.google.com/document/d/1H6m_Y3FLJ1FYGCmjXdZzoJv-JCDSxnKuSY2XiAj-c6c/edit?tab=t.0 This con...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
