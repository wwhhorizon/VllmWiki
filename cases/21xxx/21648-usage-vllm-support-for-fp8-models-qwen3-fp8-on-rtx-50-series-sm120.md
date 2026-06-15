# vllm-project/vllm#21648: [Usage]: vLLM support for FP8 models (QWEN3 FP8) on RTX 50 series / SM120

| 字段 | 值 |
| --- | --- |
| Issue | [#21648](https://github.com/vllm-project/vllm/issues/21648) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits |
| 子分类 | cold_start |
| Operator 关键词 | attention;cuda;fp8;gemm;operator;quantization;sampling |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: vLLM support for FP8 models (QWEN3 FP8) on RTX 50 series / SM120

### Issue 正文摘录

### Your current environment INFO 07-26 13:54:37 [__init__.py:235] Automatically detected platform cuda. INFO 07-26 13:54:38 [api_server.py:1769] vLLM API server version 0.10.1.dev34+g9c8b2c2a8.d20250725 INFO 07-26 13:54:38 [cli_args.py:264] non-default args: {'host': '0.0.0.0', 'model': '/mnt/f/Models/Qwen3-14B-FP8', 'trust_remote_code': True, 'max_model_len': 32768, 'quantization': 'fp8', 'served_model_name': ['Qwen3-14B-FP8']} INFO 07-26 13:54:45 [config.py:1605] Using max model len 32768 INFO 07-26 13:54:46 [config.py:2416] Chunked prefill is enabled with max_num_batched_tokens=2048. INFO 07-26 13:54:51 [__init__.py:235] Automatically detected platform cuda. INFO 07-26 13:54:53 [core.py:574] Waiting for init message from front-end. INFO 07-26 13:54:53 [core.py:72] Initializing a V1 LLM engine (v0.10.1.dev34+g9c8b2c2a8.d20250725) with config: model='/mnt/f/Models/Qwen3-14B-FP8', speculative_config=None, tokenizer='/mnt/f/Models/Qwen3-14B-FP8', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config={}, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: platform cuda. INFO 07-26 13:54:38 [api_server.py:1769] vLLM API server version 0.10.1.dev34+g9c8b2c2a8.d20250725 INFO 07-26 13:54:38 [cli_args.py:264] non-default args: {'host': '0.0.0.0', 'model': '/mnt/f/Models/Qwen3...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Usage]: vLLM support for FP8 models (QWEN3 FP8) on RTX 50 series / SM120 usage ### Your current environment INFO 07-26 13:54:37 [__init__.py:235] Automatically detected platform cuda. INFO 07-26 13:54:38 [api_server.py...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Usage]: vLLM support for FP8 models (QWEN3 FP8) on RTX 50 series / SM120 usage ### Your current environment INFO 07-26 13:54:37 [__init__.py:235] Automatically detected platform cuda. INFO 07-26 13:54:38 [api_server.py...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: vLLM support for FP8 models (QWEN3 FP8) on RTX 50 series / SM120 usage ### Your current environment INFO 07-26 13:54:37 [__init__.py:235] Automatically detected platform cuda. INFO 07-26 13:54:38 [api_server.py...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
