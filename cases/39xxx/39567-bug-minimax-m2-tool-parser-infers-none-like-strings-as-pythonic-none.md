# vllm-project/vllm#39567: [Bug]: minimax_m2_tool_parser infers none-like strings as pythonic None

| 字段 | 值 |
| --- | --- |
| Issue | [#39567](https://github.com/vllm-project/vllm/issues/39567) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: minimax_m2_tool_parser infers none-like strings as pythonic None

### Issue 正文摘录

### Your current environment current main - irrespective of env ### 🐛 Describe the bug > https://github.com/vllm-project/vllm/blob/d4cb783c10ffc091af7f09a3b052dceadc06d075/vllm/tool_parsers/minimax_m2_tool_parser.py#L163 ```py # Check if the VALUE itself indicates null (not just if null is allowed) if value.lower() in ("null", "none", "nil"): return None ``` 1. Here, minimax_m2_tool_parser infers none-like strings as pythonic None. 2. This messes with enums where "none" is an option for example. 3. As output, I want to see `"none"` for my classification case, but what I get is `None`, which breaks my workflow. Technically, this if-block should not be present at all? --- Suggested fix: delete the if-block ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ock ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ut what I get is `None`, which breaks my workflow. Technically, this if-block should not be present at all? --- Suggested fix: delete the if-block ### Before submitting a new issue... - [x] Make sure you already searche...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
