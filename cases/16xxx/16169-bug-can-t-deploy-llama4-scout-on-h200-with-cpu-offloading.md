# vllm-project/vllm#16169: [Bug]: Can't deploy Llama4 Scout on H200 with cpu offloading

| 字段 | 值 |
| --- | --- |
| Issue | [#16169](https://github.com/vllm-project/vllm/issues/16169) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cuda;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Can't deploy Llama4 Scout on H200 with cpu offloading

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am having the following logs: ```text chat-completions8 | INFO 04-07 01:01:32 [__init__.py:239] Automatically detected platform cuda. chat-completions8 | INFO 04-07 01:01:40 [api_server.py:1034] vLLM API server version 0.8.3 chat-completions8 | INFO 04-07 01:01:40 [api_server.py:1035] args: Namespace(host=None, port=8000, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, enable_ssl_refresh=False, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='meta-llama/Llama-4-Scout-17B-16E', task='auto', tokenizer=None, hf_config_path=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: completions8 | INFO 04-07 01:01:40 [api_server.py:1034] vLLM API server version 0.8.3 chat-completions8 | INFO 04-07 01:01:40 [api_server.py:1035] args: Namespace(host=None, port=8000, uvicorn_log_level='info', disable_...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=256000, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', d...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Can't deploy Llama4 Scout on H200 with cpu offloading bug ### Your current environment ### 🐛 Describe the bug I am having the following logs: ```text chat-completions8 | INFO 04-07 01:01:32 [__init__.py:239] Auto...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='meta-llama/Llama-4-Scout-17B-16E', t...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: =None, port=8000, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapter...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
