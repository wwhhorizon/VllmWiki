# vllm-project/vllm#19645: [Usage]: V1 can not support for macOS with Apple silicon.

| 字段 | 值 |
| --- | --- |
| Issue | [#19645](https://github.com/vllm-project/vllm/issues/19645) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: V1 can not support for macOS with Apple silicon.

### Issue 正文摘录

### Your current environment When I use lastest dev commit, and use V1 start. Send a request, and throw this error. ``` INFO 06-14 14:17:31 [logger.py:43] Received request cmpl-849fc2e67e9d4680a9ca0fecbad24d3f-0: prompt: '你好，你叫什', params: SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.1, temperature=0.0, top_p=1.0, top_k=0, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=True, max_tokens=20, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None, extra_args=None), prompt_token_ids: [108386, 3837, 56568, 99882, 99217], prompt_embeds shape: None, lora_request: None, prompt_adapter_request: None. INFO 06-14 14:17:31 [async_llm.py:271] Added request cmpl-849fc2e67e9d4680a9ca0fecbad24d3f-0. ERROR 06-14 14:17:31 [dump_input.py:69] Dumping input data ERROR 06-14 14:17:31 [dump_input.py:71] V1 LLM engine (v0.1.dev7115+g7e8d97d) with config: model='/Users/miaochangyu/workspace/models/Qwen/Qwen2.5-0.5B-Instruct', speculative_config=None, tokenizer='/Users/miaochangyu/workspace/models/Qw...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Usage]: V1 can not support for macOS with Apple silicon. usage;stale ### Your current environment When I use lastest dev commit, and use V1 start. Send a request, and throw this error. ``` INFO 06-14 14:17:31 [logger.p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ax_tokens=20, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None, extra_args=None), prompt_token_ids: [1083...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: 4 14:17:31 [dump_input.py:71] V1 LLM engine (v0.1.dev7115+g7e8d97d) with config: model='/Users/miaochangyu/workspace/models/Qwen/Qwen2.5-0.5B-Instruct', speculative_config=None, tokenizer='/Users/miaochangyu/workspace/m...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: rride_neuron_config={}, tokenizer_revision=None, trust_remote_code=True, dtype=torch.float16, max_seq_len=1024, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable_c...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: , stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=True, max_tokens=20, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=Tr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
