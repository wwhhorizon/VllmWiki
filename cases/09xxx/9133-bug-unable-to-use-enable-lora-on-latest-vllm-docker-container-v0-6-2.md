# vllm-project/vllm#9133: [Bug]: Unable to use --enable-lora on latest vllm docker container (v0.6.2)

| 字段 | 值 |
| --- | --- |
| Issue | [#9133](https://github.com/vllm-project/vllm/issues/9133) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unable to use --enable-lora on latest vllm docker container (v0.6.2)

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When using the '--enable-lora' the container crashes with a '/usr/bin/ld: cannot find -lcuda' error. To reproduce use: ``` podman run --rm -p 8000:8000 --device nvidia.com/gpu=0 --device nvidia.com/gpu=all --security-opt=label=disable -v ~/.cache/huggingface:/root/.cache/huggingface -v ~/.cache/lora:/root/lora --ipc=host -e VLLM_LOGGING_LEVEL=DEBUG -e VLLM_TRACE_FUNCTION=1 -e NCCL_DEBUG=TRACE docker.io/vllm/vllm-openai --model microsoft/phi-2 --enable-lora --lora-modules thealth=/root/lora/thealth-phi-2/ ``` ``` INFO 10-07 12:06:44 api_server.py:526] vLLM API server version 0.6.1.dev238+ge2c6e0a82 INFO 10-07 12:06:44 api_server.py:527] args: Namespace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=[LoRAModulePath(name='thealth', path='/root/lora/thealth-phi-2/', base_model_name=None)], prompt_adapters=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_to...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: Unable to use --enable-lora on latest vllm docker container (v0.6.2) bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When using the '--enable-lora' the container...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: Unable to use --enable-lora on latest vllm docker container (v0.6.2) bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When using the '--enable-lora' the container crashes...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: docker container (v0.6.2) bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When using the '--enable-lora' the container crashes with a '/usr/bin/ld: cannot find -lcuda' e...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: auto', quantization_param_path=None, max_model_len=None, guided_decoding_backend='outlines', distributed_executor_backend=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=1, max_parallel_loadin...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: code=False, download_dir=None, load_format='auto', config_format='auto', dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=None, guided_decoding_backend='outlines', distributed_executor_ba...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
