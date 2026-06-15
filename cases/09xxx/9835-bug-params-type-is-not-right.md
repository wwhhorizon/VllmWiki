# vllm-project/vllm#9835: [Bug] params Type is not right?

| 字段 | 值 |
| --- | --- |
| Issue | [#9835](https://github.com/vllm-project/vllm/issues/9835) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug] params Type is not right?

### Issue 正文摘录

### Your current environment vllm 0.6.3 ### 🐛 Describe the bug here, params=SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.25, temperature=0.7, top_p=0.8, top_k=-1, min_p=0.0, seed=None, stop=[], stop_token_ids=[151645], include_stop_str_in_output=False, ignore_eos=False, max_tokens=2048, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None), guided_decoding=None but when excute the follows code, it raise error: "Either SamplingParams or PoolingParams must be provided # Create a SequenceGroup based on SamplingParams or PoolingParams if isinstance(params, SamplingParams): seq_group = self._create_sequence_group_with_sampling( request_id, seq, params, arrival_time=arrival_time, lora_request=lora_request, trace_headers=trace_headers, prompt_adapter_request=prompt_adapter_request, encoder_seq=encoder_seq, priority=priority) elif isinstance(params, PoolingParams): seq_group = self._create_sequence_group_with_pooling( request_id, seq, params, arrival_time=arrival_time, lora_request=lora_request, prompt_adapter_request=prompt_adapter_request, encoder_seq=encoder_...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug] params Type is not right? bug;stale ### Your current environment vllm 0.6.3 ### 🐛 Describe the bug here, params=SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.25, temperature...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: _tokens=2048, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None), guided_decoding=None but when excute the follows code, it rais...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: .") ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: eed=None, stop=[], stop_token_ids=[151645], include_stop_str_in_output=False, ignore_eos=False, max_tokens=2048, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
