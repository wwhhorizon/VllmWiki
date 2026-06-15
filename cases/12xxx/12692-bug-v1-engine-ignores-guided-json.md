# vllm-project/vllm#12692: [Bug]: V1 engine ignores guided json

| 字段 | 值 |
| --- | --- |
| Issue | [#12692](https://github.com/vllm-project/vllm/issues/12692) |
| 状态 | closed |
| 标签 | bug;stale;v1 |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: V1 engine ignores guided json

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When making a request with to the OpenAi compatible Api with the extra fields for guided_json generation like so: ``` { "model": "Qwen/Qwen2-VL-72B-Instruct-GPTQ-Int4", "messages": [ { "role": "user", "content": "what is the height of the eiffel tower" } ], "guided_json": { "type": "object", "properties": { "height": { "type": "number" } }, "required": [ "height" ] } } ``` The output simply ignores the guided decoding paramter. When switching back to V0 it works fine. Here are the logs from the vllm server: ``` `INFO 02-03 05:59:31 logger.py:37] Received request chatcmpl-178de64763e84ddd81a9f6f62ee0f4c3: prompt: ' system\nYou are a helpful assistant. \n user\nwhat is the height of the eiffel tower \n assistant\n', params: SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=1.0, top_p=1.0, top_k=-1, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=32739, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, trunc...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: tokens=32739, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=GuidedDecodingParams(json={'type': 'object', 'p...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: n generation like so: ``` { "model": "Qwen/Qwen2-VL-72B-Instruct-GPTQ-Int4", "messages": [ { "role": "user", "content": "what is the height of the eiffel tower" } ], "guided_json": { "type": "object", "properties": { "h...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: V1 engine ignores guided json bug;stale;v1 ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When making a request with to the OpenAi compatible Api with the extra fields for...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ': ['height']}, regex=None, choice=None, grammar=None, json_object=None, backend=None, whitespace_pattern=None)), prompt_token_ids: None, lora_request: None, prompt_adapter_request: None. DEBUG 02-03 05:59:31 async_llm_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
