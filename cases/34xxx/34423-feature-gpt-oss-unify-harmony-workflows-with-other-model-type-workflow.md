# vllm-project/vllm#34423: [Feature]: GPT-OSS: Unify harmony workflows with other model type workflows

| 字段 | 值 |
| --- | --- |
| Issue | [#34423](https://github.com/vllm-project/vllm/issues/34423) |
| 状态 | open |
| 标签 | feature request;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: GPT-OSS: Unify harmony workflows with other model type workflows

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I'm working on: 1. support all tool calling capabilities for gpt-oss: `tool_choice=required`, `tool_choice= ` -> https://github.com/vllm-project/vllm/pull/33306#issuecomment-3885256588 2. increase support for structured output for gpt-oss: add the possibility for a guided decoding 3. create variants of gpt-oss, and be able to modify the identity of the model The main problem I'm facing is that `gpt-oss` type models follow a different workflow than other models: the function [_make_request_with_harmony](https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/openai/responses/serving.py#L631) For my use case, this affects me like this: 1. `tool_choice` argument is ignored: this prevents gpt-oss type models from being used reliably in agentic workflows 2. structured output: no guided decoding possibility, therefore affecting agentic workflows 3. variants of gpt-oss that use harmony format: vllm doesn't read the chat template from huggingface when formatting the input. However, the chat template is the standard way to set the formatting of request for a given model. So I wanted to change the `model_identity` from the chat-template, but t...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Feature]: GPT-OSS: Unify harmony workflows with other model type workflows feature request;stale ### 🚀 The feature, motivation and pitch I'm working on: 1. support all tool calling capabilities for gpt-oss: `tool_choic...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: GPT-OSS: Unify harmony workflows with other model type workflows feature request;stale ### 🚀 The feature, motivation and pitch I'm working on: 1. support all tool calling capabilities for gpt-oss: `tool_choice=required`...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: and be able to modify the identity of the model The main problem I'm facing is that `gpt-oss` type models follow a different workflow than other models: the function [_make_request_with_harmony](https://github.com/vllm-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
