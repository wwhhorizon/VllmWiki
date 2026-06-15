# vllm-project/vllm#28804: [Bug]: DeepSeek V3.1 Tool Parser: Leading whitespace accumulation in multi-turn tool calling conversations

| 字段 | 值 |
| --- | --- |
| Issue | [#28804](https://github.com/vllm-project/vllm/issues/28804) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: DeepSeek V3.1 Tool Parser: Leading whitespace accumulation in multi-turn tool calling conversations

### Issue 正文摘录

### Your current environment - **vLLM Version**: nightly (commit: `0b25498990f01ea2553c02731d6e2ce2d550156a`) - **Model**: DeepSeek-V3.1-Terminus - **Tool Parser**: `deepseek_v31` - **Chat Template**: `tool_chat_template_deepseekv31.jinja` - **Request Mode**: Non-streaming ### 🐛 Describe the bug ### Docker Configuration ```yaml command: > --model /models/DeepSeek-V3.1-Terminus --served-model-name DeepSeek-V3.1 --trust-remote-code --host 0.0.0.0 --port 8000 --tensor-parallel-size 8 --reasoning-parser deepseek_v3 --max-model-len 128000 --gpu-memory-utilization 0.9 --enable-auto-tool-choice --tool-call-parser deepseek_v31 --chat-template /models/DeepSeek-V3.1-Terminus/tool_chat_template_deepseekv31.jinja ``` ### Steps to Reproduce 1. Start vLLM with DeepSeek V3.1 model and `deepseek_v31` tool parser 2. Create a multi-turn conversation with tool calls (10+ rounds recommended) 3. Alternate between different tool calls in each round 4. Observe the leading whitespace in assistant responses ### Expected Behavior Assistant responses should have **no leading whitespace** regardless of the number of conversation rounds. The content should be clean and consistent across all turns. ### Actual...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: l calling conversations bug;stale ### Your current environment - **vLLM Version**: nightly (commit: `0b25498990f01ea2553c02731d6e2ce2d550156a`) - **Model**: DeepSeek-V3.1-Terminus - **Tool Parser**: `deepseek_v31` - **C...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: sion**: nightly (commit: `0b25498990f01ea2553c02731d6e2ce2d550156a`) - **Model**: DeepSeek-V3.1-Terminus - **Tool Parser**: `deepseek_v31` - **Chat Template**: `tool_chat_template_deepseekv31.jinja` - **Request Mode**:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ing whitespace accumulation in multi-turn tool calling conversations bug;stale ### Your current environment - **vLLM Version**: nightly (commit: `0b25498990f01ea2553c02731d6e2ce2d550156a`) - **Model**: DeepSeek-V3.1-Ter...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: eek-V3.1-Terminus/tool_chat_template_deepseekv31.jinja ``` ### Steps to Reproduce 1. Start vLLM with DeepSeek V3.1 model and `deepseek_v31` tool parser 2. Create a multi-turn conversation with tool calls (10+ rounds rec...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ges ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
