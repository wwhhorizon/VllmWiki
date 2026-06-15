# vllm-project/vllm#20567: [Usage]: --speculative-config is not compatible with "response_format":{"type": "json_object"}

| 字段 | 值 |
| --- | --- |
| Issue | [#20567](https://github.com/vllm-project/vllm/issues/20567) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;sampling_logits;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;sampling |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: --speculative-config is not compatible with "response_format":{"type": "json_object"}

### Issue 正文摘录

### Your current environment INFO 07-07 17:47:39 [__init__.py:239] Automatically detected platform cuda. INFO 07-07 17:47:41 [api_server.py:1043] vLLM API server version 0.8.5.post1 ```bash SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.1, temperature=0.7, top_p=0.8, top_k=20, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=2000, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=GuidedDecodingParams(json=None, regex=None, choice=None, grammar=None, json_object=True, backend=None, whitespace_pattern=None, structural_tag=None), extra_args=None), prompt_token_ids: None, lora_request: None, prompt_adapter_request: None. INFO: 192.168.50.222:56078 - "POST /v1/chat/completions HTTP/1.1" 200 OK INFO 07-07 18:10:20 [engine.py:310] Added request chatcmpl-77095ff17d574852add36412c049d1f1. ERROR 07-07 18:10:20 [serving_chat.py:885] Error in chat completion stream generator. ERROR 07-07 18:10:20 [serving_chat.py:885] Traceback (most recent call last): ERROR 07-07 18:10:2...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Usage]: --speculative-config is not compatible with "response_format":{"type": "json_object"} usage;stale ### Your current environment INFO 07-07 17:47:39 [__init__.py:239] Automatically detected platform cuda. INFO 07...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: --speculative-config is not compatible with "response_format":{"type": "json_object"} usage;stale ### Your current environment INFO 07-07 17:47:39 [__init__.py:239] Automatically detected platform cuda. INFO 07...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: platform cuda. INFO 07-07 17:47:41 [api_server.py:1043] vLLM API server version 0.8.5.post1 ```bash SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.1, temperature=0.7, top_p=0.8, to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nt INFO 07-07 17:47:39 [__init__.py:239] Automatically detected platform cuda. INFO 07-07 17:47:41 [api_server.py:1043] vLLM API server version 0.8.5.post1 ```bash SamplingParams(n=1, presence_penalty=0.0, frequency_pen...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: , stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=2000, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
