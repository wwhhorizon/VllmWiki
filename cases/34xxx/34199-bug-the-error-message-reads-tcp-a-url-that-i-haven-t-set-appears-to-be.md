# vllm-project/vllm#34199: [Bug]: The error message reads: "'tcp://a URL that I haven't set' appears to be a URI. This might be due to a Kubernetes service discovery problem."

| 字段 | 值 |
| --- | --- |
| Issue | [#34199](https://github.com/vllm-project/vllm/issues/34199) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;model_support;quantization |
| 子分类 | debug |
| Operator 关键词 | cuda;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: The error message reads: "'tcp://a URL that I haven't set' appears to be a URI. This might be due to a Kubernetes service discovery problem."

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running DeepSeek-R1-0528-Qwen-8B with vllm0.9.1, my startup command is: ```text vllm serve /home/Models/DeepSeek-R1-0528-Qwen3-8B --enable-auto-tool-choice --tool-call-parser hermes --port 5050 --max-model-len 32768 --served_model_name DeepSeek-R1-0528-Qwen3-8B --max_num_seqs 64 --dtype float16 --tensor_parallel_size 2 --gpu_memory_utilization 0.9 --uvicorn-log-level trace -enforce-eager ``` Error message as follows: ```text INFO 02-10 09:39:08 [__init__.py:244] Automatically detected platform cuda. INFO 02-10 09:39:12 [llm_engine.py:230] Initializing a V0 LLM engine (v0.9.1) with config: model='/home/Models/DeepSeek-R1-0528-Qwen3-8B', speculative_config=None, tokenizer='/home/Models/DeepSeek-R1-0528-Qwen3-8B', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=2, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=True, kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='a...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: nd=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=DeepSeek-R1-0528-Qwen3-8B, num_scheduler_steps=1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: nt environment ### 🐛 Describe the bug When running DeepSeek-R1-0528-Qwen-8B with vllm0.9.1, my startup command is: ```text vllm serve /home/Models/DeepSeek-R1-0528-Qwen3-8B --enable-auto-tool-choice --tool-call-parser h...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: a URI. This might be due to a Kubernetes service discovery problem." bug;stale ### Your current environment ### 🐛 Describe the bug When running DeepSeek-R1-0528-Qwen-8B with vllm0.9.1, my startup command is: ```text vll...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 32768 --served_model_name DeepSeek-R1-0528-Qwen3-8B --max_num_seqs 64 --dtype float16 --tensor_parallel_size 2 --gpu_memory_utilization 0.9 --uvicorn-log-level trace -enforce-eager ``` Error message as follows: ```text...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
