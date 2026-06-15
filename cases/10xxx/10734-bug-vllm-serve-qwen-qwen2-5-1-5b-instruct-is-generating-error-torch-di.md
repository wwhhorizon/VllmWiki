# vllm-project/vllm#10734: [Bug]:  (vllm serve Qwen/Qwen2.5-1.5B-Instruct) is generating error torch.distributed.DistBackendError: File name too long and same thing is happening with other models

| 字段 | 值 |
| --- | --- |
| Issue | [#10734](https://github.com/vllm-project/vllm/issues/10734) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | runtime_err |
| Operator 关键词 | attention;cuda;operator;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  (vllm serve Qwen/Qwen2.5-1.5B-Instruct) is generating error torch.distributed.DistBackendError: File name too long and same thing is happening with other models

### Issue 正文摘录

### Your current environment torch 2.5.1 torchvision 0.20.1 vllm 0.6.4.post1 ### Model Input Dumps vllm serve Qwen/Qwen2.5-1.5B-Instruct INFO 11-28 06:43:46 api_server.py:585] vLLM API server version 0.6.4.post1 INFO 11-28 06:43:46 api_server.py:586] args: Namespace(subparser='serve', model_tag='Qwen/Qwen2.5-1.5B-Instruct', config='', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='Qwen/Qwen2.5-1.5B-Instruct', task='auto', tokenizer=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', chat_template_text_format='string', trust_remote_code=False, allowed_local_media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', qua...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: (vllm serve Qwen/Qwen2.5-1.5B-Instruct) is generating error torch.distributed.DistBackendError: File name too long and same thing is happening with other models bug ### Your current environment torch 2.5
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: e, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', num_scheduler_steps=1, multi_step_stream_outputs=True, scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, speculative_mo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 2.5-1.5B-Instruct INFO 11-28 06:43:46 api_server.py:585] vLLM API server version 0.6.4.post1 INFO 11-28 06:43:46 api_server.py:586] args: Namespace(subparser='serve', model_tag='Qwen/Qwen2.5-1.5B-Instruct', config='', h...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: ='', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ve Qwen/Qwen2.5-1.5B-Instruct) is generating error torch.distributed.DistBackendError: File name too long and same thing is happening with other models bug ### Your current environment torch 2.5.1 torchvision 0.20.1 vllm

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
