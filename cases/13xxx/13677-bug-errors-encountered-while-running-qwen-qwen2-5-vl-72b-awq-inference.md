# vllm-project/vllm#13677: [Bug]: Errors Encountered While Running Qwen/Qwen2.5-VL-72B-AWQ Inference on 8x24G的4090 GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#13677](https://github.com/vllm-project/vllm/issues/13677) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Errors Encountered While Running Qwen/Qwen2.5-VL-72B-AWQ Inference on 8x24G的4090 GPUs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug python3 -m vllm.entrypoints.openai.api_server --model Qwen/Qwen2.5-VL-72B-Instruct-AWQ --host 0.0.0.0 --port 8000 --tensor-parallel-size 8 error: `INFO 02-22 00:31:01 __init__.py:207] Automatically detected platform cuda. INFO 02-22 00:31:01 api_server.py:912] vLLM API server version 0.7.3 INFO 02-22 00:31:01 api_server.py:913] args: Namespace(host='0.0.0.0', port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, enable_reasoning=False, reasoning_parser=None, tool_call_parser=None, tool_parser_plugin='', model='Qwen/Qwen2.5-VL-72B-Instruct-AWQ', task='auto', tokenizer=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto',...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: d While Running Qwen/Qwen2.5-VL-72B-AWQ Inference on 8x24G的4090 GPUs bug;stale ### Your current environment ### 🐛 Describe the bug python3 -m vllm.entrypoints.openai.api_server --model Qwen/Qwen2.5-VL-72B-Instruct-AWQ -...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ed platform cuda. INFO 02-22 00:31:01 api_server.py:912] vLLM API server version 0.7.3 INFO 02-22 00:31:01 api_server.py:913] args: Namespace(host='0.0.0.0', port=8000, uvicorn_log_level='info', allow_credentials=False,...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', dis...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Errors Encountered While Running Qwen/Qwen2.5-VL-72B-AWQ Inference on 8x24G的4090 GPUs bug;stale ### Your current environment ### 🐛 Describe the bug python3 -m vllm.entrypoints.openai.api_server --model Qwen/Qwen2...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: dtype='auto', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
