# vllm-project/vllm#14721: [Feature]: Support openai responses API interface

| 字段 | 值 |
| --- | --- |
| Issue | [#14721](https://github.com/vllm-project/vllm/issues/14721) |
| 状态 | closed |
| 标签 | good first issue;feature request |
| 评论 | 28; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support openai responses API interface

### Issue 正文摘录

### 🚀 The feature, motivation and pitch OpenAI has released a new Responses API, but vLLM does not currently support it. We request that vLLM adds compatibility with this API to stay in sync with OpenAI's updates. Supporting the Responses API will enhance vLLM's utility and competitiveness. For more details, see the OpenAI documentation * OpenAI Responses api reference https://platform.openai.com/docs/api-reference/responses * OpenAI Responses vs. Chat Completions https://platform.openai.com/docs/guides/responses-vs-chat-completions ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: eature]: Support openai responses API interface good first issue;feature request ### 🚀 The feature, motivation and pitch OpenAI has released a new Responses API, but vLLM does not currently support it. We request that v...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
