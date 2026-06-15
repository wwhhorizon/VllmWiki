# vllm-project/vllm#22517: [Bug]: Smollm3M not working anymore

| 字段 | 值 |
| --- | --- |
| Issue | [#22517](https://github.com/vllm-project/vllm/issues/22517) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Smollm3M not working anymore

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running `uv tool run vllm@v0.10.0 serve --model=HuggingFaceTB/SmolLM3-3B --max-model-len=4092 --dtype=bfloat16 --gpu-memory-utilization=0.4 --port=8091` gives me the following error: ``` INFO 08-08 14:00:06 [__init__.py:235] Automatically detected platform cuda. INFO 08-08 14:00:08 [api_server.py:1755] vLLM API server version 0.10.0 INFO 08-08 14:00:08 [cli_args.py:261] non-default args: {'port': 8091, 'model': 'HuggingFaceTB/SmolLM3-3B', 'dtype': 'bfloat16', 'max_model_len': 4092, 'gpu_memory_utilization': 0.4} INFO 08-08 14:00:13 [config.py:1604] Using max model len 4092 INFO 08-08 14:00:13 [config.py:2434] Chunked prefill is enabled with max_num_batched_tokens=2048. INFO 08-08 14:00:16 [__init__.py:235] Automatically detected platform cuda. INFO 08-08 14:00:18 [core.py:572] Waiting for init message from front-end. INFO 08-08 14:00:18 [core.py:71] Initializing a V1 LLM engine (v0.10.0) with config: model='HuggingFaceTB/SmolLM3-3B', speculative_config=None, tokenizer='HuggingFaceTB/SmolLM3-3B', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config={}, tokenizer_revision=None, trust_remote_code=Fal...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: platform cuda. INFO 08-08 14:00:08 [api_server.py:1755] vLLM API server version 0.10.0 INFO 08-08 14:00:08 [cli_args.py:261] non-default args: {'port': 8091, 'model': 'HuggingFaceTB/SmolLM3-3B', 'dtype': 'bfloat16', 'ma...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: 10.0 serve --model=HuggingFaceTB/SmolLM3-3B --max-model-len=4092 --dtype=bfloat16 --gpu-memory-utilization=0.4 --port=8091` gives me the following error: ``` INFO 08-08 14:00:06 [__init__.py:235] Automatically detected...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ### 🐛 Describe the bug Running `uv tool run vllm@v0.10.0 serve --model=HuggingFaceTB/SmolLM3-3B --max-model-len=4092 --dtype=bfloat16 --gpu-memory-utilization=0.4 --port=8091` gives me the following error: ``` INFO 08-0...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: 4] Using max model len 4092 INFO 08-08 14:00:13 [config.py:2434] Chunked prefill is enabled with max_num_batched_tokens=2048. INFO 08-08 14:00:16 [__init__.py:235] Automatically detected platform cuda. INFO 08-08 14:00:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
