# vllm-project/vllm#7389: [Bug]: Successfully deployed embedding model 'gte-Qwen2-7B-instruct', but got "TypeError: 'async for' requires an object with __aiter__ method, got coroutine" when calling it

| 字段 | 值 |
| --- | --- |
| Issue | [#7389](https://github.com/vllm-project/vllm/issues/7389) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;crash;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Successfully deployed embedding model 'gte-Qwen2-7B-instruct', but got "TypeError: 'async for' requires an object with __aiter__ method, got coroutine" when calling it

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Deployed Embedding model named 'gte-Qwen2-7B-instruct' successfully via command: ` python -m vllm.entrypoints.openai.api_server --served-model-name gte-Qwen2-7B-instruct --model /data1/iic/gte_Qwen2-7B-instruct --port 9990 --gpu-memory-utilization 0.3 ` And it ran good, got following logs: ` INFO 08-10 16:06:52 config.py:820] Chunked prefill is enabled with max_num_batched_tokens=512. INFO 08-10 16:06:52 llm_engine.py:174] Initializing an LLM engine (v0.5.4) with config: model='/data1/iic/gte_Qwen2-7B-instruct', speculative_config=None, tokenizer='/data1/iic/gte_Qwen2-7B-instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, rope_scaling=None, rope_theta=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=131072, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto, quantization_param_path=None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), observability_config=ObservabilityConfig(otlp_traces_endpo...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: -7B-instruct', but got "TypeError: 'async for' requires an object with __aiter__ method, got coroutine" when calling it bug;stale ### Your current environment ### 🐛 Describe the bug Deployed Embedding model named 'gte-Q...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ires an object with __aiter__ method, got coroutine" when calling it bug;stale ### Your current environment ### 🐛 Describe the bug Deployed Embedding model named 'gte-Qwen2-7B-instruct' successfully via command: ` pytho...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ning out of memory, consider decreasing `gpu_memory_utilization` or enforcing eager mode. You can also reduce the `max_num_seqs` as needed to decrease memory usage. INFO 08-10 16:07:26 model_runner.py:1225] Graph captur...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Successfully deployed embedding model 'gte-Qwen2-7B-instruct', but got "TypeError: 'async for' requires an object with __aiter__ method, got coroutine" when calling it bug;stale ### Your current environment ### 🐛...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: None, rope_theta=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=131072, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
