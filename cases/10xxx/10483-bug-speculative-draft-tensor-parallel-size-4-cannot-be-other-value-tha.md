# vllm-project/vllm#10483: [Bug]: speculative_draft_tensor_parallel_size=4 cannot be other value than 1

| 字段 | 值 |
| --- | --- |
| Issue | [#10483](https://github.com/vllm-project/vllm/issues/10483) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization;speculative_decoding |
| 子分类 | install |
| Operator 关键词 | kernel;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: speculative_draft_tensor_parallel_size=4 cannot be other value than 1

### Issue 正文摘录

### Your current environment ### Model Input Dumps no input, launch error ### 🐛 Describe the bug ``` No module named 'vllm._version' from vllm.version import __version__ as VLLM_VERSION INFO 11-19 23:29:07 api_server.py:528] vLLM API server version dev INFO 11-19 23:29:07 api_server.py:529] args: Namespace(host=None, port=14050, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='/models/Qwen2.5-72B-Instruct-AWQ/', tokenizer=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=False, download_dir=None, load_format='auto', config_format='auto', dtype='bfloat16', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=8192, guided_decoding_backend='outlines', distribut...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: input, launch error ### 🐛 Describe the bug ``` No module named 'vllm._version' from vllm.version import __version__ as VLLM_VERSION INFO 11-19 23:29:07 api_server.py:528] vLLM API server version dev INFO 11-19 23:29:07...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: speculative_draft_tensor_parallel_size=4 cannot be other value than 1 bug ### Your current environment ### Model Input Dumps no input, launch error ### 🐛 Describe the bug ``` No module named 'vllm._version' fro
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: code=False, download_dir=None, load_format='auto', config_format='auto', dtype='bfloat16', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=8192, guided_decoding_backend='outlines', distributed_executo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: =4 cannot be other value than 1 bug ### Your current environment ### Model Input Dumps no input, launch error ### 🐛 Describe the bug ``` No module named 'vllm._version' from vllm.version import __version__ as VLLM_VERSI...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ace(host=None, port=14050, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
