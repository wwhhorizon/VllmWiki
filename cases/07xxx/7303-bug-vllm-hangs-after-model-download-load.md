# vllm-project/vllm#7303: [Bug]: vllm hangs after model download / load

| 字段 | 值 |
| --- | --- |
| Issue | [#7303](https://github.com/vllm-project/vllm/issues/7303) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;quantization |
| 症状 | crash;mismatch;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm hangs after model download / load

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug ### On the Tesla T4 the model "hangs" after loading the model (the vram usage spikes normally and stays constant) but nothings comes after ### Setup ` containers: - name: ubuntu image: 'docker.io/vllm/vllm-openai:v0.5.3.post1' args: - '--host' - 0.0.0.0 - '--model' - microsoft/Phi-3-mini-4k-instruct - '--dtype' - float16` ### Log ``` INFO 08-08 14:40:35 api_server.py:219] vLLM API server version 0.5.3.post1 INFO 08-08 14:40:35 api_server.py:220] args: Namespace(host='0.0.0.0', port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], model='microsoft/Phi-3-mini-4k-instruct', tokenizer=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='float16', kv_cache_dtype='auto', quanti...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: False, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, num_speculative_tokens=None, speculative_draft_tensor_parallel_si...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ### Setup ` containers: - name: ubuntu image: 'docker.io/vllm/vllm-openai:v0.5.3.post1' args: - '--host' - 0.0.0.0 - '--model' - microsoft/Phi-3-mini-4k-instruct - '--dtype' - float16`
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: --model' - microsoft/Phi-3-mini-4k-instruct - '--dtype' - float16` ### Log ``` INFO 08-08 14:40:35 api_server.py:219] vLLM API server version 0.5.3.post1 INFO 08-08 14:40:35 api_server.py:220] args: Namespace(host='0.0....
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: host='0.0.0.0', port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: vllm hangs after model download / load bug ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug ### On the Tesla T4 the model "hangs" after loading the model (the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
