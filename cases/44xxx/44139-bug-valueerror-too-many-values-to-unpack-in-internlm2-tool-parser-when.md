# vllm-project/vllm#44139: BUG: ValueError too many values to unpack in internlm2_tool_parser when output contains multiple tool-call markers

| 字段 | 值 |
| --- | --- |
| Issue | [#44139](https://github.com/vllm-project/vllm/issues/44139) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> BUG: ValueError too many values to unpack in internlm2_tool_parser when output contains multiple tool-call markers

### Issue 正文摘录

## What breaks When a model using the InternLM2 tool parser produces output that contains more than one ` ` marker (e.g. a response that repeats the tool-call header, or genuinely attempts parallel tool calls), both \`extract_tool_calls\` (line 205) and \`extract_tool_calls_streaming\` (line 80) crash with: \`\`\` ValueError: too many values to unpack (expected 2) \`\`\` ## How to trigger \`\`\`python model_output = ( "Some text" " {\"name\": \"tool1\", \"parameters\": {}} " " {\"name\": \"tool2\", \"parameters\": {}} " ) text, action = model_output.split(" ") # crashes \`\`\` ## Root cause Both lines use \`str.split(delimiter)\` without a \`maxsplit\` argument. When the delimiter appears more than once, \`split()\` returns 3+ items, but the code unpacks into exactly 2 variables. ## Fix Change both calls to \`split(" ", 1)\` so only the first occurrence is used as the split point. **Affected file:** \`vllm/tool_parsers/internlm2_tool_parser.py\` lines 80 and 205.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: r when output contains multiple tool-call markers ## What breaks When a model using the InternLM2 tool parser produces output that contains more than one ` ` marker (e.g. a response that repeats the tool-call header, or...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
