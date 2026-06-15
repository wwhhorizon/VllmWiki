# vllm-project/vllm#31379: [Bug]: GLM47 the empty parameter tool report TypeError: expected string or buffer

| 字段 | 值 |
| --- | --- |
| Issue | [#31379](https://github.com/vllm-project/vllm/issues/31379) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: GLM47 the empty parameter tool report TypeError: expected string or buffer

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug [glm4_moe_tool_parser.py:123] Failed to extract tool call spec [glm4_moe_tool_parser.py:123] Traceback (most recent call last): [glm4_moe_tool_parser.py:123] File "/dist-packages/vllm/tool_parsers/glm4_moe_tool_parser.py", line 104, in extract_tool_calls [glm4_moe_tool_parser.py:123] pairs = self.func_arg_regex.findall(tc_args) [glm4_moe_tool_parser.py:123] TypeError: expected string or buffer ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: fer ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ffer bug ### Your current environment ### 🐛 Describe the bug [glm4_moe_tool_parser.py:123] Failed to extract tool call spec [glm4_moe_tool_parser.py:123] Traceback (most recent call last): [glm4_moe_tool_parser.py:123]...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
