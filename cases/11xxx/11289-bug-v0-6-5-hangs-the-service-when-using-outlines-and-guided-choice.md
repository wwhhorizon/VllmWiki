# vllm-project/vllm#11289: [Bug]: v0.6.5 hangs the service when using outlines and guided_choice

| 字段 | 值 |
| --- | --- |
| Issue | [#11289](https://github.com/vllm-project/vllm/issues/11289) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;scheduler_memory;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;kernel;operator;quantization;triton |
| 症状 | build_error;oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v0.6.5 hangs the service when using outlines and guided_choice

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug service startup command ```bash export VLLM_PLUGINS=clean_cuda_cache export OUTLINES_CACHE_DIR=/hestia/model/llm_cache/outlines export VLLM_RPC_TIMEOUT=600000 export LD_PRELOAD=/lib/x86_64-linux-gnu/libtcmalloc.so.4:$LD_PRELOAD vllm serve /hestia/model/Qwen2.5-14B-Instruct-AWQ --max-model-len 32768 --port 8001 --quantization awq --served-model-name qwen --num-gpu-blocks-override 2048 --disable-log-requests --swap-space 4 --enable-prefix-caching --enable-chunked-prefill --max-num-batched-tokens 2048 ``` service output ```bash INFO 12-18 08:27:14 api_server.py:651] vLLM API server version 0.6.5 INFO 12-18 08:27:14 api_server.py:652] args: Namespace(subparser='serve', model_tag='/hestia/model/Qwen2.5-14B-Instruct-AWQ', config='', host=None, port=8001, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, midd...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: wq --served-model-name qwen --num-gpu-blocks-override 2048 --disable-log-requests --swap-space 4 --enable-prefix-caching --enable-chunked-prefill --max-num-batched-tokens 2048 ``` service output ```bash INFO 12-18 08:27...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: uto', quantization_param_path=None, max_model_len=32768, guided_decoding_backend='xgrammar', logits_processor_pattern=None, distributed_executor_backend=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_paral...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ce output ```bash INFO 12-18 08:27:14 api_server.py:651] vLLM API server version 0.6.5 INFO 12-18 08:27:14 api_server.py:652] args: Namespace(subparser='serve', model_tag='/hestia/model/Qwen2.5-14B-Instruct-AWQ', config...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: sing outlines and guided_choice bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug service startup command ```bash export VLLM_PLUGINS=clean_cuda_cache export OUTLINES_CACHE_DIR=...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: estia/model/Qwen2.5-14B-Instruct-AWQ --max-model-len 32768 --port 8001 --quantization awq --served-model-name qwen --num-gpu-blocks-override 2048 --disable-log-requests --swap-space 4 --enable-prefix-caching --enable-ch...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
