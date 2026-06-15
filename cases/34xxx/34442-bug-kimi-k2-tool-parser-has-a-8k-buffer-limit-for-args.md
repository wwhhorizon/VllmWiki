# vllm-project/vllm#34442: [Bug]: kimi k2 tool parser has a 8k buffer limit for args

| 字段 | 值 |
| --- | --- |
| Issue | [#34442](https://github.com/vllm-project/vllm/issues/34442) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: kimi k2 tool parser has a 8k buffer limit for args

### Issue 正文摘录

### Your current environment current main - irrespective of env ### 🐛 Describe the bug https://github.com/vllm-project/vllm/blob/main/vllm/tool_parsers/kimi_k2_tool_parser.py#L46 ```py self.max_section_chars: int = 8192 self.buffer_max_size: int = 1024 ``` The K2 tool parser has a 8k buffer limit - which extends to the tool-call args. Effectively banning the API output from ever writing a file more than 8k characters long, for example. The parser also has a 1k limit for something, idk the implications of that yet, but the 8k limit is harsh for coding cases. --- Resolution: get rid of the 8k limit. Feel like it iis the engine's job to reliably produce finish_reason chunks, or graceful terminations, and the parserr should not be ~hacking this. Call for further investigation: what is the 1k limit for truly, seems like another ~hacky idea? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ea? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
