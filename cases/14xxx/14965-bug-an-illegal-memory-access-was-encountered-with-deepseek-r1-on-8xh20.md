# vllm-project/vllm#14965: [Bug]: An illegal memory access was encountered with DeepSeek-R1 on 8xH200

| 字段 | 值 |
| --- | --- |
| Issue | [#14965](https://github.com/vllm-project/vllm/issues/14965) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;kernel;moe;quantization;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: An illegal memory access was encountered with DeepSeek-R1 on 8xH200

### Issue 正文摘录

### Your current environment - Installed vllm with `uv pip install vllm` - Tried to serve the model with `vllm serve "deepseek-ai/DeepSeek-R1" -tp 8 --max-model-len 38768 --max-num-batched-tokens 38768 --gpu-memory-utilization 0.9 --trust-remote-code --port 1234` - Error: `RuntimeError: Triton Error [CUDA]: an illegal memory access was encountered` ### 🐛 Describe the bug ``` INFO 03-17 15:26:45 __init__.py:207] Automatically detected platform cuda. INFO 03-17 15:26:45 api_server.py:912] vLLM API server version 0.7.3 INFO 03-17 15:26:45 api_server.py:913] args: Namespace(subparser='serve', model_tag='deepseek-ai/DeepSeek-R1', config='', host=None, port=1234, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, enable_reasoning=False, reasonin...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, enable_reasoning=False, reasoning_parser=None, tool_call_parser=None, tool_parser_plugin=...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: countered with DeepSeek-R1 on 8xH200 bug ### Your current environment - Installed vllm with `uv pip install vllm` - Tried to serve the model with `vllm serve "deepseek-ai/DeepSeek-R1" -tp 8 --max-model-len 38768 --max-n...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=38768, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', di...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: ='', host=None, port=1234, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: onment - Installed vllm with `uv pip install vllm` - Tried to serve the model with `vllm serve "deepseek-ai/DeepSeek-R1" -tp 8 --max-model-len 38768 --max-num-batched-tokens 38768 --gpu-memory-utilization 0.9 --trust-re...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
