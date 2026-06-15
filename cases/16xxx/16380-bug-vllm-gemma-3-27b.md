# vllm-project/vllm#16380: [Bug]: vllm部署Gemma-3-27b问题

| 字段 | 值 |
| --- | --- |
| Issue | [#16380](https://github.com/vllm-project/vllm/issues/16380) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;gemm;quantization;sampling;triton |
| 症状 | crash;oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm部署Gemma-3-27b问题

### Issue 正文摘录

### Your current environment 我的启动命令是 (torch) root@vvbbovkdctrbyrag-wind-b6df56d5-r96vk:/data/coding# vllm serve Gemma-3-27b --tensor-parallel-size 4 --max-model-len 65536 --max-num-batched-tokens 16384 --port 30041 --trust-remote-code --served-model-name gemma3-27b --max-num-seqs 64 --enable-chunked-prefill --limit-mm-per-prompt image=50,video=2 --api-key k7YgF9RwP4qXmTnV2LsJ3HdO5zIc6AeB0Uv1lKpN8Q INFO 04-10 08:57:28 [__init__.py:256] Automatically detected platform cuda. INFO 04-10 08:57:30 [api_server.py:972] vLLM API server version 0.8.0rc3.dev5+g5eeabc2a.d20250318 INFO 04-10 08:57:30 [api_server.py:973] args: Namespace(subparser='serve', model_tag='Gemma-3-27b', config='', host=None, port=30041, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key='k7YgF9RwP4qXmTnV2LsJ3HdO5zIc6AeB0Uv1lKpN8Q', lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, enable_ssl_refresh=False, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiproce...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: vllm部署Gemma-3-27b问题 bug ### Your current environment 我的启动命令是 (torch) root@vvbbovkdctrbyrag-wind-b6df56d5-r96vk:/data/coding# vllm serve Gemma-3-27b --tensor-parallel-size 4 --max-model-len 65536 --max-num-batched...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: code --served-model-name gemma3-27b --max-num-seqs 64 --enable-chunked-prefill --limit-mm-per-prompt image=50,video=2 --api-key k7YgF9RwP4qXmTnV2LsJ3HdO5zIc6AeB0Uv1lKpN8Q INFO 04-10 08:57:28 [__init__.py:256] Automatica...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: type='auto', kv_cache_dtype='auto', max_model_len=65536, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=65536, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', di...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: d platform cuda. INFO 04-10 08:57:30 [api_server.py:972] vLLM API server version 0.8.0rc3.dev5+g5eeabc2a.d20250318 INFO 04-10 08:57:30 [api_server.py:973] args: Namespace(subparser='serve', model_tag='Gemma-3-27b', conf...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
