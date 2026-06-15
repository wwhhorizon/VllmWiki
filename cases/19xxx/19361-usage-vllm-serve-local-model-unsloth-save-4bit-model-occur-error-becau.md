# vllm-project/vllm#19361: [Usage]: vllm serve local model(unsloth save 4bit model )occur error because of assert param_data.shape == loaded_weight.shape error.

| 字段 | 值 |
| --- | --- |
| Issue | [#19361](https://github.com/vllm-project/vllm/issues/19361) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;gemm_linear;model_support;moe;quantization;sampling_logits |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cuda;operator;quantization;sampling |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: vllm serve local model(unsloth save 4bit model )occur error because of assert param_data.shape == loaded_weight.shape error.

### Issue 正文摘录

### Your current environment vllm 0.9.0.1 ```text INFO 06-09 19:41:28 [__init__.py:243] Automatically detected platform cuda. INFO 06-09 19:41:30 [__init__.py:31] Available plugins for group vllm.general_plugins: INFO 06-09 19:41:30 [__init__.py:33] - lora_filesystem_resolver -> vllm.plugins.lora_resolvers.filesystem_resolver:register_filesystem_resolver INFO 06-09 19:41:30 [__init__.py:36] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load. INFO 06-09 19:41:31 [api_server.py:1289] vLLM API server version 0.9.0.1 INFO 06-09 19:41:32 [cli_args.py:300] non-default args: {'model': '/workspace/script/sh/model_origin'} INFO 06-09 19:41:39 [config.py:793] This model supports multiple tasks: {'score', 'embed', 'reward', 'classify', 'generate'}. Defaulting to 'generate'. WARNING 06-09 19:41:40 [config.py:907] bitsandbytes quantization is not fully optimized yet. The speed can be slower than non-quantized models. INFO 06-09 19:41:40 [config.py:2118] Chunked prefill is enabled with max_num_batched_tokens=2048. INFO 06-09 19:41:45 [__init__.py:243] Automatically detected platform cuda. INFO 06-09 19:41:47 [core.py:438] Waiting for init message from...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: lugins to load. INFO 06-09 19:41:31 [api_server.py:1289] vLLM API server version 0.9.0.1 INFO 06-09 19:41:32 [cli_args.py:300] non-default args: {'model': '/workspace/script/sh/model_origin'} INFO 06-09 19:41:39 [config...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: r because of assert param_data.shape == loaded_weight.shape error. usage;stale ### Your current environment vllm 0.9.0.1 ```text INFO 06-09 19:41:28 [__init__.py:243] Automatically detected platform cuda. INFO 06-09 19:...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: lting to 'generate'. WARNING 06-09 19:41:40 [config.py:907] bitsandbytes quantization is not fully optimized yet. The speed can be slower than non-quantized models. INFO 06-09 19:41:40 [config.py:2118] Chunked prefill i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: vllm serve local model(unsloth save 4bit model )occur error because of assert param_data.shape == loaded_weight.shape error. usage;stale ### Your current environment vllm 0.9.0.1 ```text INFO 06-09 19:41:28 [__...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
