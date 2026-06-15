# vllm-project/vllm#21466: [Bug]: FP8 model crashes with EngineDeadError and CUDA illegal memory access on H100 (CUDA 12.8)

| 字段 | 值 |
| --- | --- |
| Issue | [#21466](https://github.com/vllm-project/vllm/issues/21466) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: FP8 model crashes with EngineDeadError and CUDA illegal memory access on H100 (CUDA 12.8)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When serving the model RedHatAI/Qwen3-32B-FP8-dynamic using vLLM, I encounter the following error after a few minutes of running: ERROR 07-21 13:02:07 [dump_input.py:69] Dumping input data for V1 LLM engine (v0.9.2) with config: model='RedHatAI/Qwen3-32B-FP8-dynamic', speculative_config=None, tokenizer='RedHatAI/Qwen3-32B-FP8-dynamic', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32000, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=compressed-tensors, enforce_eager=True, kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend='qwen3'), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=local-llm, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_p...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: h EngineDeadError and CUDA illegal memory access on H100 (CUDA 12.8) bug;stale ### Your current environment ### 🐛 Describe the bug When serving the model RedHatAI/Qwen3-32B-FP8-dynamic using vLLM, I encounter the follow...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: wen3'), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=local-llm, num_scheduler_steps=1, multi_step_str...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: FP8 model crashes with EngineDeadError and CUDA illegal memory access on H100 (CUDA 12.8) bug;stale ### Your current environment ### 🐛 Describe the bug When serving the model RedHatAI/Qwen3-32B-FP8-dynamic using...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: FP8 model crashes with EngineDeadError and CUDA illegal memory access on H100 (CUDA 12.8) bug;stale ### Your current environment ### 🐛 Describe the bug When serving the model RedHatAI/Qwen3-32B-FP8-dynamic using...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: FP8 model crashes with EngineDeadError and CUDA illegal memory access on H100 (CUDA 12.8) bug;stale ### Your current environment ### 🐛 Describe the bug When serving the model RedHatAI/Qwen3-32B-FP8-dynamic using...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
