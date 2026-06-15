# vllm-project/vllm#38855: [Bug]: Gemma4 reasoning parser fails to separate reasoning_content — <|channel> tokens stripped before parsing

| 字段 | 值 |
| --- | --- |
| Issue | [#38855](https://github.com/vllm-project/vllm/issues/38855) |
| 状态 | open |
| 标签 |  |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | frontend_api;hardware_porting;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | fp8;quantization |
| 症状 | mismatch |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma4 reasoning parser fails to separate reasoning_content — <\|channel> tokens stripped before parsing

### Issue 正文摘录

## Bug Description The `Gemma4ReasoningParser` (added in PR #38826) fails to populate `reasoning_content` in the OpenAI chat completions response. All thinking content ends up in `content` instead. ## Root Cause The model correctly generates ` thought\n...reasoning... ` tokens, confirmed via logprobs. However, vLLM's text decoding strips these special tokens (`skip_special_tokens=True`) before the reasoning parser sees the text. The `Gemma4ReasoningParser` defines `start_token` and `end_token` as text properties (`" "` / `" "`), but unlike `Qwen3ReasoningParser`, it does **not** implement `start_token_id` / `end_token_id` for token-level matching in the streaming path. The base class `extract_reasoning_streaming` receives text without special tokens, so the channel markers are invisible. The unit tests in `tests/reasoning/test_gemma4_reasoning_parser.py` pass because they inject ` ` as literal text in the test strings — this doesn't match actual serving behavior where the tokens are decoded with `skip_special_tokens=True`. ## Expected Behavior ```json { "choices": [{ "message": { "reasoning_content": "The user is asking...", "content": "2 + 2 = 4" } }] } ``` ## Actual Behavior ```...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: (0.18.2rc1.dev69+g08ed2b968) vllm serve google/gemma-4-26B-A4B-it \ --quantization fp8 \ --reasoning-parser gemma4 \ --default-chat-template-kwargs '{"enable_thinking": true}' curl http://localhost:8000/v1/chat/completi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 9+g08ed2b968 (built from main) - Model: google/gemma-4-26B-A4B-it - GPU: RTX PRO 6000 Blackwell - transformers: 5.5.0.dev0 (from git main) Also note: `Gemma4ToolParser.__init__` has a minor signature mismatch — takes `(...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Gemma4 reasoning parser fails to separate reasoning_content — <|channel> tokens stripped before parsing ## Bug Description The `Gemma4ReasoningParser` (added in PR #38826) fails to populate `reasoning_content` in...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: git main) Also note: `Gemma4ToolParser.__init__` has a minor signature mismatch — takes `(self, tokenizer)` but base class passes `(self, tokenizer, tools)`. Patched locally with `tools=None` default. correctness fronte...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: s, confirmed via logprobs. However, vLLM's text decoding strips these special tokens (`skip_special_tokens=True`) before the reasoning parser sees the text. The `Gemma4ReasoningParser` defines `start_token` and `end_tok...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
