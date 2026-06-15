# vllm-project/vllm#9416: [Usage]: How to get time_to_first_token_seconds in Metrics

| 字段 | 值 |
| --- | --- |
| Issue | [#9416](https://github.com/vllm-project/vllm/issues/9416) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to get time_to_first_token_seconds in Metrics

### Issue 正文摘录

### Your current environment vllm=0.6.0 ### How would you like to use vllm server running parameter: INFO 10-16 17:11:24 api_server.py:495] vLLM API server version 0.6.0 INFO 10-16 17:11:24 api_server.py:496] args: Namespace(host='127.0.0.1', port=9001, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template='/vllm/examples/template_chatml.jinja', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_auto_tool_choice=False, tool_call_parser=None, model='/data/llv/engine', tokenizer=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=4096, guided_decoding_backend='outlines', distributed_executor_backend=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=2, max_paralle...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: e, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', num_scheduler_steps=1, scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, speculative_model_quantization=None, num_specu...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=4096, guided_decoding_backend='outlines', distributed_executor_ba...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: st='127.0.0.1', port=9001, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template='/v...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: iprocessing=False, enable_auto_tool_choice=False, tool_call_parser=None, model='/data/llv/engine', tokenizer=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: s ``` # HELP chat_count # TYPE chat_count gauge chat_count 2 # HELP chat_latency # TYPE chat_latency gauge chat_latency 390 # HELP chat_latency_80 # TYPE chat_latency_80 gauge chat_latency_80 390 # HELP chat_latency_90...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
