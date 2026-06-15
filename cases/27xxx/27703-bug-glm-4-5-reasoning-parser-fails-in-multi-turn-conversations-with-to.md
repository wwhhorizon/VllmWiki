# vllm-project/vllm#27703: Bug: GLM-4.5 Reasoning Parser Fails in Multi-Turn Conversations with Tool Calls

| 字段 | 值 |
| --- | --- |
| Issue | [#27703](https://github.com/vllm-project/vllm/issues/27703) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Bug: GLM-4.5 Reasoning Parser Fails in Multi-Turn Conversations with Tool Calls

### Issue 正文摘录

# Bug: GLM-4.5 Reasoning Parser Fails in Multi-Turn Conversations with Tool Calls ## Environment - **vLLM Version**: 0.11.0 - **Model**: GLM-4.5 or similar reasoning models - **Server Args**: `--reasoning-parser glm45` - **OpenAI Client Version**: 2.6.1 ## Description The GLM-4.5 reasoning parser (`--reasoning-parser glm45`) works correctly for single-turn conversations and simple multi-turn conversations, but **fails to properly separate reasoning from content in Turn 3+ of conversations involving function/tool calls**. ### Expected Behavior In all conversation turns, reasoning content wrapped in ` ... ` tags should: 1. Be stripped from the visible content 2. Be sent in the `reasoning_content` field of the streaming response 3. Never appear in the regular `content` field ### Actual Behavior **Turn 3** (after tool execution): The model's reasoning appears in the `content` field with visible ` ` tags instead of being properly separated into the `reasoning_content` field. ## Reproduction ### Test Case 1: Simple Turn 3 Scenario ```python import openai client = openai.OpenAI( api_key="test", base_url="http://127.0.0.1:8888/v1" ) tools = [ { "type": "function", "function": { "name": "c...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ils in Multi-Turn Conversations with Tool Calls ## Environment - **vLLM Version**: 0.11.0 - **Model**: GLM-4.5 or similar reasoning models - **Server Args**: `--reasoning-parser glm45` - **OpenAI Client Version**: 2.6.1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ersations with Tool Calls ## Environment - **vLLM Version**: 0.11.0 - **Model**: GLM-4.5 or similar reasoning models - **Server Args**: `--reasoning-parser glm45` - **OpenAI Client Version**: 2.6.1 ## Description The GL...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ponse after tool execution): - ❌ `reasoning_content` field is empty or False - ❌ ` ` tags appear in `content` field - ❌ Reasoning is visible to end users ## Root Cause Hypothesis The reasoning parser appears to lose sta...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ❌ | **FAIL** | ### Detailed Observations **Turn 1** (Initial tool call request): - ✅ `reasoning_content` field populated correctly - ✅ Tool call executed properly - ✅ No ` ` tags in content **Turn 2** (Tool result proce...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: erly separated into the `reasoning_content` field. ## Reproduction ### Test Case 1: Simple Turn 3 Scenario ```python import openai client = openai.OpenAI( api_key="test", base_url="http://127.0.0.1:8888/v1" ) tools = [...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
