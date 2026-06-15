# vllm-project/vllm#18244: [Bug]:  vllm rtxt5090 Qwen3-14B-FP8

| 字段 | 值 |
| --- | --- |
| Issue | [#18244](https://github.com/vllm-project/vllm/issues/18244) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  vllm rtxt5090 Qwen3-14B-FP8

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm serve ~/models/Qwen3-14B-FP8 \ --served-model-name Qwen3-14B \ --api-key htxt-ai \ --device cuda \ --disable-log-requests \ --gpu-memory-utilization 0.95 \ --host 0.0.0.0 --port 6006 \ --seed 3407 \ --max-model-len 32000 \ --dtype bfloat16 \ --trust-remote-code \ --max-num-seqs 256 INFO 05-16 12:34:11 [__init__.py:248] Automatically detected platform cuda. INFO 05-16 12:34:13 [__init__.py:30] Available plugins for group vllm.general_plugins: INFO 05-16 12:34:13 [__init__.py:32] name=lora_filesystem_resolver, value=vllm.plugins.lora_resolvers.filesystem_resolver:register_filesystem_resolver INFO 05-16 12:34:13 [__init__.py:34] all available plugins for group vllm.general_plugins will be loaded. INFO 05-16 12:34:13 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load. INFO 05-16 12:34:13 [__init__.py:44] plugin lora_filesystem_resolver loaded. INFO 05-16 12:34:13 [api_server.py:1289] vLLM API server version 0.8.5.dev693+ge60f550b3.d20250515 INFO 05-16 12:34:13 [cli_args.py:297] non-default args: {'host': '0.0.0.0', 'port': 6006, 'api_key': 'htxt-ai', 'trust_remote_code': True, 'dtype': 'bfloa...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 7: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: esolver loaded. INFO 05-16 12:34:13 [api_server.py:1289] vLLM API server version 0.8.5.dev693+ge60f550b3.d20250515 INFO 05-16 12:34:13 [cli_args.py:297] non-default args: {'host': '0.0.0.0', 'port': 6006, 'api_key': 'ht...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: vllm rtxt5090 Qwen3-14B-FP8 bug;stale ### Your current environment ### 🐛 Describe the bug vllm serve ~/models/Qwen3-14B-FP8 \ --served-model-name Qwen3-14B \ --api-key htxt-ai \ --device cuda \ --disable-log-requ...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: vllm rtxt5090 Qwen3-14B-FP8 bug;stale ### Your current environment ### 🐛 Describe the bug vllm serve ~/models/Qwen3-14B-FP8 \ --served-model-name Qwen3-14B \ --api-key htxt-ai \ --device cuda \ --disable-log-requ...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: vllm rtxt5090 Qwen3-14B-FP8 bug;stale ### Your current environment ### 🐛 Describe the bug vllm serve ~/models/Qwen3-14B-FP8 \ --served-model-name Qwen3-14B \ --api-key htxt-ai \ --device cuda \ --disable-log-requ...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
