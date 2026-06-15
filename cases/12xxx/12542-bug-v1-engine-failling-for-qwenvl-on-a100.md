# vllm-project/vllm#12542: [Bug]: V1 Engine failling for QwenVL on A100

| 字段 | 值 |
| --- | --- |
| Issue | [#12542](https://github.com/vllm-project/vllm/issues/12542) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;gemm;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: V1 Engine failling for QwenVL on A100

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Command used: ```bash python3 -m vllm.entrypoints.openai.api_server --served-model-name Qwen2-VL-7B-Instruct --model Qwen/Qwen2-VL-7B-Instruct --dtype float16 --port 8080 --gpu-memory-utilization 0.998 --download-dir /mnt/shared_models/huggingface/cache/hub --limit-mm-per-prompt "image=2" ``` Error: ``` INFO 01-29 10:23:44 __init__.py:183] Automatically detected platform cuda. INFO 01-29 10:23:46 api_server.py:835] vLLM API server version 0.7.0 INFO 01-29 10:23:46 api_server.py:836] args: Namespace(host=None, port=8080, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='Qwen/Qwen2-VL-7B-Instruct', tas...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: [Bug]: V1 Engine failling for QwenVL on A100 bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Command used: ```bash python3 -m vllm.entrypoints.openai.api_server --served-model...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ed platform cuda. INFO 01-29 10:23:46 api_server.py:835] vLLM API server version 0.7.0 INFO 01-29 10:23:46 api_server.py:836] args: Namespace(host=None, port=8080, uvicorn_log_level='info', allow_credentials=False, allo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: odel-name Qwen2-VL-7B-Instruct --model Qwen/Qwen2-VL-7B-Instruct --dtype float16 --port 8080 --gpu-memory-utilization 0.998 --download-dir /mnt/shared_models/huggingface/cache/hub --limit-mm-per-prompt "image=2" ``` Err...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='Qwen/Qwen2-VL-7B-Instruct', task='au...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: pe='float16', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_pattern=None, distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel_size=1, max_parall...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
