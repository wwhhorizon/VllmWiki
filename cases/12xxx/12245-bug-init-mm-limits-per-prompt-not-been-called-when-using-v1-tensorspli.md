# vllm-project/vllm#12245: [Bug]: init_mm_limits_per_prompt not been called when using V1 + TensorSplit + Qwen2VL

| 字段 | 值 |
| --- | --- |
| Issue | [#12245](https://github.com/vllm-project/vllm/issues/12245) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | cold_start |
| Operator 关键词 | attention;cache;cuda;gemm;operator;quantization;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: init_mm_limits_per_prompt not been called when using V1 + TensorSplit + Qwen2VL

### Issue 正文摘录

### Your current environment ### Model Input Dumps No input. ### 🐛 Describe the bug V1 engine works for qwen2-vl only when single gpu, but not tensor-split(multi-gpu). ```log MAX_PIXELS=1003520 MIN_PIXELS=250880 INFO 01-21 13:45:38 __init__.py:179] Automatically detected platform cuda. INFO 01-21 13:45:42 api_server.py:768] vLLM API server version 0.6.6.post2.dev274+g81763c58 INFO 01-21 13:45:42 api_server.py:769] args: Namespace(subparser='serve', model_tag='/mnt/bn/nas-develop-lyc/mlx/users/yuchen.lyc/src/ui_vllm_deploy/bin/../model/Qwen/Qwen2-VL-7B-Instruct', config='', host='::', port=11111, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='/mnt/bn/nas-develop-lyc/mlx/users/yuchen.l...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: init_mm_limits_per_prompt not been called when using V1 + TensorSplit + Qwen2VL bug ### Your current environment ### Model Input Dumps No input. ### 🐛 Describe the bug V1 engine works for qwen2-vl only when single gpu,...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ed platform cuda. INFO 01-21 13:45:42 api_server.py:768] vLLM API server version 0.6.6.post2.dev274+g81763c58 INFO 01-21 13:45:42 api_server.py:769] args: Namespace(subparser='serve', model_tag='/mnt/bn/nas-develop-lyc/...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='/mnt/bn/nas-develop-lyc/mlx/users/yu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: uto', quantization_param_path=None, max_model_len=32768, guided_decoding_backend='lm-format-enforcer', logits_processor_pattern=None, distributed_executor_backend=None, worker_use_ray=False, pipeline_parallel_size=1, te...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=32768, guided_decoding_backend='lm-format-enforcer', logits_proce...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
