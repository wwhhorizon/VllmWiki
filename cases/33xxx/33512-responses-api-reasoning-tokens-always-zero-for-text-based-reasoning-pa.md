# vllm-project/vllm#33512: Responses API reasoning_tokens always zero for text-based reasoning parsers

| 字段 | 值 |
| --- | --- |
| Issue | [#33512](https://github.com/vllm-project/vllm/issues/33512) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Responses API reasoning_tokens always zero for text-based reasoning parsers

### Issue 正文摘录

## Summary `/v1/responses` always reports `reasoning_tokens: 0` for text-based reasoning parsers such as Qwen3 and DeepSeek R1, even when the model emits ` ... ` reasoning text. Usage accounting only recognizes Harmony channels (`analysis`/`commentary`), so Simple/Parsable contexts never count text-delimited reasoning spans. ## Impact - Billing/telemetry and dashboards under-report reasoning usage for text-based reasoning models. - Parity gap: Harmony models get correct reasoning token counts while text-tag models do not. - Downstream rate limits/quotas that rely on reasoning_tokens get misleadingly low values. ## Root cause `HarmonyContext._update_num_reasoning_tokens()` counts Harmony channels, but `/v1/responses` in Simple/Parsable contexts lacks token-based counting. The parser output is parsed for reasoning text, but the token count is never derived from ` ` start/end markers. ## Proposed fix (implemented locally) - Add a `count_reasoning_tokens(token_ids)` hook to `ReasoningParser` (default no-op). - Implement span counting in `BaseThinkingReasoningParser` between start/end thinking token IDs (used by Qwen3, DeepSeek R1, etc.). - Accumulate output token IDs in `SimpleContext...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: s reports `reasoning_tokens: 0` for text-based reasoning parsers such as Qwen3 and DeepSeek R1, even when the model emits ` ... ` reasoning text. Usage accounting only recognizes Harmony channels (`analysis`/`commentary...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: lated - PR #31094 touches chat/harmony reasoning paths; this issue is specific to `/v1/responses` Simple/Parsable contexts and text-delimited reasoning tags.
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: put. 3. Observe `usage.output_tokens_details.reasoning_tokens` == 0. ## Tests (performed locally, CPU environment) - `pytest tests/entrypoints/openai/test_serving_responses.py::test_reasoning_tokens_counted_for_text_rea...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
