# vllm-project/vllm#26760: [Feature]: Option to disable thinking in vllm bench serve

| 字段 | 值 |
| --- | --- |
| Issue | [#26760](https://github.com/vllm-project/vllm/issues/26760) |
| 状态 | closed |
| 标签 | good first issue;feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Option to disable thinking in vllm bench serve

### Issue 正文摘录

### 🚀 The feature, motivation and pitch https://docs.vllm.ai/en/latest/cli/bench/serve.html Currently, when benchmarking the model with thinking mode enabled, there's no option to disable it. Should we add support for disabling thinking mode via options like appending a postfix such as "/no_think" to the prompt, or passing an extra body parameter like "chat_template_kwargs": {"enable_thinking": False}? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: quest ### 🚀 The feature, motivation and pitch https://docs.vllm.ai/en/latest/cli/bench/serve.html Currently, when benchmarking the model with thinking mode enabled, there's no option to disable it. Should we add support...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: extra body parameter like "chat_template_kwargs": {"enable_thinking": False}? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: .vllm.ai/en/latest/cli/bench/serve.html Currently, when benchmarking the model with thinking mode enabled, there's no option to disable it. Should we add support for disabling thinking mode via options like appending a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Option to disable thinking in vllm bench serve good first issue;feature request ### 🚀 The feature, motivation and pitch https://docs.vllm.ai/en/latest/cli/bench/serve.html Currently, when benchmarking the model with thi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
