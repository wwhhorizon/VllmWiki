# vllm-project/vllm#16646: [Bug]: using TP = 16 to serving deepseek-v3 in 2*H20 On Ray cluster,  get EngineCore exception

| 字段 | 值 |
| --- | --- |
| Issue | [#16646](https://github.com/vllm-project/vllm/issues/16646) |
| 状态 | closed |
| 标签 | bug;ray;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;kernel;moe;quantization |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: using TP = 16 to serving deepseek-v3 in 2*H20 On Ray cluster,  get EngineCore exception

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug the error message is: INFO 04-15 13:36:47 [__init__.py:239] Automatically detected platform cuda. INFO 04-15 13:36:48 [api_server.py:1034] vLLM API server version 0.8.3.dev358+g24bc0a9f7 INFO 04-15 13:36:48 [api_server.py:1035] args: Namespace(subparser='serve', model_tag=' /huggingface_models/DeepSeek-V3/', config='', host=None, port=8000, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, enable_ssl_refresh=False, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model=' /huggingface_models/DeepSeek-V3/', task='auto', tokenizer=None, hf_config_path=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='a...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=32768, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', di...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: g deepseek-v3 in 2*H20 On Ray cluster, get EngineCore exception bug;ray;stale ### Your current environment ### 🐛 Describe the bug the error message is: INFO 04-15 13:36:47 [__init__.py:239] Automatically detected platfo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: platform cuda. INFO 04-15 13:36:48 [api_server.py:1034] vLLM API server version 0.8.3.dev358+g24bc0a9f7 INFO 04-15 13:36:48 [api_server.py:1035] args: Namespace(subparser='serve', model_tag=' /huggingface_models/DeepSee...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: O 04-15 13:36:48 [api_server.py:1035] args: Namespace(subparser='serve', model_tag=' /huggingface_models/DeepSeek-V3/', config='', host=None, port=8000, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: INFO 04-15 13:36:47 [__init__.py:239] Automatically detected platform cuda. INFO 04-15 13:36:48 [api_server.py:1034] vLLM API server version 0.8.3.dev358+g24bc0a9f7 INFO 04-15 13:36:48 [api_server.py:1035] args: Namespa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
