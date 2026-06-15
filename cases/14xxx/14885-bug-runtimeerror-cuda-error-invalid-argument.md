# vllm-project/vllm#14885: [Bug]: RuntimeError: CUDA error: invalid argument

| 字段 | 值 |
| --- | --- |
| Issue | [#14885](https://github.com/vllm-project/vllm/issues/14885) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: CUDA error: invalid argument

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Errors DEBUG 03-16 17:45:20 __init__.py:28] No plugins for group vllm.platform_plugins found. INFO 03-16 17:45:20 __init__.py:207] Automatically detected platform cuda. DEBUG 03-16 17:45:21 __init__.py:28] No plugins for group vllm.general_plugins found. INFO 03-16 17:45:23 config.py:2444] Downcasting torch.float32 to torch.float16. INFO 03-16 17:45:28 config.py:549] This model supports multiple tasks: {'score', 'generate', 'classify', 'reward', 'embed'}. Defaulting to 'generate'. WARNING 03-16 17:45:28 config.py:1129] Possibly too large swap space. 4.00 GiB out of the 7.70 GiB total CPU memory is allocated for the swap space. INFO 03-16 17:45:28 llm_engine.py:234] Initializing a V0 LLM engine (v0.7.3) with config: model='openai-community/gpt2', speculative_config=None, tokenizer='openai-community/gpt2', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=1024, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=None,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: kwargs=None, pooler_config=None, compilation_config={"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ral_plugins found. INFO 03-16 17:45:23 config.py:2444] Downcasting torch.float32 to torch.float16. INFO 03-16 17:45:28 config.py:549] This model supports multiple tasks: {'score', 'generate', 'classify', 'reward', 'embe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: RuntimeError: CUDA error: invalid argument bug;stale ### Your current environment ### 🐛 Describe the bug Errors DEBUG 03-16 17:45:20 __init__.py:28] No plugins for group vllm.platform_plugins found. INFO 03-16 17...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: uto, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_ti...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: RuntimeError: CUDA error: invalid argument bug;stale ### Your current environment ### 🐛 Describe the bug Errors DEBUG 03-16 17:45:20 __init__.py:28] No plugins for group vllm.platform_plugins found. INFO 03-16 17...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
