# vllm-project/vllm#7576: [Bug]: vllm运行卡住

| 字段 | 值 |
| --- | --- |
| Issue | [#7576](https://github.com/vllm-project/vllm/issues/7576) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;quantization;triton |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm运行卡住

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug (base) bob@test-ESC8000A-E11:~$ python -m vllm.entrypoints.openai.api_server \ --model /home/bob/LLaMA3-8B-Chinese-Chat-medical \ --served-model-name llama3:8b-instruct-fp16 \ --trust-remote-code \ --max-model-len 4096 \ --tensor-parallel-size 4 \ --gpu-memory-utilization 0.7 \ --port 8000 INFO 08-16 10:11:07 api_server.py:212] vLLM API server version 0.5.2 INFO 08-16 10:11:07 api_server.py:213] args: Namespace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], model='/home/bob/LLaMA3-8B-Chinese-Chat-medical', tokenizer=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=True, download_dir=None, load_format='auto', dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=4096, guided_decoding_backend='outlines', distributed_executor_b...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: False, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', scheduler_delay_factor=0.0, enable_chunked_prefill=False, speculative_model=None, num_speculative_tokens=None, speculative_draft_tensor_parallel_s...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e='auto', trust_remote_code=True, download_dir=None, load_format='auto', dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=4096, guided_decoding_backend='outlines', distributed_executor_ba...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: est-ESC8000A-E11:~$ python -m vllm.entrypoints.openai.api_server \ --model /home/bob/LLaMA3-8B-Chinese-Chat-medical \ --served-model-name llama3:8b-instruct-fp16 \ --trust-remote-code \ --max-model-len 4096 \ --tensor-p...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: pace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: auto', quantization_param_path=None, max_model_len=4096, guided_decoding_backend='outlines', distributed_executor_backend=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=4, max_parallel_loadin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
