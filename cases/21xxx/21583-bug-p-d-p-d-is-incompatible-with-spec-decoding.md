# vllm-project/vllm#21583: [Bug]: [P/D] P/d is incompatible with spec decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#21583](https://github.com/vllm-project/vllm/issues/21583) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [P/D] P/d is incompatible with spec decoding

### Issue 正文摘录

### Your current environment unsure, user report ### 🐛 Describe the bug For dev, we have had asserts in various places. We have one here that is breaking spec decoding @NickLucche - could you take a look? ```bash (VllmWorker rank=0 pid=1574) ERROR 07-25 03:42:09 [multiproc_executor.py:546] WorkerProc hit an exception. (VllmWorker rank=0 pid=1574) ERROR 07-25 03:42:09 [multiproc_executor.py:546] Traceback (most recent call last): (VllmWorker rank=0 pid=1574) ERROR 07-25 03:42:09 [multiproc_executor.py:546] File "/opt/vllm/vllm/distributed/kv_transfer/kv_connector/v1/nixl_connector.py", line 966, in _read_blocks (VllmWorker rank=0 pid=1574) ERROR 07-25 03:42:09 [multiproc_executor.py:546] assert num_local_blocks <= num_remote_blocks (VllmWorker rank=0 pid=1574) ERROR 07-25 03:42:09 [multiproc_executor.py:546] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (VllmWorker rank=0 pid=1574) ERROR 07-25 03:42:09 [multiproc_executor.py:546] AssertionError (VllmWorker rank=0 pid=1574) ERROR 07-25 03:42:09 [multiproc_executor.py:546] ERROR 07-25 03:42:09 [dump_input.py:69] Dumping input data for V1 LLM engine (v0.10.0rc2.dev90+geec694201) with config: model='/tmp/model/', speculative_config=Speculative...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ride_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=8, pipeline_parallel_size=1, disabl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: [P/D] P/d is incompatible with spec decoding bug;stale ### Your current environment unsure, user report ### 🐛 Describe the bug For dev, we have had asserts in various places. We have one here that is breaking spe...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nd=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=/tmp/model/, num_scheduler_steps=1, multi_step_s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Dumping input data for V1 LLM engine (v0.10.0rc2.dev90+geec694201) with config: model='/tmp/model/', speculative_config=SpeculativeConfig(method='eagle', model='/tmp/model/eagle_head/', num_spec_tokens=5), tokenizer='/t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
