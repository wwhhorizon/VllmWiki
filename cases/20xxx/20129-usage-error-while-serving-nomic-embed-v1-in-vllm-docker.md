# vllm-project/vllm#20129: [Usage]: Error while serving nomic-embed-v1 in vllm docker

| 字段 | 值 |
| --- | --- |
| Issue | [#20129](https://github.com/vllm-project/vllm/issues/20129) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;operator;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Error while serving nomic-embed-v1 in vllm docker

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` - Cannot run the code OS: Ubuntu 22.04.5 LTS CUDA Driver Version: 535.230.02 CUDA Version: 12.2 GPU Configuration: NVIDIA L40S 48GB ``` I am trying to serve nomic-embed-v1 and v1.5 embedding models through vllm docker, using the following command - `docker run --name nomic_inf -d --rm --runtime nvidia --gpus device=0 -v /var/models:/var/models -p 8070:8000 --ipc=host vllm/vllm-openai:latest --model /var/models/nomic-embed-text-v1.5 --served-model-name nomic-embed-text --task=embed --trust-remote-code` But I am getting the following error - ``` INFO 06-26 06:53:05 [__init__.py:239] Automatically detected platform cuda. INFO 06-26 06:53:07 [api_server.py:1034] vLLM API server version 0.8.4 INFO 06-26 06:53:07 [api_server.py:1035] args: Namespace(host=None, port=8000, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Usage]: Error while serving nomic-embed-v1 in vllm docker usage ### Your current environment ```text The output of `python collect_env.py` - Cannot run the code OS: Ubuntu 22.04.5 LTS CUDA Driver Version: 535.230.02 CU...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: model_loader_extra_config=None, use_tqdm_on_load=True, config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='auto', logits_processor_pattern=None, model_impl='auto', distribu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: buntu 22.04.5 LTS CUDA Driver Version: 535.230.02 CUDA Version: 12.2 GPU Configuration: NVIDIA L40S 48GB ``` I am trying to serve nomic-embed-v1 and v1.5 embedding models through vllm docker, using the following command...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='/var/models/nomic-embed-text-v1.5',...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: =None, port=8000, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapter...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
