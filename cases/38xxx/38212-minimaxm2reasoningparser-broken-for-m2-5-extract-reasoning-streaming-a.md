# vllm-project/vllm#38212: MiniMaxM2ReasoningParser broken for M2.5: extract_reasoning_streaming assumes no <think> start tag

| 字段 | 值 |
| --- | --- |
| Issue | [#38212](https://github.com/vllm-project/vllm/issues/38212) |
| 状态 | open |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> MiniMaxM2ReasoningParser broken for M2.5: extract_reasoning_streaming assumes no <think> start tag

### Issue 正文摘录

## Bug: `MiniMaxM2ReasoningParser` doesn't handle M2.5's ` ` start tag ### Description `MiniMaxM2ReasoningParser` overrides `extract_reasoning_streaming` with logic that assumes the model only generates ` ` (no opening ` ` tag). This was true for the original M2, but **M2.5 generates both ` ` and ` `**. The result: reasoning content (including raw ` ... ` tags) leaks into the `content` field, and `reasoning` / `reasoning_content` is always `null` — even with `include_reasoning: true`. The base class `BaseThinkingReasoningParser` already handles both tags correctly. The override in `MiniMaxM2ReasoningParser` is the sole cause of the bug. ### How to reproduce ```bash vllm serve MiniMaxAI/MiniMax-M2.5 \ --enable-auto-tool-choice \ --tool-call-parser minimax_m2 \ --reasoning-parser minimax_m2 ``` ```python # reasoning is None, tags leak into content response = client.chat.completions.create( model="MiniMaxAI/MiniMax-M2.5", messages=[{"role": "user", "content": "What is 2+2?"}], extra_body={"include_reasoning": True}, ) print(response.choices[0].message.reasoning) # None (should have content) print(response.choices[0].message.content) # " ... \n\n4" ``` ### Root cause [`MiniMaxM2Reason...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: in `MiniMaxM2ReasoningParser` is the sole cause of the bug. ### How to reproduce ```bash vllm serve MiniMaxAI/MiniMax-M2.5 \ --enable-auto-tool-choice \ --tool-call-parser minimax_m2 \ --reasoning-parser minimax_m2 ```...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ning/minimax_m2_reasoning_parser.py) overrides the base class with M2-specific logic: - It treats all content as reasoning until ` ` - It never checks for or strips the ` ` start tag - This causes the ` ` tag itself to...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: v0.17.1rc1.dev150 - Model: MiniMax-M2.5 (also reproduced with REAP-172B quantized variant) ### Workaround Use `--reasoning-parser deepseek_r1` instead, which handles both tags correctly.
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: g itself to be included in the reasoning text, and downstream the entire block ends up in `content` The base class `BaseThinkingReasoningParser.extract_reasoning_streaming` already handles both ` ` and ` ` correctly (ch...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ser` overrides `extract_reasoning_streaming` with logic that assumes the model only generates ` ` (no opening ` ` tag). This was true for the original M2, but **M2.5 generates both ` ` and ` `**. The result: reasoning c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
