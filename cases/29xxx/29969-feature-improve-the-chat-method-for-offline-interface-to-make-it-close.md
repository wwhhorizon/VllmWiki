# vllm-project/vllm#29969: [Feature]: Improve the chat method for offline interface to make it closer to the functionality of online service

| 字段 | 值 |
| --- | --- |
| Issue | [#29969](https://github.com/vllm-project/vllm/issues/29969) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Improve the chat method for offline interface to make it closer to the functionality of online service

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Improve the LLM.chat method for offline interface to make it closer to the functionality of online service, enchance LLM.chat and LLM.generate interfaces to support streaming output, and support message filtering with reasoning_paperer and tool_caperer. This way, libraries like Outline can better support streaming output for VLLM offline interface as well ### Alternatives Inherit LLM classes to achieve simple functionality ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: terface to make it closer to the functionality of online service feature request;stale ### 🚀 The feature, motivation and pitch Improve the LLM.chat method for offline interface to make it closer to the functionality of...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
