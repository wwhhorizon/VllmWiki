# vllm-project/vllm#32638: [Bug]: Multiple tool_calls parsed correctly by hermes_tool_parser, but fail in serving_chat.py with JSONDecodeError

| 字段 | 值 |
| --- | --- |
| Issue | [#32638](https://github.com/vllm-project/vllm/issues/32638) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Multiple tool_calls parsed correctly by hermes_tool_parser, but fail in serving_chat.py with JSONDecodeError

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug when a single assistant message contains **multiple tool calls**, the tool calls are correctly parsed by `hermes_tool_parser`, but the OpenAI-compatible serving path fails during post-processing. Specifically, `serving_chat.py` assumes that `function.arguments` contains a single JSON object. When multiple tool calls are present, the arguments content contains multiple JSON fragments, which leads to a `JSONDecodeError: Extra data` during `json.loads`. As a result, the request fails with HTTP 400, even though the tool parser output itself is valid. Restricting the prompt to allow **only one tool call per assistant message** avoids the issue entirely. I use Model: qwen3-next-80B-instruct version: vllm 0.13.0 tool-call-parser hermes usefor: deepagents Input： A research query bugs come when: query -> write_file and todos two tool_call at same time. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ed correctly by hermes_tool_parser, but fail in serving_chat.py with JSONDecodeError bug;stale ### Your current environment ### 🐛 Describe the bug when a single assistant message contains **multiple tool calls**, the to...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: but the OpenAI-compatible serving path fails during post-processing. Specifically, `serving_chat.py` assumes that `function.arguments` contains a single JSON object. When multiple tool calls are present, the arguments c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: one tool call per assistant message** avoids the issue entirely. I use Model: qwen3-next-80B-instruct version: vllm 0.13.0 tool-call-parser hermes usefor: deepagents Input： A research query bugs come when: query -> writ...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: n: vllm 0.13.0 tool-call-parser hermes usefor: deepagents Input： A research query bugs come when: query -> write_file and todos two tool_call at same time. ### Before submitting a new issue... - [x] Make sure you alread...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
