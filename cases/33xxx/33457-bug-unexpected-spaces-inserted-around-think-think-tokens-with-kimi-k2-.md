# vllm-project/vllm#33457: [Bug]: Unexpected spaces inserted around `<think>`/`</think>` tokens with Kimi K2-Thinking / K2.5

| 字段 | 值 |
| --- | --- |
| Issue | [#33457](https://github.com/vllm-project/vllm/issues/33457) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Unexpected spaces inserted around `<think>`/`</think>` tokens with Kimi K2-Thinking / K2.5

### Issue 正文摘录

### Your current environment vLLM 2b465570e6dd327e8422ef9c87e9b2b1454ceaed, tested with moonshotai/Kimi-K2-Thinking and moonshotai/Kimi-K2.5. ### 🐛 Describe the bug When using Kimi K2-Thinking or K2.5 with default settings, vLLM inserts spurious spaces around thinking tokens. For example, model output ` ok 1` becomes `' ok 1'` with spaces everywhere. ## The problem The `spaces_between_special_tokens` parameter defaults to `True`, which causes `_convert_tokens_to_string_with_added_encoders()` to join token groups with `' '.join(sub_texts)`. This affects all tokens in the tokenizer's `added_tokens_decoder`, regardless of whether they have `special=True`. For Kimi models, ` ` and ` ` are added tokens (IDs 163606/163607) but not marked as special. The current behavior inserts spaces around them, breaking the output format. ## Why this is unexpected The parameter name `spaces_between_special_tokens` suggests it only affects tokens marked as `special=True`, but it actually affects all added tokens. This also doesn't match native tokenizer behavior: `tokenizer.decode([think_end_id, digit_id])` produces ` 1` without spaces, but vLLM produces ` 1`. The leading space propagates through the...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ok 1'` with spaces everywhere. ## The problem The `spaces_between_special_tokens` parameter defaults to `True`, which causes `_convert_tokens_to_string_with_added_encoders()` to join token groups with `' '.join(sub_text...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: tings, vLLM inserts spurious spaces around thinking tokens. For example, model output ` ok 1` becomes `' ok 1'` with spaces everywhere. ## The problem The `spaces_between_special_tokens` parameter defaults to `True`, wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: in(sub_texts)`. This affects all tokens in the tokenizer's `added_tokens_decoder`, regardless of whether they have `special=True`. For Kimi models, ` ` and ` ` are added tokens (IDs 163606/163607) but not marked as spec...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: Fireworks and Together.ai shows the same behavior in streaming mode. ## Reproducer ```python from transformers import AutoTokenizer from vllm.tokenizers.detokenizer_utils import _convert_tokens_to_string_with_added_enco...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
