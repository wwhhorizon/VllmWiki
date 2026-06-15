# vllm-project/vllm#30554: [Bug]: When using minimax m2 model tool call, throw IndexError in serving_chat.py

| 字段 | 值 |
| --- | --- |
| Issue | [#30554](https://github.com/vllm-project/vllm/issues/30554) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: When using minimax m2 model tool call, throw IndexError in serving_chat.py

### Issue 正文摘录

### Your current environment When using the MiniMax M2 model tool call, an IndexError ("list index out of range") is raised at line 1181 in serving_chat.py: actual_call = tool_parser.streamed_args_for_tool[index] . It's caused by minimax_m2_tool_parser.py's streamed_args_for_tool field. This field always is empty lis ### 🐛 Describe the bug When using the MiniMax M2 model tool call, an IndexError ("list index out of range") is raised at line 1181 in serving_chat.py It's caused by minimax_m2_tool_parser.py's field:streamed_args_for_tool. This field always is empty list. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: st. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: When using minimax m2 model tool call, throw IndexError in serving_chat.py bug ### Your current environment When using the MiniMax M2 model tool call, an IndexError ("list index out of range") is raised at line 1...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
