# vllm-project/vllm#15016: [Usage]: {'object': 'error', 'message': 'Prompt cannot be empty', 'type': 'BadRequestError', 'param': None, 'code': 400}

| 字段 | 值 |
| --- | --- |
| Issue | [#15016](https://github.com/vllm-project/vllm/issues/15016) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;quantization;sampling |
| 症状 | oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: {'object': 'error', 'message': 'Prompt cannot be empty', 'type': 'BadRequestError', 'param': None, 'code': 400}

### Issue 正文摘录

``` (venv-llm) azureuser@a100gpu:/home/mata/llm/src/benchmark/vllm$ vllm serve google/gemma-3-12b-it --chat-template /home/mata/llm/data/models/chat_temp/unsloth--gemma-3-12b-it.jinja --gpu-memory-utiliza tion 0.9 --max_model_len 8192 INFO 03-18 08:50:29 [__init__.py:256] Automatically detected platform cuda. INFO 03-18 08:50:31 [api_server.py:972] vLLM API server version 0.8.0rc3.dev6+g53a0cf8b INFO 03-18 08:50:31 [api_server.py:973] args: Namespace(subparser='serve', model_tag='google/gemma-3-12b-it', config='', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template='/home/mata/llm/data/models/chat_temp/unsloth--gemma-3-12b-it.jinja', chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, enable_ssl_refresh=False, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='google/gemma-...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: ) azureuser@a100gpu:/home/mata/llm/src/benchmark/vllm$ vllm serve google/gemma-3-12b-it --chat-template /home/mata/llm/data/models/chat_temp/unsloth--gemma-3-12b-it.jinja --gpu-memory-utiliza tion 0.9 --max_model_len 81...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=8192, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', dis...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: e]: {'object': 'error', 'message': 'Prompt cannot be empty', 'type': 'BadRequestError', 'param': None, 'code': 400} usage ``` (venv-llm) azureuser@a100gpu:/home/mata/llm/src/benchmark/vllm$ vllm serve google/gemma-3-12b...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: dtype='auto', kv_cache_dtype='auto', max_model_len=8192, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: d platform cuda. INFO 03-18 08:50:31 [api_server.py:972] vLLM API server version 0.8.0rc3.dev6+g53a0cf8b INFO 03-18 08:50:31 [api_server.py:973] args: Namespace(subparser='serve', model_tag='google/gemma-3-12b-it', conf...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
