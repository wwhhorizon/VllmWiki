# vllm-project/vllm#15614: [Installation]: ValueError: size must contain 'shortest_edge' and 'longest_edge' keys.

| 字段 | 值 |
| --- | --- |
| Issue | [#15614](https://github.com/vllm-project/vllm/issues/15614) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 24; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization;scheduler_memory |
| 子分类 |  |
| Operator 关键词 | attention;cuda;gemm;quantization |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: ValueError: size must contain 'shortest_edge' and 'longest_edge' keys.

### Issue 正文摘录

### Your current environment ```text (opensora) ubuntu@ubuntu:~/psh$ python -m vllm.entrypoints.openai.api_server --served-model-name ui-tars --model /home/ubuntu/psh/UI-TARS-7B-DPO --limit-mm-per-prompt image=5 -tp 1 --trust-remote-code --port 8001 INFO 03-27 16:11:36 [__init__.py:239] Automatically detected platform cuda. INFO 03-27 16:11:37 [api_server.py:981] vLLM API server version 0.8.2 INFO 03-27 16:11:37 [api_server.py:982] args: Namespace(host=None, port=8001, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, enable_ssl_refresh=False, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='/home/ubuntu/psh/UI-TARS-7B-DPO', task='auto', tokenizer=None, hf_config_path=None, skip_tokenizer_init=False,...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: untu@ubuntu:~/psh$ python -m vllm.entrypoints.openai.api_server --served-model-name ui-tars --model /home/ubuntu/psh/UI-TARS-7B-DPO --limit-mm-per-prompt image=5 -tp 1 --trust-remote-code --port 8001 INFO 03-27 16:11:36...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Installation]: ValueError: size must contain 'shortest_edge' and 'longest_edge' keys. installation ### Your current environment ```text (opensora) ubuntu@ubuntu:~/psh$ python -m vllm.entrypoints.openai.api_server --serv
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', dis...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='/home/ubuntu/psh/UI-TARS-7B-DPO', ta...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: =None, port=8001, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapter...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
