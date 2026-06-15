# vllm-project/vllm#41122: [Bug] DeepSeek V4 tool calling returns boolean parameters as quoted strings which causes subagent failed in ClaudeCode

| 字段 | 值 |
| --- | --- |
| Issue | [#41122](https://github.com/vllm-project/vllm/issues/41122) |
| 状态 | closed |
| 标签 | bug;DSv4 |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug] DeepSeek V4 tool calling returns boolean parameters as quoted strings which causes subagent failed in ClaudeCode

### Issue 正文摘录

### Your current environment ## Environment - vLLM version: latest main (commit range includes DeepSeek V4 support) - Model: DeepSeek V4 Flash - Tool parser: `DeepSeekV32ToolParser` (used for V4) - Mode: **non-streaming** chat completion ## Steps to Reproduce 1. Deploy DeepSeek V4 with vLLM 2. use message endpoint for claudecode 3. triger subagent toolcall ### 🐛 Describe the bug ## Bug Summary When deploying DeepSeek V4 with vLLM and using non-streaming tool calling, boolean parameters are returned as JSON strings (e.g., `"true"`) instead of JSON booleans (`true`). This causes downstream agents/frameworks to fail input validation when the tool schema declares the parameter type as `boolean`. It happens when we use messages endpoint for ClaudeCode calling subagent ## Actual Behavior The `arguments` JSON string contains: ```json {"run_in_background": "true", ...} ``` The boolean value is wrapped in quotes, making it a JSON string. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked q...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: er` (used for V4) - Mode: **non-streaming** chat completion ## Steps to Reproduce 1. Deploy DeepSeek V4 with vLLM 2. use message endpoint for claudecode 3. triger subagent toolcall ### 🐛 Describe the bug ## Bug Summary...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ClaudeCode bug;DSv4 ### Your current environment ## Environment - vLLM version: latest main (commit range includes DeepSeek V4 support) - Model: DeepSeek V4 Flash - Tool parser: `DeepSeekV32ToolParser` (used for V4) - M...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: vLLM version: latest main (commit range includes DeepSeek V4 support) - Model: DeepSeek V4 Flash - Tool parser: `DeepSeekV32ToolParser` (used for V4) - Mode: **non-streaming** chat completion ## Steps to Reproduce 1. De...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: boolean parameters as quoted strings which causes subagent failed in ClaudeCode bug;DSv4 ### Your current environment ## Environment - vLLM version: latest main (commit range includes DeepSeek V4 support) - Model: DeepS...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
