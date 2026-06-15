# vllm-project/vllm#15199: [Bug]: Can't deserialize object reported by ray, H800*16 DeepSeek R1

| 字段 | 值 |
| --- | --- |
| Issue | [#15199](https://github.com/vllm-project/vllm/issues/15199) |
| 状态 | closed |
| 标签 | bug;ray |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;scheduler_memory;speculative_decoding |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;fp8;operator;quantization;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Can't deserialize object reported by ray, H800*16 DeepSeek R1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Ray status is ready, start serving... + vllm serve /model --tensor-parallel-size 8 --pipeline-parallel-size 2 --trust-remote-code --gpu-memory-utilization 0.92 --max-model-len 98304 --host 0.0.0.0 --port 8102 --served-model-name DeepSeek-R1 --uvicorn-log-level info INFO 03-20 08:10:14 [__init__.py:256] Automatically detected platform cuda. INFO 03-20 08:10:18 [api_server.py:977] vLLM API server version 0.8.1 INFO 03-20 08:10:18 [api_server.py:978] args: Namespace(subparser='serve', model_tag='/model', config='', host='0.0.0.0', port=8102, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, enable_ssl_refresh=False, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='/model', task='auto',...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='/model', task='auto', tokenizer=None...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: d platform cuda. INFO 03-20 08:10:18 [api_server.py:977] vLLM API server version 0.8.1 INFO 03-20 08:10:18 [api_server.py:978] args: Namespace(subparser='serve', model_tag='/model', config='', host='0.0.0.0', port=8102,...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=98304, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', di...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: host='0.0.0.0', port=8102, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: _block_manager=True, num_lookahead_slots=0, seed=None, swap_space=4, cpu_offload_gb=0, gpu_memory_utilization=0.92, num_gpu_blocks_override=None, max_num_batched_tokens=None, max_num_partial_prefills=1, max_long_partial...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
