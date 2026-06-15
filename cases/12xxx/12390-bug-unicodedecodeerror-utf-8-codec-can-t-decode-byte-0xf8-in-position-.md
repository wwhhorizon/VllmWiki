# vllm-project/vllm#12390: [Bug]: UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf8 in position 0: invalid start byte

| 字段 | 值 |
| --- | --- |
| Issue | [#12390](https://github.com/vllm-project/vllm/issues/12390) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf8 in position 0: invalid start byte

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I can start the server via the vllm serve command, ``` vllm serve /root/download/Qwen2.5-Coder-0.5B-Instruct \ --host 127.0.0.1 \ --port 6006 \ --served-model-name Qwen2.5-Coder-0.5B-Instruct \ --api-key xxx \ --gpu-memory-utilization 0.95 \ --max_model_len 4600 \ --enforce-eager ``` error log: ``` INFO 01-24 15:04:26 api_server.py:526] vLLM API server version 0.6.1.dev238+ge2c6e0a82 INFO 01-24 15:04:26 api_server.py:527] args: Namespace(model_tag='/root/download/Qwen2.5-Coder-0.5B-Instruct', config='', host='127.0.0.1', port=6006, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key='xxx', lora_modules=None, prompt_adapters=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_auto_tool_choice=False, tool_call_parser=None, model='/root/download/Qwen2.5-Coder-0.5B-Instruct', tokenizer=None, skip_tokenizer_init=False, revision=None, code_rev...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf8 in position 0: invalid start byte bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I can start the server...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: code=False, download_dir=None, load_format='auto', config_format='auto', dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=4600, guided_decoding_backend='outlines', distributed_executor_ba...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: auto', quantization_param_path=None, max_model_len=4600, guided_decoding_backend='outlines', distributed_executor_backend=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=1, max_parallel_loadin...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ` error log: ``` INFO 01-24 15:04:26 api_server.py:526] vLLM API server version 0.6.1.dev238+ge2c6e0a82 INFO 01-24 15:04:26 api_server.py:527] args: Namespace(model_tag='/root/download/Qwen2.5-Coder-0.5B-Instruct', conf...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ion 0: invalid start byte bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I can start the server via the vllm serve command, ``` vllm serve /root/download/Qwen2.5-Coder-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
