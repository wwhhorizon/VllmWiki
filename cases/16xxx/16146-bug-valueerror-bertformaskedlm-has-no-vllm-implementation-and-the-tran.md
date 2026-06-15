# vllm-project/vllm#16146: [Bug]: ValueError: BertForMaskedLM has no vLLM implementation and the Transformers implementation is not compatible with vLLM.

| 字段 | 值 |
| --- | --- |
| Issue | [#16146](https://github.com/vllm-project/vllm/issues/16146) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;operator;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ValueError: BertForMaskedLM has no vLLM implementation and the Transformers implementation is not compatible with vLLM.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm serve "/data1/wangyao/models/yz_mind/emotion_bert" --trust-remote-code True --task score --port 48993 INFO 04-07 10:34:37 [__init__.py:239] Automatically detected platform cuda. INFO 04-07 10:34:38 [api_server.py:981] vLLM API server version 0.8.2 INFO 04-07 10:34:38 [api_server.py:982] args: Namespace(subparser='serve', model_tag='/data1/wangyao/models/yz_mind/emotion_bert', config='', host=None, port=48993, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, enable_ssl_refresh=False, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='/data1/wangyao/models/yz_mind/emotion_bert', task='score', tokenizer=None, hf_config_path=None, skip_tokenizer_init...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: ion and the Transformers implementation is not compatible with vLLM. bug;stale ### Your current environment ### 🐛 Describe the bug vllm serve "/data1/wangyao/models/yz_mind/emotion_bert" --trust-remote-code True --task...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', dis...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: dtype='auto', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: d platform cuda. INFO 04-07 10:34:38 [api_server.py:981] vLLM API server version 0.8.2 INFO 04-07 10:34:38 [api_server.py:982] args: Namespace(subparser='serve', model_tag='/data1/wangyao/models/yz_mind/emotion_bert', c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: rent environment ### 🐛 Describe the bug vllm serve "/data1/wangyao/models/yz_mind/emotion_bert" --trust-remote-code True --task score --port 48993 INFO 04-07 10:34:37 [__init__.py:239] Automatically detected platform cu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
