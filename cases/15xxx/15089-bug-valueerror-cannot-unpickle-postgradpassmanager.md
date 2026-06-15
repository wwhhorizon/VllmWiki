# vllm-project/vllm#15089: [Bug]: ValueError: Cannot unpickle PostGradPassManager

| 字段 | 值 |
| --- | --- |
| Issue | [#15089](https://github.com/vllm-project/vllm/issues/15089) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ValueError: Cannot unpickle PostGradPassManager

### Issue 正文摘录

### Your current environment I am running vllm using the 0.8.0 container with the following yaml args: - "--gpu-memory-utilization" - "0.99" - "--max-model-len" - "32768" - "--model" - "/models/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/945c8663693130f8be2ee66210e062158b2a9693" - "--chat-template" - "/vllm-workspace/examples/tool_chat_template_llama3.1_json.jinja" - "--enable-auto-tool-choice" - "--tool-call-parser" - "llama3_json" - "--tensor-parallel-size" - "2" this results error ### 🐛 Describe the bug INFO 03-19 05:10:40 __init__.py:256] Automatically detected platform cuda. INFO 03-19 05:10:43 api_server.py:977] vLLM API server version 0.8.0 INFO 03-19 05:10:43 api_server.py:978] args: Namespace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template='/vllm-workspace/examples/tool_chat_template_llama3.1_json.jinja', chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, enable_ssl_refresh=False, ssl_cert_reqs=0, root_path=None, middleware=[], re...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: ValueError: Cannot unpickle PostGradPassManager bug;stale ### Your current environment I am running vllm using the 0.8.0 container with the following yaml args: - "--gpu-memory-utilization" - "0.99" - "--max-mode...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ed platform cuda. INFO 03-19 05:10:43 api_server.py:977] vLLM API server version 0.8.0 INFO 03-19 05:10:43 api_server.py:978] args: Namespace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: args: - "--gpu-memory-utilization" - "0.99" - "--max-model-len" - "32768" - "--model" - "/models/models--meta-llama--Meta-Llama-3.1-70B-Instruct/snapshots/945c8663693130f8be2ee66210e062158b2a9693" - "--chat-template" -...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=32768, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', di...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: type='auto', kv_cache_dtype='auto', max_model_len=32768, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
