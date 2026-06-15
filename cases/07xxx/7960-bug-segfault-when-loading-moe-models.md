# vllm-project/vllm#7960: [Bug]: segfault when loading MoE models

| 字段 | 值 |
| --- | --- |
| Issue | [#7960](https://github.com/vllm-project/vllm/issues/7960) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 23; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: segfault when loading MoE models

### Issue 正文摘录

### Your current environment ### Anything you want to discuss about vllm. ### Your current environment ### 🐛 Describe the bug ### 🐛 Describe the bug Cannot run mixtral 8x7b ``` INFO 08-20 20:23:00 api_server.py:212] vLLM API server version 0.5.2 INFO 08-20 20:23:00 api_server.py:213] args: Namespace(model_tag='mistralai/Mixtral-8x7B-Instruct-v0.1/', host='0.0.0.0', port=1234, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], model='mistralai/Mixtral-8x7B-Instruct-v0.1/', tokenizer=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=8192, guided_decoding_backend='outlines', distributed_executor_backend='ray', worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=8, max_parallel_loading_worke...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: mixtral 8x7b ``` INFO 08-20 20:23:00 api_server.py:212] vLLM API server version 0.5.2 INFO 08-20 20:23:00 api_server.py:213] args: Namespace(model_tag='mistralai/Mixtral-8x7B-Instruct-v0.1/', host='0.0.0.0', port=1234,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: False, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', scheduler_delay_factor=0.0, enable_chunked_prefill=False, speculative_model=None, num_speculative_tokens=None, speculative_draft_tensor_parallel_s...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=8192, guided_decoding_backend='outlines', distributed_executor_ba...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: segfault when loading MoE models bug ### Your current environment ### Anything you want to discuss about vllm. ### Your current environment ### 🐛 Describe the bug ### 🐛 Describe the bug Cannot run mixtral 8x7b ``...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: auto', quantization_param_path=None, max_model_len=8192, guided_decoding_backend='outlines', distributed_executor_backend='ray', worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=8, max_parallel_loadi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
