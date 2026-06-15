# vllm-project/vllm#15675: [Bug]: OpenAI-Compatible Server cannot be requested

| 字段 | 值 |
| --- | --- |
| Issue | [#15675](https://github.com/vllm-project/vllm/issues/15675) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: OpenAI-Compatible Server cannot be requested

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I use this command start vllm server python -m vllm.entrypoints.openai.api_server --model /mnt/f/wsl/ubuntu2204/models/Qwen2.5-0.5B --gpu_memory_utilization=0.99 --max-model-len=2048 and output the following information ```python INFO 03-28 11:37:50 [__init__.py:239] Automatically detected platform cuda. INFO 03-28 11:37:52 [api_server.py:981] vLLM API server version 0.8.2 INFO 03-28 11:37:52 [api_server.py:982] args: Namespace(host=None, port=8000, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, enable_ssl_refresh=False, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='/mnt/f/wsl/ubuntu2204/models/Qwen2.5-0.5B', task='auto', tokenizer=None, hf_con...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: OpenAI-Compatible Server cannot be requested bug;stale ### Your current environment ### 🐛 Describe the bug I use this command start vllm server python -m vllm.entrypoints.openai.api_server --model /mnt/f/wsl/ubun...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: d platform cuda. INFO 03-28 11:37:52 [api_server.py:981] vLLM API server version 0.8.2 INFO 03-28 11:37:52 [api_server.py:982] args: Namespace(host=None, port=8000, uvicorn_log_level='info', disable_uvicorn_access_log=F...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=2048, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', dis...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: mand start vllm server python -m vllm.entrypoints.openai.api_server --model /mnt/f/wsl/ubuntu2204/models/Qwen2.5-0.5B --gpu_memory_utilization=0.99 --max-model-len=2048 and output the following information ```python INF...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: dtype='auto', kv_cache_dtype='auto', max_model_len=2048, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
