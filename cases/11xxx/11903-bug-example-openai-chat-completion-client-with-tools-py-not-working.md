# vllm-project/vllm#11903: [Bug]: example/openai_chat_completion_client_with_tools.py not working

| 字段 | 值 |
| --- | --- |
| Issue | [#11903](https://github.com/vllm-project/vllm/issues/11903) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;operator;quantization;triton |
| 症状 | crash;oom;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: example/openai_chat_completion_client_with_tools.py not working

### Issue 正文摘录

### Your current environment ### Model Input Dumps **vLLM:** $ docker container stop vllm; docker container rm vllm; docker run --name vllm --runtime nvidia -e "VLLM_LOGGING_LEVEL=DEBUG" -e "NVIDIA_VISIBLE_DEVICES=GPU-8cba8394-b5d6-1e92-6658-bb6efc08abff,GPU-c05c3905-fdd9-34a3-f6c0-1437beb91c7d" -v ~/.cache/huggingface:/root/.cache/huggingface --env "HUGGING_FACE_HUB_TOKEN=hf_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" --ipc=host -p 8000:8000 vllm/vllm-openai --gpu-memory-utilization 0.95 --model cstr/llama3.1-8b-spaetzle-v90 --served-model-name llama3.1-8b-spaetzle-v90 --tensor-parallel-size 2 --enable-auto-tool-choice --tool-call-parser hermes vllm vllm INFO 01-09 07:32:00 api_server.py:712] vLLM API server version 0.6.6.post1 INFO 01-09 07:32:00 api_server.py:713] args: Namespace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=F...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=True, tool_call_parser='hermes', tool_parser_plugin='', model='cstr/llama3.1-8b-spaetzle-v90', t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: bug ### Your current environment ### Model Input Dumps **vLLM:** $ docker container stop vllm; docker container rm vllm; docker run --name vllm --runtime nvidia -e "VLLM_LOGGING_LEVEL=DEBUG" -e "NVIDIA_VISIBLE_DEVICES=G...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: lient_with_tools.py not working bug ### Your current environment ### Model Input Dumps **vLLM:** $ docker container stop vllm; docker container rm vllm; docker run --name vllm --runtime nvidia -e "VLLM_LOGGING_LEVEL=DEB...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_patter...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: auto', quantization_param_path=None, max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_pattern=None, distributed_executor_backend=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_paral...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
