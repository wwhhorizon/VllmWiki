# vllm-project/vllm#41067: [Bug]: KimiK2ReasoningParser silently corrupts streaming output when stop sequences buffer text

| 字段 | 值 |
| --- | --- |
| Issue | [#41067](https://github.com/vllm-project/vllm/issues/41067) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: KimiK2ReasoningParser silently corrupts streaming output when stop sequences buffer text

### Issue 正文摘录

**Describe the bug** `KimiK2ReasoningParser.extract_reasoning_streaming()` calls `delta_text.find(token)` after checking `token_id in delta_token_ids`, but does not guard against `find()` returning `-1`. When `stop` sequences are configured, the engine sets `output_text_buffer_length > 0`, which causes token IDs to arrive in `delta_token_ids` **before** the corresponding text is flushed into `delta_text`. In that window, `find()` returns `-1`, and the text is split at the wrong position: ```python # Line 215-221 — path end_index = delta_text.find(self._end_token) # returns -1 reasoning = delta_text[:end_index] # delta_text[:-1] → drops last char content = delta_text[end_index + len(...):] # delta_text[7:] → wrong slice # Line 223-226 — path tool_index = delta_text.find(self._tool_section_start_token) # returns -1 reasoning = delta_text[:tool_index] # delta_text[:-1] → drops last char content = delta_text[tool_index:] # delta_text[-1:] → only last char ``` The same root cause was fixed for `BaseThinkingReasoningParser`, `DeepSeekR1ReasoningParser`, `Ernie45ReasoningParser`, and `Step3p5ReasoningParser` by PR #39044 and for `Step3ReasoningParser` by PR #40352, but `KimiK2ReasoningPa...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: arser` was not included. **Reproduction** ```python from unittest.mock import MagicMock from vllm.reasoning.kimi_k2_reasoning_parser import KimiK2ReasoningParser tokenizer = MagicMock() tokenizer.get_vocab.return_value...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: es not guard against `find()` returning `-1`. When `stop` sequences are configured, the engine sets `output_text_buffer_length > 0`, which causes token IDs to arrive in `delta_token_ids` **before** the corresponding tex...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ReasoningParser` was not included. **Reproduction** ```python from unittest.mock import MagicMock from vllm.reasoning.kimi_k2_reasoning_parser import KimiK2ReasoningParser tokenizer = MagicMock() tokenizer.get_vocab.ret...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
