# vllm-project/vllm#11994: [Bug]:  Engine process failed to start while running Phi-4 GGUF

| 字段 | 值 |
| --- | --- |
| Issue | [#11994](https://github.com/vllm-project/vllm/issues/11994) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  Engine process failed to start while running Phi-4 GGUF

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug After running wget https://huggingface.co/microsoft/phi-4-gguf/resolve/main/phi-4-q4.gguf vllm serve ./phi-4-q4.gguf --tokenizer microsoft/phi-4 --host 0.0.0.0 --port 7000 Error: ``` INFO 01-13 07:27:13 api_server.py:712] vLLM API server version 0.6.6.post1 INFO 01-13 07:27:13 api_server.py:713] args: Namespace(subparser='serve', model_tag='./phi-4-q4.gguf', config='', host='0.0.0.0', port=7000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='./phi-4-q4.gguf', task='auto', tokenizer='microsoft/phi-4', skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_m...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: Engine process failed to start while running Phi-4 GGUF bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug After running wget https://huggingface.co/microsoft/phi-4-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: while running Phi-4 GGUF bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug After running wget https://huggingface.co/microsoft/phi-4-gguf/resolve/main/phi-4-q4.gguf vllm s...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 7000 Error: ``` INFO 01-13 07:27:13 api_server.py:712] vLLM API server version 0.6.6.post1 INFO 01-13 07:27:13 api_server.py:713] args: Namespace(subparser='serve', model_tag='./phi-4-q4.gguf', config='', host='0.0.0.0'...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=16384, guided_decoding_backend='xgrammar', logits_processor_patte...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: host='0.0.0.0', port=7000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
