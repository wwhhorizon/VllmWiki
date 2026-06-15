# vllm-project/vllm#5827: [Bug]: Internal Server Error when hosting Alibaba-NLP/gte-Qwen2-7B-instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#5827](https://github.com/vllm-project/vllm/issues/5827) |
| 状态 | closed |
| 标签 | bug;keep-open |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;quantization |
| 症状 | crash;oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Internal Server Error when hosting Alibaba-NLP/gte-Qwen2-7B-instruct

### Issue 正文摘录

### Your current environment Using latest available docker image: vllm/vllm-openai:v0.5.0.post1 ### 🐛 Describe the bug I am getting as response "Internal Server Error" when calling the /v1/embeddings endpoint of the Kubernetes-deployed version of the model x. I am using the following json request as body: ```json { "model": "/mnt/models/", "input": [ "test" ], "user": "user" } ``` For reference, here is the log of the vLLM container: ``` INFO 06-25 14:21:47 api_server.py:177] vLLM API server version 0.5.0.post1 INFO 06-25 14:21:47 api_server.py:178] args: Namespace(host=None, port=8080, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], model='/mnt/models/', tokenizer=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=True, download_dir='/models-cache', load_format='auto', dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_le...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: truct bug;keep-open ### Your current environment Using latest available docker image: vllm/vllm-openai:v0.5.0.post1 ### 🐛 Describe the bug I am getting as response "Internal Server Error" when calling the /v1/embeddings...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ubernetes-deployed version of the model x. I am using the following json request as body: ```json { "model": "/mnt/models/", "input": [ "test" ], "user": "user" } ``` For reference, here is the log of the vLLM container...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: rust_remote_code=True, download_dir='/models-cache', load_format='auto', dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=8000, guided_decoding_backend='outlines', distributed_executor_ba...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: pace(host=None, port=8080, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, chat_template=None, response_role='assi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Internal Server Error when hosting Alibaba-NLP/gte-Qwen2-7B-instruct bug;keep-open ### Your current environment Using latest available docker image: vllm/vllm-openai:v0.5.0.post1 ### 🐛 Describe the bug I am getti...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
