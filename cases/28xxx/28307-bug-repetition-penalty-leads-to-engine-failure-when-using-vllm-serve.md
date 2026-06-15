# vllm-project/vllm#28307: [Bug]: `repetition_penalty` leads to engine failure when using vllm serve...

| 字段 | 值 |
| --- | --- |
| Issue | [#28307](https://github.com/vllm-project/vllm/issues/28307) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;kernel;operator;quantization;sampling |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `repetition_penalty` leads to engine failure when using vllm serve...

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vLLM (0.11.0): vllm serve Qwen/Qwen3-30B-A3B-Instruct (Issue across multiple models) When adding `repetition_penalty` to request payload, the engine crashes leading to the below errors. ``` (APIServer pid=1) INFO 11-07 08:50:24 [logger.py:40] Received request cmpl-4d1abf620f01dad2f8fd2946e6d0ee3a-0: prompt: None, params: SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.6, top_p=0.9, top_k=0, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=16, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, structured_outputs=None, extra_args=None), prompt_token_ids: None, prompt_embeds shape: None, lora_request: None. (APIServer pid=1) INFO 11-07 08:50:24 [async_llm.py:316] Added request cmpl-4d1abf620f01dad2f8fd2946e6d0ee3a-0. (APIServer pid=1) INFO 11-07 08:50:25 [loggers.py:127] Engine 000: Avg prompt throughput: 0.5 tokens/s, Avg generation throughput: 0.1 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ax_tokens=16, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, structured_outputs=None, extra_args=None), prompt_token_ids: No...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: repetition_penalty` leads to engine failure when using vllm serve... bug;stale ### Your current environment ### 🐛 Describe the bug vLLM (0.11.0): vllm serve Qwen/Qwen3-30B-A3B-Instruct (Issue across multiple models) Whe...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: , stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=16, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=T...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: urrent environment ### 🐛 Describe the bug vLLM (0.11.0): vllm serve Qwen/Qwen3-30B-A3B-Instruct (Issue across multiple models) When adding `repetition_penalty` to request payload, the engine crashes leading to the below...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ions. performance attention_kv_cache;ci_build;frontend_api;model_support;quantization;sampling_logits;scheduler_memory cache;cuda;kernel;operator;quantization;sampling build_error;crash;slowdown dtype;env_dependency;mem...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
