# vllm-project/vllm#23152: [Bug]: TypeError: expected str, bytes or os.PathLike object, not NoneType

| 字段 | 值 |
| --- | --- |
| Issue | [#23152](https://github.com/vllm-project/vllm/issues/23152) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TypeError: expected str, bytes or os.PathLike object, not NoneType

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm 0.10.0 transformers 4.53.3 export CUDA_VISIBLE_DEVICES=1,2,3,4 && vllm serve Qwen2.5-VL-72B-Instruct \ --tensor-parallel-size 4 \ --dtype half \ --cpu-offload-gb 1 \ --gpu-memory-utilization 0.9 \ --host 0.0.0.0 \ --enable-auto-tool-choice \ --tool-call-parser hermes \ --no-enable-chunked-prefill \ --port 10000 启动报错 INFO 08-19 05:06:11 [__init__.py:235] Automatically detected platform cuda. INFO 08-19 05:06:14 [llm_engine.py:228] Initializing a V0 LLM engine (v0.10.0) with config: model='Qwen2.5-VL-72B-Instruct', speculative_config=None, tokenizer='Qwen2.5-VL-72B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=128000, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=4, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observa...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: 0 transformers 4.53.3 export CUDA_VISIBLE_DEVICES=1,2,3,4 && vllm serve Qwen2.5-VL-72B-Instruct \ --tensor-parallel-size 4 \ --dtype half \ --cpu-offload-gb 1 \ --gpu-memory-utilization 0.9 \ --host 0.0.0.0 \ --enable-a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: : TypeError: expected str, bytes or os.PathLike object, not NoneType bug;stale ### Your current environment ### 🐛 Describe the bug vllm 0.10.0 transformers 4.53.3 export CUDA_VISIBLE_DEVICES=1,2,3,4 && vllm serve Qwen2....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nd=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=Qwen2.5-VL-72B-Instruct, num_scheduler_steps=1,...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 3,4 && vllm serve Qwen2.5-VL-72B-Instruct \ --tensor-parallel-size 4 \ --dtype half \ --cpu-offload-gb 1 \ --gpu-memory-utilization 0.9 \ --host 0.0.0.0 \ --enable-auto-tool-choice \ --tool-call-parser hermes \ --no-ena...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
