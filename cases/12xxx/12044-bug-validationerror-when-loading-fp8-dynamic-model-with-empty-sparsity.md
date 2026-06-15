# vllm-project/vllm#12044: [Bug]: ValidationError when loading fp8-dynamic model with empty "sparsity_config"

| 字段 | 值 |
| --- | --- |
| Issue | [#12044](https://github.com/vllm-project/vllm/issues/12044) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | activation_norm;ci_build;distributed_parallel;frontend_api;gemm_linear;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | activation;cuda;fp8;quantization;triton |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ValidationError when loading fp8-dynamic model with empty "sparsity_config"

### Issue 正文摘录

### Your current environment **OS:** Ubuntu Server 22.04 LTS **GPU:** Nvidia H200 **Driver:** 550.127.08 ### Model Input Dumps _No response_ ### 🐛 Describe the bug When starting vllm like this: ``` python -m vllm.entrypoints.openai.api_server --model /models/llama-3.3-70b-instruct-fp8-dynamic --host localhost --port 10000 ``` The following error occurs: ``` INFO 01-14 13:24:33 api_server.py:712] vLLM API server version 0.6.6.post1 INFO 01-14 13:24:33 api_server.py:713] args: Namespace(host='localhost', port=10000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='/data/textgen_cache/models/llama-3.3-70b-instruct-fp8-dynamic', task='auto', tokenizer=None, skip_tokenizer_init=False, revis...

## 现有链接修复摘要

#12057 Fix: cases with empty sparsity config

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: ValidationError when loading fp8-dynamic model with empty "sparsity_config" bug ### Your current environment **OS:** Ubuntu Server 22.04 LTS **GPU:** Nvidia H200 **Driver:** 550.127.08 ### Model Input Dumps _No r...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='/data/textgen_cache/models/llama-3.3...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: rror occurs: ``` INFO 01-14 13:24:33 api_server.py:712] vLLM API server version 0.6.6.post1 INFO 01-14 13:24:33 api_server.py:713] args: Namespace(host='localhost', port=10000, uvicorn_log_level='info', allow_credential...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: ValidationError when loading fp8-dynamic model with empty "sparsity_config" bug ### Your current environment **OS:** Ubuntu Server 22.04 LTS **GPU:** Nvidia H200 **Driver:** 550.127.08 ### Model Input Dumps _No r...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: t='localhost', port=10000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#12057](https://github.com/vllm-project/vllm/pull/12057) | closes_keyword | 0.95 | Fix: cases with empty sparsity config | Fixes #12044 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
