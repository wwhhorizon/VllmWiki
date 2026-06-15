# vllm-project/vllm#28919: [Bug]: Qwen3-32B use eagle3 crash

| 字段 | 值 |
| --- | --- |
| Issue | [#28919](https://github.com/vllm-project/vllm/issues/28919) |
| 状态 | open |
| 标签 | bug;unstale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | cold_start |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-32B use eagle3 crash

### Issue 正文摘录

### Your current environment env: vllm == 0.11.0 model: Qwen3-32B,AngelSlim/Qwen3-32B_eagle3 ### 🐛 Describe the bug when I use Qwen3-32B with eagle3, when request a query, engine will crash. the log as follow: ``` INFO 11-18 14:35:55 [__init__.py:216] Automatically detected platform cuda. (APIServer pid=168309) INFO 11-18 14:36:24 [api_server.py:1839] vLLM API server version 0.11.0 (APIServer pid=168309) INFO 11-18 14:36:24 [utils.py:233] non-default args: {'port': 10002, 'uvicorn_log_level': 'debug', 'enable_log_outputs': True, 'model': '/mnt1/wanghui/model_weight/Qwen3-32B', 'trust_remote_code': True, 'max_model_len': 4096, 'served_model_name': ['qwen3-32b-eagle3'], 'speculative_config': {'model': '/mnt1/wanghui/model_weight/Qwen3-32B_eagle3', 'num_speculative_tokens': 5, 'method': 'eagle3', 'draft_tensor_parallel_size': 1}, 'enable_log_requests': True} (APIServer pid=168309) The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored. (APIServer pid=168309) INFO 11-18 14:36:24 [model.py:547] Resolved architecture: Qwen3ForCausalLM (APIServer pid=168309) `torch_dtype` is deprecated! Use `dtype` instead! (APIServer pid=168309) INFO 11-18...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: [Bug]: Qwen3-32B use eagle3 crash bug;unstale ### Your current environment env: vllm == 0.11.0 model: Qwen3-32B,AngelSlim/Qwen3-32B_eagle3 ### 🐛 Describe the bug when I use Qwen3-32B with eagle3, when request a query, e...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ver pid=168309) INFO 11-18 14:36:24 [api_server.py:1839] vLLM API server version 0.11.0 (APIServer pid=168309) INFO 11-18 14:36:24 [utils.py:233] non-default args: {'port': 10002, 'uvicorn_log_level': 'debug', 'enable_l...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser=''), observability_con...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Qwen3-32B use eagle3 crash bug;unstale ### Your current environment env: vllm == 0.11.0 model: Qwen3-32B,AngelSlim/Qwen3-32B_eagle3 ### 🐛 Describe the bug when I use Qwen3-32B with eagle3, when request a query, e...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: 7] Resolved architecture: Qwen3ForCausalLM (APIServer pid=168309) `torch_dtype` is deprecated! Use `dtype` instead! (APIServer pid=168309) INFO 11-18 14:36:24 [model.py:1510] Using max model len 4096 (APIServer pid=1683...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
