# vllm-project/vllm#11441: [Bug]: v0.6.3 not support Qwen2ForCausalLM architecture

| 字段 | 值 |
| --- | --- |
| Issue | [#11441](https://github.com/vllm-project/vllm/issues/11441) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v0.6.3 not support Qwen2ForCausalLM architecture

### Issue 正文摘录

### Your current environment ### Model Input Dumps ![image](https://github.com/user-attachments/assets/8cd76a7d-a782-4962-aa8d-eedb4d7cbc53) ### 🐛 Describe the bug error log ``` INFO 12-24 00:20:08 api_server.py:528] vLLM API server version dev INFO 12-24 00:20:08 api_server.py:529] args: Namespace(subparser='serve', model_tag='/data/wufanghao/RAG/models/qwen2.5-7b', config='', host=None, port=8003, uvicorn_log_level='info', allow_credentials=False, a llowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl _ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin ='', model='/data/wufanghao/RAG/models/qwen2.5-7b', tokenizer=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=False, downloa d_dir=None, load_format='auto', config_format='auto', dtype='auto', kv_cache_dtype='auto', quantization_param_...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: e, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', num_scheduler_steps=1, multi_step_stream_outputs=True, scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, speculative_mo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: g error log ``` INFO 12-24 00:20:08 api_server.py:528] vLLM API server version dev INFO 12-24 00:20:08 api_server.py:529] args: Namespace(subparser='serve', model_tag='/data/wufanghao/RAG/models/qwen2.5-7b', config='',...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: v0.6.3 not support Qwen2ForCausalLM architecture bug ### Your current environment ### Model Input Dumps ![image](https://github.com/user-attachments/assets/8cd76a7d-a782-4962-aa8d-eedb4d7cbc53) ### 🐛 Describe the...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: auto', quantization_param_path=None, max_model_len=None, guided_decoding_backend='outlines', distributed_executor_backend=None , worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=1, max_parallel_loadi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ='', host=None, port=8003, uvicorn_log_level='info', allow_credentials=False, a llowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=No...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
