# vllm-project/vllm#12865: [Bug]: run deepseek-32B with vllm0.7.2 meet -lcuda error

| 字段 | 值 |
| --- | --- |
| Issue | [#12865](https://github.com/vllm-project/vllm/issues/12865) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: run deepseek-32B with vllm0.7.2 meet -lcuda error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` (ds-vllm) root@node1:~# vllm serve /root/sdb2/DeepSeek-R1-Distill-Qwen-32B --tensor-parallel-size 2 --enforce-eager --gpu_memory_utilization=0.50 --enable-chunked-prefill INFO 02-07 11:26:38 __init__.py:190] Automatically detected platform cuda. INFO 02-07 11:26:39 api_server.py:840] vLLM API server version 0.7.2 INFO 02-07 11:26:39 api_server.py:841] args: Namespace(subparser='serve', model_tag='/root/sdb2/DeepSeek-R1-Distill-Qwen-32B', config='', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, enable_reasoning=False, reasoning_parser=None, tool_call_parser=None, tool_parser_plugin='', model='/root/sdb2/DeepSeek-R1-Distill-Qwen-32B', task='auto', tokenizer=No...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: [Bug]: run deepseek-32B with vllm0.7.2 meet -lcuda error bug;stale ### Your current environment ### 🐛 Describe the bug ``` (ds-vllm) root@node1:~# vllm serve /root/sdb2/DeepSeek-R1-Distill-Qwen-32B --tensor-parallel-siz...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ed platform cuda. INFO 02-07 11:26:39 api_server.py:840] vLLM API server version 0.7.2 INFO 02-07 11:26:39 api_server.py:841] args: Namespace(subparser='serve', model_tag='/root/sdb2/DeepSeek-R1-Distill-Qwen-32B', confi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', dis...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: g ``` (ds-vllm) root@node1:~# vllm serve /root/sdb2/DeepSeek-R1-Distill-Qwen-32B --tensor-parallel-size 2 --enforce-eager --gpu_memory_utilization=0.50 --enable-chunked-prefill INFO 02-07 11:26:38 __init__.py:190] Autom...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: dtype='auto', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
