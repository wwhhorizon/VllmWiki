# vllm-project/vllm#13044: [Bug]: codegemma-7b crashes without error

| 字段 | 值 |
| --- | --- |
| Issue | [#13044](https://github.com/vllm-project/vllm/issues/13044) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: codegemma-7b crashes without error

### Issue 正文摘录

### Your current environment ```text Wen trying to run codegemma7b [https://huggingface.co/google/codegemma-7b] it crashes without any error. I am using the following arguments: --max-model-len=4600 --gpu-memory-utilization=0.90 and I have tested vLLM version 0.6.3 and 0.7.2 with the same result. ``` ### 🐛 Describe the bug It deployments stops after this: INFO 02-10 15:12:06 api_server.py:526] vLLM API server version 0.6.3.dev183+g0f75993c INFO 02-10 15:12:06 api_server.py:527] args: Namespace(host=None, port=8080, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_auto_tool_choice=False, tool_call_parser=None, model='/mnt/models', tokenizer=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=False, download_dir=None, load_format='auto', config_format...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: codegemma-7b crashes without error bug;stale ### Your current environment ```text Wen trying to run codegemma7b [https://huggingface.co/google/codegemma-7b] it crashes without any error. I am using the following...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: codegemma-7b crashes without error bug;stale ### Your current environment ```text Wen trying to run codegemma7b [https://huggingface.co/google/codegemma-7b] it crashes without any error. I am using the following...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: code=False, download_dir=None, load_format='auto', config_format='auto', dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=4600, guided_decoding_backend='outlines', distributed_executor_ba...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: pace(host=None, port=8080, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: l-len=4600 --gpu-memory-utilization=0.90 and I have tested vLLM version 0.6.3 and 0.7.2 with the same result. ``` ### 🐛 Describe the bug It deployments stops after this: INFO 02-10 15:12:06 api_server.py:526] vLLM API s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
