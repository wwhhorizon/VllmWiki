# vllm-project/vllm#10429: [Bug]: rocm issue

| 字段 | 值 |
| --- | --- |
| Issue | [#10429](https://github.com/vllm-project/vllm/issues/10429) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | quantization |
| 症状 | crash |
| 根因提示 | dtype |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: rocm issue

### Issue 正文摘录

### Your current environment ### Model Input Dumps `vllm serve mistralai/Mistral-7B-Instruct-v0.3 --trust-remote-code --enable-chunked-prefill --max_num_batched_tokens 1024` ### 🐛 Describe the bug When I ran `vllm serve mistralai/Mistral-7B-Instruct-v0.3 --trust-remote-code --enable-chunked-prefill --max_num_batched_tokens 1024` I got following error on amd rad machine: ``` WARNING 11-15 19:35:50 rocm.py:13] `fork` method is not supported by ROCm. VLLM_WORKER_MULTIPROC_METHOD is overridden to `spawn` instead. INFO 11-15 19:35:53 api_server.py:564] vLLM API server version 0.6.3.post2.dev355+g9d5b4e4d INFO 11-15 19:35:53 api_server.py:565] args: Namespace(subparser='serve', model_tag='mistralai/Mistral-7B-Instruct-v0.3', config='', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_auto_tool_choice=False, tool_c...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: mistralai/Mistral-7B-Instruct-v0.3 --trust-remote-code --enable-chunked-prefill --max_num_batched_tokens 1024` ### 🐛 Describe the bug When I ran `vllm serve mistralai/Mistral-7B-Instruct-v0.3 --trust-remote-code --enabl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: rocm issue bug;rocm ### Your current environment ### Model Input Dumps `vllm serve mistralai/Mistral-7B-Instruct-v0.3 --trust-remote-code --enable-chunked-prefill --max_num_batched_tokens 1024` ### 🐛 Describe the...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: `spawn` instead. INFO 11-15 19:35:53 api_server.py:564] vLLM API server version 0.6.3.post2.dev355+g9d5b4e4d INFO 11-15 19:35:53 api_server.py:565] args: Namespace(subparser='serve', model_tag='mistralai/Mistral-7B-Inst...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ='', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: auto', quantization_param_path=None, max_model_len=None, guided_decoding_backend='outlines', distributed_executor_backend=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=1, max_parallel_loadin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
