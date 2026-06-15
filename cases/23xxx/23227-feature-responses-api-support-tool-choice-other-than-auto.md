# vllm-project/vllm#23227: [Feature][Responses API] Support tool_choice other than "auto"

| 字段 | 值 |
| --- | --- |
| Issue | [#23227](https://github.com/vllm-project/vllm/issues/23227) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][Responses API] Support tool_choice other than "auto"

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Current response API only supports tool_choice="auto". For other tool_choice, e.g., tool_choice="required", we need to properly enable structure output. See the OpenAI API doc for tool_choice here https://platform.openai.com/docs/guides/function-calling#tool-choice ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature][Responses API] Support tool_choice other than "auto" feature request;stale ### 🚀 The feature, motivation and pitch Current response API only supports tool_choice="auto". For other tool_choice, e.g., tool_choic...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
