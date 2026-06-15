# vllm-project/vllm#15332: [Bug]: RuntimeError: The size of tensor a (1059) must match the size of tensor b (376) at non-singleton dimension, DeepSeek R1 H20x16 pp2, v1 engine

| 字段 | 值 |
| --- | --- |
| Issue | [#15332](https://github.com/vllm-project/vllm/issues/15332) |
| 状态 | closed |
| 标签 | bug;ray;stale |
| 评论 | 29; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;scheduler_memory;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cache;cuda;fp8;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: The size of tensor a (1059) must match the size of tensor b (376) at non-singleton dimension, DeepSeek R1 H20x16 pp2, v1 engine

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug DeepSeek-R1 H20 * 16 vllm0.8.1 pp2 and tp8， v1 engine，server crashed, the log as follows vllm serve /model --tensor-parallel-size 8 --pipeline-parallel-size 2 --trust-remote-code --gpu-memory-utilization 0.92 --max-model-len 98304 --host 0.0.0.0 --port 8102 --served-model-name DeepSeek-R1 --uvicorn-log-level info INFO 03-22 13:13:23 [__init__.py:256] Automatically detected platform cuda. INFO 03-22 13:13:27 [api_server.py:977] vLLM API server version 0.8.1 INFO 03-22 13:13:27 [api_server.py:978] args: Namespace(subparser='serve', model_tag='/model', config='', host='0.0.0.0', port=8102, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, enable_ssl_refresh=False, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, too...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: 6) at non-singleton dimension, DeepSeek R1 H20x16 pp2, v1 engine bug;ray;stale ### Your current environment ### 🐛 Describe the bug DeepSeek-R1 H20 * 16 vllm0.8.1 pp2 and tp8， v1 engine，server crashed, the log as follows...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: d platform cuda. INFO 03-22 13:13:27 [api_server.py:977] vLLM API server version 0.8.1 INFO 03-22 13:13:27 [api_server.py:978] args: Namespace(subparser='serve', model_tag='/model', config='', host='0.0.0.0', port=8102,...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=98304, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', di...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: host='0.0.0.0', port=8102, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: 1 pp2 and tp8， v1 engine，server crashed, the log as follows vllm serve /model --tensor-parallel-size 8 --pipeline-parallel-size 2 --trust-remote-code --gpu-memory-utilization 0.92 --max-model-len 98304 --host 0.0.0.0 --...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
