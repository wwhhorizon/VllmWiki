# vllm-project/vllm#20357: [Usage]: vLLM 0.8.5 post1 unable to run GLM-4.1V-9B-Thinking large model, error message `glm4v` cannot recognize this architecture

| 字段 | 值 |
| --- | --- |
| Issue | [#20357](https://github.com/vllm-project/vllm/issues/20357) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization;scheduler_memory |
| 子分类 | env_compat |
| Operator 关键词 | cuda;quantization |
| 症状 | crash |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: vLLM 0.8.5 post1 unable to run GLM-4.1V-9B-Thinking large model, error message `glm4v` cannot recognize this architecture

### Issue 正文摘录

### Your current environment INFO 07-02 14:51:22 [__init__.py:239] Automatically detected platform cuda. INFO 07-02 14:51:26 [api_server.py:1043] vLLM API server version 0.8.5.post1 INFO 07-02 14:51:26 [api_server.py:1044] args: Namespace(subparser='serve', model_tag='/data/GLM-4.1V-9B-Thinking', config='', host='0.0.0.0', port=6003, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key='', lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, enable_ssl_refresh=False, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='/data/GLM-4.1V-9B-Thinking', task='auto', tokenizer=None, hf_config_path=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=True, allowed_local_media_path=None, load_fo...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Usage]: vLLM 0.8.5 post1 unable to run GLM-4.1V-9B-Thinking large model, error message `glm4v` cannot recognize this architecture usage ### Your current environment INFO 07-02 14:51:22 [__init__.py:239] Automatically d...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: platform cuda. INFO 07-02 14:51:26 [api_server.py:1043] vLLM API server version 0.8.5.post1 INFO 07-02 14:51:26 [api_server.py:1044] args: Namespace(subparser='serve', model_tag='/data/GLM-4.1V-9B-Thinking', config='',...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: .0.0', port=6003, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key='', lora_modules=None, prompt_adapters=...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='/data/GLM-4.1V-9B-Thinking', task='a...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: e, model_loader_extra_config={}, use_tqdm_on_load=True, config_format= , dtype='auto', max_model_len=2048, guided_decoding_backend='auto', reasoning_parser=None, logits_processor_pattern=None, model_impl='auto', distrib...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
