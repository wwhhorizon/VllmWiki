# vllm-project/vllm#24578: [Bug]: --enable-log-outputs Not Working in vLLM v0.10.1

| 字段 | 值 |
| --- | --- |
| Issue | [#24578](https://github.com/vllm-project/vllm/issues/24578) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | cache;cuda;fp8;quantization;sampling |
| 症状 | build_error;oom;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: --enable-log-outputs Not Working in vLLM v0.10.1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The --enable-log-outputs flag in vLLM (version vllm/vllm-openai:v0.10.1) does not log model outputs in the server logs, despite being enabled alongside --enable-log-requests, VLLM_LOG_LEVEL=TRACE, and --uvicorn-log-level trace. The logs show request details (e.g., prompt and sampling parameters) and server status (HTTP 200 OK), but the generated output text is missing. the generation is missing in logs #### out logs is INFO 09-10 19:10:43 [__init__.py:241] Automatically detected platform cuda. INFO 09-10 19:10:44 [llm_engine.py:222] Initializing a V0 LLM engine (v0.10.1) with config: model='/models/unsloth/Qwen3-4B-Thinking-2507-GGUF/Qwen3-4B-Thinking-2507-Q4_1.gguf', speculative_config=None, tokenizer='/models/unsloth/Qwen3-4B-Thinking-2507-GGUF/Qwen3-4B-Thinking-2507-Q4_1.gguf', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=1000, download_dir=None, load_format=gguf, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=gguf, enforce_eager=False, kv_cache_dtype=...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: onment ### 🐛 Describe the bug The --enable-log-outputs flag in vLLM (version vllm/vllm-openai:v0.10.1) does not log model outputs in the server logs, despite being enabled alongside --enable-log-requests, VLLM_LOG_LEVEL...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: ride_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=1000, download_dir=None, load_format=gguf, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: s INFO 09-10 19:10:43 [__init__.py:241] Automatically detected platform cuda. INFO 09-10 19:10:44 [llm_engine.py:222] Initializing a V0 LLM engine (v0.10.1) with config: model='/models/unsloth/Qwen3-4B-Thinking-2507-GGU...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: 22] Initializing a V0 LLM engine (v0.10.1) with config: model='/models/unsloth/Qwen3-4B-Thinking-2507-GGUF/Qwen3-4B-Thinking-2507-Q4_1.gguf', speculative_config=None, tokenizer='/models/unsloth/Qwen3-4B-Thinking-2507-GG...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: log-outputs flag in vLLM (version vllm/vllm-openai:v0.10.1) does not log model outputs in the server logs, despite being enabled alongside --enable-log-requests, VLLM_LOG_LEVEL=TRACE, and --uvicorn-log-level trace. The...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
