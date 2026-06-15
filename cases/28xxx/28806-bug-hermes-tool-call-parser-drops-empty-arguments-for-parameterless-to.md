# vllm-project/vllm#28806: [Bug]: Hermes tool call parser drops empty arguments for parameterless tools while streaming

| 字段 | 值 |
| --- | --- |
| Issue | [#28806](https://github.com/vllm-project/vllm/issues/28806) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Hermes tool call parser drops empty arguments for parameterless tools while streaming

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Bug description I am facing an issue when using the OpenAI-compatible server + hermes tool call parser (used with Qwen2.5-7B-Instruct in this case): During streaming, the parser seems to incorrectly handle tool calls that don't require arguments. It seems to omit the empty "arguments" dict. However, due to that the server won't send a streaming chunk containing the arguments (in this case "{}"). Only the initial chunk containing the tool name, followed by a chunk with finish_reason "tool_calls". Sample output with a parameterless "switch_led_on" tool: ``` data: {"id":"chatcmpl-e50cbabd787e4b3cb6a088cd7858ca41","object":"chat.completion.chunk","created":1763290465,"model":"Qwen/Qwen2.5-7B-Instruct-AWQ","choices":[{"index":0,"delta":{"role":"assistant","content":""},"logprobs":null,"finish_reason":null}],"prompt_token_ids":null} data: {"id":"chatcmpl-e50cbabd787e4b3cb6a088cd7858ca41","object":"chat.completion.chunk","created":1763290465,"model":"Qwen/Qwen2.5-7B-Instruct-AWQ","choices":[{"index":0,"delta":{"tool_calls":[{"id":"chatcmpl-tool-7e08fc7ab28d41d1ab812c23ed2bd5c7","type":"function","index":0,"function":{"name":"switch_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: rrent environment ### 🐛 Describe the bug ### Bug description I am facing an issue when using the OpenAI-compatible server + hermes tool call parser (used with Qwen2.5-7B-Instruct in this case): During streaming, the par...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: using the OpenAI-compatible server + hermes tool call parser (used with Qwen2.5-7B-Instruct in this case): During streaming, the parser seems to incorrectly handle tool calls that don't require arguments. It seems to om...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: parser drops empty arguments for parameterless tools while streaming bug;stale ### Your current environment ### 🐛 Describe the bug ### Bug description I am facing an issue when using the OpenAI-compatible server + herme...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
