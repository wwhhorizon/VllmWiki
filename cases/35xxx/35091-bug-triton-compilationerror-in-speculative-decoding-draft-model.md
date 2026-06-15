# vllm-project/vllm#35091: [Bug]: Triton CompilationError in speculative decoding (draft_model)

| 字段 | 值 |
| --- | --- |
| Issue | [#35091](https://github.com/vllm-project/vllm/issues/35091) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Triton CompilationError in speculative decoding (draft_model)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When enabling speculative decoding with method='draft_model', the engine crashes with a Triton compilation error during token sampling (Qwen3-14B-AWQ and Qwen3-1.7B as draft model) : ``` (EngineCore_DP0 pid=150) ERROR 02-23 02:23:19 [dump_input.py:72] Dumping input data for V1 LLM engine (v0.15.1) with config: model='Qwen/Qwen3-14B-AWQ', speculative_config=SpeculativeConfig(method='draft_model', model='Qwen/Qwen3-1.7B', num_spec_tokens=6), tokenizer='Qwen/Qwen3-14B-AWQ', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=16384, download_dir='/data/', load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size=1, disable_custom_all_reduce=False, quantization=awq_marlin, enforce_eager=False, enable_return_routed_experts=False, kv_cache_dtype=auto, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser_plugin='', enable_in_reasoning=False), observability_c...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: [Bug]: Triton CompilationError in speculative decoding (draft_model) bug;stale ### Your current environment ### 🐛 Describe the bug When enabling speculative decoding with method='draft_model', the engine crashes with a...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: False), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None, kv_cache_metrics=False, kv_cache_metrics_sample=0.01, cudagraph_metrics=Fal...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Bug]: Triton CompilationError in speculative decoding (draft_model) bug;stale ### Your current environment ### 🐛 Describe the bug When enabling speculative decoding with method='draft_model', the engine crashes with a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Triton CompilationError in speculative decoding (draft_model) bug;stale ### Your current environment ### 🐛 Describe the bug When enabling speculative decoding with method='draft_model', the engine crashes with a...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=16384, download_dir='/data/', load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
