# vllm-project/vllm#11858: [Bug]: TypeError: '_PlaceholderModuleAttr' object is not callable for RunAI SafetensorsStreamer()

| 字段 | 值 |
| --- | --- |
| Issue | [#11858](https://github.com/vllm-project/vllm/issues/11858) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TypeError: '_PlaceholderModuleAttr' object is not callable for RunAI SafetensorsStreamer()

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Previous S3 pickling bug encountered: https://github.com/vllm-project/vllm/issues/11819 The Pickling issue was fixed after applying the change in this PR: https://github.com/vllm-project/vllm/pull/11825 However, when loading into multiple GPUs again, a new error has surfaced. This is the command used: `vllm serve s3://llama-3.3-70b-instruct --load-format runai_streamer --max-num-seqs 8 --tensor-parallel-size 4` ``` root@479c323b83e5:/usr/local/bin# vllm serve s3://llama-3.3-70b-instruct --load-format runai_streamer --max-num-seqs 8 --tensor-parallel-size 4 INFO 01-08 16:17:19 api_server.py:712] vLLM API server version 0.6.6.post1 INFO 01-08 16:17:19 api_server.py:713] args: Namespace(subparser='serve', model_tag='s3://llama-3.3-70b-instruct', config='', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_r...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='s3://llama-3.3-70b-instruct', task='...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: rallel-size 4 INFO 01-08 16:17:19 api_server.py:712] vLLM API server version 0.6.6.post1 INFO 01-08 16:17:19 api_server.py:713] args: Namespace(subparser='serve', model_tag='s3://llama-3.3-70b-instruct', config='', host...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: for RunAI SafetensorsStreamer() bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Previous S3 pickling bug encountered: https://github.com/vllm-project/vllm/issues/11819 The Pic...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: auto', quantization_param_path=None, max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_pattern=None, distributed_executor_backend=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_paral...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: =None, download_dir=None, load_format='runai_streamer', config_format= , dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_patter...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
