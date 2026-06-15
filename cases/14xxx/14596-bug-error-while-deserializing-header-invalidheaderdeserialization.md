# vllm-project/vllm#14596: [Bug]: Error while deserializing header: InvalidHeaderDeserialization

| 字段 | 值 |
| --- | --- |
| Issue | [#14596](https://github.com/vllm-project/vllm/issues/14596) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | install |
| Operator 关键词 | attention;cuda;kernel;operator;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error while deserializing header: InvalidHeaderDeserialization

### Issue 正文摘录

### Your current environment root@node37:/disk1/qwen-2.5-vl-72b-in-awq-0226# docker compose -f docker-compose.yml down [+] Running 2/2 ✔ Container qwen-2.5-vl-72b-in-awq Removed 2.0s ✔ Network qwen-25-vl-72b-in-awq-0226_default Removed 0.2s root@node37:/disk1/qwen-2.5-vl-72b-in-awq-0226# docker compose -f docker-compose.yml up -d [+] Running 2/2 ✔ Network qwen-25-vl-72b-in-awq-0226_default Created 0.1s ✔ Container qwen-2.5-vl-72b-in-awq Started 0.5s root@node37:/disk1/qwen-2.5-vl-72b-in-awq-0226# docker logs -f qwen-2.5-vl-72b-in-awq INFO 03-10 21:30:35 __init__.py:207] Automatically detected platform cuda. INFO 03-10 21:30:35 api_server.py:912] vLLM API server version 0.7.3 INFO 03-10 21:30:35 api_server.py:913] args: Namespace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, e...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: our current environment root@node37:/disk1/qwen-2.5-vl-72b-in-awq-0226# docker compose -f docker-compose.yml down [+] Running 2/2 ✔ Container qwen-2.5-vl-72b-in-awq Removed
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='float16', kv_cache_dtype='auto', max_model_len=32768, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto',...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: aderDeserialization bug ### Your current environment root@node37:/disk1/qwen-2.5-vl-72b-in-awq-0226# docker compose -f docker-compose.yml down [+] Running 2/2 ✔ Container qwen-2.5-vl-72b-in-awq Removed
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, enable_reasoning=False, reasoning_parser=None, tool_call_parser=None, tool_parser_plugin=...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: pace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
