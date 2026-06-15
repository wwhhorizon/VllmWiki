# vllm-project/vllm#3808: [Bug]: AssertionError: libcuda.so cannot found with vllm/vllm-openai:v0.4.0

| 字段 | 值 |
| --- | --- |
| Issue | [#3808](https://github.com/vllm-project/vllm/issues/3808) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;moe;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AssertionError: libcuda.so cannot found with vllm/vllm-openai:v0.4.0

### Issue 正文摘录

### Your current environment Running in Kubernetes on H100 in vllm/vllm-openai:v0.4.0 ### 🐛 Describe the bug Seems like there have been some weird dependency issues since v0.2.7. We would love to use flash attention when you are able to fix this! Thank you! 🙇 ```bash INFO 04-02 23:55:08 api_server.py:148] vLLM API server version 0.4.0 INFO 04-02 23:55:08 api_server.py:149] args: Namespace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=True, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, served_model_name=None, lora_modules=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], model='mistralai/Mixtral-8x7B-v0.1', tokenizer=None, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='auto', kv_cache_dtype='auto', max_model_len=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=2, max_parallel_loading_workers=None, ray_workers_use_nsight=False, block_size=16, enable_prefix_caching=False, use_v2_block_manager...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ai:v0.4.0 ### 🐛 Describe the bug Seems like there have been some weird dependency issues since v0.2.7. We would love to use flash attention when you are able to fix this! Thank you! 🙇 ```bash INFO 04-02 23:55:08 api_ser...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: ave been some weird dependency issues since v0.2.7. We would love to use flash attention when you are able to fix this! Thank you! 🙇 ```bash INFO 04-02 23:55:08 api_server.py:148] vLLM API server version 0.4.0 INFO 04-0...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='auto', kv_cache_dtype='auto', max_model_len=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=2, max_parallel_load...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: AssertionError: libcuda.so cannot found with vllm/vllm-openai:v0.4.0 bug;stale ### Your current environment Running in Kubernetes on H100 in vllm/vllm-openai:v0.4.0 ### 🐛 Describe the bug Seems like there have been some...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: '*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, served_model_name=None, lora_modules=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cer...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
