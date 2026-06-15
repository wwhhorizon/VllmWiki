# vllm-project/vllm#14925: [Bug]: V0+TP doesn't work with trust remote code for custom configuration

| 字段 | 值 |
| --- | --- |
| Issue | [#14925](https://github.com/vllm-project/vllm/issues/14925) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 |  |
| Operator 关键词 | attention;cache;cuda;quantization;triton |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: V0+TP doesn't work with trust remote code for custom configuration

### Issue 正文摘录

### Your current environment Nightly ### 🐛 Describe the bug ``` vllm --version INFO 03-17 04:56:52 [__init__.py:256] Automatically detected platform cuda. 0.7.4.dev497+ga73e183e ``` Use the model such as Deepseek's family of models, which have custom `configuration_deepseek.py`. In the V0 engine, we see the following error ``` vllm serve /home/vllm-dev/DeepSeek-V2-Lite --trust-remote-code --tensor-parallel-size 2 INFO 03-17 04:59:17 [__init__.py:256] Automatically detected platform cuda. INFO 03-17 04:59:18 [api_server.py:972] vLLM API server version 0.7.4.dev497+ga73e183e INFO 03-17 04:59:18 [api_server.py:973] args: Namespace(subparser='serve', model_tag='/home/vllm-dev/DeepSeek-V2-Lite', config='', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, enable_ssl_refresh=False, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, ena...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: # Your current environment Nightly ### 🐛 Describe the bug ``` vllm --version INFO 03-17 04:56:52 [__init__.py:256] Automatically detected platform cuda. 0.7.4.dev497+ga73e183e ``` Use the model such as Deepseek's family...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', dis...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='/home/vllm-dev/DeepSeek-V2-Lite', ta...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: _block_manager=True, num_lookahead_slots=0, seed=None, swap_space=4, cpu_offload_gb=0, gpu_memory_utilization=0.9, num_gpu_blocks_override=None, max_num_batched_tokens=None, max_num_partial_prefills=1, max_long_partial_...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: ='', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
