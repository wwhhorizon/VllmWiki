# vllm-project/vllm#24282: [Bug]: Deployment of Apertus-Instruct-8B failed with error

| 字段 | 值 |
| --- | --- |
| Issue | [#24282](https://github.com/vllm-project/vllm/issues/24282) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;operator;quantization;sampling |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Deployment of Apertus-Instruct-8B failed with error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug INFO 09-04 15:32:04 [__init__.py:241] Automatically detected platform cuda. WARNING 09-04 15:32:06 [__init__.py:1764] argument 'task' is deprecated [1;36m(APIServer pid=1)[0;0m INFO 09-04 15:32:06 [api_server.py:1882] vLLM API server version 0.10.2rc2.dev0+g5438967fb.d20250904 [1;36m(APIServer pid=1)[0;0m INFO 09-04 15:32:06 [utils.py:328] non-default args: {'port': 8080, 'model': '/mnt/models', 'task': 'generate', 'trust_remote_code': True, 'served_model_name': ['test-apertus-8b']} [1;36m(APIServer pid=1)[0;0m The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored. [1;36m(APIServer pid=1)[0;0m INFO 09-04 15:32:17 [__init__.py:744] Resolved architecture: ApertusForCausalLM [1;36m(APIServer pid=1)[0;0m `torch_dtype` is deprecated! Use `dtype` instead! [1;36m(APIServer pid=1)[0;0m INFO 09-04 15:32:17 [__init__.py:1773] Using max model len 65536 [1;36m(APIServer pid=1)[0;0m INFO 09-04 15:32:18 [scheduler.py:222] Chunked prefill is enabled with max_num_batched_tokens=8192. /usr/local/lib/python3.12/dist-packages/transformers/utils/hub.py:111: FutureWarning: Using `TRANSFOR...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: er pid=1)[0;0m INFO 09-04 15:32:06 [api_server.py:1882] vLLM API server version 0.10.2rc2.dev0+g5438967fb.d20250904 [1;36m(APIServer pid=1)[0;0m INFO 09-04 15:32:06 [utils.py:328] non-default args: {'port': 8080, 'mo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Deployment of Apertus-Instruct-8B failed with error bug;stale ### Your current environment ### 🐛 Describe the bug INFO 09-04 15:32:04 [__init__.py:241] Automatically detected platform cuda. WARNING 09-04 15:32:06...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: d architecture: ApertusForCausalLM [1;36m(APIServer pid=1)[0;0m `torch_dtype` is deprecated! Use `dtype` instead! [1;36m(APIServer pid=1)[0;0m INFO 09-04 15:32:17 [__init__.py:1773] Using max model len 65536 [1;36m...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ;0m INFO 09-04 15:32:06 [utils.py:328] non-default args: {'port': 8080, 'model': '/mnt/models', 'task': 'generate', 'trust_remote_code': True, 'served_model_name': ['test-apertus-8b']} [1;36m(APIServer pid=1)[0;0m The...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
