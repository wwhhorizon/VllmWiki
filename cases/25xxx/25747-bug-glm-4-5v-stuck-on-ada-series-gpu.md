# vllm-project/vllm#25747: [Bug]: GLM-4.5V stuck on Ada series GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#25747](https://github.com/vllm-project/vllm/issues/25747) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GLM-4.5V stuck on Ada series GPU

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm trying to run GLM-4.5V-FP8 on a cluster with 8x RTX4090, the program stuck when processing some requests. here are the logs of the stuck. ```text (APIServer pid=1) INFO: 10.80.0.3:35040 - "POST /v1/chat/completions HTTP/1.1" 200 OK (APIServer pid=1) INFO 09-26 00:00:41 [v1/metrics/loggers.py:123] Engine 000: Avg prompt throughput: 7.6 tokens/s, Avg generation throughput: 40.3 tokens/s, Running: 2 reqs, Waiting: 0 reqs, GPU KV cache usage: 16.3%, Prefix cache hit rate: 35.8% (EngineCore_DP0 pid=726) ERROR 09-26 00:00:43 [logging_utils/dump_input.py:69] Dumping input data for V1 LLM engine (v0.10.2) with config: model='/models/GLM-4.5V-FP8', speculative_config=None, tokenizer='/models/GLM-4.5V-FP8', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=65536, download_dir=None, load_format=auto, tensor_parallel_size=4, pipeline_parallel_size=2, data_parallel_size=1, disable_custom_all_reduce=False, quantization=compressed-tensors, enforce_eager=False, kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto',...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: [Bug]: GLM-4.5V stuck on Ada series GPU bug;stale ### Your current environment ### 🐛 Describe the bug I'm trying to run GLM-4.5V-FP8 on a cluster with 8x RTX4090, the program stuck when processing some requests. here ar...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: lm45'), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=GLM-4.5V, enable_prefix_caching=True, chunked_pr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: ls/dump_input.py:69] Dumping input data for V1 LLM engine (v0.10.2) with config: model='/models/GLM-4.5V-FP8', speculative_config=None, tokenizer='/models/GLM-4.5V-FP8', skip_tokenizer_init=False, tokenizer_mode=auto, r...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: rrent environment ### 🐛 Describe the bug I'm trying to run GLM-4.5V-FP8 on a cluster with 8x RTX4090, the program stuck when processing some requests. here are the logs of the stuck. ```text (APIServer pid=1) INFO: 10.8...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend='glm45'), observabilit...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
