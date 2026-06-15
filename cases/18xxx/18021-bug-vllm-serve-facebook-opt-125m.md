# vllm-project/vllm#18021: [Bug]: vllm serve facebook/opt-125m

| 字段 | 值 |
| --- | --- |
| Issue | [#18021](https://github.com/vllm-project/vllm/issues/18021) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm serve facebook/opt-125m

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm serve facebook/opt-125m outputs: (vllmenv) c0274@50u24:~$ vllm serve facebook/opt-125m INFO 05-12 16:54:11 [__init__.py:239] Automatically detected platform cuda. INFO 05-12 16:54:16 [api_server.py:1043] vLLM API server version 0.8.5.post1 INFO 05-12 16:54:16 [api_server.py:1044] args: Namespace(subparser='serve', model_tag='facebook/opt-125m', config='', host=None, port=8000, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, enable_ssl_refresh=False, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='facebook/opt-125m', task='auto', tokenizer=None, hf_config_path=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revisi...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: O 05-12 16:54:16 [api_server.py:1044] args: Namespace(subparser='serve', model_tag='facebook/opt-125m', config='', host=None, port=8000, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=Fals...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: e, model_loader_extra_config={}, use_tqdm_on_load=True, config_format= , dtype='auto', max_model_len=None, guided_decoding_backend='auto', reasoning_parser=None, logits_processor_pattern=None, model_impl='auto', distrib...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: vllm serve facebook/opt-125m bug;stale ### Your current environment ### 🐛 Describe the bug vllm serve facebook/opt-125m outputs: (vllmenv) c0274@50u24:~$ vllm serve facebook/opt-125m INFO 05-12 16:54:11 [__init__...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: platform cuda. INFO 05-12 16:54:16 [api_server.py:1043] vLLM API server version 0.8.5.post1 INFO 05-12 16:54:16 [api_server.py:1044] args: Namespace(subparser='serve', model_tag='facebook/opt-125m', config='', host=None...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: True, config_format= , dtype='auto', max_model_len=None, guided_decoding_backend='auto', reasoning_parser=None, logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
