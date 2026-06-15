# vllm-project/vllm#24140: [Bug]: Deepseek V3.1 tool_choice=required，输出混乱

| 字段 | 值 |
| --- | --- |
| Issue | [#24140](https://github.com/vllm-project/vllm/issues/24140) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Deepseek V3.1 tool_choice=required，输出混乱

### Issue 正文摘录

### Your current environment response_required = client_tool_choice.chat.completions.create( model=model_name_tool_choice, messages=messages_required, # temperature=0, max_tokens=1024, tools=tools, tool_choice="required", # Force the model to call a tool ) Content: get_current_weather arguments_get_current_weather Content: [Choice(finish_reason='tool_calls', index=0, logprobs=None, message=ChatCompletionMessage(content=' get_current_weather arguments_get_current_weather ', refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=[], reasoning_content=None), matched_stop=None)] 使用required出现工具调用输出混乱的问题，怀疑还是jinja模版的问题 ### 🐛 Describe the bug 工具调用输出混乱 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 出混乱 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: t response_required = client_tool_choice.chat.completions.create( model=model_name_tool_choice, messages=messages_required, # temperature=0, max_tokens=1024, tools=tools, tool_choice="required", # Force the model to cal...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Deepseek V3.1 tool_choice=required，输出混乱 bug;stale ### Your current environment response_required = client_tool_choice.chat.completions.create( model=model_name_tool_choice, messages=messages_required, # temperatu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
