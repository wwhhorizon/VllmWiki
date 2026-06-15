# vllm-project/vllm#17225: [Bug]: vLLM CPU with PyTorch 2.7.0 crashes with RuntimeError: "reshape_and_cache_cpu_impl" not implemented for 'Half'

| 字段 | 值 |
| --- | --- |
| Issue | [#17225](https://github.com/vllm-project/vllm/issues/17225) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM CPU with PyTorch 2.7.0 crashes with RuntimeError: "reshape_and_cache_cpu_impl" not implemented for 'Half'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug This issue is discovered when updating PyTorch to its latest 2.7.0 release. When serving the example model `facebook/opt-125m` on CPU, the server crashes with the following error: ``` ERROR! Intel® Extension for PyTorch* needs to work with PyTorch 2.6.*, but PyTorch 2.7.0+cpu is found. Please switch to the matching version and run again. INFO 04-26 04:06:06 [__init__.py:239] Automatically detected platform cpu. INFO 04-26 04:06:13 [api_server.py:1043] vLLM API server version 0.1.dev6077+g1a4cc8c.d20250426 INFO 04-26 04:06:13 [api_server.py:1044] args: Namespace(subparser='serve', model_tag='facebook/opt-125m', config='', host=None, port=8000, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, enable_ssl_refresh=False, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False,...

## 现有链接修复摘要

#18430 [Bugfix] Add half type support in reshape_and_cache_cpu_impl on x86 cpu platform

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='facebook/opt-125m', task='auto', tok...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: rch 2.6.*, but PyTorch 2.7.0+cpu is found. Please switch to the matching version and run again. INFO 04-26 04:06:06 [__init__.py:239] Automatically detected platform cpu. INFO 04-26 04:06:13 [api_server.py:1043] vLLM AP...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: e, model_loader_extra_config={}, use_tqdm_on_load=True, config_format= , dtype='auto', max_model_len=None, guided_decoding_backend='auto', reasoning_parser=None, logits_processor_pattern=None, model_impl='auto', distrib...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: True, config_format= , dtype='auto', max_model_len=None, guided_decoding_backend='auto', reasoning_parser=None, logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: =None, port=8000, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapter...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#18430](https://github.com/vllm-project/vllm/pull/18430) | closes_keyword | 0.95 | [Bugfix] Add half type support in reshape_and_cache_cpu_impl on x86 cpu platform | FIX #17225 (*link existing issues this PR will resolve*) <!--- pyml disable-next-line no-emphasis-as-heading --> |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
