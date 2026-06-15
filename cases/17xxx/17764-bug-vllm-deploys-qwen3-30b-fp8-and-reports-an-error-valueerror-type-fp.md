# vllm-project/vllm#17764: [Bug]: vllm deploys qwen3 30B fp8 and reports an error: ValueError("type fp8e4nv not supported in this architecture. The supported fp8 dtypes are ('fp8e4b15', 'fp8e5')"),

| 字段 | 值 |
| --- | --- |
| Issue | [#17764](https://github.com/vllm-project/vllm/issues/17764) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm deploys qwen3 30B fp8 and reports an error: ValueError("type fp8e4nv not supported in this architecture. The supported fp8 dtypes are ('fp8e4b15', 'fp8e5')"),

### Issue 正文摘录

### Your current environment Linux A100 NVIDIA GPU vllm ==0.8.5.post1+cu118 python==3.10 ### 🐛 Describe the bug ``` INFO 05-07 09:58:52 [llm_engine.py:240] Initializing a V0 LLM engine (v0.8.5.post1) with config: model='/home/xinference/cache/qwen3-fp8-30b', speculative_config=None, tokenizer='/home/xinference/cache/qwen3-fp8-30b', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=40960, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=fp8, enforce_eager=False, kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines', reasoning_backend=None), observability_config=ObservabilityConfig(show_hidden_metrics=False, otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_time=False), seed=None, served_model_name=/home/xinference/cache/qwen3-fp8-30b, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=None, chunked_prefill_enabled=True, use_async_output_proc=True, disable_mm_preproce...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: vllm deploys qwen3 30B fp8 and reports an error: ValueError("type fp8e4nv not supported in this architecture. The supported fp8 dtypes are ('fp8e4b15', 'fp8e5')"), bug;stale ### Your current environment Linux A10...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: architecture. The supported fp8 dtypes are ('fp8e4b15', 'fp8e5')"), bug;stale ### Your current environment Linux A100 NVIDIA GPU vllm ==0.8.5.post1+cu118 python==3.10 ### 🐛 Describe the bug ``` INFO 05-07 09:58:52 [llm_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: kwargs=None, pooler_config=None, compilation_config={"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: fp8 and reports an error: ValueError("type fp8e4nv not supported in this architecture. The supported fp8 dtypes are ('fp8e4b15', 'fp8e5')"), bug;stale ### Your current environment Linux A100 NVIDIA GPU vllm ==0.8.5.post...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: vllm deploys qwen3 30B fp8 and reports an error: ValueError("type fp8e4nv not supported in this architecture. The supported fp8 dtypes are ('fp8e4b15', 'fp8e5')"), bug;stale ### Your current environment Linux A10...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
