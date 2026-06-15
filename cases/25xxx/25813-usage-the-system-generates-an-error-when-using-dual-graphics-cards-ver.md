# vllm-project/vllm#25813: [Usage]: The system generates an error when using dual graphics cards; version 10.1.1 functions correctly, but version 10.2 triggers an error upon execution.

| 字段 | 值 |
| --- | --- |
| Issue | [#25813](https://github.com/vllm-project/vllm/issues/25813) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;moe;operator;quantization |
| 症状 | crash;import_error;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: The system generates an error when using dual graphics cards; version 10.1.1 functions correctly, but version 10.2 triggers an error upon execution.

### Issue 正文摘录

### Your current environment wsl docker ### How would you like to use vllm wsl docker The system generates an error when using dual graphics cards; version 10.1.1 functions correctly, but version 10.2 triggers an error upon execution. By the way, will the use of "--kv-cache-dtype fp8" in my setup result in a loss of precision? The model I am using is also in fp8 format. docker ``` services: vllm-openai-8000: runtime: nvidia # 使用所有gpu deploy: resources: reservations: devices: - driver: nvidia count: all capabilities: - gpu command: > --model /models/safetensors/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8 --served-model-name Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8 --gpu-memory-utilization 0.5 --kv-cache-dtype fp8 --enable-expert-parallel --tensor-parallel-size 2 --enable-auto-tool-choice --tool-call-parser hermes volumes: - ./models/.cache/huggingface:/root/.cache/huggingface - ./models/safetensors:/models/safetensors dns: - 8.8.8.8 ports: - 8001:8000 ipc: host image: vllm/vllm-openai:v0.10.1.1 ``` log ``` (APIServer pid=1) INFO 09-27 17:46:55 [api_server.py:1896] vLLM API server version 0.10.2 (APIServer pid=1) INFO 09-27 17:46:55 [utils.py:328] non-default args: {'enable_auto_tool_choice'...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Usage]: The system generates an error when using dual graphics cards; version 10.1.1 functions correctly, but version 10.2 triggers an error upon execution. usage ### Your current environment wsl docker ### How would y...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: iggers an error upon execution. By the way, will the use of "--kv-cache-dtype fp8" in my setup result in a loss of precision? The model I am using is also in fp8 format. docker ``` services: vllm-openai-8000: runtime: n...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: of "--kv-cache-dtype fp8" in my setup result in a loss of precision? The model I am using is also in fp8 format. docker ``` services: vllm-openai-8000: runtime: nvidia # 使用所有gpu deploy: resources: reservations: devices:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: . (APIServer pid=1) WARNING 09-27 17:47:11 [arg_utils.py:1587] Chunked prefill is enabled by default for models with max_model_len > 32K. Chunked prefill might not work with some features or models. If you encounter any...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: , kv_cache_dtype=fp8, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_co...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
