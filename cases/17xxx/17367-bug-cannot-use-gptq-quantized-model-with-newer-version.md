# vllm-project/vllm#17367: [Bug]: Cannot use GPTQ quantized model with newer version

| 字段 | 值 |
| --- | --- |
| Issue | [#17367](https://github.com/vllm-project/vllm/issues/17367) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;gemm;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Cannot use GPTQ quantized model with newer version

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I was able to run a gptq quantized model with vLLM version 0.6.2, when I tried to use latest version of vLLM I am not able to run the same model in same GPU. The error log that I got in newer version is below: INFO 04-29 08:40:12 [__init__.py:239] Automatically detected platform cuda. INFO 04-29 08:40:16 [llm_engine.py:240] Initializing a V0 LLM engine (v0.8.5) with config: model='Qwen2.5-14B-Instruct-GPTQ-Int4/', speculative_config=None, tokenizer='Qwen2.5-14B-Instruct-GPTQ-Int4/', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=8192, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=gptq_bitblas, enforce_eager=True, kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='auto', reasoning_backend=None), observability_config=ObservabilityConfig(show_hidden_metrics=False, otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_time=False), seed=No...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: Cannot use GPTQ quantized model with newer version bug ### Your current environment ### 🐛 Describe the bug I was able to run a gptq quantized model with vLLM version 0.6.2, when I tried to use latest version of v...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Cannot use GPTQ quantized model with newer version bug ### Your current environment ### 🐛 Describe the bug I was able to run a gptq quantized model with vLLM version 0.6.2, when I tried to use latest version of v...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: Cannot use GPTQ quantized model with newer version bug ### Your current environment ### 🐛 Describe the bug I was able to run a gptq quantized model with vLLM version 0.6.2, when I tried to use latest version of v...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: LM engine (v0.8.5) with config: model='Qwen2.5-14B-Instruct-GPTQ-Int4/', speculative_config=None, tokenizer='Qwen2.5-14B-Instruct-GPTQ-Int4/', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neur...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: uto, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='auto', reasoning_backend=None), observability_config=ObservabilityConfig(show_hidden_metrics=False, otlp_traces_endpoint=None, collect_mod...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
