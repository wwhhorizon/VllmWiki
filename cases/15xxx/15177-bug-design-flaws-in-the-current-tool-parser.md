# vllm-project/vllm#15177: [Bug]: Design flaws in the current tool parser.

| 字段 | 值 |
| --- | --- |
| Issue | [#15177](https://github.com/vllm-project/vllm/issues/15177) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Design flaws in the current tool parser.

### Issue 正文摘录

### Your current environment v0.8.0 ### 🐛 Describe the bug During streaming multi-step output, the state configuration of the current tool parser base class is not properly designed. https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/openai/tool_parsers/abstract_tool_parser.py#L18-L32 ``` def __init__(self, tokenizer: AnyTokenizer): self.prev_tool_call_arr: list[dict] = [] # the index of the tool call that is currently being parsed self.current_tool_id: int = -1 self.current_tool_name_sent: bool = False self.streamed_args_for_tool: list[str] = [] self.model_tokenizer = tokenizer ``` The extract_tool_calls_streaming method frequently encounters exceptions when parsing multi-step outputs when I use hermes. This issue is particularly prone to occur in the v0 multiple step or v1 architecture. The state field design in the base class becomes invalid when processing incrementally delta text containing complete JSON body.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 0 ### 🐛 Describe the bug During streaming multi-step output, the state configuration of the current tool parser base class is not properly designed. https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/openai...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: This issue is particularly prone to occur in the v0 multiple step or v1 architecture. The state field design in the base class becomes invalid when processing incrementally delta text containing complete JSON body.
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: .current_tool_id: int = -1 self.current_tool_name_sent: bool = False self.streamed_args_for_tool: list[str] = [] self.model_tokenizer = tokenizer ``` The extract_tool_calls_streaming method frequently encounters excepti...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Design flaws in the current tool parser. bug;stale ### Your current environment v0.8.0 ### 🐛 Describe the bug During streaming multi-step output, the state configuration of the current tool parser base class is n...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
