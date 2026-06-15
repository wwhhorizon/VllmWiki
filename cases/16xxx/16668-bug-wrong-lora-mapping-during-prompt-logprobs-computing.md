# vllm-project/vllm#16668: [Bug]: Wrong lora mapping during prompt logprobs computing

| 字段 | 值 |
| --- | --- |
| Issue | [#16668](https://github.com/vllm-project/vllm/issues/16668) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | cold_start |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Wrong lora mapping during prompt logprobs computing

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Just run the `multilora_inference` example ```bash root:/vllm-workspace/vllm-master# VLLM_USE_V1=1 python3 examples/offline_inference/multilora_inference.py INFO 04-15 08:10:34 [__init__.py:239] Automatically detected platform cuda. INFO 04-15 08:10:41 [config.py:697] This model supports multiple tasks: {'reward', 'generate', 'classify', 'score', 'embed'}. Defaulting to 'generate'. INFO 04-15 08:10:42 [config.py:1956] Chunked prefill is enabled with max_num_batched_tokens=2048. WARNING 04-15 08:10:42 [config.py:2644] LoRA with chunked prefill is still experimental and may be unstable. INFO 04-15 08:10:42 [core.py:61] Initializing a V1 LLM engine (v0.8.5.dev22+g1575c1701) with config: model='/root/vllm/Llama-2-7b-chat-hf', speculative_config=None, tokenizer='/root/vllm/Llama-2-7b-chat-hf', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=4096, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=Fa...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: nit__.py:239] Automatically detected platform cuda. INFO 04-15 08:10:41 [config.py:697] This model supports multiple tasks: {'reward', 'generate', 'classify', 'score', 'embed'}. Defaulting to 'generate'. INFO 04-15 08:1...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Wrong lora mapping during prompt logprobs computing bug;stale ### Your current environment ### 🐛 Describe the bug Just run the `multilora_inference` example ```bash root:/vllm-workspace/vllm-master# VLLM_USE_V1=1...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: uto, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='auto', reasoning_backend=None), observability_config=ObservabilityConfig(show_hidden_metrics=False, otlp_traces_endpoint=None, collect_mod...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ed_attention","vllm.unified_attention_with_output"],"use_inductor":true,"compile_sizes":[],"use_cudagraph":true,"cudagraph_num_of_warmups":1,"cudagraph_capture_sizes":[512,504,496,488,480,472,464,456,448,440,432,424,416...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: de_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=4096, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable_c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
