# vllm-project/vllm#12867: [Usage]: Use local model ERROR, Use `repo_type` argument if needed.

| 字段 | 值 |
| --- | --- |
| Issue | [#12867](https://github.com/vllm-project/vllm/issues/12867) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;quantization |
| 症状 | crash |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Use local model ERROR, Use `repo_type` argument if needed.

### Issue 正文摘录

```text vllm serve /mnt/cpn-pod/models/deepseek-ai/DeepSeek-R1 --served-model-name deepseek-ai/DeepSeek-R1 -tp 8 -pp 2 --distributed-executor-backend=ray --trust-remote-code ``` I remember command like that can work in previous version, but now will raise error ``` root@86051:/vllm-workspace# vllm serve /mnt/cpn-pod/models/deepseek-ai/DeepSeek-R1 --served-model-name deepseek-ai/DeepSeek-R1 -tp 8 -pp 2 --distributed-executor-backend=ray --trust-remote-code INFO 02-06 22:00:47 __init__.py:183] Automatically detected platform cuda. INFO 02-06 22:00:49 api_server.py:838] vLLM API server version 0.7.1 INFO 02-06 22:00:49 api_server.py:839] args: Namespace(subparser='serve', model_tag='/mnt/cpn-pod/models/deepseek-ai/DeepSeek-R1', config='', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=F...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: Use local model ERROR, Use `repo_type` argument if needed. usage ```text vllm serve /mnt/cpn-pod/models/deepseek-ai/DeepSeek-R1 --served-model-name deepseek-ai/DeepSeek-R1 -tp 8 -pp 2 --distributed-executor-bac...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, enable_reasoning=False, reasoning_parser=None, tool_call_parser=None, tool_parser_plugin=...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: trust-remote-code ``` I remember command like that can work in previous version, but now will raise error ``` root@86051:/vllm-workspace# vllm serve /mnt/cpn-pod/models/deepseek-ai/DeepSeek-R1 --served-model-name deepse...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_pattern=None, distributed_executor_b...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ='', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
