# vllm-project/vllm#14247: [Bug]: 【Janus-Pro-7B】 KeyError: 'multi_modality'

| 字段 | 值 |
| --- | --- |
| Issue | [#14247](https://github.com/vllm-project/vllm/issues/14247) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 【Janus-Pro-7B】 KeyError: 'multi_modality'

### Issue 正文摘录

### Your current environment root@node37:/disk1/Janus-Pro-7B# cat docker-compose.yml version: '3.3' services: # vllm vllm-openai: image: vllm/vllm-openai:v0.7.3 container_name: Janus-Pro-7B restart: always runtime: nvidia ports: - 8107:8000 volumes: - /disk1/:/models command: > --model /models/Janus-Pro-7B --trust_remote_code --tokenizer_mode="auto" --dtype=bfloat16 --max_num_seqs=128 --tensor_parallel_size=1 --gpu-memory-utilization=0.9 --max-model-len=32768 --served-model-name=Janus-Pro-7B deploy: resources: reservations: devices: - driver: nvidia capabilities: [gpu] device_ids: [ "3" ] ipc: host networks: vllm: root@node37:/disk1/Janus-Pro-7B# docker logs -f Janus-Pro-7B INFO 03-04 17:35:18 __init__.py:207] Automatically detected platform cuda. INFO 03-04 17:35:18 api_server.py:912] vLLM API server version 0.7.3 INFO 03-04 17:35:18 api_server.py:913] args: Namespace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ' bug ### Your current environment root@node37:/disk1/Janus-Pro-7B# cat docker-compose.yml version: '3.3' services: # vllm vllm-openai: image: vllm/vllm-openai:v0.7.3 container_name: Janus-Pro-7B restart: always runtime...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: s-Pro-7B --trust_remote_code --tokenizer_mode="auto" --dtype=bfloat16 --max_num_seqs=128 --tensor_parallel_size=1 --gpu-memory-utilization=0.9 --max-model-len=32768 --served-model-name=Janus-Pro-7B deploy: resources: re...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ntime: nvidia ports: - 8107:8000 volumes: - /disk1/:/models command: > --model /models/Janus-Pro-7B --trust_remote_code --tokenizer_mode="auto" --dtype=bfloat16 --max_num_seqs=128 --tensor_parallel_size=1 --gpu-memory-u...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, enable_reasoning=False, reasoning_parser=None, tool_call_parser=None, tool_parser_plugin=...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: pace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
