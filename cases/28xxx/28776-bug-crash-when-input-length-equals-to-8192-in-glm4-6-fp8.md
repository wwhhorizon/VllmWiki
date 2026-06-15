# vllm-project/vllm#28776: [Bug]: Crash when input length equals to 8192 in GLM4.6-FP8

| 字段 | 值 |
| --- | --- |
| Issue | [#28776](https://github.com/vllm-project/vllm/issues/28776) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;frontend_api;model_support;moe;quantization |
| 子分类 | runtime_err |
| Operator 关键词 | cuda;fp8;kernel;moe;operator;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Crash when input length equals to 8192 in GLM4.6-FP8

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` (VllmWorker TP1 pid=22110) ERROR 11-14 22:48:02 [multiproc_executor.py:596] File "/usr/local/lib/python3.12/dist-packages/torch/_inductor/runtime/triton_heuristics.py", line 1264, in run (EngineCore_0 pid=21936) ERROR 11-14 22:48:02 [dump_input.py:69] Dumping input data for V1 LLM engine (v0.10.2.dev2+gf5635d62e.d20250805) with config: model='/file_system/common-models/ZhipuAI/GLM-4.6-FP8', speculative_config=None, tokenizer='/file_system/common-models/ZhipuAI/GLM-4.6-FP8', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=202752, download_dir=None, load_format=auto, tensor_parallel_size=8, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=compressed-tensors, enforce_eager=False, kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None,...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: Crash when input length equals to 8192 in GLM4.6-FP8 bug;stale ### Your current environment ### 🐛 Describe the bug ``` (VllmWorker TP1 pid=22110) ERROR 11-14 22:48:02 [multiproc_executor.py:596] File "/usr/local/...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: File "/usr/local/lib/python3.12/dist-packages/torch/_inductor/runtime/triton_heuristics.py", line 1264, in run (EngineCore_0 pid=21936) ERROR 11-14 22:48:02 [dump_input.py:69] Dumping input data for V1 LLM engine (v0.10...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Crash when input length equals to 8192 in GLM4.6-FP8 bug;stale ### Your current environment ### 🐛 Describe the bug ``` (VllmWorker TP1 pid=22110) ERROR 11-14 22:48:02 [multiproc_executor.py:596] File "/usr/local/...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nd=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=/file_system/common-models/ZhipuAI/GLM-4.6-FP8,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: v2+gf5635d62e.d20250805) with config: model='/file_system/common-models/ZhipuAI/GLM-4.6-FP8', speculative_config=None, tokenizer='/file_system/common-models/ZhipuAI/GLM-4.6-FP8', skip_tokenizer_init=False, tokenizer_mod...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
