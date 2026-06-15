# vllm-project/vllm#9232: [Bug]: AssertionError: Error in memory profiling. Initial free memory 85470478336, current free memory 85470478336. This happens when the GPU memory was not properly cleaned up before initializing the vLLM instance. [rank0]:[W1010 16:28:18.581149478 CudaIPCTypes.cpp:16] Producer process has been terminated before all shared CUDA tensors released. See Note [Sharing CUDA tensors] ERROR 10-10 16:28:20 api_server.py:188] RPCServer process died before responding to readiness probe

| 字段 | 值 |
| --- | --- |
| Issue | [#9232](https://github.com/vllm-project/vllm/issues/9232) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;fp8;quantization;triton |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AssertionError: Error in memory profiling. Initial free memory 85470478336, current free memory 85470478336. This happens when the GPU memory was not properly cleaned up before initializing the vLLM instance. [rank0]:[W1010 16:28:18.581149478 CudaIPCTypes.cpp:16] Producer process has been terminated before all shared CUDA tensors released. See Note [Sharing CUDA tensors] ERROR 10-10 16:28:20 api_server.py:188] RPCServer process died before responding to readiness probe

### Issue 正文摘录

### Your current environment ### Model Input Dumps ``` INFO 10-10 16:27:39 api_server.py:495] vLLM API server version 0.6.1.post1 INFO 10-10 16:27:39 api_server.py:496] args: Namespace(model_tag='Imran1/Qwen2.5-72B-Instruct-FP8', config='', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key='token-abc123', lora_modules=None, prompt_adapters=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_auto_tool_choice=False, tool_call_parser=None, model='Imran1/Qwen2.5-72B-Instruct-FP8', tokenizer=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=False, download_dir=None, load_format='auto', config_format='auto', dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=2000, guided_decoding_backend='outlines', distributed_executor_backend=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parall...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: e, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', num_scheduler_steps=1, scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, speculative_model_quantization=None, num_specu...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: pi_server.py:496] args: Namespace(model_tag='Imran1/Qwen2.5-72B-Instruct-FP8', config='', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_he...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: e responding to readiness probe bug ### Your current environment ### Model Input Dumps ``` INFO 10-10 16:27:39 api_server.py:495] vLLM API server version 0.6.1.post1 INFO 10-10 16:27:39 api_server.py:496] args: Namespac...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: auto', quantization_param_path=None, max_model_len=2000, guided_decoding_backend='outlines', distributed_executor_backend=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=2, max_parallel_loadin...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ='', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key='token-abc123', lora_modules=None, prompt_adapters=None, chat_te...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
