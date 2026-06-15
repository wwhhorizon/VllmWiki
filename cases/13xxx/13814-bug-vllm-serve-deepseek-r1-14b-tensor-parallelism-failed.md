# vllm-project/vllm#13814: [Bug]: vLLM serve Deepseek-R1-14B tensor parallelism failed

| 字段 | 值 |
| --- | --- |
| Issue | [#13814](https://github.com/vllm-project/vllm/issues/13814) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM serve Deepseek-R1-14B tensor parallelism failed

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```bash CUDA_VISIBLE_DEVICES=2,3 vllm serve ./deepseek-r1-14b --max_model_len 8192 --tensor-parallel-size 2 ``` If I disable tensor parallelism, everything works fine. However, as long as I set tensor-parallel-size > 1, it will get stuck when loading the model. The log is as follows: ``` DEBUG 02-25 15:59:17 scripts.py:139] Setting VLLM_WORKER_MULTIPROC_METHOD to 'spawn' INFO 02-25 15:59:17 api_server.py:712] vLLM API server version 0.6.6.post1 INFO 02-25 15:59:17 api_server.py:713] args: Namespace(subparser='serve', model_tag='./deepseek-r1-14b', config='', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='./deep...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='./deepseek-r1-14b', task='auto', tok...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: METHOD to 'spawn' INFO 02-25 15:59:17 api_server.py:712] vLLM API server version 0.6.6.post1 INFO 02-25 15:59:17 api_server.py:713] args: Namespace(subparser='serve', model_tag='./deepseek-r1-14b', config='', host=None,...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: auto', quantization_param_path=None, max_model_len=8192, guided_decoding_backend='xgrammar', logits_processor_pattern=None, distributed_executor_backend=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_paral...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=8192, guided_decoding_backend='xgrammar', logits_processor_patter...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: ='', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
