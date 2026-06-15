# vllm-project/vllm#13719: [Bug]: [Qwen2.5-VL-72B-Instruct-4bit](VllmWorkerProcess pid=191) WARNING 02-22 22:09:01 custom_all_reduce.py:136] Custom allreduce is disabled because it's not supported on more than two PCIe-only GPUs.

| 字段 | 值 |
| --- | --- |
| Issue | [#13719](https://github.com/vllm-project/vllm/issues/13719) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cuda;quantization;triton |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [Qwen2.5-VL-72B-Instruct-4bit](VllmWorkerProcess pid=191) WARNING 02-22 22:09:01 custom_all_reduce.py:136] Custom allreduce is disabled because it's not supported on more than two PCIe-only GPUs.

### Issue 正文摘录

### Your current environment root@node37:/disk1/qwen-2.5-vl-72b-4bit# cat docker-compose.yml ﻿version: '3.3' services: # vllm vllm-openai: image: vllm/vllm-openai:v0.7.3 container_name: qwen2.5-72b-4bit restart: always runtime: nvidia ports: - 8001:8000 volumes: - /disk1/:/models command: > --model /models/qwen-2.5-vl-72b-4bit --tokenizer_mode="auto" --dtype=bfloat16 --tensor_parallel_size=4 --gpu-memory-utilization=0.9 --max-model-len=16384 --served-model-name=Qwen2.5-VL-72B-Instruct-4bit deploy: resources: reservations: devices: - driver: nvidia capabilities: [gpu] device_ids: [ "0","1","2", "3" ] ipc: host networks: vllm: root@node37:/disk1/qwen-2.5-vl-72b-4bit# root@node37:/disk1/qwen-2.5-vl-72b-4bit# docker logs -f qwen2.5-72b-4bit INFO 02-22 22:08:41 __init__.py:207] Automatically detected platform cuda. INFO 02-22 22:08:41 api_server.py:912] vLLM API server version 0.7.3 INFO 02-22 22:08:41 api_server.py:913] args: Namespace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto',...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: disabled because it's not supported on more than two PCIe-only GPUs. bug;stale ### Your current environment root@node37:/disk1/qwen-2.5-vl-72b-4bit# cat docker-compose.yml ﻿version: '3.3' services: # vllm vllm-openai: i...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ustom allreduce is disabled because it's not supported on more than two PCIe-only GPUs. bug;stale ### Your current environment root@node37:/disk1/qwen-2.5-vl-72b-4bit# cat docker-compose.yml ﻿version: '3.3' services: #...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: model /models/qwen-2.5-vl-72b-4bit --tokenizer_mode="auto" --dtype=bfloat16 --tensor_parallel_size=4 --gpu-memory-utilization=0.9 --max-model-len=16384 --served-model-name=Qwen2.5-VL-72B-Instruct-4bit deploy: resources:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: [Qwen2.5-VL-72B-Instruct-4bit](VllmWorkerProcess pid=191) WARNING 02-22 22:09:01 custom_all_reduce.py:136] Custom allreduce is disabled because it's not supported on more than two PCIe-only GPUs. bug;stale ### Yo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ='bfloat16', kv_cache_dtype='auto', max_model_len=16384, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
