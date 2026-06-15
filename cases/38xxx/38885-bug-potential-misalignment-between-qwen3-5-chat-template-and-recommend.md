# vllm-project/vllm#38885: [Bug]: Potential misalignment between qwen3.5 chat template and recommended tool parser

| 字段 | 值 |
| --- | --- |
| Issue | [#38885](https://github.com/vllm-project/vllm/issues/38885) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Potential misalignment between qwen3.5 chat template and recommended tool parser

### Issue 正文摘录

### Your current environment NA ### 🐛 Describe the bug Qwen3.5's chat template uses | string for scalar tool call argument values, producing Python str() representations instead of JSON literals. This breaks tool call parsing at inference time for models fine-tuned using this chat template. Qwen3.5 chat template: ``` {%- set args_value = args_value | tojson | safe if args_value is mapping or (args_value is sequence and args_value is not string) else args_value | string %} ``` Only mappings and non-string sequences get tojson. Other types like None go through | string gets converted to "None". So, the model trained on this chat template would emit "None" instead of "null". [Recommended vllm qwen3 coder tool parser which can only parse string "null" but not "None".](https://github.com/vllm-project/vllm/blob/550643541956cf913a2346f69af3be89c5c93a6b/vllm/tool_parsers/qwen3coder_tool_parser.py#L139) Qwen3 coder is fine because its chat template correctly calls tojson on all non-string arguments and converts null to "null" ``` {%- set args_value = args_value if args_value is string else args_value | tojson | safe %} ``` ### Before submitting a new issue... - [x] Make sure you already se...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: e: ``` {%- set args_value = args_value | tojson | safe if args_value is mapping or (args_value is sequence and args_value is not string) else args_value | string %} ``` Only mappings and non-string sequences get tojson....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Potential misalignment between qwen3.5 chat template and recommended tool parser bug ### Your current environment NA ### 🐛 Describe the bug Qwen3.5's chat template uses | string for scalar tool call argument valu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: s chat template uses | string for scalar tool call argument values, producing Python str() representations instead of JSON literals. This breaks tool call parsing at inference time for models fine-tuned using this chat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
