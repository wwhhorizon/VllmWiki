# vllm-project/vllm#38488: [Bug]: `reasoning_content` silently dropped on incoming assistant messages

| 字段 | 值 |
| --- | --- |
| Issue | [#38488](https://github.com/vllm-project/vllm/issues/38488) |
| 状态 | open |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: `reasoning_content` silently dropped on incoming assistant messages

### Issue 正文摘录

### Your current environment Reproducible on current `main`. Bug is in `vllm/entrypoints/chat_utils.py`. ### 🐛 Describe the bug `_parse_chat_message_content` reads `reasoning` from incoming messages but never falls back to `reasoning_content`: ```python reasoning = message.get("reasoning") # never checks "reasoning_content" ``` PR #33635 (commit bf001da, "Interleaved thinking keeps compatibility with reasoning_content") added compat for the **output** side (writes both fields to `result_msg`), but missed the **input** read. `CustomChatCompletionMessageParam` also only declares `reasoning`. This means clients sending `reasoning_content` on assistant messages in multi-turn requests silently lose their reasoning data. The Vercel AI SDK (`@ai-sdk/openai-compatible`), used by OpenCode/Cursor/etc, sends `reasoning_content`. The docs promise it still works: > `reasoning` used to be called `reasoning_content`. For now, `reasoning_content` will continue to work. > — `docs/features/reasoning_outputs.md` The existing test (`test_multi_turn_tools_and_reasoning`) doesn't catch this because it round-trips via `choice.message.model_dump()`, which uses the output field name `reasoning`. **Impact:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: pped on incoming assistant messages ### Your current environment Reproducible on current `main`. Bug is in `vllm/entrypoints/chat_utils.py`. ### 🐛 Describe the bug `_parse_chat_message_content` reads `reasoning` from in...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: tly dropped on incoming assistant messages ### Your current environment Reproducible on current `main`. Bug is in `vllm/entrypoints/chat_utils.py`. ### 🐛 Describe the bug `_parse_chat_message_content` reads `reasoning`...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: r "" print("reasoning: ", "PASS" if SECRET in test("reasoning") else "FAIL") print("reasoning_content:", "PASS" if SECRET in test("reasoning_content") else "FAIL") # Expected: both PASS # Actual: reasoning PASS, reasoni...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: easoning`) doesn't catch this because it round-trips via `choice.message.model_dump()`, which uses the output field name `reasoning`. **Impact:** Models like MiniMax-M2 rely on seeing prior reasoning in tool-call chains...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
