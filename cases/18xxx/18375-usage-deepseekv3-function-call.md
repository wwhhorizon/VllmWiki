# vllm-project/vllm#18375: [Usage]: 无法使用deepseekv3的 function call

| 字段 | 值 |
| --- | --- |
| Issue | [#18375](https://github.com/vllm-project/vllm/issues/18375) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | env_compat |
| Operator 关键词 | cuda;fp8;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: 无法使用deepseekv3的 function call

### Issue 正文摘录

### Your current environment ``` (xinference2) u@se:~$ python -m vllm.entrypoints.openai.api_server --served-model-name DeepSeek-V3-0324 --model /data/model/DeepSeek-V3-0324 --tensor-parallel-size 8 --port 5001 --enable-prefix-caching --enable-chunked-prefill --trust-remote-code --kv-cache-dtype auto --quantization fp8 --enable-auto-tool-choice --tool-call-parser deepseek_v3 --chat-template /data/model/tool_chat_template_deepseekv3.jinja INFO 05-20 10:21:09 [__init__.py:239] Automatically detected platform cuda. INFO 05-20 10:21:11 [api_server.py:1043] vLLM API server version 0.8.5.post1 INFO 05-20 10:21:11 [api_server.py:1044] args: Namespace(host=None, port=5001, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template='/data/model/tool_chat_template_deepseekv3.jinja', chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, enable_ssl_refresh=False, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multip...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ference2) u@se:~$ python -m vllm.entrypoints.openai.api_server --served-model-name DeepSeek-V3-0324 --model /data/model/DeepSeek-V3-0324 --tensor-parallel-size 8 --port 5001 --enable-prefix-caching --enable-chunked-pref...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Usage]: 无法使用deepseekv3的 function call usage;stale ### Your current environment ``` (xinference2) u@se:~$ python -m vllm.entrypoints.openai.api_server --served-model-name DeepSeek-V3-0324 --model /data/model/DeepSeek-V3...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: aching --enable-chunked-prefill --trust-remote-code --kv-cache-dtype auto --quantization fp8 --enable-auto-tool-choice --tool-call-parser deepseek_v3 --chat-template /data/model/tool_chat_template_deepseekv3.jinja INFO...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: platform cuda. INFO 05-20 10:21:11 [api_server.py:1043] vLLM API server version 0.8.5.post1 INFO 05-20 10:21:11 [api_server.py:1044] args: Namespace(host=None, port=5001, uvicorn_log_level='info', disable_uvicorn_access...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: =None, port=5001, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapter...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
