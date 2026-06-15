# vllm-project/vllm#20995: [Bug]: Unable to use Qwen/Qwen2.5-Omni-7B with --mm-processor-kwargs

| 字段 | 值 |
| --- | --- |
| Issue | [#20995](https://github.com/vllm-project/vllm/issues/20995) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;multimodal_vlm;quantization |
| 子分类 | install |
| Operator 关键词 | attention;cuda;gemm;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unable to use Qwen/Qwen2.5-Omni-7B with --mm-processor-kwargs

### Issue 正文摘录

### Your current environment ``` INFO 07-15 08:08:10 [cli_args.py:309] non-default args: {'port': 8080, 'model': 'Qwen/Qwen2.5-Omni-7B', 'tensor_parallel_size': 4, 'mm_processor_kwargs': {'use_audio_in_video': True}} INFO 07-15 08:08:24 [llm_engine.py:230] Initializing a V0 LLM engine (v0.9.1) with config: model='Qwen/Qwen2.5-Omni-7B', speculative_config=None, tokenizer='Qwen/Qwen2.5-Omni-7B', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=4, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='xgrammar', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=None, served_model_name=Qwen/Qwen2.5-Omni-7B, num_scheduler_steps=1, multi_step_stream_outputs=True, e...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: Unable to use Qwen/Qwen2.5-Omni-7B with --mm-processor-kwargs bug;stale ### Your current environment ``` INFO 07-15 08:08:10 [cli_args.py:309] non-default args: {'port': 8080, 'model': 'Qwen/Qwen2.5-Omni-7B', 'te...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: nd=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=None, served_model_name=Qwen/Qwen2.5-Omni-7B, num_scheduler_steps=1,...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ride_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=4, pipeline_parallel_size=1, disable...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Unable to use Qwen/Qwen2.5-Omni-7B with --mm-processor-kwargs bug;stale ### Your current environment ``` INFO 07-15 08:08:10 [cli_args.py:309] non-default args: {'port': 8080, 'model': 'Qwen/Qwen2.5-Omni-7B', 'te...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='xgrammar', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
