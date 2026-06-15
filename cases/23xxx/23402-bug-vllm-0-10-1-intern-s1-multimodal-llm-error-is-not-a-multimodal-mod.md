# vllm-project/vllm#23402: [Bug]: vLLM 0.10.1 - Intern-S1 MultiModal LLM - error: "is not a multimodal model"

| 字段 | 值 |
| --- | --- |
| Issue | [#23402](https://github.com/vllm-project/vllm/issues/23402) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | attention;cache;cuda;fp8;moe;quantization;sampling |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM 0.10.1 - Intern-S1 MultiModal LLM - error: "is not a multimodal model"

### Issue 正文摘录

### Your current environment InternS1 is not able to process images I tested this model with vLLM 0.10.1. It does load, but does not seem to support multi modal inputs, like images. ``` INFO 08-21 03:37:24 [__init__.py:241] Automatically detected platform cuda. (APIServer pid=1) INFO 08-21 03:37:26 [api_server.py:1805] vLLM API server version 0.10.1 (APIServer pid=1) INFO 08-21 03:37:26 [utils.py:326] non-default args: {'port': 8081, 'api_key': ['test'], 'enable_auto_tool_choice': True, 'tool_call_parser': 'internlm', 'model': '/usr/src/Intern-S1-FP8', 'trust_remote_code': True, 'served_model_name': ['Intern-S1-FP8'], 'reasoning_parser': 'deepseek_r1', 'tensor_parallel_size': 4, 'limit_mm_per_prompt': {'image': 4}} (APIServer pid=1) The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored. (APIServer pid=1) INFO 08-21 03:37:32 [__init__.py:711] Resolved architecture: Qwen3MoeForCausalLM (APIServer pid=1) INFO 08-21 03:37:33 [__init__.py:1750] Using max model len 40960 (APIServer pid=1) INFO 08-21 03:37:34 [scheduler.py:222] Chunked prefill is enabled with max_num_batched_tokens=8192. INFO 08-21 03:37:38 [__init__.py:241] Automatically...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: y:1750] Using max model len 40960 (APIServer pid=1) INFO 08-21 03:37:34 [scheduler.py:222] Chunked prefill is enabled with max_num_batched_tokens=8192. INFO 08-21 03:37:38 [__init__.py:241] Automatically detected platfo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: ice': True, 'tool_call_parser': 'internlm', 'model': '/usr/src/Intern-S1-FP8', 'trust_remote_code': True, 'served_model_name': ['Intern-S1-FP8'], 'reasoning_parser': 'deepseek_r1', 'tensor_parallel_size': 4, 'limit_mm_p...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: vLLM 0.10.1 - Intern-S1 MultiModal LLM - error: "is not a multimodal model" bug ### Your current environment InternS1 is not able to process images I tested this model with vLLM 0.10.1. It does load, but does not...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend='deepseek_r1'), observ...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: PIServer pid=1) INFO 08-21 03:37:26 [api_server.py:1805] vLLM API server version 0.10.1 (APIServer pid=1) INFO 08-21 03:37:26 [utils.py:326] non-default args: {'port': 8081, 'api_key': ['test'], 'enable_auto_tool_choice...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
