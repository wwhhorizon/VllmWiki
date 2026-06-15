# vllm-project/vllm#13815: [Bug]: ValueError: invalid literal for int() with base 10 for device_id_to_physical_device_id` function

| 字段 | 值 |
| --- | --- |
| Issue | [#13815](https://github.com/vllm-project/vllm/issues/13815) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;scheduler_memory |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ValueError: invalid literal for int() with base 10 for device_id_to_physical_device_id` function

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm an issue loading a model downloaded offline (I have no internet access to get the model via the usual method), but I'm not sure why I'm getting a `ValueError: invalid literal for int() with base 10: 'GPU-52a3a85d-3c55-ca3a-a955-82c69ed360fc'` with the `device_id_to_physical_device_id` function on vLLM v0.7.3 and v0.7.0 (I previously thought that if I upgraded to v0.7.3, it would solve the issue). ``` (vllm) [hong0259@x1000c0s4b0n1 vllm]$ CUDA_VISIBLE_DEVICES=GPU-52a3a85d-3c55-ca3a-a955-82c69ed360fc vllm serve /home/users/ntu/h ong0259/scratch/models--deepseek-ai--DeepSeek-R1-Distill-Qwen-14B/snapshots/5ee96d8a09692e87087a6e0496d87124a1cdc3fe --max-model -len 10000 --dtype auto INFO 02-25 16:17:56 [__init__.py:207] Automatically detected platform cuda. INFO 02-25 16:18:02 [api_server.py:911] vLLM API server version 0.7.3.dev328+g4a8cfc755 INFO 02-25 16:18:02 [api_server.py:912] args: Namespace(subparser='serve', model_tag='/home/users/ntu/hong0259/scratch/models--deepseek-ai--DeepSeek-R1-Distill-Qwen-14B/snapshots/5ee96d8a09692e87087a6e0496d87124a1cdc3fe', config='', host=None, port=8000, uvicorn_log_level='info', allow_creden...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: d platform cuda. INFO 02-25 16:18:02 [api_server.py:911] vLLM API server version 0.7.3.dev328+g4a8cfc755 INFO 02-25 16:18:02 [api_server.py:912] args: Namespace(subparser='serve', model_tag='/home/users/ntu/hong0259/scr...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: pshots/5ee96d8a09692e87087a6e0496d87124a1cdc3fe --max-model -len 10000 --dtype auto INFO 02-25 16:17:56 [__init__.py:207] Automatically detected platform cuda. INFO 02-25 16:18:02 [api_server.py:911] vLLM API server ver...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: r current environment ### 🐛 Describe the bug I'm an issue loading a model downloaded offline (I have no internet access to get the model via the usual method), but I'm not sure why I'm getting a `ValueError: invalid lit...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, enable_reasoning=False, reasoning_parser=None, tool_call_parser=None, tool_parser_plugin=...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: type='auto', kv_cache_dtype='auto', max_model_len=10000, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
