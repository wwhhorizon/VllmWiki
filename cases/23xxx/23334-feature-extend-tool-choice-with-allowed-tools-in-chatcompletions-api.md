# vllm-project/vllm#23334: [Feature]: Extend tool_choice with allowed_tools in ChatCompletions API

| 字段 | 值 |
| --- | --- |
| Issue | [#23334](https://github.com/vllm-project/vllm/issues/23334) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Extend tool_choice with allowed_tools in ChatCompletions API

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I want to use `allowed_tools` in `tool_choice` to limit available tools to call Or i want to add some extra available tools to call with specific tool in `tool_choice` ### Alternatives _No response_ ### Additional context https://platform.openai.com/docs/api-reference/chat/create ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ools to call Or i want to add some extra available tools to call with specific tool in `tool_choice` ### Alternatives _No response_ ### Additional context https://platform.openai.com/docs/api-reference/chat/create ### B...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: e]: Extend tool_choice with allowed_tools in ChatCompletions API feature request ### 🚀 The feature, motivation and pitch I want to use `allowed_tools` in `tool_choice` to limit available tools to call Or i want to add s...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
