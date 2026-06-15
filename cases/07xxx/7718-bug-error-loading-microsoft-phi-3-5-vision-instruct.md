# vllm-project/vllm#7718: [Bug]: Error loading microsoft/Phi-3.5-vision-instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#7718](https://github.com/vllm-project/vllm/issues/7718) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;operator;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error loading microsoft/Phi-3.5-vision-instruct

### Issue 正文摘录

### Your current environment vllm version: `Version: 0.5.4` ### 🐛 Describe the bug Repro command: ``` vllm serve microsoft/Phi-3.5-vision-instruct --trust-remote-code --max-model-len 4096 ``` Error: ``` vllm serve microsoft/Phi-3.5-vision-instruct --trust-remote-code --max-model-len 4096 INFO 08-21 04:43:37 api_server.py:339] vLLM API server version 0.5.4 INFO 08-21 04:43:37 api_server.py:340] args: Namespace(model_tag='microsoft/Phi-3.5-vision-instruct', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, model='microsoft/Phi-3.5-vision-instruct', tokenizer=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=True, download_dir=None, load_format='auto', dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=4096...

## 现有链接修复摘要

#7710 [Model] Fix Phi-3.5-vision-instruct 'num_crops' issue | #7916 [Bugfix] Fix phi3v incorrect image_idx when using async engine

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: False, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, num_speculative_tokens=None, speculative_draft_tensor_parallel_si...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e='auto', trust_remote_code=True, download_dir=None, load_format='auto', dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=4096, guided_decoding_backend='outlines', distributed_executor_ba...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: auto', quantization_param_path=None, max_model_len=4096, guided_decoding_backend='outlines', distributed_executor_backend=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=1, max_parallel_loadin...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ct', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ` vllm serve microsoft/Phi-3.5-vision-instruct --trust-remote-code --max-model-len 4096 ``` Error: ``` vllm serve microsoft/Phi-3.5-vision-instruct --trust-remote-code --max-model-len 4096 INFO 08-21 04:43:37 api_server...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#7710](https://github.com/vllm-project/vllm/pull/7710) | closes_keyword | 0.95 | [Model] Fix Phi-3.5-vision-instruct 'num_crops' issue | FIX #7718 **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <details> <!-- inside this <details> section, markdown rendering do |
| [#7916](https://github.com/vllm-project/vllm/pull/7916) | closes_keyword | 0.95 | [Bugfix] Fix phi3v incorrect image_idx when using async engine | Fix a bug reported in #7718 - The incorrect `image_idx` breaks the phi3-vision model server deployment, which doesn't pass prompt to input_processor directly. **BEFORE SUBMITTI |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
