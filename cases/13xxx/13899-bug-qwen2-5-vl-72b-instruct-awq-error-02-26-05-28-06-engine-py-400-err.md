# vllm-project/vllm#13899: [Bug]: 【Qwen2.5-VL-72B-Instruct-AWQ】ERROR 02-26 05:28:06 engine.py:400] Error while deserializing header: InvalidHeaderDeserialization

| 字段 | 值 |
| --- | --- |
| Issue | [#13899](https://github.com/vllm-project/vllm/issues/13899) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cuda;kernel;quantization;triton |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 【Qwen2.5-VL-72B-Instruct-AWQ】ERROR 02-26 05:28:06 engine.py:400] Error while deserializing header: InvalidHeaderDeserialization

### Issue 正文摘录

### Your current environment vllm0.7.3 https://modelscope.cn/models/Qwen/Qwen2.5-VL-72B-Instruct-AWQ [2025-02-26 updated] ![Image](https://github.com/user-attachments/assets/d185f086-99f6-402d-97cd-ab12ffa7dedb) ### 🐛 Describe the bug root@node37:/disk1/qwen-2.5-vl-72b-in-awq-0226# docker compose -f docker-compose.yml down [+] Running 2/2 ✔ Container qwen-2.5-vl-72b-in-awq Removed 6.0s ✔ Network qwen-25-vl-72b-in-awq-0226_default Removed 0.1s root@node37:/disk1/qwen-2.5-vl-72b-in-awq-0226# vi docker-compose.yml version: '3.3' services: # vllm vllm-openai: image: vllm/vllm-openai:v0.7.3 container_name: qwen-2.5-vl-72b-in-awq restart: always environment: - VLLM_WORKER_MULTIPROC_METHOD=spawn runtime: nvidia ports: - 8001:8000 volumes: - /disk1/:/models command: > --model /models/qwen-2.5-vl-72b-in-awq-0226 --tokenizer_mode="auto" --dtype=float16 --max_num_seqs 16 --tensor_parallel_size=2 --gpu-memory-utilization=0.9 --max-model-len=32768 --served-model-name=Qwen2.5-VL-72B-Instruct-AWQ deploy: resources: reservations: devices: - driver: nvidia capabilities: [gpu] device_ids: [ "2", "3" ] ipc: host networks: vllm: ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ "docker-compose.yml" [dos] 33L, 832C...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: :400] Error while deserializing header: InvalidHeaderDeserialization bug;stale ### Your current environment vllm0.7.3 https://modelscope.cn/models/Qwen/Qwen2.5-VL-72B-Instruct-AWQ [2025-02-26 updated] ![Image](https://g...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ### 🐛 Describe the bug root@node37:/disk1/qwen-2.5-vl-72b-in-awq-0226# docker compose -f docker-compose.yml down [+] Running 2/2 ✔ Container qwen-2.5-vl-72b-in-awq Removed
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: models/qwen-2.5-vl-72b-in-awq-0226 --tokenizer_mode="auto" --dtype=float16 --max_num_seqs 16 --tensor_parallel_size=2 --gpu-memory-utilization=0.9 --max-model-len=32768 --served-model-name=Qwen2.5-VL-72B-Instruct-AWQ de...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: 【Qwen2.5-VL-72B-Instruct-AWQ】ERROR 02-26 05:28:06 engine.py:400] Error while deserializing header: InvalidHeaderDeserialization bug;stale ### Your current environment vllm0.7.3 https://modelscope.cn/models/Qwen/Q...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: e='float16', kv_cache_dtype='auto', max_model_len=32768, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
