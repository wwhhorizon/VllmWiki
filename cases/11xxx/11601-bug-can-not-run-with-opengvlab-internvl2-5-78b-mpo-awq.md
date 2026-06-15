# vllm-project/vllm#11601: [Bug]: can not run with OpenGVLab/InternVL2_5-78B-MPO-AWQ

| 字段 | 值 |
| --- | --- |
| Issue | [#11601](https://github.com/vllm-project/vllm/issues/11601) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: can not run with OpenGVLab/InternVL2_5-78B-MPO-AWQ

### Issue 正文摘录

### Your current environment ### Model Input Dumps INFO 12-29 17:33:39 api_server.py:712] vLLM API server version 0.6.6 INFO 12-29 17:33:39 api_server.py:713] args: Namespace(host='0.0.0.0', port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='/root/hf_model/OpenGVLab/InternVL2_5-78B-MPO-AWQ', task='auto', tokenizer=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=True, allowed_local_media_path=None, download_dir=None, load_format='auto', config_format= , dtype='float16', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=6400, guided_decoding_backend='xgrammar', logits_processor...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 9: [Bug]: can not run with OpenGVLab/InternVL2_5-78B-MPO-AWQ bug;stale ### Your current environment ### Model Input Dumps INFO 12-29 17:33:39 api_server.py:712] vLLM API server version 0.6.6 INFO 12-29 17:33:39 api_server....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: [Bug]: can not run with OpenGVLab/InternVL2_5-78B-MPO-AWQ bug;stale ### Your current environment ### Model Input Dumps INFO 12-29 17:33:39 api_server.py:712] vLLM API server version 0.6.6 INFO 12-29 17:33:39 api_server....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: odel Input Dumps INFO 12-29 17:33:39 api_server.py:712] vLLM API server version 0.6.6 INFO 12-29 17:33:39 api_server.py:713] args: Namespace(host='0.0.0.0', port=8000, uvicorn_log_level='info', allow_credentials=False,...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='float16', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=6400, guided_decoding_backend='xgrammar', logits_processor_pat...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: auto', quantization_param_path=None, max_model_len=6400, guided_decoding_backend='xgrammar', logits_processor_pattern=None, distributed_executor_backend=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_paral...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
