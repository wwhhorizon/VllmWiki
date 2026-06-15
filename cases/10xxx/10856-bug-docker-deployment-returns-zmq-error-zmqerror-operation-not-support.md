# vllm-project/vllm#10856: [Bug]: Docker deployment returns zmq.error.ZMQError: Operation not supported

| 字段 | 值 |
| --- | --- |
| Issue | [#10856](https://github.com/vllm-project/vllm/issues/10856) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 24; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Docker deployment returns zmq.error.ZMQError: Operation not supported

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Tried to serve a Llama model using vllm docker deployment, but encounter zmq error Followed the instruction as documented in https://docs.vllm.ai/en/latest/serving/deploying_with_docker.html **Command** ``` docker run --runtime nvidia --gpus '"device=3"' -v ~/.cache/huggingface:/root/.cache/huggingface --env "HUGGING_FACE_HUB_TOKEN= " -p 8050:8000 --ipc=host vllm/vllm-openai:v0.6.4 --model meta-llama/Llama-Guard-3-1B ``` **Error** ``` INFO 12-02 23:35:00 api_server.py:585] vLLM API server version 0.6.4 INFO 12-02 23:35:00 api_server.py:586] args: Namespace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='meta-llama/Llama-Guard-3-1B', task='auto',...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: Docker deployment returns zmq.error.ZMQError: Operation not supported bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Tried to serve a Llama model using vllm docke
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: : Operation not supported bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Tried to serve a Llama model using vllm docker deployment, but encounter zmq error Followed the...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: ocker deployment returns zmq.error.ZMQError: Operation not supported bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Tried to serve a Llama model using vllm docker deplo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=None, guided_decoding_backend='outlines', distributed_executor_ba...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: pace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
