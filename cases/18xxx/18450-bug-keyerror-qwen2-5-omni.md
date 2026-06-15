# vllm-project/vllm#18450: [Bug]: KeyError: 'qwen2_5_omni'

| 字段 | 值 |
| --- | --- |
| Issue | [#18450](https://github.com/vllm-project/vllm/issues/18450) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: KeyError: 'qwen2_5_omni'

### Issue 正文摘录

### Your current environment root@node37:/disk1/Qwen2.5-Omni-7B# cat docker-compose.yml #version: '3.3' services: # vllm vllm-openai: image: vllm/vllm-openai:v0.8.5 container_name: Qwen2.5-Omni-7B restart: unless-stopped runtime: nvidia ports: - 8007:8000 volumes: - /disk1:/models command: > --model /models/Qwen2.5-Omni-7B --tokenizer_mode="auto" --trust-remote-code --dtype=bfloat16 --max_num_seqs=256 --tensor_parallel_size=1 --gpu-memory-utilization=0.9 --max-model-len=65536 --served-model-name=Qwen2.5-Omni-7B deploy: resources: reservations: devices: - driver: nvidia capabilities: [gpu] device_ids: [ "0" ] ipc: host networks: vllm: root@node37:/disk1/Qwen2.5-Omni-7B# docker compose -f docker-compose.yml down root@node37:/disk1/Qwen2.5-Omni-7B# docker compose -f docker-compose.yml up -d [+] Running 2/2 ✔ Network qwen25-omni-7b_default Created 0.1s ✔ Container Qwen2.5-Omni-7B Started 0.7s root@node37:/disk1/Qwen2.5-Omni-7B# docker logs -f Qwen2.5-Omni-7B INFO 05-20 19:04:51 [__init__.py:239] Automatically detected platform cuda. INFO 05-20 19:04:56 [api_server.py:1043] vLLM API server version 0.8.5 INFO 05-20 19:04:56 [api_server.py:1044] args: Namespace(host=None, port=8000, uvic...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ug ### Your current environment root@node37:/disk1/Qwen2.5-Omni-7B# cat docker-compose.yml #version: '3.3' services: # vllm vllm-openai: image: vllm/vllm-openai:v0.8.5 container_name: Qwen2.5-Omni-7B restart: unless-sto...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: KeyError: 'qwen2_5_omni' bug ### Your current environment root@node37:/disk1/Qwen2.5-Omni-7B# cat docker-compose.yml #version: '3.3' services: # vllm vllm-openai: image: vllm/vllm-openai:v0.8.5 container_name: Qw...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: -Omni-7B --tokenizer_mode="auto" --trust-remote-code --dtype=bfloat16 --max_num_seqs=256 --tensor_parallel_size=1 --gpu-memory-utilization=0.9 --max-model-len=65536 --served-model-name=Qwen2.5-Omni-7B deploy: resources:...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: =None, port=8000, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapter...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='/models/Qwen2.5-Omni-7B', task='auto...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
