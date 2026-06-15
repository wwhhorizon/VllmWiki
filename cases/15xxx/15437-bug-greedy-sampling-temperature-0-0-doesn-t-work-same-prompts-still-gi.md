# vllm-project/vllm#15437: [Bug]: Greedy sampling (temperature=0.0) doesn't work, same prompts still give different outputs. (gemma-3-4it, ...)

| 字段 | 值 |
| --- | --- |
| Issue | [#15437](https://github.com/vllm-project/vllm/issues/15437) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Greedy sampling (temperature=0.0) doesn't work, same prompts still give different outputs. (gemma-3-4it, ...)

### Issue 正文摘录

### Your current environment vllm==0.8.1 transformers=4.50.0 GPU A100 40 GB model gemma-3-4b-it SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0, top_p=1.0, top_k=-1, min_p=0.0, seed=42, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=1024, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None, extra_args=None) ### 🐛 Describe the bug I see that greedy sampling with temperature = 0.0 is causing different results to be generated each time even though it is the same prompt. I hope this problem can be solved. And if more specifically, which models actually support greedy sampling. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: stale ### Your current environment vllm==0.8.1 transformers=4.50.0 GPU A100 40 GB model gemma-3-4b-it SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0, top_p=1.0, to...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: mperature=0.0) doesn't work, same prompts still give different outputs. (gemma-3-4it, ...) bug;stale ### Your current environment vllm==0.8.1 transformers=4.50.0 GPU A100 40 GB model gemma-3-4b-it SamplingParams(n=1, pr...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: Greedy sampling (temperature=0.0) doesn't work, same prompts still give different outputs. (gemma-3-4it, ...) bug;stale ### Your current environment vllm==0.8.1 transformers=4.50.0 GPU A100 40 GB model gemma-3-4b-it Sam...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: _tokens=1024, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None, extra_args=None) ### 🐛 Describe the bug I...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: , stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=1024, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
