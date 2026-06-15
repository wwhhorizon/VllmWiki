# vllm-project/vllm#43220: [Bug]: Streaming reasoning tokens truncated when `</think>` and `<tool_call>` appear in the same delta

| 字段 | 值 |
| --- | --- |
| Issue | [#43220](https://github.com/vllm-project/vllm/issues/43220) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Streaming reasoning tokens truncated when `</think>` and `<tool_call>` appear in the same delta

### Issue 正文摘录

### Your current environment OS: any vllm: main ### 🐛 Describe the bug **Problem Description:** When using Qwen3.5 models with streaming inference, Multi-Token Prediction (MTP), thinking mode enabled, and tool calling, the last few tokens of the thinking section are occasionally truncated. Non-streaming inference works correctly. **Reproduction Steps:** 1. Enable streaming inference with Qwen3.5 model 2. Enable thinking mode (`--reasoning-parser qwen3`) 3. Enable tool calling (`--tool-call-parser qwen3_coder`) 4. Use MTP (default behavior in Qwen3.5) 5. Trigger responses where model output contains reasoning followed by tool calls **Expected Behavior:** The complete reasoning content should be streamed to the client before transitioning to tool call parsing. **Actual Behavior:** When MTP generates multiple tokens in a single inference step that include both the reasoning end token (` `) and the tool call start token (` `), the reasoning tokens immediately preceding ` ` are lost. **Example:** config: num_speculative_tokens=3 something output like I will use the tool Write. the delta_text is "Write. " - MTP output tokens: `["Write", ".", " ", " "]` - Expected streaming output: reaso...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: vllm: main ### 🐛 Describe the bug **Problem Description:** When using Qwen3.5 models with streaming inference, Multi-Token Prediction (MTP), thinking mode enabled, and tool calling, the last few tokens of the thinking s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ep. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ing tokens immediately preceding ` ` are lost. **Example:** config: num_speculative_tokens=3 something output like I will use the tool Write. the delta_text is "Write. " - MTP output tokens: `["Write", ".", " ", " "]` -...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
