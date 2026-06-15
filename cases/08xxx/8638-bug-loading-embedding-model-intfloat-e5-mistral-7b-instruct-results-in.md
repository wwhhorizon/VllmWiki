# vllm-project/vllm#8638: [Bug]: loading embedding model intfloat/e5-mistral-7b-instruct results in a bind error 

| 字段 | 值 |
| --- | --- |
| Issue | [#8638](https://github.com/vllm-project/vllm/issues/8638) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: loading embedding model intfloat/e5-mistral-7b-instruct results in a bind error 

### Issue 正文摘录

### Your current environment ### Model Input Dumps vllm-eb_1 | INFO 09-19 08:56:24 api_server.py:520] vLLM API server version 0.6.1.post2 vllm-eb_1 | INFO 09-19 08:56:24 api_server.py:521] args: Namespace(host='0.0.0.0', port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_auto_tool_choice=False, tool_call_parser=None, model='intfloat/e5-mistral-7b-instruct', tokenizer=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=True, download_dir='/models', load_format='auto', config_format='auto', dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=None, guided_decoding_backend='outlines', distributed_executor_backend=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=8, max_parallel_loading_worke...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: e, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', num_scheduler_steps=1, scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, speculative_model_quantization=None, num_specu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: mps vllm-eb_1 | INFO 09-19 08:56:24 api_server.py:520] vLLM API server version 0.6.1.post2 vllm-eb_1 | INFO 09-19 08:56:24 api_server.py:521] args: Namespace(host='0.0.0.0', port=8000, uvicorn_log_level='info', allow_cr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: loading embedding model intfloat/e5-mistral-7b-instruct results in a bind error bug ### Your current environment ### Model Input Dumps vllm-eb_1 | INFO 09-19 08:56:24 api_server.py:520] vLLM API server version 0....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: auto', quantization_param_path=None, max_model_len=None, guided_decoding_backend='outlines', distributed_executor_backend=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=8, max_parallel_loadin...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: =True, download_dir='/models', load_format='auto', config_format='auto', dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=None, guided_decoding_backend='outlines', distributed_executor_ba...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
