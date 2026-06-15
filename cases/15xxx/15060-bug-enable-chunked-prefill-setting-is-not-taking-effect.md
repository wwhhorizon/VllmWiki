# vllm-project/vllm#15060: [Bug]: --enable-chunked-prefill setting is not taking effect

| 字段 | 值 |
| --- | --- |
| Issue | [#15060](https://github.com/vllm-project/vllm/issues/15060) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: --enable-chunked-prefill setting is not taking effect

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I don't specify a setting for --enable-chunked-prefill I see it listed as None in the log. I was trying to use Llama-3.1.8b to make embeddings so I set my HF config.json architecture=LlamaModel and set --task embedding. After doing this VLLM outputted an error that chunked prefill is not supported for pooling models. So I set --enable-chunked-prefill to False, but the setting is not taking effect, and I get the same error. I see this in the log: INFO 03-18 20:10:54 api_server.py:835] vLLM API server version 0.7.0 INFO 03-18 20:10:54 api_server.py:836] args: Namespace(host='0.0.0.0', port=10000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plug...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ### Your current environment ### 🐛 Describe the bug When I don't specify a setting for --enable-chunked-prefill I see it listed as None in the log. I was trying to use Llama-3.1.8b to make embeddings so I set my HF conf...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=8000, guided_decoding_backend='xgrammar', logits_processor_pattern=None, distributed_executor_b...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: -chunked-prefill I see it listed as None in the log. I was trying to use Llama-3.1.8b to make embeddings so I set my HF config.json architecture=LlamaModel and set --task embedding. After doing this VLLM outputted an er...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: --enable-chunked-prefill setting is not taking effect bug ### Your current environment ### 🐛 Describe the bug When I don't specify a setting for --enable-chunked-prefill I see it listed as None in the log. I was...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: dtype='auto', kv_cache_dtype='auto', max_model_len=8000, guided_decoding_backend='xgrammar', logits_processor_pattern=None, distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel_size=1, max_parall...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
