# vllm-project/vllm#16662: [Bug]: OOM error during LLAMA 4 meta-llama/Llama-4-Scout-17B-16E-Instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#16662](https://github.com/vllm-project/vllm/issues/16662) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: OOM error during LLAMA 4 meta-llama/Llama-4-Scout-17B-16E-Instruct

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Getting out of Memory error while trying to serve `meta-llama/Llama-4-Scout-17B-16E-Instruct` . here's the stack trace ``` DEBUG 04-15 12:02:29 [__init__.py:28] No plugins for group vllm.platform_plugins found. DEBUG 04-15 12:02:29 [__init__.py:34] Checking if TPU platform is available. DEBUG 04-15 12:02:29 [__init__.py:44] TPU platform is not available because: No module named 'libtpu' DEBUG 04-15 12:02:29 [__init__.py:52] Checking if CUDA platform is available. DEBUG 04-15 12:02:29 [__init__.py:72] Confirmed CUDA platform is available. DEBUG 04-15 12:02:29 [__init__.py:100] Checking if ROCm platform is available. DEBUG 04-15 12:02:29 [__init__.py:114] ROCm platform is not available because: No module named 'amdsmi' DEBUG 04-15 12:02:29 [__init__.py:122] Checking if HPU platform is available. DEBUG 04-15 12:02:29 [__init__.py:129] HPU platform is not available because habana_frameworks is not found. DEBUG 04-15 12:02:29 [__init__.py:140] Checking if XPU platform is available. DEBUG 04-15 12:02:29 [__init__.py:150] XPU platform is not available because: No module named 'intel_extension_for_pytorch' DEBUG 04-15 12:02:29 [__init__....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: _plugins found. INFO 04-15 12:02:30 [api_server.py:1034] vLLM API server version 0.8.4 INFO 04-15 12:02:30 [api_server.py:1035] args: Namespace(subparser='serve', model_tag='meta-llama/Llama-4-Scout-17B-16E-Instruct', c...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: model_loader_extra_config=None, use_tqdm_on_load=True, config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='auto', logits_processor_pattern=None, model_impl='auto', distribu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: OOM error during LLAMA 4 meta-llama/Llama-4-Scout-17B-16E-Instruct bug ### Your current environment ### 🐛 Describe the bug Getting out of Memory error while trying to serve `meta-llama/Llama-4-Scout-17B-16E-Instr...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='meta-llama/Llama-4-Scout-17B-16E-Ins...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: dtype='auto', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='auto', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel_siz...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
