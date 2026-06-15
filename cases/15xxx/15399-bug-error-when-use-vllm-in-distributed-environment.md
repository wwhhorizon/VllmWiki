# vllm-project/vllm#15399: [Bug]: Error when use vllm in distributed environment

| 字段 | 值 |
| --- | --- |
| Issue | [#15399](https://github.com/vllm-project/vllm/issues/15399) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error when use vllm in distributed environment

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```text INFO 03-24 09:41:05 __init__.py:207] Automatically detected platform cuda. INFO 03-24 09:41:30 config.py:549] This model supports multiple tasks: {'generate', 'score', 'reward', 'classify', 'embed'}. Defaulting to 'generate'. WARNING 03-24 09:41:30 config.py:676] Async output processing can not be enabled with pipeline parallel INFO 03-24 09:41:30 llm_engine.py:234] Initializing a V0 LLM engine (v0.7.3) with config: model='/home/mpi_share/env/bz/model/opt-1.3b', speculative_config=None, tokenizer='/home/mpi_share/env/bz/model/opt-1.3b', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=2048, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=2, pipeline_parallel_size=2, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_time=False)...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: kwargs=None, pooler_config=None, compilation_config={"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ine (v0.7.3) with config: model='/home/mpi_share/env/bz/model/opt-1.3b', speculative_config=None, tokenizer='/home/mpi_share/env/bz/model/opt-1.3b', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, overrid...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: uto, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_ti...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: de_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=2048, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=2, pipeline_parallel_size=2, disable_c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ext INFO 03-24 09:41:05 __init__.py:207] Automatically detected platform cuda. INFO 03-24 09:41:30 config.py:549] This model supports multiple tasks: {'generate', 'score', 'reward', 'classify', 'embed'}. Defaulting to '...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
