# vllm-project/vllm#23176: [Bug]: RuntimeError: Engine core initialization failed.

| 字段 | 值 |
| --- | --- |
| Issue | [#23176](https://github.com/vllm-project/vllm/issues/23176) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | runtime_err |
| Operator 关键词 | attention;cuda;operator;quantization;sampling |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: Engine core initialization failed.

### Issue 正文摘录

`(vllm2) ss345@dell-5820:~/vllm-local-build/vllm$ vllm serve "google/gemma-3-270m" INFO 08-19 13:12:30 [__init__.py:241] Automatically detected platform cuda. (APIServer pid=1179246) INFO 08-19 13:12:33 [api_server.py:1805] vLLM API server version 0.10.1rc2.dev34+g5bfe0dea7.d20250819 (APIServer pid=1179246) INFO 08-19 13:12:33 [utils.py:326] non-default args: {'model_tag': 'google/gemma-3-270m', 'model': 'google/gemma-3-270m'} (APIServer pid=1179246) INFO 08-19 13:12:39 [__init__.py:711] Resolved architecture: Gemma3ForCausalLM (APIServer pid=1179246) INFO 08-19 13:12:39 [__init__.py:1750] Using max model len 32768 (APIServer pid=1179246) INFO 08-19 13:12:40 [scheduler.py:222] Chunked prefill is enabled with max_num_batched_tokens=2048. INFO 08-19 13:12:45 [__init__.py:241] Automatically detected platform cuda. (EngineCore_0 pid=1179302) INFO 08-19 13:12:47 [core.py:644] Waiting for init message from front-end. (EngineCore_0 pid=1179302) INFO 08-19 13:12:47 [core.py:74] Initializing a V1 LLM engine (v0.10.1rc2.dev34+g5bfe0dea7.d20250819) with config: model='google/gemma-3-270m', speculative_config=None, tokenizer='google/gemma-3-270m', skip_tokenizer_init=False, tokenizer_mode=aut...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Bug]: RuntimeError: Engine core initialization failed. installation `(vllm2) ss345@dell-5820:~/vllm-local-build/vllm$ vllm serve "google/gemma-3-270m" INFO 08-19 13:12:30 [__init__.py:241] Automatically detected platfo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: ride_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: tive_config=None, tokenizer='google/gemma-3-270m', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_se...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ion `(vllm2) ss345@dell-5820:~/vllm-local-build/vllm$ vllm serve "google/gemma-3-270m" INFO 08-19 13:12:30 [__init__.py:241] Automatically detected platform cuda. (APIServer pid=1179246) INFO 08-19 13:12:33 [api_server....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
