# vllm-project/vllm#32557: [Bug]: SamplingParams bad_words to _bad_words_token_ids

| 字段 | 值 |
| --- | --- |
| Issue | [#32557](https://github.com/vllm-project/vllm/issues/32557) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: SamplingParams bad_words to _bad_words_token_ids

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi Team, I think `update_from_tokenizer` of `SamplingParams` has the potential to convert `bad_words` to `_bad_words_token_ids` incorrectly. This [line](https://github.com/vllm-project/vllm/blob/2f03035a618f03c412b8a540606c7b1816839390/vllm/sampling_params.py#L530) checks if the number of token ids is the same with/without a leading space. However, in some models, a leading space is usually converted into a single token. Without a leading space, the word is converted into multiple tokens. For example, using `Qwen/Qwen3-0.6B`, if I set `bad_words=['exaggerated']`, the code first does not add a leading space and encodes the word as `[327, 10114, 657]`. Then, it adds a leading space and encodes the word as `[61158]`. Now, because the length of `[61158]` dose not equal to the length of `[327, 10114, 657]`, the code fail to add `[61158]` as one of the `_bad_words_token_ids`. This is causing tokens with a leading space, like `Ġexaggerated`, to never be added to `_bad_words_token_ids`. A manual solution is to set `_bad_words_token_ids` with token ids. But since `bad_words` is a more straightforward argument of `SamplingParams`, it is be...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: of token ids is the same with/without a leading space. However, in some models, a leading space is usually converted into a single token. Without a leading space, the word is converted into multiple tokens. For example,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 886 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
