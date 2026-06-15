# vllm-project/vllm#21987: [Bug]: min_tokens is not respected when stop is triggered early

| 字段 | 值 |
| --- | --- |
| Issue | [#21987](https://github.com/vllm-project/vllm/issues/21987) |
| 状态 | closed |
| 标签 | bug;good first issue |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: min_tokens is not respected when stop is triggered early

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # Observed behavior When both min_tokens and stop are specified in the sampling parameters, vLLM currently stops generation as soon as a stop sequence is encountered — even if the min_tokens threshold has not yet been reached. # Expected behavior The model should continue generating tokens until both conditions are satisfied: - At least min_tokens tokens have been generated, and - A stop sequence is encountered. prompts = [ "test/", ] sampling_params = SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.0, top_p=1.0, top_k=0, min_p=0.0, seed=None, stop=['\n'], stop_token_ids=[], bad_words=[], include_stop_str_in_output=True, ignore_eos=False, max_tokens=200, min_tokens=200, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None, extra_args=None) llm = LLM(model="ibm-granite/granite-3.3-8b-instruct") outputs = llm.generate(prompts, sampling_params) # Print outputs "generated_text": "test\n" "generated_token_count": 2, "input_token_count": 3, "stop_reason": "stop" ### Before submitting a n...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: scribe the bug # Observed behavior When both min_tokens and stop are specified in the sampling parameters, vLLM currently stops generation as soon as a stop sequence is encountered — even if the min_tokens threshold has...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: op" ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: oken_ids=[], bad_words=[], include_stop_str_in_output=True, ignore_eos=False, max_tokens=200, min_tokens=200, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_p...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: min_tokens threshold has not yet been reached. # Expected behavior The model should continue generating tokens until both conditions are satisfied: - At least min_tokens tokens have been generated, and - A stop sequence...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: been generated, and - A stop sequence is encountered. prompts = [ "test/", ] sampling_params = SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.0, top_p=1.0, top_k=0...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
