# vllm-project/vllm#20726: [Bug]: Excuse me, I run the model qwen2.5-7B and get an error, single card 5060TI16G:

| 字段 | 值 |
| --- | --- |
| Issue | [#20726](https://github.com/vllm-project/vllm/issues/20726) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits |
| 子分类 | cold_start |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Excuse me, I run the model qwen2.5-7B and get an error, single card 5060TI16G:

### Issue 正文摘录

### Your current environment services: vllm: container_name: vllm restart: no image: vllm/vllm-openai:latest runtime: nvidia ipc: host #environment: # - HF_HUB_OFFLINE = 1 # - CUDA_VISIBLE_DEVICES = 0 volumes: - D:\vllm\models\qwen2.5:/models command: [ "--model", "/models/Qwen2.5-7B", "--served_model_name", "Qwen2.5-7B", "--gpu_memory_utilization", "0.90", "--max_model_len", "1024 ", "--tensor-parallel-size", "1" ] ports: - 8010:8000 deploy: resources: reservations: devices: - driver: nvidia capabilities: [ gpu ] count: all ### 🐛 Describe the bug 2025-07-10 08:48:52 INFO 07-09 17:48:52 [__init__.py:244] Automatically detected platform cuda. 2025-07-10 08:48:57 INFO 07-09 17:48:57 [api_server.py:1395] vLLM API server version 0.9.2 2025-07-10 08:48:57 INFO 07-09 17:48:57 [cli_args.py:325] non-default args: {'model': '/models/Qwen2.5-7B', 'max_model_len': 1024, 'served_model_name': ['Qwen2.5-7B'], 'gpu_memory_utilization': 0.85} 2025-07-10 08:49:04 INFO 07-09 17:49:04 [config.py:841] This model supports multiple tasks: {'classify', 'reward', 'generate', 'embed'}. Defaulting to 'generate'. 2025-07-10 08:49:04 INFO 07-09 17:49:04 [config.py:1472] Using max model len 1024 2025-07-10 08...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: -07-10 08:48:57 INFO 07-09 17:48:57 [api_server.py:1395] vLLM API server version 0.9.2 2025-07-10 08:48:57 INFO 07-09 17:48:57 [cli_args.py:325] non-default args: {'model': '/models/Qwen2.5-7B', 'max_model_len': 1024, '...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Excuse me, I run the model qwen2.5-7B and get an error, single card 5060TI16G: bug;stale ### Your current environment services: vllm: container_name: vllm restart: no image: vllm/vllm-openai:latest runtime: nvidi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: I run the model qwen2.5-7B and get an error, single card 5060TI16G: bug;stale ### Your current environment services: vllm: container_name: vllm restart: no image: vllm/vllm-openai:latest runtime: nvidia ipc: host #envir...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ride_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=1024, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
