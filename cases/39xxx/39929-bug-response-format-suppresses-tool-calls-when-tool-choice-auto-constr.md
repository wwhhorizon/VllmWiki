# vllm-project/vllm#39929: [Bug]: `response_format` suppresses tool calls when `tool_choice: "auto"` — constrained decoding prevents tool generation

| 字段 | 值 |
| --- | --- |
| Issue | [#39929](https://github.com/vllm-project/vllm/issues/39929) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: `response_format` suppresses tool calls when `tool_choice: "auto"` — constrained decoding prevents tool generation

### Issue 正文摘录

### Your current environment - vLLM: latest - Model: Qwen3.5-27B (likely affects all models served via vLLM) - Python: 3.12 - OS: macOS / Linux - `tool_choice`: `"auto"` (default) ### 🐛 Describe the bug ## Description When a chat completion request includes both `tools` and `response_format` (e.g. `json_object` or `json_schema`) with `tool_choice: "auto"` (the default), vLLM applies constrained decoding from `response_format`, which forces the model to produce JSON content. The model never generates tool calls — it returns `tool_calls: []` and answers directly as JSON. This was already identified and fixed for `tool_choice: "required"` in #32006, where `response_format` is cleared when tool calling is forced. However, the same issue exists for `tool_choice: "auto"` and has no fix. OpenAI's API handles this correctly — with `tool_choice: "auto"` + `response_format`, the model can still return `tool_calls`. The `response_format` only constrains the final text response, not tool call generation. The two features coexist. ## Reproduction ```bash # tool_choice: "auto" (default) + response_format — tools SKIPPED curl -s "$VLLM_ENDPOINT/v1/chat/completions" \ -H "Content-Type: applicatio...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: `response_format` suppresses tool calls when `tool_choice: "auto"` — constrained decoding prevents tool generation bug ### Your current environment - vLLM: latest - Model: Qwen3.5-27B (likely affects all models s...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: The `"auto"` case was not addressed. Under `"auto"`, the model should decide whether to call tools or respond directly — but constrained decoding from `response_format` removes that choice by forcing JSON output. Possib...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: d"` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: default) ### 🐛 Describe the bug ## Description When a chat completion request includes both `tools` and `response_format` (e.g. `json_object` or `json_schema`) with `tool_choice: "auto"` (the default), vLLM applies cons...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ing prevents tool generation bug ### Your current environment - vLLM: latest - Model: Qwen3.5-27B (likely affects all models served via vLLM) - Python: 3.12 - OS: macOS / Linux - `tool_choice`: `"auto"` (default) ### 🐛...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
