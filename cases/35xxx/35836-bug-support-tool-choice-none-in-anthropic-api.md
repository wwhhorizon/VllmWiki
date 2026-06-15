# vllm-project/vllm#35836: [Bug]: Support tool_choice=none in Anthropic API

| 字段 | 值 |
| --- | --- |
| Issue | [#35836](https://github.com/vllm-project/vllm/issues/35836) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Support tool_choice=none in Anthropic API

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The OpenAI API supports setting `tool_choice=none` to explicitly disable tool usage. However, the Anthropic API currently does not support this scenario. 1. `/v1/chat/completions` When using the OpenAI-compatible endpoint with: ``` "tool_choice": "none" ``` The request is accepted. 2. `/v1/messages` When using the Anthropic-style endpoint with: ``` "tool_choice": { "type": "none" } ``` It returns the following error: ``` { "error": { "message": "[{'type': 'literal_error', 'loc': ('body', 'tool_choice', 'type'), 'msg': \"Input should be 'auto', 'any' or 'tool'\", 'input': 'none', 'ctx': {'expected': \"'auto', 'any' or 'tool'\"}}]", "type": "Bad Request", "code": 400 } } ``` This indicates that the current Anthropic API implementation only supports: ``` "auto" "any" "tool" ``` and does not allow "none". ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ribe the bug The OpenAI API supports setting `tool_choice=none` to explicitly disable tool usage. However, the Anthropic API currently does not support this scenario. 1. `/v1/chat/completions` When using the OpenAI-comp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: e". ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: the OpenAI-compatible endpoint with: ``` "tool_choice": "none" ``` The request is accepted. 2. `/v1/messages` When using the Anthropic-style endpoint with: ``` "tool_choice": { "type": "none" } ``` It returns the follow...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
