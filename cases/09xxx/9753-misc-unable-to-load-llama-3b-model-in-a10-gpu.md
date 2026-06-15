# vllm-project/vllm#9753: [Misc]: Unable to load Llama 3B model in A10 GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#9753](https://github.com/vllm-project/vllm/issues/9753) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | cuda;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Misc]: Unable to load Llama 3B model in A10 GPU

### Issue 正文摘录

### Anything you want to discuss about vllm. Hi, I am unable to load Llama 3.2B model in A10 GPU. Initializing an LLM engine (v0.6.3.post1) with config: model='Llama-3.2-3B-Instruct', speculative_config=None, tokenizer='Llama-3.2-3B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, rope_scaling=None, rope_theta=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=2048, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=True, kv_cache_dtype=fp8_e5m2, quantization_param_path=None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_time=False), seed=0, served_model_name=Llama-3.2-3B-Instruct, num_scheduler_steps=1, chunked_prefill_enabled=False multi_step_stream_outputs=True, enable_prefix_caching=False, use_async_output_proc=False, use_cached_outputs=False, mm_processor_kwargs=None) I get the error below Failed to load model w...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: None, rope_theta=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=2048, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Misc]: Unable to load Llama 3B model in A10 GPU stale ### Anything you want to discuss about vllm. Hi, I am unable to load Llama 3.2B model in A10 GPU. Initializing an LLM engine (v0.6.3.post1) with config: model='Llam...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Misc]: Unable to load Llama 3B model in A10 GPU stale ### Anything you want to discuss about vllm. Hi, I am unable to load Llama 3.2B model in A10 GPU. Initializing an LLM engine (v0.6.3.post1) with config: model='Llam...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ue, kv_cache_dtype=fp8_e5m2, quantization_param_path=None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, coll...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
