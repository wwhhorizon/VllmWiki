# vllm-project/vllm#27645: [Bug]: Qwen3-VL-235B-A22B-Instruct stuck with assert placeholder < len(self._out_of_band_tensors)

| 字段 | 值 |
| --- | --- |
| Issue | [#27645](https://github.com/vllm-project/vllm/issues/27645) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-VL-235B-A22B-Instruct stuck with assert placeholder < len(self._out_of_band_tensors)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running VLLM on 8* RTX4090 48G (similar to RTX6000 ada) with model Qwen3-VL-235B-A22B-Instruct-FP8, VLLM crash on ray, throw an assert error. ``` (EngineCore_DP0 pid=683) 2025-10-28 01:31:15,907 INFO compiled_dag_node.py:2171 -- Tearing down compiled DAG (EngineCore_DP0 pid=683) ERROR 10-28 01:31:15 [dump_input.py:69] Dumping input data for V1 LLM engine (v0.11.0) with config: model='/models/Qwen3-VL-235B-A22B-Instruct-FP8', speculative_config=None, tokenizer='/models/Qwen3-VL-235B-A22B-Instruct-FP8', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=262144, download_dir=None, load_format=auto, tensor_parallel_size=2, pipeline_parallel_size=4, data_parallel_size=1, disable_custom_all_reduce=False, quantization=fp8, enforce_eager=False, kv_cache_dtype=auto, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, o...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: truct stuck with assert placeholder < len(self._out_of_band_tensors) bug;stale ### Your current environment ### 🐛 Describe the bug When running VLLM on 8* RTX4090 48G (similar to RTX6000 ada) with model Qwen3-VL-235B-A2...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: error. ``` (EngineCore_DP0 pid=683) 2025-10-28 01:31:15,907 INFO compiled_dag_node.py:2171 -- Tearing down compiled DAG (EngineCore_DP0 pid=683) ERROR 10-28 01:31:15 [dump_input.py:69] Dumping input data for V1 LLM engi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: 4090 48G (similar to RTX6000 ada) with model Qwen3-VL-235B-A22B-Instruct-FP8, VLLM crash on ray, throw an assert error. ``` (EngineCore_DP0 pid=683) 2025-10-28 01:31:15,907 INFO compiled_dag_node.py:2171 -- Tearing down...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen3-VL-235B-A22B-Instruct stuck with assert placeholder < len(self._out_of_band_tensors) bug;stale ### Your current environment ### 🐛 Describe the bug When running VLLM on 8* RTX4090 48G (similar to RTX6000 ada...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser=''), observability_con...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
