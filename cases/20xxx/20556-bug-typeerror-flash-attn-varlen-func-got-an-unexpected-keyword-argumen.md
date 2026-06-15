# vllm-project/vllm#20556: [Bug]: TypeError: flash_attn_varlen_func() got an unexpected keyword argument 'num_splits'

| 字段 | 值 |
| --- | --- |
| Issue | [#20556](https://github.com/vllm-project/vllm/issues/20556) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TypeError: flash_attn_varlen_func() got an unexpected keyword argument 'num_splits'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm serve a gguf version of qwen3 when inferencing , the main error is TypeError: flash_attn_varlen_func() got an unexpected keyword argument 'num_splits' ```commandline INFO 07-07 00:40:14 [__init__.py:244] Automatically detected platform cuda. INFO 07-07 00:40:17 [api_server.py:1393] vLLM API server version 0.9.2.dev226+g9a3b88328.d20250705 INFO 07-07 00:40:17 [cli_args.py:325] non-default args: {'model': '/models/unsloth/Qwen3-0.6B-GGUF/Qwen3-0.6B-Q4_1.gguf', 'max_model_len': 16000, 'served_model_name': ['Qwen3-0.6B-GGUF'], 'reasoning_parser': 'deepseek_r1', 'gpu_memory_utilization': 0.6, 'swap_space': 8.0} INFO 07-07 00:40:31 [config.py:840] This model supports multiple tasks: {'generate', 'reward', 'classify', 'embed'}. Defaulting to 'generate'. ERROR 07-07 00:40:31 [config.py:130] Error retrieving safetensors: Repo id must be in the form 'repo_name' or 'namespace/repo_name': '/models/unsloth/Qwen3-0.6B-GGUF/Qwen3-0.6B-Q4_1.gguf'. Use `repo_type` argument if needed., retrying 1 of 2 ERROR 07-07 00:40:33 [config.py:128] Error retrieving safetensors: Repo id must be in the form 'repo_name' or 'namespace/repo_name': '/models/u...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: than non-quantized models. INFO 07-07 00:40:33 [config.py:2284] Chunked prefill is enabled with max_num_batched_tokens=2048. WARNING 07-07 00:40:33 [config.py:1632] Possibly too large swap space. 8.00 GiB out of the 19....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: # Your current environment ### 🐛 Describe the bug vllm serve a gguf version of qwen3 when inferencing , the main error is TypeError: flash_attn_varlen_func() got an unexpected keyword argument 'num_splits' ```commandlin...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: gument if needed. INFO 07-07 00:40:33 [config.py:3367] Downcasting torch.float32 to torch.bfloat16. INFO 07-07 00:40:33 [config.py:1471] Using max model len 16000 WARNING 07-07 00:40:33 [config.py:959] gguf quantization...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend='deepseek_r1'), observ...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: 07-07 00:40:17 [cli_args.py:325] non-default args: {'model': '/models/unsloth/Qwen3-0.6B-GGUF/Qwen3-0.6B-Q4_1.gguf', 'max_model_len': 16000, 'served_model_name': ['Qwen3-0.6B-GGUF'], 'reasoning_parser': 'deepseek_r1', '...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
