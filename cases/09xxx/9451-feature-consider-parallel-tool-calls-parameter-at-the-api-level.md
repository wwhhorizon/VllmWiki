# vllm-project/vllm#9451: [Feature]: Consider parallel_tool_calls parameter at the API level

| 字段 | 值 |
| --- | --- |
| Issue | [#9451](https://github.com/vllm-project/vllm/issues/9451) |
| 状态 | closed |
| 标签 | feature request;tool-calling |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Consider parallel_tool_calls parameter at the API level

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, there is a [parallel_tool_calls](https://github.com/vllm-project/vllm/blob/18b296fdb2248e8a65bf005e7193ebd523b875b6/vllm/entrypoints/openai/protocol.py#L177) field that is part of the `ChatCompletionRequest` pydantic class. However, this field is only there for being compatible with OpenAI's API. In other words, it's not being used at all according to the documentation or the code: ``` # NOTE this will be ignored by VLLM -- the model determines the behavior parallel_tool_calls: Optional[bool] = False ``` Would it be possible to consider implementing the logic behind this field for different model families. For instance, in the case of llama3.1-8b-insturct, tool calling works, but the model ends up returning three tool calls instead of one by one. This makes me lose compatibility with frameworks like LangGraph. Here's an example request and response: **Request** ``` { "messages": [ { "content": "You are a helpful assistant tasked with performing arithmetic on a set of inputs.", "role": "system" }, { "content": "Add 3 and 4. Multiply the output by 2. Divide the output by 5", "role": "user" } ], "model": "meta-llama/Meta-Llama-3.1-8B...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: cumentation or the code: ``` # NOTE this will be ignored by VLLM -- the model determines the behavior parallel_tool_calls: Optional[bool] = False ``` Would it be possible to consider implementing the logic behind this f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: he model determines the behavior parallel_tool_calls: Optional[bool] = False ``` Would it be possible to consider implementing the logic behind this field for different model families. For instance, in the case of llama...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: eature]: Consider parallel_tool_calls parameter at the API level feature request;tool-calling ### 🚀 The feature, motivation and pitch Currently, there is a [parallel_tool_calls](https://github.com/vllm-project/vllm/blob...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
