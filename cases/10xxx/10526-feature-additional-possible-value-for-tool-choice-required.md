# vllm-project/vllm#10526: [Feature]: Additional possible value for `tool_choice`: `required`

| 字段 | 值 |
| --- | --- |
| Issue | [#10526](https://github.com/vllm-project/vllm/issues/10526) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Additional possible value for `tool_choice`: `required`

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I'm currently making an agent using LLM which required using external tools. There is step in completion where tools is required to be called but what kind of tool is used is up to the LLM. In [openAI API](https://platform.openai.com/docs/api-reference/chat/create), there is parameter called `tool_choice` and we could set it to `required` to make LLM always use external tools but we as user do not choice what tool to use. ### Alternatives _No response_ ### Additional context Here is what is written in openAI API documentation ![image](https://github.com/user-attachments/assets/9269028c-3dd6-4dad-8e2a-f825cbdd7679) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: eature]: Additional possible value for `tool_choice`: `required` feature request;stale ### 🚀 The feature, motivation and pitch I'm currently making an agent using LLM which required using external tools. There is step i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 79) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
