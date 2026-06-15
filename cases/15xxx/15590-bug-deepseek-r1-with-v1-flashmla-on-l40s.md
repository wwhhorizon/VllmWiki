# vllm-project/vllm#15590: [Bug]: DeepSeek R1 with V1+FLASHMLA on L40S

| 字段 | 值 |
| --- | --- |
| Issue | [#15590](https://github.com/vllm-project/vllm/issues/15590) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;operator;quantization |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeek R1 with V1+FLASHMLA on L40S

### Issue 正文摘录

### Your current environment I am running DeepSeek R1 671B on 4 nodes of L40S, each equipped with 8 GPUs. After creating the ray cluster, my launch command can be simplified as the following: ### 🐛 Describe the bug INFO 03-27 10:28:42 [__init__.py:239] Automatically detected platform cuda. INFO 03-27 10:28:46 [api_server.py:981] vLLM API server version 0.8.2 INFO 03-27 10:28:46 [api_server.py:982] args: Namespace(subparser='serve', model_tag='/root/.cache/huggingface', config='', host='0.0.0.0', port=8000, uvicorn_log_level='inf o', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_a dapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, enable_ssl_refresh= False, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto _tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='/root/.cache/huggingface', task='auto', tokenizer=None, hf_config_pat...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: [Bug]: DeepSeek R1 with V1+FLASHMLA on L40S bug;stale ### Your current environment I am running DeepSeek R1 671B on 4 nodes of L40S, each equipped with 8 GPUs. After creating the ray cluster, my launch command can be si...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: edia_path=None, download_dir=None, load_format= 'auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=131072, guided_decoding_backend='xgrammar', logits_processor_pattern=No ne, model_impl='auto',...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: d platform cuda. INFO 03-27 10:28:46 [api_server.py:981] vLLM API server version 0.8.2 INFO 03-27 10:28:46 [api_server.py:982] args: Namespace(subparser='serve', model_tag='/root/.cache/huggingface', config='', host='0....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: FO 03-27 10:28:46 [api_server.py:982] args: Namespace(subparser='serve', model_tag='/root/.cache/huggingface', config='', host='0.0.0.0', port=8000, uvicorn_log_level='inf o', disable_uvicorn_access_log=False, allow_cre...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: ype='auto', kv_cache_dtype='auto', max_model_len=131072, guided_decoding_backend='xgrammar', logits_processor_pattern=No ne, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=4, tensor_paralle...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
