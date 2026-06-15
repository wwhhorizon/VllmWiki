# vllm-project/vllm#17109: [Bug]: Tool calls data comes in content field after text chunks

| 字段 | 值 |
| --- | --- |
| Issue | [#17109](https://github.com/vllm-project/vllm/issues/17109) |
| 状态 | closed |
| 标签 | bug;stale;tool-calling |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Tool calls data comes in content field after text chunks

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Started the model with following config; ``` Initializing a V1 LLM engine (v0.8.5.dev152+g5536b30a4.d20250422) with config: model='meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8', speculative_config=None, tokenizer='meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=500000, download_dir='/app/data/models', load_format=LoadFormat.SAFETENSORS, tensor_parallel_size=4, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=compressed-tensors, enforce_eager=False, kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='auto', reasoning_backend=None), observability_config=ObservabilityConfig(show_hidden_metrics=False, otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_time=False), seed=None, served_model_name=meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=True, chunked_prefill_enabled=True,...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: 50422) with config: model='meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8', speculative_config=None, tokenizer='meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8', skip_tokenizer_init=False, tokenizer_mode=auto, revi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Tool calls data comes in content field after text chunks bug;stale;tool-calling ### Your current environment ### 🐛 Describe the bug Started the model with following config; ``` Initializing a V1 LLM engine (v0.8....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ed_attention","vllm.unified_attention_with_output"],"use_inductor":true,"compile_sizes":[],"use_cudagraph":true,"cudagraph_num_of_warmups":1,"cudagraph_capture_sizes":[512,504,496,488,480,472,464,456,448,440,432,424,416...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ing ### Your current environment ### 🐛 Describe the bug Started the model with following config; ``` Initializing a V1 LLM engine (v0.8.5.dev152+g5536b30a4.d20250422) with config: model='meta-llama/Llama-4-Maverick-17B-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: uto, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='auto', reasoning_backend=None), observability_config=ObservabilityConfig(show_hidden_metrics=False, otlp_traces_endpoint=None, collect_mod...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
