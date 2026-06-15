# vllm-project/vllm#44326: [Bug]: GLM-4.7 streaming tool parser drops inline zero-argument tool calls

| 字段 | 值 |
| --- | --- |
| Issue | [#44326](https://github.com/vllm-project/vllm/issues/44326) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: GLM-4.7 streaming tool parser drops inline zero-argument tool calls

### Issue 正文摘录

### Your current environment Verified against vLLM upstream/main: ```text 6314de8ba ``` This is a parser-level repro and does not require model weights or GPU/NPU execution. ### 🐛 Describe the bug The `glm47` tool parser supports GLM-4.7 inline tool-call syntax in non-streaming mode, including zero-argument calls like: ```text get_current_time ``` However, the streaming parser drops the same tool call. In Chat Completions streaming this appears as a final `finish_reason: "tool_calls"` chunk without any streamed `delta.tool_calls`, while non-streaming returns the correct function call. This also reproduces when combining `--reasoning-parser glm45` with `--tool-call-parser glm47`, because `glm45` delegates to the DeepSeek thinking parser and then passes the post-` ` content to the GLM47 tool parser. ### Minimal repro ```python import json from vllm.entrypoints.openai.chat_completion.protocol import ChatCompletionRequest from vllm.parser.abstract_parser import _WrappedParser from vllm.reasoning.deepseek_v3_reasoning_parser import ( DeepSeekV3ReasoningWithThinkingParser, ) from vllm.tool_parsers.glm47_moe_tool_parser import Glm47MoeModelToolParser class FakeTokenizer: def get_vocab(se...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: alls`, while non-streaming returns the correct function call. This also reproduces when combining `--reasoning-parser glm45` with `--tool-call-parser glm47`, because `glm45` delegates to the DeepSeek thinking parser and...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: post-` ` content to the GLM47 tool parser. ### Minimal repro ```python import json from vllm.entrypoints.openai.chat_completion.protocol import ChatCompletionRequest from vllm.parser.abstract_parser import _WrappedParse...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: or. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ```text 6314de8ba ``` This is a parser-level repro and does not require model weights or GPU/NPU execution. ### 🐛 Describe the bug The `glm47` tool parser supports GLM-4.7 inline tool-call syntax in non-streaming mode,...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: DeepSeekV3ReasoningWithThinkingParser, ) from vllm.tool_parsers.glm47_moe_tool_parser import Glm47MoeModelToolParser class FakeTokenizer: def get_vocab(self): return { " ": 154841, " ": 154842, " ": 154843, " ": 154844,

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
