# vllm-project/vllm#15653: [Bug]: vllm server dead issue

| 字段 | 值 |
| --- | --- |
| Issue | [#15653](https://github.com/vllm-project/vllm/issues/15653) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | cuda;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm server dead issue

### Issue 正文摘录

### Your current environment I used version of v0.7.0 - Here is my envirionment, and I want to use `kv_transfer_config` with LMCache - I run out the issue with only **tensor parallel** 4, in kubenetes + docker environment ``` INFO 03-27 05:06:19 llm_engine.py:232] Initializing an LLM engine (v0.7.0) with config: model='LGAI-EXAONE/EXAONE-3.5-32B-Instruct', speculative_config=None, tokenizer='LGAI-EXAONE/EXAONE-3.5-32B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=32768, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=4, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_time=False), seed=0, served_model_name=exaone1, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=False, chunked_prefill_enabled=False, use_async_output_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ]: vllm server dead issue bug;stale ### Your current environment I used version of v0.7.0 - Here is my envirionment, and I want to use `kv_transfer_config` with LMCache - I run out the issue with only **tensor parallel*...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: vllm server dead issue bug;stale ### Your current environment I used version of v0.7.0 - Here is my envirionment, and I want to use `kv_transfer_config` with LMCache - I run out the issue with only **tensor paral...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: de_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=32768, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=4, pipeline_parallel_size=1, disable_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ntization=None, enforce_eager=False, kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, colle...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ion of v0.7.0 - Here is my envirionment, and I want to use `kv_transfer_config` with LMCache - I run out the issue with only **tensor parallel** 4, in kubenetes + docker environment ``` INFO 03-27 05:06:19 llm_engine.py...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
