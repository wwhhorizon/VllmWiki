# vllm-project/vllm#16313: [Feature]: Support structured output and tool call together

| 字段 | 值 |
| --- | --- |
| Issue | [#16313](https://github.com/vllm-project/vllm/issues/16313) |
| 状态 | open |
| 标签 | feature request;unstale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support structured output and tool call together

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### Checklist - [ ] 1. If the issue you raised is not a feature but a question, please raise a discussion at https://github.com/sgl-project/sglang/discussions/new/choose Otherwise, it will be closed. - [ ] 2. Please use English, otherwise it will be closed. ### Motivation as discussed in: https://www.reddit.com/r/LocalLLaMA/comments/1h2y7ys/why_can_you_not_use_structured_output_and_tool/ request support for tool execution followed by structured response output, similar to how OpenAI handles function calls (Tool Calls) and Schema outputs in the gpt-4o-mini API. OpenAI supports this capability through a workflow where: The model can first execute one or more tool calls to perform calculations or retrieve information After receiving the results of these tool calls, the model can then produce a final structured response conforming to a predefined schema **Example Implementation from OpenAI** Input to OpenAI User query: "current age of University of Oxford is 928" Available tools: add, subtract, multiply, divide, round Response format: Schema with current_age and calculated_age fields Execution flow: 1. Model analyzes query and determines it need...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: closed. ### Motivation as discussed in: https://www.reddit.com/r/LocalLLaMA/comments/1h2y7ys/why_can_you_not_use_structured_output_and_tool/ request support for tool execution followed by structured response output, sim...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Calls) and Schema outputs in the gpt-4o-mini API. OpenAI supports this capability through a workflow where: The model can first execute one or more tool calls to perform calculations or retrieve information After receiv...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Support structured output and tool call together feature request;unstale ### 🚀 The feature, motivation and pitch ### Checklist - [ ] 1. If the issue you raised is not a feature but a question, please raise a...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 'number', 'description': 'The multiplicand in the multiplication.'}, 'decimal_places': {'type': 'integer', 'description': 'The number of decimal\nplaces to round to. Defaults to 2.'}}, 'required': ['a', 'b', 'decimal_pl...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: '}}, 'required': ['a', 'b'], 'type': 'object', 'additionalProperties': False}}}, {'type': 'function', 'function': {'name': 'sub', 'description': 'Do subtraction between two numbers.', 'strict': True, 'parameters': {'pro...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
