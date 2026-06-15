# vllm-project/vllm#10116: [Bug]: vllm0.6.3.post1  7B model can not use cmd vllm.entrypoints.openai.api_server on wsl

| 字段 | 值 |
| --- | --- |
| Issue | [#10116](https://github.com/vllm-project/vllm/issues/10116) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 44; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm0.6.3.post1  7B model can not use cmd vllm.entrypoints.openai.api_server on wsl

### Issue 正文摘录

### Your current environment ### Model Input Dumps INFO 11-07 17:49:14 api_server.py:530] vLLM API server version 0.6.3.post1 INFO 11-07 17:49:14 api_server.py:531] args: Namespace(host='0.0.0.0', port=46000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='/mnt/d/Users/Admin/.cache/modelscope/hub/Qwen/Qwen2___5-7B-Instruct', tokenizer=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=True, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=None, guided_decoding_backend='outlines', distributed_executor_backend=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=1,...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: e, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', num_scheduler_steps=1, multi_step_stream_outputs=True, scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, speculative_mo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: odel Input Dumps INFO 11-07 17:49:14 api_server.py:530] vLLM API server version 0.6.3.post1 INFO 11-07 17:49:14 api_server.py:531] args: Namespace(host='0.0.0.0', port=46000, uvicorn_log_level='info', allow_credentials=...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: emote_code=True, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=None, guided_decoding_backend='outlines', distributed_executor_ba...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: ost='0.0.0.0', port=46000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: vllm0.6.3.post1 7B model can not use cmd vllm.entrypoints.openai.api_server on wsl bug ### Your current environment ### Model Input Dumps INFO 11-07 17:49:14 api_server.py:530] vLLM API server version 0.6.3.post1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
