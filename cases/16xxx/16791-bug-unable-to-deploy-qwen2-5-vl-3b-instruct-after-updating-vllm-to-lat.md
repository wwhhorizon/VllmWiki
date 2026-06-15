# vllm-project/vllm#16791: [Bug]: Unable to deploy Qwen2.5-VL-3B-Instruct  after updating vLLM to latest version

| 字段 | 值 |
| --- | --- |
| Issue | [#16791](https://github.com/vllm-project/vllm/issues/16791) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unable to deploy Qwen2.5-VL-3B-Instruct  after updating vLLM to latest version

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **After updating to the latest version of vLLM, I'm encountering issues when trying to deploy the qwen2.5-instruct model. The deployment process hangs indefinitely, and when terminated with Ctrl+C, the following error is displayed:** vllm serve Qwen/Qwen2.5-VL-3B-Instruct --port 12345 INFO 04-17 15:26:31 [__init__.py:239] Automatically detected platform cuda. INFO 04-17 15:26:33 [api_server.py:1034] vLLM API server version 0.8.4 INFO 04-17 15:26:33 [api_server.py:1035] args: Namespace(subparser='serve', model_tag='Qwen/Qwen2.5-VL-3B-Instruct', config='', host=None, port=12345, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, enable_ssl_refresh=False, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, to...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: : Unable to deploy Qwen2.5-VL-3B-Instruct after updating vLLM to latest version bug;stale ### Your current environment ### 🐛 Describe the bug **After updating to the latest version of vLLM, I'm encountering issues when...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: Unable to deploy Qwen2.5-VL-3B-Instruct after updating vLLM to latest version bug;stale ### Your current environment ### 🐛 Describe the bug **After updating to the latest version of vLLM, I'm encountering issues...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: model_loader_extra_config=None, use_tqdm_on_load=True, config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', dist...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: deploy Qwen2.5-VL-3B-Instruct after updating vLLM to latest version bug;stale ### Your current environment ### 🐛 Describe the bug **After updating to the latest version of vLLM, I'm encountering issues when trying to de...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: dtype='auto', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
