# vllm-project/vllm#27466: [Bug]: 运行时服务被撑爆导致的oom

| 字段 | 值 |
| --- | --- |
| Issue | [#27466](https://github.com/vllm-project/vllm/issues/27466) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling |
| 症状 | build_error;crash;oom;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 运行时服务被撑爆导致的oom

### Issue 正文摘录

### Your current environment vllm serve Qwen/Qwen3-VL-32B-Instruct --served-model-name qwenvl --port 8080 --host 0.0.0.0 --max-model-len 16384 --gpu_memory_utilization 0.98 INFO 10-24 01:21:52 [__init__.py:216] Automatically detected platform cuda. (APIServer pid=8267) INFO 10-24 01:21:55 [api_server.py:1839] vLLM API server version 0.11.0 (APIServer pid=8267) INFO 10-24 01:21:55 [utils.py:233] non-default args: {'model_tag': 'Qwen/Qwen3-VL-32B-Instruct', 'host': '0.0.0.0', 'port': 8080, 'model': 'Qwen/Qwen3-VL-32B-Instruct', 'max_model_len': 16384, 'served_model_name': ['qwenvl'], 'gpu_memory_utilization': 0.98} (APIServer pid=8267) INFO 10-24 01:21:56 [model.py:547] Resolved architecture: Qwen3VLForConditionalGeneration (APIServer pid=8267) `torch_dtype` is deprecated! Use `dtype` instead! (APIServer pid=8267) INFO 10-24 01:21:56 [model.py:1510] Using max model len 16384 (APIServer pid=8267) INFO 10-24 01:21:57 [scheduler.py:205] Chunked prefill is enabled with max_num_batched_tokens=8192. INFO 10-24 01:22:03 [__init__.py:216] Automatically detected platform cuda. (EngineCore_DP0 pid=8402) INFO 10-24 01:22:06 [core.py:644] Waiting for init message from front-end. (EngineCore_DP0...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: 运行时服务被撑爆导致的oom bug ### Your current environment vllm serve Qwen/Qwen3-VL-32B-Instruct --served-model-name qwenvl --port 8080 --host 0.0.0.0 --max-model-len 16384 --gpu_memory_utilization 0.98 INFO 10-24 01:21:52...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: 510] Using max model len 16384 (APIServer pid=8267) INFO 10-24 01:21:57 [scheduler.py:205] Chunked prefill is enabled with max_num_batched_tokens=8192. INFO 10-24 01:22:03 [__init__.py:216] Automatically detected platfo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser=''), observability_con...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: erver pid=8267) INFO 10-24 01:21:55 [api_server.py:1839] vLLM API server version 0.11.0 (APIServer pid=8267) INFO 10-24 01:21:55 [utils.py:233] non-default args: {'model_tag': 'Qwen/Qwen3-VL-32B-Instruct', 'host': '0.0....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: rchitecture: Qwen3VLForConditionalGeneration (APIServer pid=8267) `torch_dtype` is deprecated! Use `dtype` instead! (APIServer pid=8267) INFO 10-24 01:21:56 [model.py:1510] Using max model len 16384 (APIServer pid=8267)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
