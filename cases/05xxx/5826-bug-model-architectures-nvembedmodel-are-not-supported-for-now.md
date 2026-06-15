# vllm-project/vllm#5826: [Bug]: Model architectures ['NVEmbedModel'] are not supported for now

| 字段 | 值 |
| --- | --- |
| Issue | [#5826](https://github.com/vllm-project/vllm/issues/5826) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization |
| 子分类 | install |
| Operator 关键词 | attention;cuda;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Model architectures ['NVEmbedModel'] are not supported for now

### Issue 正文摘录

### Your current environment Using the Docker Image vllm/vllm-openai:v0.5.0.post1 ### 🐛 Describe the bug I am trying to run the model nvidia/NV-Embed-v1 using the latest vLLM image in a Kubernetes Cluster. Unfortunately, it seems the model is not yet supported, as I get the following error message: ``` INFO 06-25 13:36:15 api_server.py:177] vLLM API server version 0.5.0.post1 INFO 06-25 13:36:15 api_server.py:178] args: Namespace(host=None, port=8080, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], model='/mnt/models/', tokenizer=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=True, download_dir='/models-cache', load_format='auto', dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=8000, guided_decoding_backend='outlines', distributed_executor_backend=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_para...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 9: [Bug]: Model architectures ['NVEmbedModel'] are not supported for now bug;stale ### Your current environment Using the Docker Image vllm/vllm-openai:v0.5.0.post1 ### 🐛 Describe the bug I am trying to run the model nvidi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: not supported for now bug;stale ### Your current environment Using the Docker Image vllm/vllm-openai:v0.5.0.post1 ### 🐛 Describe the bug I am trying to run the model nvidia/NV-Embed-v1 using the latest vLLM image in a K...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: Bug]: Model architectures ['NVEmbedModel'] are not supported for now bug;stale ### Your current environment Using the Docker Image vllm/vllm-openai:v0.5.0.post1 ### 🐛 Describe the bug I am trying to run the model nvidia...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: rust_remote_code=True, download_dir='/models-cache', load_format='auto', dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=8000, guided_decoding_backend='outlines', distributed_executor_ba...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Model architectures ['NVEmbedModel'] are not supported for now bug;stale ### Your current environment Using the Docker Image vllm/vllm-openai:v0.5.0.post1 ### 🐛 Describe the bug I am trying to run the model nvidi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
