# vllm-project/vllm#25378: [Bug]: Qwen/Qwen3-Next-80B-A3B-Instruct-FP8 Fails Starting

| 字段 | 值 |
| --- | --- |
| Issue | [#25378](https://github.com/vllm-project/vllm/issues/25378) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen/Qwen3-Next-80B-A3B-Instruct-FP8 Fails Starting

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vLLM fail running Qwen/Qwen3-Next-80B-A3B-Instruct-FP8. ValueError: Detected some but not all shards of model.layers.0.linear_attn.in_proj are quantized. All shards of fused layers to have the same precision. ------------------ INFO 09-22 13:42:24 [__init__.py:216] Automatically detected platform cuda. (APIServer pid=509494) INFO 09-22 13:42:26 [api_server.py:1896] vLLM API server version 0.10.2 (APIServer pid=509494) INFO 09-22 13:42:26 [utils.py:328] non-default args: {'model_tag': '/root/models/Qwen3-Next-80B-A3B-Instruct-FP8', 'port': 8016, 'api_key': ['secret'], 'model': '/root/models/Qwen3-Next-80B-A3B-Instruct-FP8', 'max_model_len': 32768, 'served_model_name': ['next'], 'generation_config': 'vllm', 'gpu_memory_utilization': 0.8, 'max_num_seqs': 150, 'enable_log_requests': True} (APIServer pid=509494) INFO 09-22 13:42:34 [__init__.py:742] Resolved architecture: Qwen3NextForCausalLM (APIServer pid=509494) `torch_dtype` is deprecated! Use `dtype` instead! (APIServer pid=509494) INFO 09-22 13:42:34 [__init__.py:1815] Using max model len 32768 (APIServer pid=509494) WARNING 09-22 13:42:34 [_ipex_ops.py:16] Import error msg: No...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: Qwen/Qwen3-Next-80B-A3B-Instruct-FP8 Fails Starting bug;stale ### Your current environment ### 🐛 Describe the bug vLLM fail running Qwen/Qwen3-Next-80B-A3B-Instruct-FP8. ValueError: Detected some but not all shar...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: tn.in_proj are quantized. All shards of fused layers to have the same precision. ------------------ INFO 09-22 13:42:24 [__init__.py:216] Automatically detected platform cuda. (APIServer pid=509494) INFO 09-22 13:42:26...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: Qwen/Qwen3-Next-80B-A3B-Instruct-FP8 Fails Starting bug;stale ### Your current environment ### 🐛 Describe the bug vLLM fail running Qwen/Qwen3-Next-80B-A3B-Instruct-FP8. ValueError: Detected some but not all shar...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Qwen/Qwen3-Next-80B-A3B-Instruct-FP8 Fails Starting bug;stale ### Your current environment ### 🐛 Describe the bug vLLM fail running Qwen/Qwen3-Next-80B-A3B-Instruct-FP8. ValueError: Detected some but not all shar...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
