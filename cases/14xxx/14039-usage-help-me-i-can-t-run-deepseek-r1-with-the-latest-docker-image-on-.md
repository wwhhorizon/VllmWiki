# vllm-project/vllm#14039: [Usage]: Help me! I can't run DeepSeek-R1 with the latest docker image on my server

| 字段 | 值 |
| --- | --- |
| Issue | [#14039](https://github.com/vllm-project/vllm/issues/14039) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | install |
| Operator 关键词 | attention;cuda;fp8;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Help me! I can't run DeepSeek-R1 with the latest docker image on my server

### Issue 正文摘录

### Your current environment sorry, but this script can't run on the host, because the host's OS is just a "Docker runner" I would post logs below ### How would you like to use vllm [root@node1 ~]# docker run --ipc=host --name vllm -p 8000:8000 -v /root/DeepSeek-R1/:/root/DeepSeek-R1 --gpus all vllm/vllm-openai --model /root/DeepSeek-R1/ -tp 8 --trust-remote-code INFO 02-28 04:38:47 __init__.py:207] Automatically detected platform cuda. INFO 02-28 04:38:47 api_server.py:912] vLLM API server version 0.7.3 INFO 02-28 04:38:47 api_server.py:913] args: Namespace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, enable_reasoning=False, reasoning_parser=None, tool_call_parser=None, tool_parser_plugin='', model='/root/DeepS...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: 00 -v /root/DeepSeek-R1/:/root/DeepSeek-R1 --gpus all vllm/vllm-openai --model /root/DeepSeek-R1/ -tp 8 --trust-remote-code INFO 02-28 04:38:47 __init__.py:207] Automatically detected platform cuda. INFO 02-28 04:38:47...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Usage]: Help me! I can't run DeepSeek-R1 with the latest docker image on my server usage;stale ### Your current environment sorry, but this script can't run on the host, because the host's OS is just a "Docker runner"...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', dis...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: I can't run DeepSeek-R1 with the latest docker image on my server usage;stale ### Your current environment sorry, but this script can't run on the host, because the host's OS is just a "Docker runner" I would post logs...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: pace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
