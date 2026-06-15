# vllm-project/vllm#36433: [Bug]: matryoshka need gpu-memory???

| 字段 | 值 |
| --- | --- |
| Issue | [#36433](https://github.com/vllm-project/vllm/issues/36433) |
| 状态 | closed |
| 标签 | bug;good first issue |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;moe;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: matryoshka need gpu-memory???

### Issue 正文摘录

### Your current environment ``` vllm 0.16.0 ``` ### 🐛 Describe the bug first yaml ```yaml model: "/workspace/KaLM-embedding-multilingual-mini-instruct-v2.5" convert: embed gpu-memory-utilization: 0.85 served-model-name: KaLM-embedding-multilingual-mini-instruct-v2.5 max-model-len: 8000 port: 8000 max_num_batched_tokens: 20000 # hf-overrides: {"matryoshka_dimensions": [896, 512, 256, 128, 64, 32]} max_num_seqs: 16 block_size: 16 host: "0.0.0.0" ``` It Ok in 3GB. second yaml: ```yaml model: "/workspace/KaLM-embedding-multilingual-mini-instruct-v2.5" convert: embed gpu-memory-utilization: 0.85 served-model-name: KaLM-embedding-multilingual-mini-instruct-v2.5 max-model-len: 8000 port: 8000 max_num_batched_tokens: 20000 hf-overrides: {"matryoshka_dimensions": [896, 512, 256, 128, 64, 32]} max_num_seqs: 16 block_size: 16 host: "0.0.0.0" ``` It failed in 3GB but OK in 5GB. error log: ``` (EngineCore_DP0 pid=372) INFO 03-09 01:15:12 [core.py:97] Initializing a V1 LLM engine (v0.16.0) with config: model='/workspace/KaLM-embedding-multilingual-mini-instruct-v2.5', speculative_config=None, tokenizer='/workspace/KaLM-embedding-multilingual-mini-instruct-v2.5', skip_tokenizer_init=False, toke...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: False), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None, kv_cache_metrics=False, kv_cache_metrics_sample=0.01, cudagraph_metrics=Fal...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser_p...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ment ``` vllm 0.16.0 ``` ### 🐛 Describe the bug first yaml ```yaml model: "/workspace/KaLM-embedding-multilingual-mini-instruct-v2.5" convert: embed gpu-memory-utilization: 0.85 served-model-name: KaLM-embedding-multili...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=8000, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size=1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: , enable_return_routed_experts=False, kv_cache_dtype=auto, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
