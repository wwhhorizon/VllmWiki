# vllm-project/vllm#6169: [Bug]: TypeError: 'NoneType' object is not callable when loading Gemma 2 9B with new 0.5.1 version

| 字段 | 值 |
| --- | --- |
| Issue | [#6169](https://github.com/vllm-project/vllm/issues/6169) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | install |
| Operator 关键词 | attention;cuda;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TypeError: 'NoneType' object is not callable when loading Gemma 2 9B with new 0.5.1 version

### Issue 正文摘录

### Your current environment Idk how to run it inside a docker ### 🐛 Describe the bug Simply run the following command `docker run --runtime nvidia --gpus all -v ~/.cache/huggingface:/root/.cache/huggingface --env "HUGGING_FACE_HUB_TOKEN= " --env "VLLM_ATTENTION_BACKEND=FLASHINFER" -p 8000:8000 --ipc=host vllm/vllm-openai:latest --model google/gemma-2-9b-it` It doesn't work. Log: ``` INFO 07-06 07:29:27 api_server.py:206] vLLM API server version 0.5.1 INFO 07-06 07:29:27 api_server.py:207] args: Namespace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], model='google/gemma-2-9b-it', tokenizer=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=None, guided_decoding_backend='outlines', distributed_executo...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: TypeError: 'NoneType' object is not callable when loading Gemma 2 9B with new 0.5.1 version bug ### Your current environment Idk how to run it inside a docker ### 🐛 Describe the bug Simply run the following comma...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: tors=None, max_cpu_loras=None, fully_sharded_loras=False, device='auto', scheduler_delay_factor=0.0, enable_chunked_prefill=False, speculative_model=None, num_speculative_tokens=None, speculative_draft_tensor_parallel_s...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: 'NoneType' object is not callable when loading Gemma 2 9B with new 0.5.1 version bug ### Your current environment Idk how to run it inside a docker ### 🐛 Describe the bug Simply run the following command `docker run --r...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=None, guided_decoding_backend='outlines', distributed_executor_ba...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: pace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, chat_template=None, response_role='assi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
