# vllm-project/vllm#18163: [Bug]: llama3.1 8B Instruct on A100 40GB crashes vllm server

| 字段 | 值 |
| --- | --- |
| Issue | [#18163](https://github.com/vllm-project/vllm/issues/18163) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | attention;cuda;operator;quantization;sampling |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: llama3.1 8B Instruct on A100 40GB crashes vllm server

### Issue 正文摘录

### Your current environment I am running vllm `0.8.5` on kubernetes to host llama 3.1 8B parameter : ``` │ Container ID: containerd://3e30114e2a7f79035439e7c0eafbd27f0c9cff223218677151cb14f206f35a83 │ Image: vllm/vllm-openai:v0.8.5 │ Image ID: docker.io/vllm/vllm-openai@sha256:6cf9808ca8810fc6c3fd0451c2e7784fb224590d81f7db338e7eaf3c02a33d33 │ Port: 8000/TCP │ Host Port: 0/TCP │ Command: │ vllm │ serve │ Llama-3.1-8B-Instruct │ --dtype │ auto │ --host │ 0.0.0.0 │ --port │ 8000 │ --gpu-memory-utilization │ 0.9 │ --swap-space │ 4 ``` ### 🐛 Describe the bug The server crashes and these are the logs: ```text INFO 05-14 11:28:32 [__init__.py:239] Automatically detected platform cuda. INFO 05-14 11:28:41 [api_server.py:1043] vLLM API server version 0.8.5 INFO 05-14 11:28:41 [api_server.py:1044] args: Namespace(subparser='serve', model_tag='Llama-3.1-8B-Instruct', config='', host='0.0.0.0', port=8000, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant'...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: │ Image ID: docker.io/vllm/vllm-openai@sha256:6cf9808ca8810fc6c3fd0451c2e7784fb224590d81f7db338e7eaf3c02a33d33
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: │ --dtype
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: llama3.1 8B Instruct on A100 40GB crashes vllm server bug;stale ### Your current environment I am running vllm `0.8.5` on kubernetes to host llama 3.1 8B parameter : ``` │ Container ID: containerd://3e30114e2a7f79
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: llama3.1 8B Instruct on A100 40GB crashes vllm server bug;stale ### Your current environment I am running vllm `0.8.5` on kubernetes to host llama 3.1 8B parameter : ``` │ Container ID: containerd://3e30114e2a7f7...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: True, config_format= , dtype='auto', max_model_len=None, guided_decoding_backend='auto', reasoning_parser=None, logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
