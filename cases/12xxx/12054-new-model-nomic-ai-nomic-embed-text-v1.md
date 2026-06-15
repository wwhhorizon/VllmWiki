# vllm-project/vllm#12054: [New Model]: nomic-ai/nomic-embed-text-v1

| 字段 | 值 |
| --- | --- |
| Issue | [#12054](https://github.com/vllm-project/vllm/issues/12054) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [New Model]: nomic-ai/nomic-embed-text-v1

### Issue 正文摘录

### Your current environment Running in docker, `vllm/vllm-openai@sha256:8672d9356d4f4474695fd69ef56531d9e482517da3b31feb9c975689332a4fb0` (`:latest` as of this date) ### Model Input Dumps _No response_ ### 🐛 Describe the bug Using the below `docker-compose`: ```yaml ai-vllm-nomic: image: vllm/vllm-openai@sha256:8672d9356d4f4474695fd69ef56531d9e482517da3b31feb9c975689332a4fb0 # [target: latest] container_name: ai-vllm-nomic volumes: - /ai/lmdeploy/huggingface:/root/.cache/huggingface environment: HUGGING_FACE_HUB_TOKEN: restart: unless-stopped ports: - 127.0.0.1:8001:8000 networks: - ai command: --model nomic-ai/nomic-embed-text-v1 --trust-remote-code privileged: true deploy: resources: reservations: devices: - driver: nvidia count: 1 capabilities: [gpu] ``` This model was chosen based on the documentation for the vLLM and Continue.dev integration at: https://docs.continue.dev/customize/model-providers/more/vllm Full error: ``` INFO 01-14 11:23:22 api_server.py:712] vLLM API server version 0.6.6.post1 INFO 01-14 11:23:22 api_server.py:713] args: Namespace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_...

## 现有链接修复摘要

#17785 [New Model]: nomic-embed-text-v2-moe

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 11: [New Model]: nomic-ai/nomic-embed-text-v1 new-model ### Your current environment Running in docker, `vllm/vllm-openai@sha256:8672d9356d4f4474695fd69ef56531d9e482517da3b31feb9c975689332a4fb0` (`:latest` as of this date) #
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: i/nomic-embed-text-v1 new-model ### Your current environment Running in docker, `vllm/vllm-openai@sha256:8672d9356d4f4474695fd69ef56531d9e482517da3b31feb9c975689332a4fb0` (`:latest` as of this date) ### Model Input Dump...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='nomic-ai/nomic-embed-text-v1.5', tas...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_patter...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 392, in _init_multimodal_config if ModelRegistry.is_multimodal_model(architectures): ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/models/registry.py"...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#17785](https://github.com/vllm-project/vllm/pull/17785) | closes_keyword | 0.95 | [New Model]: nomic-embed-text-v2-moe | Fix #12054 Fix #17949 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
