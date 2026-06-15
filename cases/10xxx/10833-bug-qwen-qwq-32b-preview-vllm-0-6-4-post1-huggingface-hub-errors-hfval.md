# vllm-project/vllm#10833: [Bug]: Qwen-QwQ-32B-Preview vllm 0.6.4-post1  huggingface_hub.errors.HFValidationError:

| 字段 | 值 |
| --- | --- |
| Issue | [#10833](https://github.com/vllm-project/vllm/issues/10833) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen-QwQ-32B-Preview vllm 0.6.4-post1  huggingface_hub.errors.HFValidationError:

### Issue 正文摘录

### Your current environment ### Model Input Dumps ``` INFO 12-02 23:29:11 api_server.py:585] vLLM API server version 0.6.4.post1 INFO 12-02 23:29:11 api_server.py:586] args: Namespace(host='0.0.0.0', port=45001, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='D:\\Users\\Admin\\.cache\\modelscope\\hub\\qwen\\Qwen-QwQ-32B-Preview-GGUF\\QwQ-32B-Preview-IQ2_XS.gguf', task='auto', tokenizer=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', chat_template_text_format='string', trust_remote_code=True, allowed_local_media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=8192, guided_decoding_backend...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: Qwen-QwQ-32B-Preview vllm 0.6.4-post1 huggingface_hub.errors.HFValidationError: bug ### Your current environment ### Model Input Dumps ``` INFO 12-02 23:29:11 api_server.py:585] vLLM API server version 0.6.4.post1
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: e, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', num_scheduler_steps=1, multi_step_stream_outputs=True, scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, speculative_mo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Input Dumps ``` INFO 12-02 23:29:11 api_server.py:585] vLLM API server version 0.6.4.post1 INFO 12-02 23:29:11 api_server.py:586] args: Namespace(host='0.0.0.0', port=45001, uvicorn_log_level='info', allow_credentials=F...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 16) [11](vscode-notebook-cell:?execution_count=4&line=11) torch.cuda.empty_cache() [14](vscode-notebook-cell:?execution_count=4&line=14) llm_model_pth = MODLE_PATH ---> [16](vscode-notebook-cell:?execution_count=4&line=...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ost='0.0.0.0', port=45001, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
