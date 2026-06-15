# vllm-project/vllm#24723: [Bug]: can't  run the reranker model service on a GPU machine using only the CPU

| 字段 | 值 |
| --- | --- |
| Issue | [#24723](https://github.com/vllm-project/vllm/issues/24723) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;quantization;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: can't  run the reranker model service on a GPU machine using only the CPU

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug v0.9.2 run serve with **--device cpu** is not working on gpu device. **How to start the reranker model service on a GPU machine using only the CPU??** log : argument 'device' is deprecated。 Automatically detected platform cuda. ``` INFO 09-12 05:42:13 [__init__.py:244] Automatically detected platform cuda. WARNING 09-12 05:42:17 [__init__.py:1441] argument 'device' is deprecated INFO 09-12 05:42:17 [api_server.py:1395] vLLM API server version 0.9.2 INFO 09-12 05:42:17 [cli_args.py:325] non-default args: {'host': '0.0.0.0', 'port': 40007, 'model': '/home/models/Qwen3-Reranker-0.6B', 'task': 'score', 'max_model_len': 40000, 'served_model_name': ['qwen3-reranker-0.6b'], 'device': 'cpu'} INFO 09-12 05:42:25 [config.py:1472] Using max model len 40000 INFO 09-12 05:42:25 [arg_utils.py:1596] (Disabling) chunked prefill by default INFO 09-12 05:42:25 [arg_utils.py:1599] (Disabling) prefix caching by default INFO 09-12 05:42:25 [config.py:4601] Only "last" pooling supports chunked prefill and prefix caching; disabling both. INFO 09-12 05:42:31 [__init__.py:244] Automatically detected platform cuda. INFO 09-12 05:42:34 [core.py:526] Waitin...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ' is deprecated INFO 09-12 05:42:17 [api_server.py:1395] vLLM API server version 0.9.2 INFO 09-12 05:42:17 [cli_args.py:325] non-default args: {'host': '0.0.0.0', 'port': 40007, 'model': '/home/models/Qwen3-Reranker-0.6...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: run the reranker model service on a GPU machine using only the CPU bug;stale ### Your current environment ### 🐛 Describe the bug v0.9.2 run serve with **--device cpu** is not working on gpu device. **How to start the re...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ride_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=40000, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: can't run the reranker model service on a GPU machine using only the CPU bug;stale ### Your current environment ### 🐛 Describe the bug v0.9.2 run serve with **--device cpu** is not working on gpu device. **How to...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
