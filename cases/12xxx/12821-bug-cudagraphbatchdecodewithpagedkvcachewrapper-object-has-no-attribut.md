# vllm-project/vllm#12821: [Bug]: 'CUDAGraphBatchDecodeWithPagedKVCacheWrapper' object has no attribute 'plan' when serving QwenMoE model

| 字段 | 值 |
| --- | --- |
| Issue | [#12821](https://github.com/vllm-project/vllm/issues/12821) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;oom |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 'CUDAGraphBatchDecodeWithPagedKVCacheWrapper' object has no attribute 'plan' when serving QwenMoE model

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug * CMD: `CUDA_VISIBLE_DEVICES=1 vllm serve ./raw-moes/qwen2_5-8x0_5B-it --port 8787 --max-model-len 1024 --gpu-memory-utilization 0.6` * Logs: ``` INFO 02-06 10:07:10 __init__.py:183] Automatically detected platform cuda. INFO 02-06 10:07:11 api_server.py:838] vLLM API server version 0.7.1 INFO 02-06 10:07:11 api_server.py:839] args: Namespace(subparser='serve', model_tag='./raw-moes/qwen2_5-8x0_5B-it', config='', host=None, port=8787, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, enable_reasoning=False, reasoning_parser=None, tool_call_parser=None, tool_parser_plugin='', model='./raw-moes/qwen2_5-8x0_5B-it', task='auto', tokenizer=None, skip_tokenizer_init=False, revision=None, code_...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: 'CUDAGraphBatchDecodeWithPagedKVCacheWrapper' object has no attribute 'plan' when serving QwenMoE model bug;stale ### Your current environment ### 🐛 Describe the bug * CMD: `CUDA_VISIBLE_DEVICES=1 vllm serve ./ra...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ed platform cuda. INFO 02-06 10:07:11 api_server.py:838] vLLM API server version 0.7.1 INFO 02-06 10:07:11 api_server.py:839] args: Namespace(subparser='serve', model_tag='./raw-moes/qwen2_5-8x0_5B-it', config='', host=...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=1024, guided_decoding_backend='xgrammar', logits_processor_pattern=None, distributed_executor_b...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: codeWithPagedKVCacheWrapper' object has no attribute 'plan' when serving QwenMoE model bug;stale ### Your current environment ### 🐛 Describe the bug * CMD: `CUDA_VISIBLE_DEVICES=1 vllm serve ./raw-moes/qwen2_5-8x0_5B-it...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: dtype='auto', kv_cache_dtype='auto', max_model_len=1024, guided_decoding_backend='xgrammar', logits_processor_pattern=None, distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel_size=1, max_parall...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
