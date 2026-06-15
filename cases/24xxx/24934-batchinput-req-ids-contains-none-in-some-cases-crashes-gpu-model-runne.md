# vllm-project/vllm#24934: BatchInput.req_ids contains None in some cases, crashes gpu_model_runner code

| 字段 | 值 |
| --- | --- |
| Issue | [#24934](https://github.com/vllm-project/vllm/issues/24934) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | activation_norm;frontend_api;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 |  |
| Operator 关键词 | cuda;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> BatchInput.req_ids contains None in some cases, crashes gpu_model_runner code

### Issue 正文摘录

The assumption made here seems to be wrong, https://github.com/vllm-project/vllm/blob/0af3ce13558056b3637dd4661c89f4b037faa85a/vllm/v1/worker/gpu_input_batch.py#L267:L271 ``` Dumping input data for V1 LLM engine (v0.10.1.1) with config: model='/tmp/model', speculative_config=None, tokenizer='/tmp/model', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config={}, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=8192, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=/tmp/model, enable_prefix_caching=True, chunked_prefill_enabled=True, use_async_output_proc=False, pooler_config=PoolerConfig(pooling_type='LAST', normalize=None, dimensions=None, activatio...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: nput data for V1 LLM engine (v0.10.1.1) with config: model='/tmp/model', speculative_config=None, tokenizer='/tmp/model', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config={}, tokeniz...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: rride_neuron_config={}, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=8192, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nd=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=/tmp/model, enable_prefix_caching=True, chunked_...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: , speculative_config=None, tokenizer='/tmp/model', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config={}, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: BatchInput.req_ids contains None in some cases, crashes gpu_model_runner code The assumption made here seems to be wrong, https://github.com/vllm-project/vllm/blob/0af3ce13558056b3637dd4661c89f4b037faa85a/vllm/v1/worker...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
