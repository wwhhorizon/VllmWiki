# vllm-project/vllm#13765: [Bug]: "Loading safetensors checkpoint shards" runs twice when serving model

| 字段 | 值 |
| --- | --- |
| Issue | [#13765](https://github.com/vllm-project/vllm/issues/13765) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: "Loading safetensors checkpoint shards" runs twice when serving model

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I'm serving this model `unsloth/Mistral-Small-24B-Instruct-2501-unsloth-bnb-4bit` it seems like the safetensors checkpoint shards is being loaded twice. I tried with `google/gemma-2-2b-it` and that did not have the problem. Is this a bug, or an artifact of the model/quantization? ```bash VLLM_LOGGING_LEVEL=DEBUG vllm serve unsloth/Mistral-Small-24B-Instruct-2501-unsloth-bnb-4bit --max-model-len=15000 --served-model-name mistralai/Mistral-Small-24B-Instruct-2501 --port 8880 --quantization bitsandbytes --load-format bitsandbytes ``` ``` DEBUG 02-24 13:59:23 main.py:48] Setting VLLM_WORKER_MULTIPROC_METHOD to 'spawn' DEBUG 02-24 13:59:23 __init__.py:28] No plugins for group vllm.platform_plugins found. INFO 02-24 13:59:23 __init__.py:207] Automatically detected platform cuda. DEBUG 02-24 13:59:23 __init__.py:28] No plugins for group vllm.general_plugins found. INFO 02-24 13:59:23 api_server.py:912] vLLM API server version 0.7.3 INFO 02-24 13:59:23 api_server.py:913] args: Namespace(subparser='serve', model_tag='unsloth/Mistral-Small-24B-Instruct-2501-unsloth-bnb-4bit', config='', host=None, port=8880, uvicorn_log_level='info',...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: Loading safetensors checkpoint shards" runs twice when serving model bug;stale ### Your current environment ### 🐛 Describe the bug When I'm serving this model `unsloth/Mistral-Small-24B-Instruct-2501-unsloth-bnb-4bit` i...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: al_plugins found. INFO 02-24 13:59:23 api_server.py:912] vLLM API server version 0.7.3 INFO 02-24 13:59:23 api_server.py:913] args: Namespace(subparser='serve', model_tag='unsloth/Mistral-Small-24B-Instruct-2501-unsloth...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: hat did not have the problem. Is this a bug, or an artifact of the model/quantization? ```bash VLLM_LOGGING_LEVEL=DEBUG vllm serve unsloth/Mistral-Small-24B-Instruct-2501-unsloth-bnb-4bit --max-model-len=15000 --served-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: "Loading safetensors checkpoint shards" runs twice when serving model bug;stale ### Your current environment ### 🐛 Describe the bug When I'm serving this model `unsloth/Mistral-Small-24B-Instruct-2501-unsloth-bnb...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: type='auto', kv_cache_dtype='auto', max_model_len=15000, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
