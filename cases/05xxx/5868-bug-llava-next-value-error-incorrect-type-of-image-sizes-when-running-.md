# vllm-project/vllm#5868: [Bug]: LLaVa Next Value Error - "Incorrect type of image sizes" when running in Docker

| 字段 | 值 |
| --- | --- |
| Issue | [#5868](https://github.com/vllm-project/vllm/issues/5868) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization |
| 子分类 | precision |
| Operator 关键词 | cuda;quantization |
| 症状 | crash;mismatch |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: LLaVa Next Value Error - "Incorrect type of image sizes" when running in Docker

### Issue 正文摘录

### Your current environment Current Environment Docker image: `vllm/vllm-openai:v0.5.0.post1` Running as part of a Docker Compose stack. Relevant sections of my `docker-compose.yaml` are below. This is part of a multi-model deployment with other vLLM-based text generation/chat models running successfully behind a Traefik reverse proxy. I split out the instance running LLaVa 1.6 into its own service in the `docker-compose.yaml` to test the different commands it requires passed in on startup, it is the third service in the file. I have included the .env file entries as well. ``` ###docker-compose.yaml### services: reverseproxy: image: ${PROXY_IMAGE} container_name: reverseproxy # Enables the web UI and tells Traefik to listen to docker command: --api.insecure=true --providers.docker --api.dashboard=true ports: # The HTTP port - "80:80" # The Web UI (enabled by --api.insecure=true) - "8080:8080" volumes: # So that Traefik can listen to the Docker events - /var/run/docker.sock:/var/run/docker.sock networks: - llm-net ## Current best solution for chat/text generation models ## Change GPU device_ids if necessary vllm-server: depends_on: - reverseproxy image: ${VLLM_IMAGE} container_nam...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: sections of my `docker-compose.yaml` are below. This is part of a multi-model deployment with other vLLM-based text generation/chat models running successfully behind a Traefik reverse proxy. I split out the instance ru...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: LLaVa Next Value Error - "Incorrect type of image sizes" when running in Docker bug ### Your current environment Current Environment Docker image: `vllm/vllm-openai:v0.5.0.post1` Running as part of a Docker Compose stac...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=None, guided_decoding_backend='outlines', distributed_executor_ba...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ssor=None, image_processor_revision=None, disable_image_processor=False, scheduler_delay_factor=0.0, enable_chunked_prefill=False, speculative_model=None, num_speculative_tokens=None, speculative_max_model_len=None, spe...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: host='0.0.0.0', port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, chat_template='template_llava.jinja', r...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
